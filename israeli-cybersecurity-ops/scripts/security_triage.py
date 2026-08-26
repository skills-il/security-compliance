#!/usr/bin/env python3
"""
Security Alert Triage Tool

Standalone script that guides security analysts through incident triage
using a structured workflow aligned with INCD guidelines and Israeli
cybersecurity best practices.

Usage:
    python security_triage.py --example
    python security_triage.py --severity-calc --cvss 8.5 --asset production --data pii --blast network_segment
    python security_triage.py --json '{"alert_id":"ALERT-123","cvss":7.5,"asset":"production","data":"pii","blast":"network_segment","is_critical_infra":false,"has_data_breach":true}'
    python security_triage.py --output incident_report.json
"""

import argparse
import json
import sys
from datetime import datetime


# Severity scoring matrix
CVSS_WEIGHT = 0.3
ASSET_WEIGHT = 0.25
DATA_WEIGHT = 0.25
BLAST_WEIGHT = 0.2

ASSET_CRITICALITY = {
    "production": 10,
    "staging": 6,
    "development": 3,
    "test": 1,
}

DATA_SENSITIVITY = {
    "health": 10,
    "financial": 9,
    "pii": 8,
    "credentials": 9,
    "business_confidential": 7,
    "internal": 4,
    "public": 1,
}

BLAST_RADIUS = {
    "organization_wide": 10,
    "network_segment": 8,
    "multiple_hosts": 6,
    "single_host": 3,
    "single_container": 1,
}


NEUTRAL_SCORE = 5


def _lookup(table: dict, value: str, label: str) -> int:
    """Look a category up, warning when it is not recognised.

    Falling back silently is unsafe in a triage tool: the neutral default of 5
    sits BELOW production (10) and above development (3), so an unrecognised
    value can move an incident in either direction without the analyst knowing.
    """
    key = str(value).lower().strip()
    if key in table:
        return table[key]
    print(
        f"WARNING: unrecognised {label} value {value!r}; scoring it as the "
        f"neutral {NEUTRAL_SCORE}. Valid values: {', '.join(sorted(table))}.",
        file=sys.stderr,
    )
    return NEUTRAL_SCORE


def calculate_severity(cvss: float, asset: str, data: str, blast: str,
                       cvss_applicable: bool | None = None) -> dict:
    """Calculate composite severity score."""
    # Clamp here, not only in the interactive path. --severity-calc and --json
    # previously accepted any float, so a mistyped "99" produced "Score: 34.8/10.0"
    # and an automatic CRITICAL from a value that is not on the CVSS scale.
    try:
        cvss = float(cvss)
    except (TypeError, ValueError):
        print("WARNING: CVSS is not a number, treating as 0.0.", file=sys.stderr)
        cvss = 0.0
    if not 0.0 <= cvss <= 10.0:
        print(f"WARNING: CVSS {cvss} is outside the 0.0-10.0 scale, clamping.",
              file=sys.stderr)
        cvss = min(max(cvss, 0.0), 10.0)

    # An unrecognised category silently scored 5, so a typo like "prodution"
    # quietly DOWNGRADED a production incident from 10 to 5. Warn loudly and
    # name the valid values instead of failing silently.
    asset_score = _lookup(ASSET_CRITICALITY, asset, "asset")
    data_score = _lookup(DATA_SENSITIVITY, data, "data")
    blast_score = _lookup(BLAST_RADIUS, blast, "blast")

    # CVSS only exists for VULNERABILITIES. Ransomware, insider exfiltration,
    # unauthorised access and destructive attacks have none, and callers pass 0.
    # With a fixed 0.30 CVSS weight the ceiling for those incidents was
    # 0.25*10 + 0.25*10 + 0.20*10 = 7.0, BELOW the 8.5 CRITICAL threshold, so no
    # non-vulnerability incident could ever be classified CRITICAL. Org-wide
    # ransomware on production health data scored 7.0 / "containment within 4
    # hours". When CVSS is not applicable, drop the dimension and renormalise
    # the remaining weights to 1.0 instead of scoring it as a zero.
    if cvss_applicable is None:
        cvss_applicable = cvss > 0.0

    if cvss_applicable:
        composite = (
            cvss * CVSS_WEIGHT
            + asset_score * ASSET_WEIGHT
            + data_score * DATA_WEIGHT
            + blast_score * BLAST_WEIGHT
        )
    else:
        denom = ASSET_WEIGHT + DATA_WEIGHT + BLAST_WEIGHT
        composite = (
            asset_score * ASSET_WEIGHT
            + data_score * DATA_WEIGHT
            + blast_score * BLAST_WEIGHT
        ) / denom

    if composite >= 8.5:
        classification = "CRITICAL"
        action = "Immediate containment required. Escalate to security lead and management."
    elif composite >= 6.5:
        classification = "HIGH"
        action = "Containment within 4 hours. Notify security team lead."
    elif composite >= 4.0:
        classification = "MEDIUM"
        action = "Add to current sprint for remediation. Monitor for escalation."
    elif composite >= 2.0:
        classification = "LOW"
        action = "Add to backlog. Review in next security review meeting."
    else:
        classification = "INFORMATIONAL"
        action = "Document and close. No immediate action required."

    return {
        "composite_score": round(composite, 2),
        "classification": classification,
        "recommended_action": action,
        "breakdown": {
            "cvss_used": cvss if cvss_applicable else None,
            "cvss_applicable": bool(cvss_applicable),
            "weighting": ("cvss+asset+data+blast" if cvss_applicable
                          else "asset+data+blast, renormalised (no CVSS)"),
            "cvss_contribution": round(cvss * CVSS_WEIGHT, 2),
            "asset_contribution": round(asset_score * ASSET_WEIGHT, 2),
            "data_contribution": round(data_score * DATA_WEIGHT, 2),
            "blast_contribution": round(blast_score * BLAST_WEIGHT, 2),
        },
    }


SUPERVISED_SECTORS = {
    "banking": "Supervisor of Banks, Proper Conduct of Banking Business Directive 364",
    "finance": "Supervisor of Banks, Proper Conduct of Banking Business Directive 364",
    "insurance": "Capital Market, Insurance and Savings Authority",
    "pension": "Capital Market, Insurance and Savings Authority",
    "health": "Ministry of Health",
    "hmo": "Ministry of Health",
    "hospital": "Ministry of Health",
}


def incd_reporting_check(classification: str, is_critical_infra: bool,
                          has_data_breach: bool, sector: str = None) -> dict:
    """Determine INCD, Privacy Authority and sector-regulator reporting duties.

    These three run INDEPENDENTLY. Reporting to CERT-IL does not discharge the
    Privacy Protection Authority duty, and neither discharges a sector
    regulator's duty. A supervised bank, insurer, pension manager, HMO or
    hospital frequently is NOT INCD-designated critical infrastructure, so an
    is_critical_infra=False answer must not be read as "no report is owed".
    """
    report = {
        "incd_reporting_required": False,
        "reporting_deadline": None,
        "privacy_authority_notification": False,
        "sector_regulator_reporting": None,
        "channel": None,
        "notes": [],
    }

    key = (sector or "").strip().lower()
    if key in SUPERVISED_SECTORS:
        report["sector_regulator_reporting"] = SUPERVISED_SECTORS[key]
        report["notes"].append(
            f"Supervised entity: a separate report is likely owed to {SUPERVISED_SECTORS[key]}, "
            f"independently of INCD and of the Privacy Protection Authority."
        )
    elif not key:
        report["notes"].append(
            "Sector not supplied, so sector-regulator reporting was NOT assessed. "
            "Pass \"sector\" (banking, finance, insurance, pension, health, hmo, "
            "hospital) if the entity is supervised. A missed sector report is the "
            "most common reporting failure in an Israeli incident."
        )

    if is_critical_infra:
        report["incd_reporting_required"] = True
        if classification in ("CRITICAL", "HIGH"):
            report["reporting_deadline"] = "Immediately (INCD 119 hotline)"
            report["channel"] = "INCD 119 hotline"
        else:
            report["reporting_deadline"] = "As soon as possible"
            report["channel"] = "INCD cyber-event-report service (gov.il)"
        report["notes"].append("Critical infrastructure: mandatory INCD reporting")

    if has_data_breach:
        report["privacy_authority_notification"] = True
        report["notes"].append(
            "Data breach: notify Privacy Protection Authority immediately for a serious security incident (Amendment 13, in force 2025-08-14; the law says 'immediately', not a 72-hour clock)"
        )
        report["notes"].append(
            "If significant harm possible: notify affected individuals"
        )

    if not is_critical_infra:
        report["notes"].append(
            "Voluntary reporting to CERT-IL is available for any incident and is "
            "free for private-sector organisations. Note it is ASSISTANCE, not a "
            "regulatory filing: it does not discharge the Privacy Protection "
            "Authority duty, and neither discharges a sector regulator's duty "
            "(Supervisor of Banks under Directive 364, Capital Market Insurance "
            "and Savings Authority, Ministry of Health). Confirm which regulator "
            "supervises the entity, because these duties run independently."
        )

    return report


def reconcile_action(severity: dict, reporting: dict) -> dict:
    """Make a statutory duty dominate the recommended action.

    The severity score and the reporting duties were computed independently, so
    the tool could print "Document and close. No immediate action required."
    directly above "Privacy Authority: NOTIFICATION REQUIRED". An analyst acting
    on recommended_action would close an incident that carries an "immediately"
    duty under Amendment 13. A required notification always outranks a low score.
    """
    duties = []
    if reporting.get("privacy_authority_notification"):
        duties.append(
            "assess whether this is a SERIOUS security incident under regulation "
            "11(d) of the Information Security Regulations 2017 and, if so, notify "
            "the Privacy Protection Authority IMMEDIATELY (not within 72 hours). "
            "Do NOT wait for the investigation to finish; an initial report is what "
            "is required"
        )
    if reporting.get("incd_reporting_required"):
        duties.append(
            f"report to the INCD ({reporting.get('channel') or 'cyber-event-report service'}), "
            f"deadline: {reporting.get('reporting_deadline')}"
        )
    if duties:
        severity = dict(severity)
        severity["recommended_action"] = (
            severity["recommended_action"]
            + " REPORTING DUTY APPLIES REGARDLESS OF THIS CLASSIFICATION: "
            + "; ".join(duties)
            + ". Preserve forensic evidence (capture volatile memory) BEFORE containment."
        )
    return severity


def run_interactive_triage() -> dict:
    """Run an interactive triage session."""
    print("=" * 60)
    print("Security Alert Triage, Israeli Cybersecurity Ops")
    print("=" * 60)
    print()

    # Gather alert information
    alert_id = input("Alert ID (or description): ").strip() or "UNKNOWN"
    source_tool = input("Source tool (wiz/snyk/sentinelone/checkpoint/other): ").strip() or "other"
    alert_type = input("Alert type (vulnerability/malware/unauthorized_access/misconfiguration/other): ").strip() or "other"

    # CVSS
    try:
        cvss = float(input("CVSS score (0.0-10.0, or 0 if unknown): ").strip())
        cvss = min(max(cvss, 0.0), 10.0)
    except ValueError:
        cvss = 5.0
        print("  Using default CVSS: 5.0")

    # Asset criticality
    print(f"\nAsset environments: {', '.join(ASSET_CRITICALITY.keys())}")
    asset = input("Affected asset environment: ").strip() or "production"

    # Data sensitivity
    print(f"\nData types: {', '.join(DATA_SENSITIVITY.keys())}")
    data = input("Data sensitivity level: ").strip() or "internal"

    # Blast radius
    print(f"\nBlast radius options: {', '.join(BLAST_RADIUS.keys())}")
    blast = input("Estimated blast radius: ").strip() or "single_host"

    # Israeli-specific context
    is_critical_infra = input("\nCritical infrastructure (energy/water/finance/health/comms/transport/gov)? [y/n]: ").strip().lower() == "y"
    has_data_breach = input("Personal data breach involved? [y/n]: ").strip().lower() == "y"

    # Calculate
    severity = calculate_severity(cvss, asset, data, blast)
    reporting = incd_reporting_check(severity["classification"], is_critical_infra, has_data_breach, sector)
    severity = reconcile_action(severity, reporting)

    # Build report
    incident = {
        "triage_timestamp": datetime.now().isoformat(),
        "alert_id": alert_id,
        "source_tool": source_tool,
        "alert_type": alert_type,
        "inputs": {
            "cvss": cvss,
            "asset_environment": asset,
            "data_sensitivity": data,
            "blast_radius": blast,
            "is_critical_infrastructure": is_critical_infra,
            "has_data_breach": has_data_breach,
            "sector": sector,
        },
        "severity_assessment": severity,
        "reporting_requirements": reporting,
    }

    # Display results
    print()
    print("=" * 60)
    print("TRIAGE RESULTS")
    print("=" * 60)
    print(f"Alert: {alert_id}")
    print(f"Source: {source_tool}")
    print(f"Type: {alert_type}")
    print()
    print(f"Composite Score: {severity['composite_score']}/10.0")
    print(f"Classification: {severity['classification']}")
    print(f"Recommended Action: {severity['recommended_action']}")
    print()
    print("Score Breakdown:")
    for key, val in severity["breakdown"].items():
        print(f"  {key}: {val}")

    print()
    print("REPORTING REQUIREMENTS:")
    print(f"  INCD Reporting: {'REQUIRED' if reporting['incd_reporting_required'] else 'Not required (voluntary recommended)'}")
    if reporting["reporting_deadline"]:
        print(f"  Deadline: {reporting['reporting_deadline']}")
    if reporting["channel"]:
        print(f"  Channel: {reporting['channel']}")
    if reporting["privacy_authority_notification"]:
        print(f"  Privacy Authority: NOTIFICATION REQUIRED")
    for note in reporting["notes"]:
        print(f"  Note: {note}")

    # Response steps
    print()
    print("RECOMMENDED RESPONSE STEPS:")
    if severity["classification"] in ("CRITICAL", "HIGH"):
        print("  1. CONTAIN: Isolate affected systems immediately")
        print("  2. PRESERVE: Collect forensic evidence before remediation")
        print("  3. ESCALATE: Notify security lead and management")
        if reporting["incd_reporting_required"]:
            print("  4. REPORT: Contact INCD via hotline (critical infrastructure)")
        if reporting["privacy_authority_notification"]:
            print("  5. NOTIFY: Report to Privacy Protection Authority (data breach)")
        print("  6. REMEDIATE: Apply fixes after evidence collection")
        print("  7. DOCUMENT: Full incident report with timeline")
        print("  8. REVIEW: Post-incident review within 1 week")
    elif severity["classification"] == "MEDIUM":
        print("  1. MONITOR: Watch for escalation indicators")
        print("  2. PLAN: Schedule remediation in current sprint")
        print("  3. DOCUMENT: Record finding and planned response")
        if reporting["privacy_authority_notification"]:
            print("  4. ASSESS: Determine if data breach notification needed")
    else:
        print("  1. DOCUMENT: Record the alert and assessment")
        print("  2. CLOSE: Mark as triaged, no immediate action")
        print("  3. TREND: Monitor for pattern with similar alerts")

    return incident


def severity_calculator(cvss=None, asset=None, data=None, blast=None):
    """Quick severity calculation without full triage.

    Args:
        cvss: CVSS score (0-10). If None, prompts interactively.
        asset: Asset environment key. If None, prompts interactively.
        data: Data sensitivity key. If None, prompts interactively.
        blast: Blast radius key. If None, prompts interactively.
    """
    print("Quick Severity Calculator")
    print("-" * 30)

    if cvss is None:
        try:
            cvss = float(input("CVSS (0-10): "))
        except (ValueError, EOFError):
            cvss = 5.0
    if asset is None:
        print(f"Assets: {', '.join(ASSET_CRITICALITY.keys())}")
        asset = input("Asset: ").strip()
    if data is None:
        print(f"Data: {', '.join(DATA_SENSITIVITY.keys())}")
        data = input("Data: ").strip()
    if blast is None:
        print(f"Blast: {', '.join(BLAST_RADIUS.keys())}")
        blast = input("Blast: ").strip()

    result = calculate_severity(cvss, asset, data, blast)
    print(f"\nCVSS: {result['breakdown']['cvss_used']}, Asset: {asset}, "
          f"Data: {data}, Blast: {blast}")
    print(f"Score: {result['composite_score']}, {result['classification']}")
    print(f"Action: {result['recommended_action']}")
    # This mode has no is_critical_infra / has_data_breach inputs, so it cannot
    # decide the reporting duty. It must NOT stay silent about it either: a
    # classification with no report prompt is how a mandatory notification gets
    # missed. Say what is unresolved.
    print(
        "\nReporting duties NOT assessed in this mode. Re-run with --json "
        "(setting is_critical_infra and has_data_breach) to evaluate them. "
        "Reminder: a serious security incident affecting personal data must be "
        "notified to the Privacy Protection Authority IMMEDIATELY, critical "
        "infrastructure must report to the INCD (119 hotline / "
        "gov.il/he/service/cyber-event-report), and a supervised entity may owe "
        "a separate report to its sector regulator. These duties run "
        "independently of this score."
    )
    return result


def run_from_json(json_input: str) -> dict:
    """Run triage from JSON input (non-interactive).

    Args:
        json_input: JSON string with triage parameters.

    Returns:
        Incident report dictionary.
    """
    try:
        params = json.loads(json_input)
    except json.JSONDecodeError:
        print("Error: Invalid JSON input.", file=sys.stderr)
        sys.exit(1)

    alert_id = params.get("alert_id", "UNKNOWN")
    source_tool = params.get("source_tool", "other")
    alert_type = params.get("alert_type", "other")
    cvss = params.get("cvss", 0.0)
    asset = params.get("asset", "production")
    data = params.get("data", "internal")
    blast = params.get("blast", "single_host")
    is_critical_infra = params.get("is_critical_infra", False)
    has_data_breach = params.get("has_data_breach", False)
    sector = params.get("sector")

    severity = calculate_severity(cvss, asset, data, blast)
    reporting = incd_reporting_check(severity["classification"], is_critical_infra, has_data_breach, sector)
    severity = reconcile_action(severity, reporting)

    incident = {
        "triage_timestamp": datetime.now().isoformat(),
        "alert_id": alert_id,
        "source_tool": source_tool,
        "alert_type": alert_type,
        "inputs": {
            "cvss": cvss,
            "asset_environment": asset,
            "data_sensitivity": data,
            "blast_radius": blast,
            "is_critical_infrastructure": is_critical_infra,
            "has_data_breach": has_data_breach,
            "sector": sector,
        },
        "severity_assessment": severity,
        "reporting_requirements": reporting,
    }

    print(f"Alert: {alert_id} ({alert_type})")
    print(f"Score: {severity['composite_score']}/10.0, {severity['classification']}")
    print(f"Action: {severity['recommended_action']}")
    if reporting["incd_reporting_required"]:
        print(f"INCD Reporting: REQUIRED ({reporting['reporting_deadline']})")
    if reporting["privacy_authority_notification"]:
        print("Privacy Authority: NOTIFICATION REQUIRED")
    if reporting["sector_regulator_reporting"]:
        print(f"Sector Regulator: LIKELY REQUIRED ({reporting['sector_regulator_reporting']})")
    if alert_type in ("malware", "ransomware"):
        print(
            "Ransomware note: paying a ransom is a LEGAL decision, not a SOC decision. "
            "A payment to an entity linked to a designated terrorist organisation can "
            "expose the payer to liability under the Counter-Terrorism Law 2016 and the "
            "Prohibition on Money Laundering Law, plus foreign sanctions exposure. "
            "Do not pay without counsel and without engaging INCD/CERT-IL."
        )

    return incident


def run_example() -> dict:
    """Run a demo triage with example data."""
    print("=== Example: Production Data Breach ===")
    print()
    example_json = json.dumps({
        "alert_id": "ALERT-2026-001",
        "source_tool": "wiz",
        "alert_type": "unauthorized_access",
        "cvss": 8.5,
        "asset": "production",
        "data": "pii",
        "blast": "network_segment",
        "is_critical_infra": False,
        "has_data_breach": True,
    })
    return run_from_json(example_json)


def main():
    parser = argparse.ArgumentParser(
        description="Security Alert Triage Tool, Israeli Cybersecurity Ops"
    )
    parser.add_argument("--output", "-o", help="Output JSON report file path")
    parser.add_argument("--severity-calc", action="store_true",
                        help="Quick severity calculator mode")
    parser.add_argument("--cvss", type=float, help="CVSS score (use with --severity-calc)")
    parser.add_argument("--asset", choices=sorted(ASSET_CRITICALITY),
                        help="Asset environment (use with --severity-calc)")
    parser.add_argument("--data", choices=sorted(DATA_SENSITIVITY),
                        help="Data sensitivity (use with --severity-calc)")
    parser.add_argument("--blast", choices=sorted(BLAST_RADIUS),
                        help="Blast radius (use with --severity-calc)")
    parser.add_argument("--json", help="JSON string with triage parameters (non-interactive)")
    parser.add_argument("--example", action="store_true", help="Run example triage")
    args = parser.parse_args()

    if args.example:
        incident = run_example()
    elif args.severity_calc:
        result = severity_calculator(args.cvss, args.asset, args.data, args.blast)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as fh:
                json.dump(result, fh, indent=2, ensure_ascii=False)
            print(f"\nSaved to {args.output}")
        return
    elif args.json:
        incident = run_from_json(args.json)
    else:
        incident = run_interactive_triage()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(incident, f, indent=2, ensure_ascii=False)
        print(f"\nIncident report saved to: {args.output}")


if __name__ == "__main__":
    main()
