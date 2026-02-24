# Israeli Privacy Shield Skill — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a skill for Israeli Privacy Protection Law compliance — database registration, consent requirements, cross-border transfers, and breach notification.

**Architecture:** Domain-Specific Intelligence skill (Pattern 5). Embeds Israeli privacy regulations with compliance checking workflow.

**Tech Stack:** SKILL.md, references for Privacy Protection Law and regulations, compliance checklists.

---

## Research

### Israeli Privacy Protection Law (1981)
- **Full name:** Protection of Privacy Law, 5741-1981 (Chok Haganat HaPratiut)
- **Regulations 2017:** Information Security Regulations — detailed security requirements
- **Enforcer:** Privacy Protection Authority (Rashut LeHaganat HaPratiut), under Ministry of Justice
- **Key principles:** Consent, purpose limitation, data minimization, security, cross-border restrictions
- **Database registration:** Mandatory for databases with 10,000+ records or sensitive data

### Key Requirements
1. **Database registration** with Privacy Protection Authority
2. **Consent** for collection and processing
3. **Purpose limitation** — use data only for stated purpose
4. **Security measures** — per 2017 regulations (basic/medium/high levels)
5. **Cross-border transfers** — adequate protection required
6. **Breach notification** — mandatory since 2017
7. **Data subject rights** — access, correction, deletion
8. **GDPR alignment** — Israel has EU adequacy decision, but laws differ

### Use Cases
1. **Compliance assessment** — Check if organization meets Israeli privacy requirements
2. **Database registration** — Guide through registration process
3. **Privacy policy drafting** — Key elements for Israeli privacy policy
4. **Breach response** — Steps for handling a data breach
5. **GDPR vs Israeli law** — Compare and highlight differences

---

## Build Steps

### Task 1: Create SKILL.md

```markdown
---
name: israeli-privacy-shield
description: >-
  Israeli Privacy Protection Law compliance guidance including database
  registration, consent requirements, data security, cross-border transfers,
  and breach notification. Use when user asks about Israeli privacy law,
  "haganat pratiut", data protection in Israel, GDPR compliance for Israeli
  companies, privacy policy requirements, or database registration. Covers
  the Privacy Protection Law 1981 and 2017 Security Regulations. Do NOT use
  for EU GDPR-only questions without Israeli context.
license: MIT
compatibility: "No network required. Works with Claude Code, Claude.ai, Cursor."
metadata:
  author: skills-il
  version: 1.0.0
  category: security-compliance
  tags: [privacy, data-protection, compliance, gdpr, regulation, israel]
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
Must register with Privacy Protection Authority if:
- Database has 10,000+ records AND used for direct marketing, OR
- Database has 10,000+ records AND contains sensitive information, OR
- Database owned by public body, OR
- Database used for credit/financial information services

Registration URL: `https://www.gov.il/he/departments/privacy_authority`

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
- [ ] Security officer/DPO appointed (if required)

## GDPR vs Israeli Law Key Differences
| Aspect | Israeli Law | GDPR |
|--------|------------|------|
| Legal basis | Consent primary, limited exceptions | 6 legal bases |
| DPO requirement | Only for high-level databases | Broader requirement |
| Breach notification | "Without delay", no specific hours | 72 hours |
| Penalties | Criminal + civil, relatively low fines | Up to 4% global revenue |
| Right to erasure | Limited | Comprehensive (right to be forgotten) |
| Database registration | Required for qualifying databases | Not required (replaced by ROPA) |
| Extra-territorial scope | Limited | Broad |

## Examples

### Example 1: SaaS Startup Compliance
User says: "I'm building a SaaS with Israeli customers, what privacy requirements apply?"
Result: Assessment of security level, database registration need, privacy policy requirements, recommended consent mechanisms.

### Example 2: Data Breach Response
User says: "We discovered a data breach affecting Israeli users"
Result: Step-by-step breach response: contain, assess, notify authority, notify users if significant harm, document.

## Troubleshooting

### Error: "Unsure about security level"
Cause: Borderline case between basic/medium/high
Solution: When in doubt, apply the higher level. The cost difference is small compared to non-compliance risk.
```
