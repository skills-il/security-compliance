#!/usr/bin/env python3
"""
Israeli Privacy Protection Law — Compliance Checker

Standalone script that walks through a compliance assessment for the
Israeli Privacy Protection Law 1981 and 2017 Security Regulations.

Usage:
    python compliance_checker.py --example
    python compliance_checker.py --json '{"record_count":50000,"has_sensitive":true,"is_government":false,"is_health_finance":true,"is_direct_marketing":false,"is_credit_service":false,"has_cross_border":true}'
    python compliance_checker.py --output report.json
"""

import argparse
import json
import sys
from datetime import datetime


def determine_security_level(record_count: int, has_sensitive: bool,
                              is_government: bool, is_health_finance: bool) -> str:
    """Determine the required security level per 2017 regulations."""
    if is_government or is_health_finance or record_count >= 100_000:
        return "high"
    if record_count >= 10_000 or has_sensitive:
        return "medium"
    return "basic"


def check_registration_required(record_count: int, has_sensitive: bool,
                                 is_direct_marketing: bool, is_public_body: bool,
                                 is_credit_service: bool) -> bool:
    """Check if database registration with Privacy Protection Authority is required."""
    if is_public_body:
        return True
    if is_credit_service:
        return True
    if record_count >= 10_000 and is_direct_marketing:
        return True
    if record_count >= 10_000 and has_sensitive:
        return True
    return False


def build_checklist(security_level: str) -> list:
    """Build compliance checklist based on security level."""
    base_checklist = [
        {"item": "Physical security of premises", "level": "basic"},
        {"item": "Access control (user authentication)", "level": "basic"},
        {"item": "Activity logging", "level": "basic"},
        {"item": "Backup procedures", "level": "basic"},
        {"item": "Written security procedures document", "level": "basic"},
        {"item": "Employee awareness training", "level": "basic"},
        {"item": "Privacy policy published (Hebrew)", "level": "basic"},
        {"item": "Consent mechanisms in place", "level": "basic"},
        {"item": "Data subject request handling process", "level": "basic"},
    ]

    medium_additions = [
        {"item": "Encryption of data at rest and in transit", "level": "medium"},
        {"item": "Security officer (memune al bitachon meida) appointed", "level": "medium"},
        {"item": "Periodic access review", "level": "medium"},
        {"item": "Enhanced logging and monitoring", "level": "medium"},
        {"item": "Incident response procedures", "level": "medium"},
        {"item": "Third-party access controls", "level": "medium"},
        {"item": "Data processing agreements with service providers", "level": "medium"},
        {"item": "Cross-border transfer safeguards", "level": "medium"},
    ]

    high_additions = [
        {"item": "Annual security audit by external auditor", "level": "high"},
        {"item": "Comprehensive incident response plan", "level": "high"},
        {"item": "Data Protection Officer (DPO) appointed", "level": "high"},
        {"item": "Penetration testing conducted", "level": "high"},
        {"item": "Advanced encryption standards", "level": "high"},
        {"item": "Detailed data flow mapping", "level": "high"},
        {"item": "Regular employee training program", "level": "high"},
        {"item": "Business continuity plan", "level": "high"},
    ]

    checklist = list(base_checklist)
    if security_level in ("medium", "high"):
        checklist.extend(medium_additions)
    if security_level == "high":
        checklist.extend(high_additions)
    return checklist


def run_interactive_assessment() -> dict:
    """Run an interactive compliance assessment."""
    print("=" * 60)
    print("Israeli Privacy Protection Law — Compliance Assessment")
    print("=" * 60)
    print()
    print("DISCLAIMER: This tool provides guidance only. It does not")
    print("replace legal counsel. Consult a privacy attorney for")
    print("specific compliance decisions.")
    print()

    # Gather information
    org_name = input("Organization name: ").strip() or "Unknown"

    try:
        record_count = int(input("Number of records in your database(s): ").strip())
    except ValueError:
        record_count = 0

    has_sensitive = input("Contains sensitive data? (health, genetics, political, criminal) [y/n]: ").strip().lower() == "y"
    is_government = input("Is this a government/public body? [y/n]: ").strip().lower() == "y"
    is_health_finance = input("Health or financial sector? [y/n]: ").strip().lower() == "y"
    is_direct_marketing = input("Used for direct marketing? [y/n]: ").strip().lower() == "y"
    is_credit_service = input("Credit/financial information service? [y/n]: ").strip().lower() == "y"
    has_cross_border = input("Transfers data outside Israel? [y/n]: ").strip().lower() == "y"

    # Determine results
    security_level = determine_security_level(record_count, has_sensitive,
                                               is_government, is_health_finance)
    registration_required = check_registration_required(record_count, has_sensitive,
                                                         is_direct_marketing,
                                                         is_government or False,
                                                         is_credit_service)
    checklist = build_checklist(security_level)

    # Build report
    report = {
        "assessment_date": datetime.now().isoformat(),
        "organization": org_name,
        "inputs": {
            "record_count": record_count,
            "has_sensitive_data": has_sensitive,
            "is_government": is_government,
            "is_health_finance": is_health_finance,
            "is_direct_marketing": is_direct_marketing,
            "is_credit_service": is_credit_service,
            "has_cross_border_transfer": has_cross_border,
        },
        "results": {
            "security_level": security_level,
            "registration_required": registration_required,
            "cross_border_review_needed": has_cross_border,
        },
        "checklist": checklist,
    }

    # Display results
    print()
    print("=" * 60)
    print("ASSESSMENT RESULTS")
    print("=" * 60)
    print(f"Organization: {org_name}")
    print(f"Security Level Required: {security_level.upper()}")
    print(f"Database Registration Required: {'YES' if registration_required else 'NO'}")
    print(f"Cross-Border Transfer Review: {'NEEDED' if has_cross_border else 'N/A'}")
    print()
    print("COMPLIANCE CHECKLIST:")
    print("-" * 40)
    for i, item in enumerate(checklist, 1):
        print(f"  [ ] {i}. {item['item']} ({item['level']} level)")

    if registration_required:
        print()
        print("ACTION REQUIRED: Register database with Privacy Protection Authority")
        print("URL: https://www.gov.il/he/departments/privacy_authority")

    if has_cross_border:
        print()
        print("ACTION REQUIRED: Review cross-border transfer safeguards")
        print("Ensure recipient country has adequate protection or contractual safeguards")

    print()
    print("REMINDER: Consult a licensed privacy attorney (orech din)")
    print("for specific compliance decisions.")

    return report


def run_from_json(json_input: str, org_name: str = "Unknown") -> dict:
    """Run compliance assessment from JSON input (non-interactive).

    Args:
        json_input: JSON string with assessment parameters.
        org_name: Organization name.

    Returns:
        Assessment report dictionary.
    """
    try:
        params = json.loads(json_input)
    except json.JSONDecodeError:
        print("Error: Invalid JSON input.", file=sys.stderr)
        sys.exit(1)

    record_count = params.get("record_count", 0)
    has_sensitive = params.get("has_sensitive", False)
    is_government = params.get("is_government", False)
    is_health_finance = params.get("is_health_finance", False)
    is_direct_marketing = params.get("is_direct_marketing", False)
    is_credit_service = params.get("is_credit_service", False)
    has_cross_border = params.get("has_cross_border", False)

    security_level = determine_security_level(record_count, has_sensitive,
                                               is_government, is_health_finance)
    registration_required = check_registration_required(record_count, has_sensitive,
                                                         is_direct_marketing,
                                                         is_government,
                                                         is_credit_service)
    checklist = build_checklist(security_level)

    report = {
        "assessment_date": datetime.now().isoformat(),
        "organization": org_name,
        "inputs": {
            "record_count": record_count,
            "has_sensitive_data": has_sensitive,
            "is_government": is_government,
            "is_health_finance": is_health_finance,
            "is_direct_marketing": is_direct_marketing,
            "is_credit_service": is_credit_service,
            "has_cross_border_transfer": has_cross_border,
        },
        "results": {
            "security_level": security_level,
            "registration_required": registration_required,
            "cross_border_review_needed": has_cross_border,
        },
        "checklist": checklist,
    }

    print(f"Organization: {org_name}")
    print(f"Security Level Required: {security_level.upper()}")
    print(f"Database Registration Required: {'YES' if registration_required else 'NO'}")
    print(f"Cross-Border Transfer Review: {'NEEDED' if has_cross_border else 'N/A'}")
    print(f"Checklist items: {len(checklist)}")

    return report


def run_example() -> dict:
    """Run a demo assessment with example data."""
    print("=== Example: Israeli Health-Tech Startup ===")
    print()
    example_json = json.dumps({
        "record_count": 50000,
        "has_sensitive": True,
        "is_government": False,
        "is_health_finance": True,
        "is_direct_marketing": False,
        "is_credit_service": False,
        "has_cross_border": True,
    })
    report = run_from_json(example_json, org_name="Example Health-Tech Startup")
    print()
    print("COMPLIANCE CHECKLIST:")
    print("-" * 40)
    for i, item in enumerate(report["checklist"], 1):
        print(f"  [ ] {i}. {item['item']} ({item['level']} level)")
    return report


def main():
    parser = argparse.ArgumentParser(
        description="Israeli Privacy Protection Law Compliance Checker"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path for JSON report",
        default=None
    )
    parser.add_argument(
        "--json",
        help='JSON string with parameters (non-interactive mode)',
        default=None
    )
    parser.add_argument(
        "--org-name",
        help="Organization name (used with --json)",
        default="Unknown"
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Run example assessment"
    )
    args = parser.parse_args()

    if args.example:
        report = run_example()
    elif args.json:
        report = run_from_json(args.json, args.org_name)
    else:
        report = run_interactive_assessment()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()
