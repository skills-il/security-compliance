# Israeli Privacy Protection Law — Implementation Requirements

## Overview
The Protection of Privacy Law, 5741-1981 (Chok Haganat HaPratiyut) and the 2017
Information Security Regulations define the code-level requirements for Israeli
privacy compliance.

## Consent Implementation Requirements

### Legal Requirements Mapped to Code
1. **Informed consent** — display purpose before collection
   - Show Hebrew-language description of data purpose
   - List all data types being collected
   - Disclose third-party recipients
2. **Specific consent** — separate consent per purpose
   - Do not bundle marketing consent with service consent
   - Maintain separate consent records per purpose
3. **Freely given** — equal prominence for accept/reject
   - "Reject All" button must be as visible as "Accept All"
   - No pre-checked boxes for non-essential processing
4. **Documentable** — store consent proof
   - Record: timestamp, IP, purpose, version, user action

### Consent Record Schema
Required fields for a valid consent record:
- Subject identifier (hashed or pseudonymized)
- Consent type (essential, analytics, marketing)
- Purpose description (Hebrew + English)
- Grant timestamp (ISO-8601)
- Withdrawal timestamp (null if active)
- Consent policy version
- Legal basis

## DSAR Implementation Requirements

### Response Timeline
- Maximum 30 days from receipt of valid request
- Identity verification must be completed before processing
- Acceptable identity documents: Teudat Zehut, passport, biometric

### Required DSAR Types
1. **Access (Zchut Iyun)** — provide all stored data about the subject
2. **Correction (Zchut Tikun)** — fix inaccurate data upon request
3. **Deletion** — limited right; not as broad as GDPR Article 17
4. **Marketing objection** — must honor opt-out from direct marketing

### Implementation Requirements
- Centralized data discovery across all storage systems
- Structured response format (machine-readable preferred)
- Secure delivery mechanism
- Audit trail for all DSAR activities

## Database Registration Requirements

### Registration Criteria
A database must be registered with the PPA when:
1. 10,000+ records AND used for direct marketing
2. 10,000+ records AND contains sensitive data
3. Owned by a public body
4. Used for credit/financial information services

### Registration Payload Fields
- Database name and purpose (matarat ha-maagar)
- Owner entity (Israeli business number)
- Data types stored
- Data sources (direct collection, third party, public)
- Data recipients
- Security level (basic, medium, high)
- Cross-border transfer status
- Retention period

### Registration Portal
URL: https://www.gov.il/he/departments/privacy_authority

## Cross-Border Transfer Requirements

### Adequate Countries
Countries recognized as providing adequate protection:
- EU/EEA member states (Israel has EU adequacy decision)
- United Kingdom
- Switzerland, New Zealand, Uruguay, Japan, South Korea, Canada, Argentina

### Transfer Without Adequacy
For countries not on the adequacy list (including the US):
1. Explicit informed consent for the specific transfer
2. Contractual safeguards (similar to EU SCCs)
3. Contract necessity
4. Legal proceedings necessity
5. Vital interests

### Code Implementation
- Validate destination country against adequacy list before transfer
- Document transfer basis for audit trail
- Block transfers without valid basis

## Audit Trail Requirements

### Events to Log
- Consent granted and withdrawn
- DSAR received and completed
- Data access by employees/operators
- Cross-border transfers executed
- Security incidents detected and reported
- Retention policy enforcement actions

### Retention of Audit Records
- Minimum 5 years for security-related logs (2017 Regulations)
- Recommended 7 years for full compliance coverage
- Immutable storage (append-only)

## GDPR Bridging Requirements

### Dual-Compliance Rules
For Israeli companies also subject to GDPR:
- Use the stricter requirement from each framework
- Implement all 6 GDPR legal bases (not just consent)
- Apply 72-hour breach notification (GDPR) rather than "without delay"
- Implement full right to erasure (GDPR standard)
- Maintain both database registration AND Records of Processing Activities (ROPA)
- Appoint DPO if either framework requires it
