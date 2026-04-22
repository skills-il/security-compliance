#!/usr/bin/env python3
"""
check_standard.py - rules-based Israeli standards import checker.

Takes a product category keyword and returns:
  - applicable Israeli Standard (SI) numbers
  - whether the standard is declared mandatory (takan rishmi)
  - recommended approval route
  - required lab tests / documents
  - typical timeline band
  - fast-track eligibility

Every rule below maps to an entry in evidence.json. If you add a new
category or change a rule, add matching evidence first.

Usage:
    python scripts/check_standard.py --list
    python scripts/check_standard.py --category toy
    python scripts/check_standard.py --category hair-dryer
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass, field


@dataclass
class StandardRule:
    category: str
    aliases: list[str]
    si_numbers: list[str]
    mandatory: bool
    approval_route: str
    required_tests: list[str]
    timeline_band: str
    fast_track: str
    notes: str
    authority: str


RULES: list[StandardRule] = [
    StandardRule(
        category="toy",
        aliases=["toys", "children-toy", "ride-on", "plush", "doll", "finger-paint"],
        si_numbers=["SI 562 part 1", "SI 562 part 2", "SI 562 part 3", "SI 562 part 7"],
        mandatory=True,
        approval_route="Type approval by SII, or EU-recognition route via Toy Safety Directive from Feb/Mar 2025",
        required_tests=[
            "EN 71-1 mechanical/physical",
            "EN 71-2 flammability",
            "EN 71-3 chemical migration",
            "Hebrew user manual / labelling",
        ],
        timeline_band="Type approval: weeks. EU route: days after notification if dossier is complete.",
        fast_track="Toy safety is in the phased 2025 EU-recognition catalogue.",
        notes="SI 562 part 3 was revised November 2022 with transition until 16 April 2023. Battery-powered toys may also trigger SI 900 electrical safety.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="household-electrical",
        aliases=["hair-dryer", "kettle", "dishwasher", "microwave", "blender", "toaster", "appliance"],
        si_numbers=["SI 900 (family)", "e.g., SI 900 part 2.5 dishwashers", "SI 900 part 2.29 battery chargers"],
        mandatory=True,
        approval_route="Type approval by SII plus shipment approval, or Green/Gold/Diamond easement plan once eligible",
        required_tests=[
            "IEC 60335-1 safety",
            "Relevant IEC 60335-2-xx particular requirements",
            "EMC per SII EMC rules",
            "Hebrew user manual",
        ],
        timeline_band="Type approval typically several weeks; subsequent shipments days with a valid product file.",
        fast_track="NOT available via January 2025 EU-recognition route: AC mains 50-1000 V AC / 75-1500 V DC is explicitly excluded.",
        notes="Declaration-based entry (July 2024) possible with ILAC-accredited report but random surveillance applies.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="food-contact-plastic",
        aliases=["plastic-container", "food-packaging", "baby-bottle", "food-contact"],
        si_numbers=["SI 5113"],
        mandatory=True,
        approval_route="SII filing, accepts US FDA or EU Directive dossier as fallback",
        required_tests=[
            "Migration testing per SI 5113",
            "FDA 21 CFR compliance documentation (if applicable)",
            "EU Regulation 10/2011 compliance (if applicable)",
        ],
        timeline_band="Varies with dossier completeness; usually weeks.",
        fast_track="Food-contact materials phased into the EU-recognition catalogue from March 2025.",
        notes="Use FDA 21 CFR where available; otherwise EU Directive; otherwise Israeli Ministry of Health rules.",
        authority="Standards Institution of Israel (SII), https://www.sii.org.il",
    ),
    StandardRule(
        category="cosmetic",
        aliases=["cosmetics", "skincare", "moisturiser", "shampoo", "cream", "makeup"],
        si_numbers=["Pharmacists' Regulations (Cosmetics) 5783-2022"],
        mandatory=True,
        approval_route="Notification to the Israeli Ministry of Health (MoH) confirming EU compliance; no SII testing required if dossier is complete",
        required_tests=[
            "EU CPNP file",
            "EU safety assessment",
            "Manufacturing facility documentation",
        ],
        timeline_band="Immediate upon valid notification; registration fee cancelled after reform.",
        fast_track="Notification model replaces the old SII + MoH registration regime.",
        notes="Regulated by the Ministry of Health, not SII. Old SII testing + registration pathway is superseded.",
        authority="Israeli Ministry of Health, https://www.gov.il/en/service/application-for-cosmetic-import-permits",
    ),
    StandardRule(
        category="motor-vehicle",
        aliases=["car", "passenger-car", "truck", "motorcycle", "vehicle"],
        si_numbers=["Israeli Mandatory Requirements (IMR 2025)"],
        mandatory=True,
        approval_route="Type approval via a licensed importer under the Ministry of Transport and Road Safety",
        required_tests=[
            "EU 2018/858 WVTA homologation (accepted)",
            "US or Canadian homologation (accepted as technical prerequisite)",
            "Notarised Israeli Registration Requirements",
        ],
        timeline_band="Homologation lead time typically months for a new model; personal imports follow a separate procedure.",
        fast_track="NOT in the January 2025 EU-regulation catalogue. IMR already recognises EU 2018/858.",
        notes="Personal imports have their own procedure at gov.il Ministry of Transport.",
        authority="Ministry of Transport and Road Safety, https://www.gov.il/en/departments/units/vehicle_division_maintenance_services",
    ),
    StandardRule(
        category="radio-wireless",
        aliases=["drone", "router", "bluetooth", "wifi", "iot", "radio"],
        si_numbers=["Wireless Telegraph Regulations (Certificates of Compliance) Amendment, 4 July 2022"],
        mandatory=True,
        approval_route="Ministry of Communications DoC/CoC based on EU regulations for the radio portion; SII filing for electrical safety and EMC",
        required_tests=[
            "EU RED (2014/53/EU) test suite",
            "EMC report",
            "Electrical safety (if mains powered)",
        ],
        timeline_band="Days to weeks depending on MoC workload.",
        fast_track="Radio portion accepts EU DoC/CoC since 4 July 2022.",
        notes="Mains-powered radio devices still trigger SI 900 evaluation.",
        authority="Ministry of Communications and SII",
    ),
    StandardRule(
        category="food",
        aliases=["packaged-food", "grocery", "beverage", "dairy", "infant-formula"],
        si_numbers=["Public Health (Food) regulations; 2016 parallel-import framework (Model A/B)"],
        mandatory=True,
        approval_route="Ministry of Health parallel-import / declaration path; SII is not the regulator",
        required_tests=[
            "Hebrew labelling",
            "Ministry of Health notification / declaration",
            "Certificate of origin and manufacturer documentation",
        ],
        timeline_band="Varies by sub-category (fresh, processed, infant formula, etc.).",
        fast_track="Food is EXCLUDED from the January 2025 EU-regulation catalogue. Use the Ministry of Health framework instead.",
        notes="2016 reform enabled parallel imports; check Kol Zchut and Ministry of Health guidance.",
        authority="Israeli Ministry of Health",
    ),
    StandardRule(
        category="ppe",
        aliases=["personal-protective-equipment", "helmet", "safety-goggles", "respirator", "gloves"],
        si_numbers=["Applicable SI standards aligned with EU PPE Regulation (EU) 2016/425"],
        mandatory=True,
        approval_route="EU-recognition route via PPE Regulation from 1 January 2025, or type approval fallback",
        required_tests=[
            "EU-notified body test report (Category II and III)",
            "EU Declaration of Conformity",
            "Instruction leaflet including Hebrew",
        ],
        timeline_band="EU route: days after filing. Type approval fallback: weeks.",
        fast_track="PPE is in the first wave of the January 2025 EU-recognition catalogue.",
        notes="PPE was named explicitly in the initial catalogue.",
        authority="SII and Ministry of Economy Commissioner of Standardization",
    ),
    StandardRule(
        category="chemical",
        aliases=["chemicals", "industrial-chemical", "cleaning-product"],
        si_numbers=["Israeli chemical-safety standards aligned with REACH"],
        mandatory=True,
        approval_route="EU-recognition route via REACH from 1 January 2025; specific SI standards apply for consumer products",
        required_tests=[
            "REACH registration dossier (if applicable)",
            "Safety Data Sheet in Hebrew",
        ],
        timeline_band="Depends on category and volume.",
        fast_track="Chemical safety (REACH) is in the first wave of the 2025 EU-recognition catalogue.",
        notes="Hazardous substances may need a Ministry of Environmental Protection permit.",
        authority="SII and Ministry of Environmental Protection",
    ),
]


def find_rule(query: str) -> StandardRule | None:
    q = query.strip().lower().replace("_", "-")
    for rule in RULES:
        if q == rule.category or q in rule.aliases:
            return rule
    for rule in RULES:
        if q in rule.category or any(q in alias for alias in rule.aliases):
            return rule
    return None


def format_rule(rule: StandardRule) -> str:
    out = []
    out.append(f"Category: {rule.category}")
    out.append(f"Applicable SI numbers: {', '.join(rule.si_numbers)}")
    out.append(f"Mandatory (takan rishmi): {'yes' if rule.mandatory else 'no'}")
    out.append(f"Recommended approval route: {rule.approval_route}")
    out.append("Required tests / documents:")
    for item in rule.required_tests:
        out.append(f"  - {item}")
    out.append(f"Typical timeline: {rule.timeline_band}")
    out.append(f"Fast-track: {rule.fast_track}")
    out.append(f"Authority: {rule.authority}")
    out.append(f"Notes: {rule.notes}")
    out.append("")
    out.append("Disclaimer: regulatory guidance only, not legal advice. Verify the current mandatory-standards list on https://www.sii.org.il before filing.")
    return "\n".join(out)


def list_categories() -> str:
    lines = ["Supported categories:"]
    for rule in RULES:
        alias_str = ", ".join(rule.aliases[:4])
        lines.append(f"  - {rule.category} (aliases: {alias_str})")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--category", help="Product category keyword (e.g., toy, hair-dryer, cosmetic)")
    parser.add_argument("--list", action="store_true", help="List supported categories")
    parser.add_argument("--json", action="store_true", help="Output result as JSON")
    args = parser.parse_args(argv)

    if args.list:
        print(list_categories())
        return 0

    if not args.category:
        parser.print_help()
        return 1

    rule = find_rule(args.category)
    if rule is None:
        print(f"No rule for category '{args.category}'. Run with --list to see supported categories.", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(asdict(rule), indent=2, ensure_ascii=False))
    else:
        print(format_rule(rule))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
