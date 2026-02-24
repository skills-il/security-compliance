#!/usr/bin/env python3
"""
Security Alert Triage Tool

Standalone script that guides security analysts through incident triage
using a structured workflow aligned with INCD guidelines and Israeli
cybersecurity best practices.

Usage:
    python security_triage.py
    python security_triage.py --output incident_report.json
    python security_triage.py --severity-calc
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


def calculate_severity(cvss: float, asset: str, data: str, blast: str) -> dict:
    """Calculate composite severity score."""
    asset_score = ASSET_CRITICALITY.get(asset.lower(), 5)
    data_score = DATA_SENSITIVITY.get(data.lower(), 5)
    blast_score = BLAST_RADIUS.get(blast.lower(), 5)

    composite = (
        cvss * CVSS_WEIGHT
        + asset_score * ASSET_WEIGHT
        + data_score * DATA_WEIGHT
        + blast_score * BLAST_WEIGHT
    )

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
            "cvss_contribution": round(cvss * CVSS_WEIGHT, 2),
            "asset_contribution": round(asset_score * ASSET_WEIGHT, 2),
            "data_contribution": round(data_score * DATA_WEIGHT, 2),
            "blast_contribution": round(blast_score * BLAST_WEIGHT, 2),
        },
    }


def incd_reporting_check(classification: str, is_critical_infra: bool,
                          has_data_breach: bool) -> dict:
    """Determine INCD reporting requirements."""
    report = {
        "incd_reporting_required": False,
        "reporting_deadline": None,
        "privacy_authority_notification": False,
        "channel": None,
        "notes": [],
    }

    if is_critical_infra:
        report["incd_reporting_required"] = True
        if classification in ("CRITICAL", "HIGH"):
            report["reporting_deadline"] = "Immediately (INCD hotline)"
            report["channel"] = "INCD 24/7 hotline"
        else:
            report["reporting_deadline"] = "Within 24 hours"
            report["channel"] = "CERT-IL portal"
        report["notes"].append("Critical infrastructure: mandatory INCD reporting")

    if has_data_breach:
        report["privacy_authority_notification"] = True
        report["notes"].append(
            "Data breach: notify Privacy Protection Authority 'without delay'"
        )
        report["notes"].append(
            "If significant harm possible: notify affected individuals"
        )

    if classification == "CRITICAL" and not is_critical_infra:
        report["notes"].append(
            "Voluntary INCD reporting recommended for critical incidents"
        )

    return report


def run_interactive_triage() -> dict:
    """Run an interactive triage session."""
    print("=" * 60)
    print("Security Alert Triage — Israeli Cybersecurity Ops")
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
    reporting = incd_reporting_check(severity["classification"], is_critical_infra, has_data_breach)

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


def severity_calculator():
    """Quick severity calculation without full triage."""
    print("Quick Severity Calculator")
    print("-" * 30)
    try:
        cvss = float(input("CVSS (0-10): "))
    except ValueError:
        cvss = 5.0
    print(f"Assets: {', '.join(ASSET_CRITICALITY.keys())}")
    asset = input("Asset: ").strip()
    print(f"Data: {', '.join(DATA_SENSITIVITY.keys())}")
    data = input("Data: ").strip()
    print(f"Blast: {', '.join(BLAST_RADIUS.keys())}")
    blast = input("Blast: ").strip()

    result = calculate_severity(cvss, asset, data, blast)
    print(f"\nScore: {result['composite_score']} — {result['classification']}")
    print(f"Action: {result['recommended_action']}")


def main():
    parser = argparse.ArgumentParser(
        description="Security Alert Triage Tool — Israeli Cybersecurity Ops"
    )
    parser.add_argument("--output", "-o", help="Output JSON report file path")
    parser.add_argument("--severity-calc", action="store_true",
                        help="Quick severity calculator mode")
    args = parser.parse_args()

    if args.severity_calc:
        severity_calculator()
        return

    incident = run_interactive_triage()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(incident, f, indent=2, ensure_ascii=False)
        print(f"\nIncident report saved to: {args.output}")


if __name__ == "__main__":
    main()
