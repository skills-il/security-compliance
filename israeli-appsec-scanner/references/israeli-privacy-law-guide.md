# Israeli Privacy Protection Law: Developer Guide

A practical summary of Israel's Privacy Protection Law (1981) and its regulations, written for developers building applications that handle personal data of Israeli residents.

## Overview

Israel's privacy framework consists of:

1. **Privacy Protection Law, 5741-1981** (the primary law)
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

## Database Registration Requirements

### When Registration Is Required

You must register your database with the PPA if it meets ANY of these criteria:

- Contains data on more than 10,000 individuals
- Contains "sensitive information" (health, genetic, financial, criminal, political opinions, religious beliefs)
- Contains information about individuals who have not consented to its inclusion
- Is used for direct marketing purposes
- Belongs to a public body

### Registration Process

1. Submit application to the PPA Registrar
2. Provide: database name, purpose, categories of data, types of data subjects, data recipients, security measures, database manager details
3. Receive registration number
4. Renew annually
5. Notify the registrar of any material changes

### Practical Implications for Developers

```
If your app stores user profiles with personal data:
  - Count unique individuals in your database
  - If approaching 10,000, plan for registration
  - If storing health/financial data, register regardless of count
  - Display registration number in your privacy policy
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

### Right to Deletion (Section 14A)

- Individuals can request deletion of data collected without consent or not in compliance with the law
- Evaluate each request based on its merits
- Document your decision and reasoning

### Right to Object to Direct Marketing (Section 17G)

- Individuals can opt out of direct marketing at any time
- You must honor opt-out requests promptly
- Maintain an internal "do not contact" list

## Information Security Regulations (2017)

The 2017 regulations classify databases into four security levels based on the number of data subjects, sensitivity of data, and number of people with access.

### Security Levels

| Level | Criteria | Examples |
|-------|----------|---------|
| Basic | Up to 100 data subjects, up to 3 authorized users | Small business customer list |
| Medium | 100-10,000 data subjects, or up to 100 authorized users | Medium SaaS application |
| High | 10,000+ data subjects, or sensitive data, or 100+ authorized users | Consumer application, health app |
| Critical | Designated by PPA due to special risk | Large financial institution |

### Requirements by Level

**All levels (Basic and above):**
- Appoint a database manager
- Document security procedures
- Control physical and logical access
- Use authentication for all users
- Log access to the database
- Have an incident response procedure

**Medium and above (additional):**
- Conduct periodic security assessments
- Implement access control policies with role separation
- Encrypt data in transit
- Maintain access logs for at least 24 months
- Perform annual security audits
- Document all security incidents

**High and above (additional):**
- Encrypt data at rest
- Perform penetration testing annually
- Implement intrusion detection
- Have a dedicated information security officer
- Conduct employee security training
- Maintain a business continuity plan

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

### General Rule

Personal data may be transferred outside Israel only if the destination country provides an "adequate level of protection."

### Recognized Countries

The PPA maintains a list of countries with adequate protection, which generally includes:
- EU/EEA member states
- Countries recognized under EU adequacy decisions
- Other countries evaluated by the PPA

### Transfer Without Adequacy

When the destination lacks adequate protection, transfer is permitted if:

1. **Consent**: The data subject consented to the specific transfer
2. **Contract**: The transfer is necessary for a contract with the data subject
3. **Contractual safeguards**: Standard Contractual Clauses (SCCs) or binding corporate rules are in place
4. **Public interest**: Approved by the PPA for reasons of public interest

### Cloud Services Guidance

For Israeli companies using cloud services (AWS, GCP, Azure):

- Data may be processed in regions outside Israel
- Ensure your cloud provider agreement includes adequate contractual safeguards
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
2. **Missing database registration**: Monitor your user count and register before reaching 10,000
3. **No Hebrew privacy policy**: Israeli law requires accessibility in Hebrew
4. **Ignoring the security regulations**: The 2017 regulations have specific technical requirements
5. **Not logging data access**: Access logs must be retained for 24 months
6. **Transferring data without safeguards**: Cloud services in the US require contractual safeguards
7. **No incident response plan**: You must have documented procedures before an incident occurs
8. **Marketing without consent**: Direct marketing requires explicit opt-in consent

## Resources

- Privacy Protection Authority (PPA): https://www.gov.il/en/departments/the_privacy_protection_authority
- Privacy Protection Law text (Hebrew): https://www.nevo.co.il/law_html/law01/133_001.htm
- Information Security Regulations (2017): Available on the PPA website
- PPA guidance documents: Published periodically on the PPA website

This guide is for informational purposes and does not constitute legal advice. Consult with an Israeli privacy lawyer for specific compliance questions.
