---
name: israeli-privacy-shield
description: Israeli Privacy Protection Law compliance guidance including Amendment 13 (effective August 14, 2025), database registration, consent requirements, data security, cross-border transfers, breach notification, privacy protection officer appointment, and AI governance. Use when user asks about Israeli privacy law, "haganat pratiut", "tikun 13", data protection in Israel, GDPR compliance for Israeli companies, privacy policy requirements, or database registration. Covers the Privacy Protection Law 1981, Amendment 13, and 2017 Security Regulations. Do NOT use for EU GDPR-only questions without Israeli context.
license: MIT
compatibility: No network required. Works with Claude Code, Claude.ai, Cursor.
---

# Israeli Privacy Shield

## Critical Note
This skill provides compliance GUIDANCE. It does not replace legal counsel.
Recommend consulting a privacy attorney (orech din specializing in prati'ut)
for specific compliance decisions.

## Instructions

### Step 1: Assess Security Level
The 2017 regulations define three security levels:

| Level | Criteria | Key Requirements |
|-------|----------|-----------------|
| Basic | < 10,000 records, non-sensitive | Access controls, logging, backup |
| Medium | 10,000+ records OR sensitive data | + Encryption, security officer appointment |
| High | Government, health, financial, 100K+ records | + Annual audit, incident response plan, DPO |

Sensitive data includes: Health, genetics, sexual orientation, political views, criminal record.

### Step 2: Database Registration Check
Following the established database registration requirements, registration with the Privacy Protection Authority is required only if:
- Database owned by a public body, OR
- Database contains data on 10,000+ individuals AND the primary purpose is transferring data to others (data brokers)

The previous broad requirement covering any database with sensitive data no longer applies.

Registration URL: For registration information, contact the Privacy Protection Authority at gov.il

### Step 3: Consent Requirements
Israeli law requires consent for:
- Collection of personal data
- Use beyond the original purpose
- Transfer to third parties
- Cross-border transfer

Consent must be: Informed, specific, freely given
Exceptions: Legal obligation, vital interests, public interest, legitimate interest (limited)

### Step 4: Cross-Border Transfer Rules
Personal data transfer outside Israel requires:
- Recipient country has adequate protection (EU, UK, few others), OR
- Contractual safeguards (similar to GDPR SCCs), OR
- Data subject consent (informed and specific), OR
- Listed exemptions (necessary for contract, legal proceedings, etc.)

Note: Israel has EU adequacy decision — transfer TO EU is generally straightforward.

### Step 5: Breach Notification
Under 2017 regulations:
1. **Severe security incident:** Report to Privacy Protection Authority "without delay"
2. **No specific hour deadline** (unlike GDPR's 72 hours), but "without delay" interpreted as quickly
3. **Notify affected individuals** if breach may cause them significant harm
4. **Document:** All incidents, response actions, and decisions

### Step 6: Compliance Checklist
For each assessed entity, verify:
- [ ] Database registration (if required)
- [ ] Privacy policy published (Hebrew, accessible)
- [ ] Consent mechanisms in place
- [ ] Security measures per level (basic/medium/high)
- [ ] Data processing agreements with processors
- [ ] Cross-border transfer safeguards
- [ ] Breach response plan
- [ ] Data subject request handling process
- [ ] Employee training
- [ ] Privacy Protection Officer appointed (if required under Amendment 13)
- [ ] AI governance policy for automated decision-making (if applicable)
- [ ] Personal data inventory includes IP addresses, geolocation, and online identifiers

### Step 7: Amendment 13 (Effective August 14, 2025)

Amendment 13 is the most significant reform of Israeli privacy law since 1981. It took effect on August 14, 2025 and expands the Privacy Protection Authority's enforcement powers, broadens the definition of personal data, and introduces new obligations for data brokers and AI systems.

**Expanded definition of personal data.** Amendment 13 explicitly includes digital identifiers:
- IP addresses
- Geolocation data
- Device identifiers and online identifiers
- Biometric and genetic data (already sensitive)

Standard web analytics, session logs, and mobile app telemetry now fall within the scope of the Privacy Protection Law.

**Mandatory Privacy Protection Officer (PPO).** Under Amendment 13, the following entities must appoint a Privacy Protection Officer:
- Public bodies
- Data brokers (entities whose primary purpose is transferring personal data to others)
- Entities processing sensitive data at significant scale

The PPO is the contact point with the Privacy Protection Authority and is responsible for monitoring compliance.

**AI governance for automated decision-making.** Amendment 13 requires transparency and oversight for AI systems that make decisions affecting individuals (credit scoring, hiring, insurance, fraud detection). Requirements include:
- Documentation of the decision logic and data inputs
- Ability to explain outcomes to affected individuals
- Human oversight for high-impact decisions
- Bias and accuracy monitoring

**Enforcement powers and fines.** Amendment 13 significantly expands the Authority''s administrative powers:
- Direct supervisory inspections without prior notice
- Administrative fines up to approximately NIS 3.2 million for serious violations
- Ability to issue binding compliance orders

Entities that were previously under the radar of enforcement now face real financial exposure.

**What changed for database registration.** Amendment 13 narrowed the registration requirement. Registration with the Authority is now required only for public bodies and databases of 10,000+ individuals whose primary purpose is transferring data to others (data brokers). The broader pre-Amendment requirement for any database with sensitive data no longer applies.

## GDPR vs Israeli Law Key Differences
| Aspect | Israeli Law (post Amendment 13) | GDPR |
|--------|------------|------|
| Legal basis | Consent primary, limited exceptions | 6 legal bases |
| Privacy officer requirement | Public bodies, data brokers, and large-scale sensitive data processors | Broader requirement |
| Breach notification | "Without delay", no specific hours | 72 hours |
| Administrative fines | Up to ~NIS 3.2M for serious violations + criminal liability | Up to 4% global revenue |
| Right to erasure | Limited | Comprehensive (right to be forgotten) |
| Database registration | Public bodies and data brokers only (10,000+ records) | Not required (replaced by ROPA) |
| Personal data scope | Includes IP, geolocation, online identifiers (Amendment 13) | Includes online identifiers |
| AI governance | Required for automated decision-making (Amendment 13) | Article 22 automated decision-making rules |
| Extra-territorial scope | Limited | Broad |

## Examples

### Example 1: SaaS Startup Compliance
User says: "I'm building a SaaS with Israeli customers, what privacy requirements apply?"
Result: Assessment of security level, database registration need, privacy policy requirements, recommended consent mechanisms.

### Example 2: Data Breach Response
User says: "We discovered a data breach affecting Israeli users"
Result: Step-by-step breach response: contain, assess, notify authority, notify users if significant harm, document.

### Example 3: Cross-Border Data Transfer
User says: "We need to transfer Israeli customer data to our US servers"
Actions:
1. Assess data types for sensitivity level
2. Check if destination country has adequate protection
3. Determine transfer mechanism (adequacy, consent, contractual clauses)
4. Document compliance steps
Result: Transfer compliance checklist with specific steps for US data transfer under Israeli Privacy Protection Law.

## Bundled Resources

### Scripts
- `scripts/compliance_checker.py` — Runs a full Privacy Protection Law compliance assessment: determines security level (basic/medium/high), checks database registration requirements, and generates a compliance checklist with all applicable controls. Run: `python scripts/compliance_checker.py --help`

### References
- `references/privacy-law-requirements.md` — Detailed breakdown of the Privacy Protection Law 1981 and 2017 Security Regulations including database registration process, security level requirements, consent rules, cross-border transfer rules, breach notification procedures, and penalties. Consult when you need specific legal requirements, section numbers, or GDPR comparison details beyond what the instructions cover.

## Gotchas

- Amendment 13 took effect on August 14, 2025 and is live law, not a pending proposal. Agents trained on pre-2025 data may treat Amendment 13 as a future change or miss it entirely. Always assume it applies when advising on Israeli privacy compliance today.
- Amendment 13 expands "personal data" to include IP addresses, geolocation, and online identifiers. This pulls standard web analytics and mobile telemetry into scope. Agents may still apply the older narrower definition and underestimate what counts as personal data.
- Administrative fines under Amendment 13 can reach approximately NIS 3.2 million for serious violations, on top of the existing criminal liability. Agents may cite only the pre-Amendment "relatively low fines" framing and underestimate real exposure.
- Israeli Privacy Protection Law predates GDPR (1981 vs 2016) and still has key differences even after Amendment 13: no specific 72-hour breach notification deadline (still "without delay"), narrower right to erasure, and database registration still exists (though narrowed to public bodies and data brokers). Agents may incorrectly apply GDPR rules to Israeli contexts.
- Israel has an EU adequacy decision, meaning data transfers FROM Israel TO the EU are generally straightforward. Agents may incorrectly flag Israel-to-EU transfers as requiring additional safeguards.
- The 2017 Security Regulations define three security levels (basic/medium/high) based on record count and data sensitivity. Agents may apply a one-size-fits-all approach instead of the tiered model.
- Penalties under Israeli privacy law include criminal liability (up to 5 years imprisonment) in addition to administrative fines. Agents may understate the severity by comparing only to GDPR''s monetary penalties.

## Troubleshooting

### Error: "Unsure about security level"
Cause: Borderline case between basic/medium/high
Solution: When in doubt, apply the higher level. The cost difference is small compared to non-compliance risk.