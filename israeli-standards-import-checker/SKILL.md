---
name: israeli-standards-import-checker
description: "Check whether a product requires Standards Institution of Israel (SII, Mechon HaTikanim) approval under an official standard (takan rishmi) before it can be imported into Israel. Returns applicable SI numbers, approval route (type approval, shipment approval, Maslol Plus declaration, EU-CoC recognition), required lab tests, timelines, and fast-track options based on the 2016 food parallel-import reform and the 2022/2025 electronics + EU-regulation reforms. Use when a user asks about importing electronics, toys, cosmetics, food-contact materials, vehicles, or building materials into Israel, asks about CE/type approval, or has a shipment stuck at Israeli customs. Do NOT use for customs duty calculation (use israeli-customs-duty-calculator) or for general product safety review outside the Israeli regulatory context."
license: MIT
compatibility: Works with Claude Code, Claude.ai, Cursor, and other coding agents. Network access helpful for verifying current SI standard lists on the SII website.
---

# Israeli Standards Import Checker

## Problem

Products regularly get stuck, seized, or fined at Israeli customs when the importer fails to show compliance with a mandatory Israeli Standard (takan rishmi). The rules changed substantially with the 2022 electronics reform and the January 2025 "What's Good for Europe is Good for Israel" EU-recognition reform, and the old "just use CE" shortcut still does not work for many categories (for example AC mains electrical equipment in the 50-1000 V range). Importers and their advisors need a structured way to check, per product, which SI number applies, which approval route is open, and what documentation the shipment must carry.

## Instructions

Always state at the start: this skill gives regulatory guidance, not legal advice. For a specific shipment, verify the current mandatory standards list on the SII website and consult the Commissioner of Standardization or a licensed customs broker.

### Step 1: Identify the product category

Ask for, or infer from the user's input:
- Product type (e.g., LED lamp, children's ride-on toy, hair dryer, infant formula, plastic food container, passenger car, drone)
- Intended use (consumer, commercial, industrial)
- Voltage / power rating for electrical products
- Age range for toys
- Whether it is a personal import (ye'vu ishi) or commercial

### Step 2: Check whether the category has an official Israeli Standard (takan rishmi)

A takan rishmi is mandatory; a plain takan yisra'eli is voluntary. Only the Minister of Economy can declare a standard mandatory, and the Commissioner of Standardization enforces it. The master list lives on the SII website and is updated through the official gazette Reshumot.

Common categories with mandatory standards (verify current status before relying on these in a filing):

| Category | Typical SI | Notes |
|---|---|---|
| Toys | SI 562 (parts 1, 2, 3, 7 ...) | Based on EN 71. Part 3 (chemical migration) last revised November 2022. |
| Household electrical appliances | SI 900 family (equivalent to IEC 60335-1) | Many sub-parts are mandatory (e.g., 2.5 dishwashers, 2.29 chargers). |
| Plastic food-contact materials | SI 5113 | Accepts US FDA or EU Directive as fallback. |
| Cosmetics | Pharmacists' Regulations (Cosmetics) 5783-2022, MoH notification | Post-reform: notification only for EU-compliant products, registration fee cancelled. |
| Passenger vehicles | Israeli Mandatory Requirements (IMR) | Adopts EU 2018/858 WVTA; US/Canadian homologation accepted. |
| Food | Various public-health regulations | Covered by the 2016 food-import reform (parallel import + Model A/B). |

### Step 3: Determine the approval route

Pick the route that fits the category and reform status:

1. Type approval (ishur tipus) by SII: covers a specific model; once granted, subsequent shipments of the same model can use shipment approvals or an easement plan. Required for categories still excluded from EU recognition (for example AC mains electrical equipment 50-1000 V AC / 75-1500 V DC).
2. Per-shipment approval: each shipment is sampled and tested before release. Default for new importers and Group 2/3 (higher-risk) products.
3. Importer easement plans via Maslol Plus: Green (50% sample), Gold (33% sample after 12 months on Green), Diamond (sell before testing completes). Available only for Group 1 products with a clean history and ISO 9001 factory.
4. Declaration-based entry: from July 1, 2024, importers can declare compliance using ILAC-accredited foreign lab reports; spot-checked under the Ministry of Economy's random-surveillance programme (from July 7, 2024).
5. EU-CoC / EU-regulation recognition: from January 1, 2025 a catalogue of ~42 EU regulations is an optional import route (REACH, LVD, EMC, PPE first; toys and food-contact materials phased in from February/March 2025). Food, motor vehicles, and official fire-safety-covered items are excluded.
6. Radio / wireless: under the July 4, 2022 Ministry of Communications amendment, DoC/CoC compliant with EU regulations is accepted for radio equipment.

### Step 4: List required lab tests and documents

Typical documentation package:
- Manufacturer test report from an ILAC-accredited lab
- Product file (tik mutzar) with technical drawings, BOM, and user manual (Hebrew required for consumer products)
- CE Declaration of Conformity and EU test reports (for the EU recognition route)
- Importer declaration form and Maslol Plus submission
- Sample units for SII testing when the route requires it

### Step 5: Estimate a timeline

Give a rough band and flag that exact turnaround depends on SII queue, category, and whether the product file already exists. Do not invent fee numbers; point the user to the SII importer service centre for the current fee schedule:
- Electrical: 03-6465160
- Electronics: 03-6465050
- Chemicals / health / environment: 03-6465138
- Mechanics / hydraulics: 03-6465141

### Step 6: Flag fast-track options

If the product qualifies for the EU-recognition route, the declaration-based route, or an easement plan, recommend that as the primary filing. Note the residual risk: random surveillance can still sample the shipment, and a failed sample can trigger market withdrawal and fines.

### Step 7: Warn about non-compliance consequences

Imports arriving without the correct approval can be held, seized, or destroyed at customs. Businesses are legally obliged to notify the Commissioner of Standardization if a product later fails to meet mandatory requirements.

## Examples

### Example 1: CE-marked children's ride-on toy

User says: "I want to import a CE-marked electric ride-on car for toddlers from a European brand."
Result: Toys are covered by SI 562 (mandatory, based on EN 71). From February 2025, toy safety is in the EU-recognition catalogue, so CE plus a DoC aligned with the Toy Safety Directive can potentially use the EU route. The battery and motor parts may still trigger SI 900 (electrical safety), which is not yet in the EU fast-track. Recommend: open a product file with SII Electrical (03-6465160), submit via Maslol Plus, keep the EN 71 test report and EU DoC with the shipment.

### Example 2: Imported hair dryer (220 V)

User says: "We're bringing 500 hair dryers from China."
Result: Hair dryers are household electrical appliances under the SI 900 family. Because AC mains equipment in the 50-1000 V range is still excluded from the January 2025 EU-recognition fast track, CE alone is not enough. Route: type approval by SII plus per-shipment sampling, or Green/Gold easement plan once a clean record is built. Ensure the manual is in Hebrew.

### Example 3: EU-compliant skincare cream

User says: "A French brand wants to sell a moisturiser in Israel."
Result: Covered by the Pharmacists' Regulations (Cosmetics) 5783-2022. The reform replaced the old SII + MoH registration pathway with a notification to the Israeli Ministry of Health confirming EU compliance. Registration fee is cancelled. No SII lab test required if the EU dossier is in order, but keep the EU CPNP file and safety assessment available.

## Bundled Resources

### References

- `references/common-official-standards.md` - Table of common product categories and their SI (Israeli Standard) numbers. Consult when you need to look up the standard number for a specific product type.
- `references/approval-routes.md` - Decision guide between type approval, shipment approval, easement plans, declaration-based entry, and EU-CoC recognition. Consult when picking a filing route.
- `references/fast-track-options.md` - Rules for the 2016 food parallel-import reform, the 2022 electronics/radio reforms, and the 2025 EU-regulation recognition catalogue. Consult when assessing whether a shortcut applies.

### Scripts

- `scripts/check_standard.py` - Hardcoded rules engine that takes a product category and returns applicable SI numbers, whether the standard is mandatory, the recommended approval route, required tests, and typical timeline band. Run: `python scripts/check_standard.py --category toy` or `--list` to see supported categories.

## Recommended MCP Servers

No MCP server currently wraps the SII or the Commissioner of Standardization. Until one exists, verify live standards lists directly on the SII website (https://www.sii.org.il) and the Ministry of Economy's standardization policy page. A future MCP could expose Maslol Plus and the Reshumot gazette.

## Gotchas

- Voluntary (takan yisra'eli) vs official (takan rishmi) is a frequent trap. A product can meet a standard that is not mandatory and still be blocked at customs because a different mandatory standard applies.
- The January 2025 EU-recognition catalogue covers only the listed regulations (REACH, LVD, EMC, PPE first, toys and food-contact materials phased in). AC mains electrical equipment 50-1000 V AC / 75-1500 V DC is explicitly excluded; food, motor vehicles, and items under official fire-safety standards are also excluded. Agents often assume CE is now universally accepted; it is not.
- A type approval (ishur tipus) covers a specific model only. Sister models, different voltages, or firmware variants need fresh filings.
- Samples must usually be sent and tested before the shipment arrives, not after. Planning the test slot late is a common delay cause.
- Israeli standards are revised by publication in Reshumot, sometimes with very short transition windows (SI 562 part 3 gave only five months in 2022-2023). Always check the current version, not a cached PDF.
- Personal imports (ye'vu ishi) follow a lighter regime than commercial imports and often pass under exemption thresholds, but the exemption does not cover resale.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| SII home (English) | https://www.sii.org.il/en | Contact centres, standards, certifications |
| SII importers | https://www.sii.org.il/en/importers/ | Maslol Plus filing, importer contact emails |
| SII services and tracks | https://www.sii.org.il/en/services-and-tracks/ | Overview of importer services |
| SII easement plans | https://www.sii.org.il/en/tracks/ | Green / Gold / Diamond plan rules |
| Commissioner of Standardization (Ministry of Economy) | https://www.gov.il/en/departments/general/standartization_policy_in_israel_legislation | Enforcement policy, mandatory standards, Reshumot |
| Standards Law 5713-1953 (Knesset) | https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawPrimary.aspx?t=lawlaws&st=lawlaws&lawitemid=2000626 | Primary statute |
| US ITA standards guide | https://www.trade.gov/country-commercial-guides/israel-trade-standards | Plain-English overview, declaration reform |
| Kol Zchut | https://www.kolzchut.org.il | Consumer rights on imports (Hebrew) |

## Troubleshooting

### Error: "Customs is holding our shipment, says no standards certificate"

Cause: The product probably falls under an official standard (takan rishmi) and no type approval or declaration was filed before the container arrived.
Solution: Contact the relevant SII importer centre (electrical 03-6465160, electronics 03-6465050, chemicals 03-6465138, mechanics 03-6465141) and file retroactively via Maslol Plus. Arrange sampling at the port. If release is urgent, a customs broker can sometimes request a limited shipment approval.

### Error: "CE should be enough, why is SII still asking for tests?"

Cause: The category is outside the January 2025 EU-recognition catalogue, or the product is AC mains electrical equipment (50-1000 V AC / 75-1500 V DC) which is explicitly excluded.
Solution: Use type approval by SII or the importer easement plan instead. Keep the EU test reports, since they speed up the SII file even when full recognition is not available.

### Error: "Our factory changed component supplier; can we still use the same type approval?"

Cause: Type approvals cover a specific model configuration. Material changes can invalidate it.
Solution: Contact the SII case handler, submit the engineering change notice, and ask whether a variant approval or fresh file is required before the next shipment leaves the origin port.
