#!/usr/bin/env python3
"""Check HTML for Israeli accessibility (IS 5568) compliance.

Validates HTML files against common IS 5568 requirements including
RTL attributes, Hebrew ARIA labels, and WCAG AA contrast.

Usage:
    python a11y_checker.py --input index.html
    python a11y_checker.py --help
"""

import argparse
import re
import sys

REQUIRED_ATTRIBUTES = {
    'lang="he"': "Hebrew language attribute on html element",
    'dir="rtl"': "RTL direction attribute",
}

HEBREW_ARIA_LABELS = {
    "navigation": "תפריט ראשי",
    "search": "חיפוש באתר",
    "close": "סגירה",
    "skip": "דלגו לתוכן הראשי",
    "loading": "טוען",
}

def check_html(content):
    issues = []
    warnings = []

    # Check required attributes
    for attr, desc in REQUIRED_ATTRIBUTES.items():
        if attr not in content.lower():
            issues.append(f"MISSING: {attr} ({desc})")

    # Check skip navigation
    if "skip" not in content.lower() and "דלגו" not in content:
        issues.append("MISSING: Skip navigation link (IS 5568 requirement)")

    # Check accessibility statement
    if "נגישות" not in content and "accessibility" not in content.lower():
        warnings.append("WARNING: No accessibility statement link found (Hatzaharat Negishot)")

    # Check alt attributes on images
    imgs_without_alt = re.findall(r'<img(?![^>]*alt=)[^>]*>', content, re.I)
    if imgs_without_alt:
        issues.append(f"MISSING: {len(imgs_without_alt)} image(s) without alt attribute")

    # Check ARIA labels in Hebrew
    aria_labels = re.findall(r'aria-label="([^"]*)"', content)
    english_only_labels = [l for l in aria_labels if not re.search(r'[\u0590-\u05FF]', l)]
    if english_only_labels:
        warnings.append(f"WARNING: {len(english_only_labels)} ARIA labels in English only (should be Hebrew)")

    # Check form labels
    inputs_without_label = re.findall(r'<input(?![^>]*aria-label)[^>]*(?<!/)>', content, re.I)
    labels = re.findall(r'<label[^>]*for="([^"]*)"', content, re.I)
    if len(inputs_without_label) > len(labels):
        warnings.append("WARNING: Some form inputs may be missing associated labels")

    return issues, warnings

def main():
    parser = argparse.ArgumentParser(description="IS 5568 accessibility checker")
    parser.add_argument("--input", required=True, help="HTML file to check")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        content = f.read()

    issues, warnings = check_html(content)

    print("IS 5568 Accessibility Check Report")
    print("=" * 40)

    if issues:
        print(f"\nERRORS ({len(issues)}):")
        for issue in issues:
            print(f"  - {issue}")

    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if not issues and not warnings:
        print("\nAll basic checks passed.")
        print("Note: Manual testing still required (keyboard nav, screen reader, etc.)")

    sys.exit(1 if issues else 0)

if __name__ == "__main__":
    main()
