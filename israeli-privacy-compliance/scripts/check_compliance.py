#!/usr/bin/env python3
"""
Israeli Privacy Compliance — Code Pattern Checker

Checks a codebase for privacy compliance implementation patterns:
consent management, DSAR handling, cross-border transfers, and audit logging.

Usage:
    python check_compliance.py --help
    python check_compliance.py --example
    python check_compliance.py --scan /path/to/project
    python check_compliance.py --json '{"has_consent":true,"has_dsar":false,"has_cross_border":true,"has_audit_log":true,"has_gdpr_bridge":false,"record_count":50000}'
"""

import argparse
import json
import os
import sys
from datetime import datetime


def scan_directory(path):
    """Scan a project directory for privacy compliance patterns."""
    results = {
        "has_consent": False,
        "has_dsar": False,
        "has_cross_border": False,
        "has_audit_log": False,
        "has_gdpr_bridge": False,
        "has_data_minimization": False,
        "has_pseudonymization": False,
        "has_retention_policy": False,
        "findings": [],
    }

    consent_patterns = ["consent", "haskama", "opt_in", "opt-in", "cookie_consent"]
    dsar_patterns = ["dsar", "subject_access", "data_request", "bakashat_meida",
                     "right_to_access", "right_of_access"]
    cross_border_patterns = ["cross_border", "data_transfer", "adequacy",
                             "transfer_safeguard", "scc"]
    audit_patterns = ["audit_log", "audit_trail", "privacy_event", "compliance_log"]
    gdpr_patterns = ["gdpr", "eu_compliance", "dual_compliance", "ropa"]
    minimization_patterns = ["data_minimization", "field_allowlist", "filter_fields",
                             "allowed_fields"]
    pseudonymization_patterns = ["pseudonymize", "anonymize", "hash_identifier",
                                  "de_identify"]
    retention_patterns = ["retention", "data_expiry", "cleanup_expired",
                          "enforce_retention"]

    for root, _dirs, files in os.walk(path):
        # Skip common non-source directories
        base = os.path.basename(root)
        if base in ("node_modules", ".git", "__pycache__", "venv", ".venv", "vendor"):
            continue

        for filename in files:
            if not filename.endswith((".py", ".js", ".ts", ".tsx", ".jsx", ".rb",
                                      ".go", ".java", ".cs", ".php")):
                continue

            filepath = os.path.join(root, filename)
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read().lower()
            except (OSError, IOError):
                continue

            rel_path = os.path.relpath(filepath, path)

            for pattern in consent_patterns:
                if pattern in content:
                    results["has_consent"] = True
                    results["findings"].append(
                        {"file": rel_path, "pattern": "consent", "match": pattern})
                    break

            for pattern in dsar_patterns:
                if pattern in content:
                    results["has_dsar"] = True
                    results["findings"].append(
                        {"file": rel_path, "pattern": "dsar", "match": pattern})
                    break

            for pattern in cross_border_patterns:
                if pattern in content:
                    results["has_cross_border"] = True
                    results["findings"].append(
                        {"file": rel_path, "pattern": "cross_border", "match": pattern})
                    break

            for pattern in audit_patterns:
                if pattern in content:
                    results["has_audit_log"] = True
                    results["findings"].append(
                        {"file": rel_path, "pattern": "audit_log", "match": pattern})
                    break

            for pattern in gdpr_patterns:
                if pattern in content:
                    results["has_gdpr_bridge"] = True
                    results["findings"].append(
                        {"file": rel_path, "pattern": "gdpr_bridge", "match": pattern})
                    break

            for pattern in minimization_patterns:
                if pattern in content:
                    results["has_data_minimization"] = True
                    results["findings"].append(
                        {"file": rel_path, "pattern": "data_minimization",
                         "match": pattern})
                    break

            for pattern in pseudonymization_patterns:
                if pattern in content:
                    results["has_pseudonymization"] = True
                    results["findings"].append(
                        {"file": rel_path, "pattern": "pseudonymization",
                         "match": pattern})
                    break

            for pattern in retention_patterns:
                if pattern in content:
                    results["has_retention_policy"] = True
                    results["findings"].append(
                        {"file": rel_path, "pattern": "retention_policy",
                         "match": pattern})
                    break

    return results


def build_checklist(params):
    """Build a privacy compliance implementation checklist."""
    checklist = []

    # Consent management
    if params.get("has_consent"):
        checklist.append({
            "item": "Consent management system",
            "status": "FOUND",
            "priority": "critical",
        })
    else:
        checklist.append({
            "item": "Consent management system",
            "status": "MISSING",
            "priority": "critical",
            "action": "Implement consent collection with purpose, timestamp, "
                       "and withdrawal mechanism",
        })

    # DSAR handling
    if params.get("has_dsar"):
        checklist.append({
            "item": "DSAR handling workflow",
            "status": "FOUND",
            "priority": "critical",
        })
    else:
        checklist.append({
            "item": "DSAR handling workflow",
            "status": "MISSING",
            "priority": "critical",
            "action": "Implement data subject access request pipeline "
                       "with 30-day SLA tracking",
        })

    # Cross-border transfer safeguards
    if params.get("has_cross_border"):
        checklist.append({
            "item": "Cross-border transfer safeguards",
            "status": "FOUND",
            "priority": "high",
        })
    else:
        checklist.append({
            "item": "Cross-border transfer safeguards",
            "status": "MISSING",
            "priority": "high",
            "action": "Implement transfer validation with adequacy checks "
                       "and consent documentation",
        })

    # Audit logging
    if params.get("has_audit_log"):
        checklist.append({
            "item": "Privacy audit trail",
            "status": "FOUND",
            "priority": "high",
        })
    else:
        checklist.append({
            "item": "Privacy audit trail",
            "status": "MISSING",
            "priority": "high",
            "action": "Add immutable audit logging for consent, DSAR, "
                       "transfers, and breach events",
        })

    # GDPR bridging
    if params.get("has_gdpr_bridge"):
        checklist.append({
            "item": "GDPR dual-compliance bridging",
            "status": "FOUND",
            "priority": "medium",
        })
    else:
        checklist.append({
            "item": "GDPR dual-compliance bridging",
            "status": "MISSING",
            "priority": "medium",
            "action": "Implement region-aware compliance logic for "
                       "Israeli + EU requirements",
        })

    # Data minimization
    if params.get("has_data_minimization"):
        checklist.append({
            "item": "Data minimization patterns",
            "status": "FOUND",
            "priority": "medium",
        })
    else:
        checklist.append({
            "item": "Data minimization patterns",
            "status": "MISSING",
            "priority": "medium",
            "action": "Implement field allowlists per data collection purpose",
        })

    # Pseudonymization
    if params.get("has_pseudonymization"):
        checklist.append({
            "item": "Pseudonymization / anonymization",
            "status": "FOUND",
            "priority": "medium",
        })
    else:
        checklist.append({
            "item": "Pseudonymization / anonymization",
            "status": "MISSING",
            "priority": "medium",
            "action": "Implement identifier hashing or pseudonymization "
                       "for stored personal data",
        })

    # Retention policy
    if params.get("has_retention_policy"):
        checklist.append({
            "item": "Data retention enforcement",
            "status": "FOUND",
            "priority": "medium",
        })
    else:
        checklist.append({
            "item": "Data retention enforcement",
            "status": "MISSING",
            "priority": "medium",
            "action": "Implement automated retention enforcement with "
                       "configurable expiry periods",
        })

    # Database registration check
    record_count = params.get("record_count", 0)
    if record_count >= 10000:
        checklist.append({
            "item": "PPA database registration",
            "status": "REVIEW NEEDED",
            "priority": "critical",
            "action": "Database has 10,000+ records. Verify registration "
                       "with Privacy Protection Authority at "
                       "https://www.gov.il/he/departments/privacy_authority",
        })

    return checklist


def display_results(checklist, scan_path=None):
    """Display compliance checklist results."""
    print("=" * 60)
    print("Israeli Privacy Compliance — Code Pattern Check")
    print("=" * 60)
    if scan_path:
        print(f"Scanned: {scan_path}")
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print()

    found = sum(1 for c in checklist if c["status"] == "FOUND")
    missing = sum(1 for c in checklist if c["status"] == "MISSING")
    review = sum(1 for c in checklist if c["status"] == "REVIEW NEEDED")

    print(f"Results: {found} found, {missing} missing, {review} need review")
    print("-" * 60)

    for i, item in enumerate(checklist, 1):
        icon = "PASS" if item["status"] == "FOUND" else "FAIL"
        if item["status"] == "REVIEW NEEDED":
            icon = "WARN"
        print(f"  [{icon}] {i}. {item['item']} (priority: {item['priority']})")
        if "action" in item:
            print(f"         Action: {item['action']}")

    print()
    print("DISCLAIMER: This tool provides implementation guidance only.")
    print("Consult a privacy attorney for specific compliance decisions.")


def run_example():
    """Run example compliance check."""
    print("=== Example: Fintech Startup Compliance Check ===")
    print()
    params = {
        "has_consent": True,
        "has_dsar": False,
        "has_cross_border": True,
        "has_audit_log": True,
        "has_gdpr_bridge": False,
        "has_data_minimization": False,
        "has_pseudonymization": True,
        "has_retention_policy": False,
        "record_count": 50000,
    }
    checklist = build_checklist(params)
    display_results(checklist)
    return checklist


def main():
    parser = argparse.ArgumentParser(
        description="Israeli Privacy Compliance Code Pattern Checker"
    )
    parser.add_argument(
        "--scan",
        help="Path to project directory to scan for compliance patterns",
        default=None,
    )
    parser.add_argument(
        "--json",
        help="JSON string with compliance parameters (non-interactive mode)",
        default=None,
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path for JSON report",
        default=None,
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Run example compliance check",
    )
    args = parser.parse_args()

    if args.example:
        checklist = run_example()
    elif args.scan:
        scan_results = scan_directory(args.scan)
        checklist = build_checklist(scan_results)
        display_results(checklist, scan_path=args.scan)
    elif args.json:
        try:
            params = json.loads(args.json)
        except json.JSONDecodeError:
            print("Error: Invalid JSON input.", file=sys.stderr)
            sys.exit(1)
        checklist = build_checklist(params)
        display_results(checklist)
    else:
        parser.print_help()
        sys.exit(0)

    if args.output:
        report = {
            "assessment_date": datetime.now().isoformat(),
            "checklist": checklist,
        }
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()
