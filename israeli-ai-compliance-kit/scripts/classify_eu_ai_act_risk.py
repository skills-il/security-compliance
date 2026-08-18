#!/usr/bin/env python3
"""Classify an AI system under the EU AI Act (Regulation 2024/1689).

Walks through a question tree covering Article 5 (prohibited), Annex III
(high-risk categories), limited-risk transparency obligations, and GPAI
obligations. Outputs a classification, reasoning, and a next-step checklist
for Israeli providers.

Not legal advice. Use with counsel for production deployments.

Usage:
    python classify_eu_ai_act_risk.py              # interactive
    python classify_eu_ai_act_risk.py --example    # run against a sample input
    python classify_eu_ai_act_risk.py --input case.json
"""

import argparse
import json
import sys

ANNEX_III_CATEGORIES = [
    ("biometrics", "Biometric identification, categorization, or emotion recognition"),
    ("critical_infra", "Safety components of critical infrastructure"),
    ("education", "Education, vocational training, student assessment"),
    ("employment", "Recruitment, worker management, access to self-employment"),
    ("essential_services", "Credit scoring, insurance underwriting, public benefits"),
    ("law_enforcement", "Policing, evidence assessment, profiling for crime"),
    ("migration", "Migration, asylum, border control"),
    ("justice", "Administration of justice, democratic processes"),
]

PROHIBITED_PRACTICES = [
    ("social_scoring", "General-purpose social scoring by public authorities"),
    ("biometric_public", "Real-time remote biometric ID in public for law enforcement"),
    ("emotion_work_school", "Emotion recognition in workplace or educational settings"),
    ("predictive_policing_profile", "Predictive policing based solely on profiling"),
    ("untargeted_scraping_face", "Untargeted scraping of facial images from the internet"),
    ("vulnerability_exploitation", "Exploiting vulnerabilities of specific groups"),
]


def ask_yn(q: str) -> bool:
    while True:
        ans = input(f"{q} [y/n]: ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please answer y or n.")


def classify(answers: dict) -> dict:
    reasons = []
    next_steps = []

    # Step 1: prohibited?
    for key, label in PROHIBITED_PRACTICES:
        if answers.get(f"prohibited_{key}"):
            return {
                "classification": "Prohibited",
                "reasons": [f"Matches prohibited practice: {label}"],
                "next_steps": ["Cannot be placed on the EU market. Redesign or exclude EU."],
            }

    # Step 2: in scope?
    in_scope = (
        answers.get("eu_placed_on_market")
        or answers.get("eu_put_into_service")
        or answers.get("eu_output_used")
    )
    if not in_scope:
        return {
            "classification": "Out of scope",
            "reasons": [
                "System is not placed on the EU market, not put into service in the EU, "
                "and its output is not used in the EU."
            ],
            "next_steps": [
                "Re-run this classification if EU deployment plans change.",
                "Document the scoping decision with date and owner.",
            ],
        }

    # Step 3: GPAI?
    if answers.get("is_gpai"):
        gpai_obligations = [
            "Technical documentation for downstream developers",
            "Information summary of copyrighted training data",
            "Copyright policy for TDM opt-outs",
            "Compliance with Union copyright law",
        ]
        if answers.get("gpai_systemic_risk"):
            gpai_obligations += [
                "Model evaluations and adversarial testing",
                "Cybersecurity protections",
                "Serious incident reporting",
                "Track Article 51 thresholds and designation procedures",
            ]
        reasons.append("System is a general-purpose AI model.")
        next_steps += gpai_obligations

    # Step 4: high-risk?
    matched_annex = [
        label for key, label in ANNEX_III_CATEGORIES if answers.get(f"annex_iii_{key}")
    ]
    if matched_annex:
        reasons.append(f"Matches Annex III category: {'; '.join(matched_annex)}")
        next_steps += [
            "Implement risk management system across the lifecycle",
            "Ensure data governance for training, validation, and test sets",
            "Produce technical documentation per Annex IV",
            "Enable logging for traceability",
            "Provide transparency and information to deployers",
            "Enable human oversight",
            "Meet accuracy, robustness, and cybersecurity requirements",
            "Implement quality management system",
            "Perform conformity assessment (Annex VI or VII)",
            "Register in the EU database",
            "Apply CE marking",
            "Appoint authorized representative in the EU (Article 22)",
            "Establish post-market monitoring and incident reporting",
        ]
        if answers.get("is_gpai"):
            return {
                "classification": "High-risk + GPAI",
                "reasons": reasons,
                "next_steps": next_steps,
            }
        return {
            "classification": "High-risk",
            "reasons": reasons,
            "next_steps": next_steps,
        }

    # Step 5: limited-risk transparency?
    if (
        answers.get("is_chatbot_or_voice")
        or answers.get("is_deepfake_or_synthetic")
        or answers.get("is_emotion_recognition_general")
    ):
        reasons.append("System interacts with users or produces synthetic content.")
        next_steps += [
            "Disclose to users that they interact with AI",
            "Mark synthetic content as machine-readable AI-generated",
            "Inform users when emotion recognition or biometric categorization is used",
        ]
        if answers.get("is_gpai"):
            return {
                "classification": "Limited-risk + GPAI",
                "reasons": reasons,
                "next_steps": next_steps,
            }
        return {
            "classification": "Limited-risk",
            "reasons": reasons,
            "next_steps": next_steps,
        }

    if answers.get("is_gpai"):
        label = (
            "GPAI with systemic risk"
            if answers.get("gpai_systemic_risk")
            else "GPAI (no additional risk tier)"
        )
        return {
            "classification": label,
            "reasons": reasons,
            "next_steps": next_steps,
        }

    return {
        "classification": "Minimal-risk",
        "reasons": ["System does not trigger prohibited, high-risk, or limited-risk categories."],
        "next_steps": [
            "Consider voluntary codes of conduct",
            "Document the decision and review periodically",
        ],
    }


def interactive() -> dict:
    print("EU AI Act classifier. Answer each question y or n.\n")
    a = {}
    print("--- Prohibited practices ---")
    for key, label in PROHIBITED_PRACTICES:
        a[f"prohibited_{key}"] = ask_yn(label)
    print("\n--- EU scope ---")
    a["eu_placed_on_market"] = ask_yn("Is the system placed on the EU market?")
    a["eu_put_into_service"] = ask_yn("Is it put into service in the EU under your name?")
    a["eu_output_used"] = ask_yn("Is the system output used in the EU?")
    print("\n--- System type ---")
    a["is_gpai"] = ask_yn("Is the system a general-purpose AI model (foundation model)?")
    if a["is_gpai"]:
        a["gpai_systemic_risk"] = ask_yn(
            "Does the GPAI model meet the systemic-risk threshold (e.g. 10^25 FLOPs training)?"
        )
    print("\n--- Annex III categories ---")
    for key, label in ANNEX_III_CATEGORIES:
        a[f"annex_iii_{key}"] = ask_yn(label)
    print("\n--- Limited-risk transparency ---")
    a["is_chatbot_or_voice"] = ask_yn("Does the system interact with users via chat or voice?")
    a["is_deepfake_or_synthetic"] = ask_yn("Does it produce synthetic audio, image, or video?")
    a["is_emotion_recognition_general"] = ask_yn("Does it perform emotion recognition outside work/school?")
    return a


def render(result: dict) -> str:
    lines = [f"## Classification: {result['classification']}", "", "### Reasoning"]
    for r in result["reasons"]:
        lines.append(f"- {r}")
    lines.append("")
    lines.append("### Next Steps")
    for s in result["next_steps"]:
        lines.append(f"- {s}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Classify an AI system under the EU AI Act.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--input", help="JSON file of answers (skip interactive)")
    parser.add_argument("--example", action="store_true", help="Run with a sample Hebrew summarizer")
    args = parser.parse_args()

    if args.example:
        answers = {
            "eu_placed_on_market": False,
            "eu_put_into_service": False,
            "eu_output_used": False,
            "is_gpai": False,
            "is_chatbot_or_voice": False,
            "is_deepfake_or_synthetic": False,
            "is_emotion_recognition_general": False,
        }
        for key, _ in PROHIBITED_PRACTICES:
            answers[f"prohibited_{key}"] = False
        for key, _ in ANNEX_III_CATEGORIES:
            answers[f"annex_iii_{key}"] = False
    elif args.input:
        try:
            with open(args.input, "r", encoding="utf-8") as f:
                answers = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Error loading input: {e}", file=sys.stderr)
            return 1
    else:
        answers = interactive()

    result = classify(answers)
    print(render(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
