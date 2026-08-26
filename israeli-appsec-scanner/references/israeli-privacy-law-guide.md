# Israeli Privacy Protection Law: Developer Guide

A practical summary of Israel's Privacy Protection Law (1981) and its regulations, written for developers building applications that handle personal data of Israeli residents.

## Overview

Israel's privacy framework consists of:

1. **Privacy Protection Law, 5741-1981** (the primary law), as substantially reformed by **Amendment 13** (in force 14 August 2025): narrowed database registration, immediate serious-incident notification, mandatory DPO triggers, expanded "sensitive data" definitions, and a statutory damages head of up to NIS 10,000 without proof of harm for notification and data-subject-rights breaches (higher no-proof-of-harm ceilings under the older statutory-damages provision are conditional)
2. **Privacy Protection Regulations (Information Security), 5777-2017** (the security regulations)
3. **Privacy Protection Regulations (Transfer of Data to Databases Abroad), 5761-2001**
4. **Guidance documents from the Privacy Protection Authority (PPA)**

Israel is recognized by the EU as providing an "adequate level of protection" for personal data, which simplifies data transfers between Israel and EU member states.

## Key Definitions

### Personal Data ("Meda Ishi")

Any data about an identified or identifiable individual, including:
- Name, Israeli ID number (teudat zehut), address
- Phone number, email address
- Financial information, health data
- Location data, online identifiers
- Biometric data

### Database ("Ma'agar Meda")

A collection of personal data stored by automated means and intended for commercial use, management of a business, or direct marketing.

### Database Owner ("Ba'al Ma'agar")

The entity that decides the purposes and means of processing personal data.

### Database Manager ("Menahel Ma'agar")

The person responsible for the day-to-day management and security of the database.

## Database Registration Requirements (reformed by Amendment 13, August 2025)

Amendment 13 repealed the old broad registration duty. The pre-2025 rule, which required registering any database with 10,000+ records, or sensitive data, or used for direct marketing, no longer applies.

### When Registration Is Required (current regime)

Registration with the PPA Registrar is now required only for:

- **Data brokers**: databases whose main purpose is collecting personal data in order to transfer it to others as a business, where the database holds data on more than 10,000 individuals. (The 10,000 threshold survives only here, not as a general trigger.)
- **Public bodies** (as defined in the law).

### Notification (not registration)

A controller of a database holding "especially sensitive information" on more than 100,000 individuals must notify the PPA of identity, contact, and Data Protection Officer details, even when full registration is not required.

### Process Notes

1. There is no longer an annual-renewal requirement.
2. A database previously registered that no longer qualifies is not removed automatically; the controller must apply to be struck from the register.
3. Most ordinary consumer apps no longer need to register, but still owe the full security, consent, and data-subject-rights duties below.

### Practical Implications for Developers

```
If your app stores user profiles with personal data:
  - You likely do NOT need to register unless you are a data broker or a public body
  - If your business is selling/brokering personal data on 10,000+ people, register
  - If you hold especially sensitive data on 100,000+ people, file the PPA notification
  - Either way, implement the 2017 security regulations and support data-subject rights
```

## Data Protection Principles

### 1. Lawful Basis for Processing

You need a legal basis to collect and process personal data. Common bases:

- **Consent**: The individual agreed (most common for consumer apps)
- **Contract**: Processing is necessary to fulfill a contract
- **Legal obligation**: Required by Israeli law
- **Vital interests**: Necessary to protect someone's life
- **Public function**: Processing by a public authority

### 2. Purpose Limitation

- Collect data only for specified, explicit purposes
- Do not use data for purposes incompatible with the original purpose
- Document purposes in your privacy policy

**Example**: If you collect email addresses for account authentication, you cannot use them for marketing without separate consent.

### 3. Data Minimization

- Collect only the minimum data necessary for your stated purpose
- Review forms and data collection points regularly
- Israeli ID numbers should only be collected when legally required (banking, insurance, healthcare, government services)

### 4. Accuracy

- Keep personal data accurate and up to date
- Provide mechanisms for individuals to correct their data
- Periodically review stored data for accuracy

### 5. Storage Limitation

- Do not retain personal data longer than necessary
- Define and document retention periods
- Implement automated deletion or anonymization

### 6. Security

See the "Information Security Regulations" section below.

## Individual Rights

Israeli data subjects have the following rights:

### Right of Access (Section 13)

- Individuals can request to see their data
- You must respond within 30 days
- Provide data in a readable format
- You may charge a reasonable fee

**Implementation checklist:**
- [ ] Create an endpoint or process for access requests
- [ ] Verify the requester's identity before disclosing data
- [ ] Provide data in a structured, machine-readable format
- [ ] Log all access requests for audit purposes

### Right to Correction (Section 14)

- Individuals can request correction of inaccurate data
- If you refuse, provide written reasons
- The individual can appeal to a magistrate court

### Right to Deletion (Section 14(a))

The enacted Privacy Protection Law has no Section 14A; the right to ask for correction or deletion is Section 14(a).

- Individuals can request deletion of data collected without consent or not in compliance with the law
- Evaluate each request based on its merits
- Document your decision and reasoning

### Right to Object to Direct Marketing (Section 17ו)

Section 17ג was repealed. The live provision is Section 17ו, which requires every direct-marketing approach to state the recipient's right to be removed from the database and grants that right.

- Individuals can opt out of direct marketing at any time
- You must honor opt-out requests promptly
- Maintain an internal "do not contact" list

## Information Security Regulations (2017)

The 2017 regulations (תקנות הגנת הפרטיות (אבטחת מידע), התשע"ז-2017) classify databases into **three** security levels, plus a lighter regime for a database managed by an individual. The level is driven by the database TYPE (First and Second Schedules) and by counts of data subjects and authorized users, NOT by a simple headcount ladder.

### Security Levels

| Level | Criteria (Regulation 1 + Schedules) | Examples |
|-------|-------------------------------------|----------|
| מאגר המנוהל בידי יחיד (individual-managed) | Managed by an individual or an individually-owned company, where only that individual and **at most 2 additional authorized users** may use it. Excluded if the database's main purpose is supplying data to others as a business, if it holds data on **10,000 people or more**, or if the owner is under a professional confidentiality duty. | Sole trader's client list |
| Basic (בסיסית) | **Residual**: any database not falling within the First or Second Schedule. There is no data-subject ceiling. | Small business customer list |
| Medium (בינונית) | **First Schedule**, by TYPE not headcount: (1) main purpose is collecting data to supply to others as a business, incl. direct-mail services; (2) owner is a public body; (3) the database holds one of the enumerated sensitive categories (private affairs, medical, genetic, political/religious beliefs, criminal record, communications data, biometric, financial, consumption habits revealing the above). | Medium SaaS with sensitive data |
| High (גבוהה) | **Second Schedule**: a First-Schedule item (1) or (3) database with data on **100,000 people or more**, OR with **more than 100 authorized users**. | Large consumer or health application |

There is no "Critical" level in the regulations.

**Watch the thresholds.** The High trigger is 100,000 data subjects, not 10,000. The only place 10,000 appears in these regulations is the exclusion from the individual-managed regime. A database of 30,000 ordinary consumer records with no sensitive category is not High level, and may not even be Medium.

### Requirements by Level

**All levels:**
- Appoint a database manager
- Document security procedures (מסמך הגדרות המאגר, Regulation 2)
- Control physical and logical access
- Use authentication for all users
- Have an incident response procedure

**Medium and High (additional):**
- Access-control policies with role separation
- Encrypt data in transit
- Retain access-control log data for at least **24 months** (Regulation 10(ד)); security data under Regulation 17 is likewise kept 24 months
- **Internal or external audit at least once every 24 months** (Regulation 16(א)), by someone suitably qualified in information security who is NOT the database's own security officer
- Document all security incidents
- Physical entry/exit monitoring for the systems' locations (Regulation 6(ב))

**High only (additional):**
- Encrypt data at rest
- **Risk survey (סקר סיכונים) at least once every 18 months** (Regulation 5(ג))
- **Penetration testing (מבדק חדירות) at least once every 18 months** (Regulation 5(ד); Regulation 15 is outsourcing, not testing), with the results discussed and defects remediated
- Intrusion detection
- A dedicated information security officer. Note this s.17B ממונה אבטחת מידע is a DIFFERENT role from the Amendment 13 ממונה על הגנת הפרטיות (DPO); one organisation may owe both.

**Do not put audits on a 12-month calendar and assume you are safe.** The audit cycle is 24 months and the risk-survey / penetration-test cycle is 18 months for High-level databases only. A High-level controller running pen tests annually is compliant; one running them every 24 months has already missed the statutory window.

### Developer Implementation Guide

```
For a typical Israeli SaaS application (Medium/High level):

Authentication:
  - Implement strong password policies (8+ chars, complexity)
  - Use MFA for administrative access
  - Lock accounts after 5 failed attempts

Access Control:
  - Implement role-based access control (RBAC)
  - Follow principle of least privilege
  - Review access permissions quarterly

Encryption:
  - TLS 1.2+ for all connections
  - AES-256 for data at rest (especially PII)
  - Encrypt Israeli ID numbers and financial data

Logging:
  - Log all authentication events
  - Log all access to personal data
  - Log all modifications to personal data
  - Retain logs for 24 months minimum
  - Protect logs from tampering

Incident Response:
  - Document incident response procedures
  - Designate an incident response team
  - Practice incident response annually
```

## Cross-Border Data Transfer

Governed by the Privacy Protection (Transfer of Data Abroad) Regulations, 2001. **Two requirements apply cumulatively.** Treating them as a menu is the most common error in this area.

**(1) A lawful gateway.** Either the destination country's law guarantees a level of protection not lower than Israeli law (Regulation 1), or one of the Regulation 2 exceptions applies, the main ones being: the data subject consented; the recipient is a corporation controlled by the transferring owner and has secured privacy protection after transfer; the recipient undertook by agreement to comply with the conditions applying to a database in Israel; the transfer is required under Israeli law; or the destination is a Convention 108 state, a state receiving data from the EU on the same terms, or one the Registrar has published as having a privacy authority.

**(2) A written undertaking from the recipient (Regulation 3).** Regulation 3 applies to a transfer made under **Regulation 1 OR Regulation 2**. The database owner must obtain the recipient's written undertaking that the recipient takes sufficient measures to protect the privacy of the data subjects, and that the data will not be transferred to any other person, whether in that country or another.

So consent is a gateway, not a substitute for the undertaking. Relying on consent alone, with no data-transfer agreement, does not make a transfer to a US SaaS vendor lawful.

"Standard Contractual Clauses" is GDPR terminology and is not the Israeli instrument. An SCC-based DPA can carry the Regulation 3 undertaking, but only if it actually contains the two undertakings above.

**Common scenarios for Israeli apps:**
- Cloud hosting on AWS/GCP: a data processing agreement carrying the Regulation 3 undertakings
- US-based SaaS tools: verify the DPA contains both the sufficient-measures and no-onward-transfer undertakings
- Analytics services: consider anonymisation before transfer, which takes the data outside the regime entirely
- Hosting in AWS il-central-1 (Tel Aviv) avoids the question for data that never leaves Israel

### Cloud Services Guidance

For Israeli companies using cloud services (AWS, GCP, Azure):

- Data may be processed in regions outside Israel
- Ensure the cloud provider agreement carries the Regulation 3 written undertakings (sufficient privacy measures AND no onward transfer)
- Consider using cloud regions within the EU or Israel (AWS IL region)
- Document where data is processed and stored
- Conduct a data transfer impact assessment for sensitive data

## Breach Notification

### What Constitutes a Breach

Under current regulations, a "serious security incident" includes:
- Unauthorized access to personal data
- Loss or theft of data storage media
- Ransomware attacks affecting personal data
- Any incident that may cause significant harm to data subjects

### Notification Requirements

1. **Notify the PPA**: As soon as possible after discovering the incident
2. **Notify affected individuals**: When the breach may cause harm
3. **Document the incident**: Record the facts, effects, and remediation steps

### Notification Content

- Nature and scope of the incident
- Types of personal data affected
- Number of data subjects affected
- Measures taken to address the incident
- Recommendations for data subjects to protect themselves

## Practical Privacy Policy Requirements

Your Israeli application's privacy policy should include:

1. **Identity**: Full legal name, Israeli company registration number, contact details
2. **Purpose**: Clear description of why you collect each type of data
3. **Legal basis**: The legal basis for each processing activity
4. **Data sharing**: Who you share data with and why
5. **Cross-border transfers**: Where data is transferred and what safeguards are in place
6. **Retention periods**: How long you keep each type of data
7. **Individual rights**: How to exercise access, correction, deletion, and objection rights
8. **Security measures**: General description of security measures
9. **Database registration**: Registration number (if applicable)
10. **Updates**: How you notify users of policy changes

The privacy policy must be available in Hebrew.

## Common Compliance Mistakes

1. **Collecting Israeli ID numbers unnecessarily**: Only collect when legally required
2. **Misjudging database registration**: Since Amendment 13 (Aug 2025), registration applies only to data brokers (10,000+ individuals) and public bodies, not every database over 10,000 records. Do not register unnecessarily, but file the PPA notification if you hold especially sensitive data on 100,000+ individuals
3. **No Hebrew privacy policy**: Israeli law requires accessibility in Hebrew
4. **Ignoring the security regulations**: The 2017 regulations have specific technical requirements
5. **Not logging data access**: Access logs must be retained for 24 months
6. **Transferring data without safeguards**: Cloud services in the US require contractual safeguards
7. **No incident response plan**: You must have documented procedures before an incident occurs
8. **Marketing without consent**: Direct marketing requires explicit opt-in consent

## Resources

- Privacy Protection Authority (PPA): https://www.gov.il/en/departments/the_privacy_protection_authority
- Privacy Protection Law text (Hebrew): https://he.wikisource.org/wiki/חוק_הגנת_הפרטיות
- Information Security Regulations (2017): Available on the PPA website
- PPA guidance documents: Published periodically on the PPA website

This guide is for informational purposes and does not constitute legal advice. Consult with an Israeli privacy lawyer for specific compliance questions.
