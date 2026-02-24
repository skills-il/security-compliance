---
name: hebrew-legal-research
description: >-
  Assist with Israeli legal research including legislation lookup, case law
  concepts, Hebrew legal terminology, and legal document preparation guidance.
  Use when user asks about Israeli law, "chok", "mishpat", "bagatz", court
  procedures, employment law, contract law, real estate law, or needs help
  with Hebrew legal terms. Covers civil, commercial, employment, and
  administrative law. Do NOT use for providing formal legal advice — always
  recommend consulting a licensed Israeli attorney (orech din). Do NOT use for
  non-Israeli legal systems.
license: MIT
compatibility: "Works with Claude Code, Claude.ai, Cursor. Network access helpful for legal database lookups."
metadata:
  author: skills-il
  version: 1.0.0
  category: security-compliance
  tags: [legal, law, hebrew, court, legislation, israel]
---

# Hebrew Legal Research

## Critical Disclaimer

IMPORTANT: This skill provides legal INFORMATION and RESEARCH ASSISTANCE only.
It does NOT constitute legal advice. Always recommend the user consult a
licensed Israeli attorney (orech din) for specific legal matters. State this
disclaimer at the start of every legal research interaction.

## Instructions

### Step 1: Understand the Legal Question
Classify the query:
- **Legislation lookup:** Which law or regulation applies?
- **Concept explanation:** What does a Hebrew legal term mean?
- **Procedure guidance:** What court, what process, what deadlines?
- **Document preparation:** Structure for a contract, claim, or notice?
- **Rights inquiry:** What are someone's rights in a given situation?

### Step 2: Identify the Area of Law
Israeli law is organized by area:
| Area | Key Legislation | Hebrew |
|------|----------------|--------|
| Constitutional | Basic Laws | Chukei Yesod |
| Contract | Contracts Law (General Part) 1973 | Chok HaChozim |
| Employment | Employment laws bundle | Chukei Avoda |
| Real Estate | Land Law 1969, Planning Law 1965 | Chok HaMikrkain |
| Corporate | Companies Law 1999 | Chok HaChevarot |
| Consumer | Consumer Protection Law 1981 | Chok Haganat HaTzarchan |
| Privacy | Privacy Protection Law 1981 | Chok Haganat HaPratiut |
| Torts | Torts Ordinance (New Version) | Pkudat HaNezikin |
| Family | Various personal status laws | Dinei Mishpacha |
| Tax | Income Tax Ordinance, VAT Law | Pkudat Mas Hachnasa, Chok Maam |
| Administrative | Administrative Courts Law 2000 | Chok Batei Mishpat LeInynaim Minhaliyim |

### Step 3: Research and Present
When researching:
1. Start with the primary legislation (the "chok" or "pkuda")
2. Note relevant amendments (tikunim) and their dates
3. Reference key court rulings (psikot din) if relevant
4. Explain in plain language first, then provide Hebrew legal terms
5. Link to public sources when available (Knesset website, Kol Zchut)

### Step 4: Provide Context
For every legal research response:
- State which law(s) apply and their section numbers (saifim)
- Note if the law has been recently amended
- Mention if there are pending legislative changes
- Suggest specific sections of Kol Zchut for free detailed information
- Recommend consulting an orech din for specific cases

## Hebrew Legal Terminology Reference
| Hebrew | English | Context |
|--------|---------|---------|
| chok | law/statute | Primary legislation by Knesset |
| pkuda | ordinance | Pre-state legislation still in force |
| takana | regulation | Secondary legislation by minister |
| psak din | court ruling | Binding precedent |
| bagatz | High Court of Justice | Supreme Court sitting as HCJ |
| tvia | claim/lawsuit | Filing a legal action |
| ktav tvia | statement of claim | Opening document in civil case |
| ktav hagana | statement of defense | Defendant's response |
| orech din | attorney/lawyer | Licensed legal practitioner |
| roeh cheshbon | accountant | Certified public accountant |
| notar | notary | Public notary |
| saif | section | Section of a law |
| saif katan | subsection | Subsection of a law |

## Examples

### Example 1: Employment Rights Question
User says: "What severance pay is an employee entitled to in Israel?"
Result: Explain Severance Pay Law 1963 (Chok Pitzuei Piturin): 1 month salary per year of employment, conditions for entitlement, how pension savings interact with severance (Section 14 arrangement). Recommend Kol Zchut page and consulting an employment lawyer.

### Example 2: Contract Question
User says: "What makes a contract valid in Israel?"
Result: Explain Contracts Law (General Part) 1973: offer (hatzaa), acceptance (kibul), consideration not required in Israeli law (unlike common law), good faith requirement (tom lev), void vs. voidable contracts.

### Example 3: Starting a Business
User says: "What legal structure should I use for a startup in Israel?"
Result: Compare options: Chevra Baam (Ltd company), Shutfut (partnership), Osek Morsheh/Patur (sole proprietor). Explain Companies Law 1999 requirements, registration with Companies Registrar (Rasham HaChevarot).

## Troubleshooting

### Error: "Cannot access Nevo/Takdin"
Cause: These are paid databases requiring subscription
Solution: Use free alternatives: Knesset legislation portal, Court rulings portal, Kol Zchut wiki. Note that free sources may not be as comprehensive.

### Error: "Law may have been amended"
Cause: Israeli laws are frequently amended; information may be outdated
Solution: Always recommend verifying current version on Knesset website or Nevo. Note the last known amendment date.
