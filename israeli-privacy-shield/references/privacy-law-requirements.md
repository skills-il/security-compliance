# Israeli Privacy Protection Law — Detailed Requirements

## Overview
The Protection of Privacy Law, 5741-1981 (Chok Haganat HaPratiut) is Israel's primary
data protection legislation. It was significantly strengthened by the Information Security
Regulations of 2017.

## Enforcement Authority
- **Privacy Protection Authority** (Rashut LeHaganat HaPratiut)
- Under the Ministry of Justice
- Website: https://www.gov.il/he/departments/privacy_authority
- Has enforcement powers including inspections and penalties

## Database Registration Requirements

### When Registration is Required
A database must be registered with the Privacy Protection Authority if:
1. It contains data on more than 10,000 individuals AND is used for direct marketing
2. It contains data on more than 10,000 individuals AND includes sensitive data
3. It is owned or managed by a public body
4. It is used for providing credit information services
5. It contains information about a person's health, genetics, or financial status

### Registration Process
1. Submit Form 1 to Privacy Protection Authority
2. Include: database name, purpose, types of data, data sources, recipients
3. Renewal required periodically
4. Changes to database purpose or scope require updated registration

## Security Levels and Requirements

### Basic Level
Applies to: Databases with fewer than 10,000 records containing non-sensitive data

Requirements:
- Physical security of premises
- Access control (user authentication)
- Activity logging
- Backup procedures
- Written security procedures document
- Employee awareness

### Medium Level
Applies to: Databases with 10,000+ records OR containing sensitive data

Additional requirements beyond Basic:
- Encryption of data at rest and in transit
- Appointment of a security officer (memune al bitachon meida)
- Periodic access review
- Enhanced logging and monitoring
- Incident response procedures
- Third-party access controls
- Data processing agreements with service providers

### High Level
Applies to: Government databases, health data, financial data, or databases with 100,000+ records

Additional requirements beyond Medium:
- Annual security audit by external auditor
- Comprehensive incident response plan
- Data Protection Officer (DPO) appointment
- Penetration testing
- Advanced encryption standards
- Detailed data flow mapping
- Regular employee training program
- Business continuity plan

## Consent Requirements

### Valid Consent Must Be
- **Informed:** Data subject knows what data is collected and for what purpose
- **Specific:** Consent for each distinct purpose of processing
- **Freely given:** No undue pressure or bundling with unrelated services
- **Documentable:** Organization must be able to demonstrate consent was obtained

### When Consent is Required
- Initial collection of personal data
- Any use beyond the originally stated purpose
- Transfer of data to third parties
- Cross-border transfer of data
- Processing of sensitive data categories

### Consent Exceptions
Consent is not required when:
- Processing is required by law
- Processing is necessary to protect vital interests
- Processing is in the public interest
- Processing is necessary for performance of a contract
- Limited legitimate interest exception (interpreted narrowly by Israeli courts)

## Cross-Border Data Transfer

### General Rule
Personal data may not be transferred outside Israel unless the recipient country
provides adequate protection for personal data.

### Countries with Adequate Protection
- European Union member states (Israel has EU adequacy decision)
- United Kingdom
- Other countries recognized by the Privacy Protection Authority

### Transfer Without Adequacy
Transfers to countries without adequate protection are permitted if:
- Data subject has given informed consent to the specific transfer
- Transfer is necessary for contract performance
- Transfer is necessary for legal proceedings
- Transfer is necessary to protect vital interests
- Contractual safeguards are in place (similar to EU Standard Contractual Clauses)

## Breach Notification

### What Constitutes a Breach
A "severe security incident" requiring notification includes:
- Unauthorized access to personal data
- Unauthorized disclosure of personal data
- Loss or destruction of personal data
- Any incident that may cause significant harm to data subjects

### Notification to Authority
- Must be reported "without delay" to the Privacy Protection Authority
- No specific hour deadline (unlike GDPR's 72 hours)
- "Without delay" is interpreted as the shortest reasonable time
- Must include: nature of breach, data affected, measures taken, contact information

### Notification to Data Subjects
- Required if the breach may cause "significant harm" to individuals
- Must include: nature of breach, potential consequences, measures taken, recommendations
- Should be in clear, plain language (Hebrew)

### Documentation
- All security incidents must be documented regardless of severity
- Documentation must include: timeline, scope, response actions, decisions, lessons learned
- Retain documentation for at least 5 years

## Penalties

### Criminal Penalties
- Violations of the Privacy Protection Law can result in criminal prosecution
- Maximum penalties: Up to 5 years imprisonment for severe violations
- Fines as determined by criminal court

### Civil Liability
- Data subjects may sue for damages resulting from privacy violations
- Compensation for non-material damage (emotional distress) is available
- Class actions are possible for widespread violations

### Administrative Enforcement
- Privacy Protection Authority can issue orders and impose conditions
- Authority can require corrective measures
- Authority can publicize violations (naming and shaming)

## GDPR Comparison Notes

### Areas Where Israeli Law is Stricter
- Database registration requirement (no GDPR equivalent since ROPA replaced it)
- Criminal penalties for privacy violations

### Areas Where GDPR is Stricter
- Higher financial penalties (up to 4% of global annual revenue)
- Broader extra-territorial application
- More comprehensive right to erasure (right to be forgotten)
- More detailed lawful basis framework (6 legal bases vs. consent-primary)
- More comprehensive DPO requirements
- Data Protection Impact Assessment requirement
- Privacy by Design and by Default as legal requirements

### Key Practical Differences for Multinational Companies
- Companies operating in both Israel and EU must comply with both frameworks
- Israeli adequacy decision means data flows from EU to Israel are generally permitted
- Israeli companies processing EU residents' data must comply with GDPR
- Recommended approach: comply with the stricter requirement in each area
