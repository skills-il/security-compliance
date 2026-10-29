#!/usr/bin/env python3
"""Compute payer exposure under s.24(c) of the Payment Services Law, 5779-2019.

This is a convenience only. The same calculation can be done by hand in a few
seconds, and the skill never depends on running it, so the skill works fine on
hosts that cannot execute scripts.

SCOPE GATE. Chapter VI of the law is headed "misuse of a payment instrument",
and s.1 defines misuse as use "by someone not entitled to it under the payment
services contract". A victim who was deceived into giving a payment order
THEMSELVES was entitled under the contract, so s.24 does not reach that case and
this script must refuse to compute for it. Hence --unauthorised is mandatory.

s.24(c) sets liability BEFORE notice at the LOWER of:
  (1) 75 NIS fixed, plus 30 NIS per day from the day the payer LEARNED of the
      theft, loss or misuse until the day notice was given. Capped at 450 NIS if
      notice was given within 30 days of the FIRST misuse. The day of notice is
      excluded from the count when notice is given on the same day the payer
      learned.
  (2) The amount actually transacted during the misuse BEFORE notice. Charges
      made after notice carry no liability (s.24(b)) and must not be included.

Day counting: this script reads the Interpretation Law, 5741-1981, s.10(a)
(where a period runs "from" a given day, that day is not counted) as applying,
so the day the payer learned is excluded and the day of notice is included
(learned 1 Sept, notice 4 Sept = 3 days). That is a reading, not a settled rule:
counting both ends adds 30 NIS, and the output says so. Same-day notice gives
0 days either way, by the statute's own proviso.

After notice, liability for further misuse is zero (s.24(b)).

Two things this script deliberately does NOT do:
  - It does not apply s.24(d), which removes the whole s.24(c) limit when the payer made
    the essential component available to another person. Whether that provision
    reaches someone DECEIVED into disclosing a code is untested, and no script
    should pretend to resolve it.
  - It does not tell anyone whether they will be reimbursed. It reports what the
    statutory limbs compute to, nothing more.
  - It does not compute anything at all for a transfer the payer gave. There is
    no s.24 figure for that case; the answer is not a smaller number, it is a
    different regime.

Usage:
  python3 liability_clock.py --unauthorised --learned 2026-09-01 \
      --notified 2026-09-04 --amount 4200
  python3 liability_clock.py --unauthorised --learned 2026-09-01 \
      --notified 2026-09-04 --amount 4200 --first-misuse 2026-08-30
"""

import argparse
import math
from datetime import date, datetime

FIXED_COMPONENT = 75
PER_DAY = 30
CAP_WITHIN_30_DAYS = 450
CAP_WINDOW_DAYS = 30


def parse_date(value: str) -> date:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected YYYY-MM-DD, got {value!r}")


def compute(learned: date, notified: date, amount: float, first_misuse: date | None):
    if notified < learned:
        raise SystemExit("Notice cannot precede the day the payer learned.")
    if not math.isfinite(amount) or amount < 0:
        raise SystemExit("The amount must be a finite, non-negative number of NIS.")
    if first_misuse is not None and first_misuse > notified:
        raise SystemExit(
            "The first misuse is after the notice date. Misuse after notice carries no\n"
            "liability at all (s.24(b)), so there is nothing to compute for it here.")

    days = (notified - learned).days
    same_day = days == 0

    limb_one = FIXED_COMPONENT + PER_DAY * days

    cap_applied = False
    if first_misuse is not None:
        within_window = (notified - first_misuse).days <= CAP_WINDOW_DAYS
        if within_window and limb_one > CAP_WITHIN_30_DAYS:
            limb_one = CAP_WITHIN_30_DAYS
            cap_applied = True

    binding = min(limb_one, amount)

    return {
        "days_counted": days,
        "same_day_notice": same_day,
        "limb_one": limb_one,
        "limb_two_amount_transacted": amount,
        "cap_applied": cap_applied,
        "exposure": binding,
        "binding_limb": "fixed+daily" if limb_one <= amount else "amount transacted",
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--unauthorised", action="store_true",
                   help="REQUIRED. Confirms this was use of the payment instrument by someone "
                        "NOT entitled under the payment services contract. If the payer gave the "
                        "payment order themselves, even after being deceived, do NOT pass this "
                        "flag: s.24 does not apply and the script will refuse to compute.")
    p.add_argument("--learned", type=parse_date, required=True,
                   help="Date the payer learned of the theft, loss or misuse (YYYY-MM-DD)")
    p.add_argument("--notified", type=parse_date, required=True,
                   help="Date notice was given to the bank or card issuer (YYYY-MM-DD)")
    p.add_argument("--amount", type=float, required=True,
                   help="Amount of the misuse charges made BEFORE notice was given, in NIS. "
                        "Leave out anything charged after notice: that is 0 NIS under s.24(b).")
    p.add_argument("--first-misuse", type=parse_date, default=None,
                   help="Date of the first misuse, if known. Needed to test the 450 NIS cap.")
    args = p.parse_args()

    if not args.unauthorised:
        raise SystemExit(
            "Refusing to compute.\n\n"
            "s.24 governs only 'misuse' (שימוש לרעה), which s.1 defines as use of the payment\n"
            "instrument by someone NOT entitled to it under the payment services contract.\n\n"
            "Answer this first:\n"
            "  Did someone else use the card or account details?\n"
            "    -> yes: re-run with --unauthorised\n"
            "  Or did the payer move the money themselves after being talked into it?\n"
            "    -> then s.24 does not apply at all. There is no figure to compute here.\n"
            "       The levers are a recall to the beneficiary bank and a police report\n"
            "       carrying the beneficiary details, or s.17 for a card purchase that was\n"
            "       never delivered. See Step 1B of SKILL.md."
        )

    r = compute(args.learned, args.notified, args.amount, args.first_misuse)

    print("Exposure under s.24(c), Payment Services Law 5779-2019")
    print("-" * 56)
    print(f"  Days counted (learned to notice)   : {r['days_counted']}")
    if r["same_day_notice"]:
        print("    Notice given the same day, so no days are counted.")
    print(f"  Limb 1, {FIXED_COMPONENT} + {PER_DAY}/day{' (capped at ' + str(CAP_WITHIN_30_DAYS) + ')' if r['cap_applied'] else ''}"
          f"{'':<4}: {r['limb_one']:.0f} NIS")
    print(f"  Limb 2, charged before notice      : {r['limb_two_amount_transacted']:.0f} NIS")
    print(f"  Binding limb                       : {r['binding_limb']}")
    print()
    # When the first-misuse date is unknown we cannot tell whether the 450 cap bites.
    # Print a RANGE rather than the uncapped figure: the headline number is the one the
    # user quotes to the bank, and quoting an overstated one is the exact failure this
    # skill exists to prevent.
    untested_cap = (
        args.first_misuse is None
        and not r["cap_applied"]
        and r["exposure"] > CAP_WITHIN_30_DAYS
    )
    if untested_cap:
        lo = min(CAP_WITHIN_30_DAYS, r["limb_two_amount_transacted"])
        print(f"  Exposure before notice             : {lo:.0f} to {r['exposure']:.0f} NIS")
        print("    The date of first misuse is unknown, so it is not known whether the")
        print(f"    {CAP_WITHIN_30_DAYS} NIS cap applies. Do NOT quote the upper figure to the bank as")
        print("    if it were settled. Supply --first-misuse to resolve this.")
    else:
        print(f"  Exposure before notice             : {r['exposure']:.0f} NIS")
    print("  Exposure for misuse after notice   : 0 NIS  (s.24(b))")
    if r["days_counted"] > 0:
        print(f"  Day count excludes the day the payer learned (Interpretation Law s.10(a)).")
        print(f"  If the bank counts both ends, limb 1 is {PER_DAY} NIS higher before any cap.")

    both_ends_could_hit_cap = r["limb_one"] + PER_DAY > CAP_WITHIN_30_DAYS and r["days_counted"] > 0
    if args.first_misuse is None and not untested_cap and both_ends_could_hit_cap \
            and r["binding_limb"] == "fixed+daily":
        print()
        print("  Note: --first-misuse was not supplied. On the both-ends count limb 1 would")
        print("        pass 450 NIS, so the cap could then matter. Supply --first-misuse.")
    elif args.first_misuse is None and not untested_cap:
        print()
        print("  Note: --first-misuse was not supplied, but the 450 NIS cap could not")
        print("        change the result here.")

    print()
    print("  Refund is due no later than 8 business days from notice (s.27(a)).")
    print("  A later re-debit requires 15 days' written reasons first (s.27(b)).")
    print()
    print("  This does NOT account for s.24(d), which removes the whole limit where the")
    print("  essential component was made available to another person. Whether")
    print("  that reaches a DECEIVED disclosure is untested. s.26 (the payer acted")
    print("  with intent to deceive) overrides every limit. s.24(e): NO liability at all")
    print("  under (c) or (d) where the provider did not allow notice or cancellation of")
    print("  the instrument, at any time, in a reasonable manner. Not legal advice.")


if __name__ == "__main__":
    main()
