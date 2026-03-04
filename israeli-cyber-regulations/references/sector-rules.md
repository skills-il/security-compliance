# Sector-Specific Cybersecurity Regulations Reference

## Financial Services

### Bank of Israel Directive 361 — Cyber Risk Management
**Applies to:** Banks, insurance companies, credit card companies, and other BOI-regulated entities.

**Full title:** Proper Conduct of Banking Business Directive 361 — Cyber Defense Management

**Core requirements:**

#### Governance
- Board of directors must approve the cybersecurity strategy and policy
- Board must receive quarterly cybersecurity status reports
- Board must approve the annual cybersecurity work plan and budget
- A board member or committee must be designated as cyber-responsible

#### Personnel
- Dedicated CISO (Chief Information Security Officer) must be appointed
- CISO must report directly to senior management (CEO or deputy)
- CISO must have appropriate qualifications and experience
- Adequate staffing for cybersecurity function

#### Security Operations
- 24/7 Security Operations Center (SOC) for significant institutions
- Continuous monitoring of all critical systems and networks
- Real-time alert triage and escalation procedures
- Integration with CERT-IL for threat intelligence

#### Testing and Assessment
- Annual external penetration testing by a qualified Israeli firm
- Internal vulnerability assessments at least quarterly
- Red team exercises for major banks (recommended annually)
- Third-party security assessments of critical vendors

#### Third-Party Risk
- Due diligence on all technology vendors and service providers
- Cloud computing requires prior BOI approval
- Outsourcing of IT functions requires notification to BOI
- Ongoing monitoring of vendor security posture

#### Incident Management
- Report significant cyber events to Banking Supervision within 24 hours
- Maintain detailed incident response plan, tested annually
- Post-incident analysis and lessons learned within 30 days
- Customer notification for incidents affecting personal data

#### Business Continuity
- Disaster recovery site with tested failover capability
- Annual DR drill with documented results reported to BOI
- Recovery Time Objective (RTO) aligned with business criticality
- Backup integrity verification procedures

### Bank of Israel Directive 357 — Payment Services Security
**Applies to:** Payment service providers, payment initiation services, fintech companies with BOI licenses.

**Key control areas:**

#### Transaction Security
- Real-time fraud detection and prevention for all payment channels
- Multi-factor authentication (MFA) for high-value or high-risk transactions
- Transaction limits and velocity checks
- Behavioral analytics for anomaly detection

#### Data Protection
- End-to-end encryption for payment data in transit
- Encryption at rest for stored payment credentials
- PCI DSS compliance required for card data handling
- Tokenization for payment credential storage

#### API and Open Banking Security
- Secure API design following Open Banking standards
- OAuth 2.0 / OpenID Connect for API authentication
- API rate limiting and abuse prevention
- Certificate-based mutual TLS for inter-institution APIs

#### Consumer Protection
- Real-time alerts for suspicious transactions
- Easy mechanism for customers to dispute and freeze accounts
- Transparent disclosure of security practices
- Clear incident communication procedures

#### Pre-Launch Requirements
- New licensees must submit cybersecurity assessment to BOI before launch
- Assessment must cover: architecture review, penetration test results, SOC readiness
- BOI may require remediation before granting operational approval
- Ongoing reporting obligations post-launch

## Healthtech / Digital Health

### Ministry of Health Cyber Requirements
**Applies to:** Hospitals, HMOs (kupot cholim), digital health companies, medical device manufacturers.

#### Patient Data Protection
- Encryption required for all patient data (at rest and in transit)
- Access controls: role-based with minimum necessary access
- Audit trails for all access to patient records
- De-identification requirements for research and analytics use

#### Health Information Systems
- MOH approval required for core clinical systems (EMR/EHR)
- System availability requirements: 99.9% for critical clinical systems
- Change management procedures for clinical system updates
- Integration security for HL7/FHIR-based health data exchange

#### Medical Device Cybersecurity
- Pre-market: cybersecurity risk assessment required for MOH registration
- Software Bill of Materials (SBOM) for connected medical devices
- Vulnerability disclosure and patch management procedures
- Post-market surveillance for cybersecurity vulnerabilities
- Alignment with FDA and EU MDR cybersecurity guidance

#### Telemedicine Security
- Secure video communication (end-to-end encryption)
- Patient identity verification before clinical session
- Recording and storage policies per MOH guidelines
- Cross-border telemedicine additional requirements

#### Reporting
- Cyber incidents affecting patient safety: immediate reporting to MOH
- Data breaches involving patient data: report to Privacy Protection Authority
- Medical device vulnerabilities: report to MOH Medical Devices Division

## Defense / Aerospace

### MALMAB (Directorate of Security of the Defense Establishment)
**Applies to:** Defense contractors, aerospace companies, companies handling classified information.

#### Classification Levels
- **Shamur (Restricted):** Basic access controls and need-to-know
- **Sodi (Confidential):** Enhanced physical and logical security
- **Sodi Beyoter (Secret):** Air-gapped systems, personnel clearances
- **Sodi Beyoter Beyoter (Top Secret):** Maximum security controls

#### Requirements for Defense Contractors
- Facility Security Clearance (FSC) from MALMAB
- Personnel Security Clearance for employees handling classified data
- Physical security for areas processing classified information
- Air-gapped networks for Secret and above classifications
- Regular security audits by MALMAB inspectors
- Supply chain security assessments for sub-contractors

## Telecom / ISPs

### Ministry of Communications Requirements
**Applies to:** Telecommunications providers, ISPs, mobile operators.

#### Network Security
- Infrastructure protection against DDoS and network-level attacks
- Redundancy and resilience for critical communication infrastructure
- Monitoring and detection capabilities for network anomalies
- Incident response procedures for service-affecting events

#### Lawful Intercept
- Compliance with Wiretap Law (Chok Ha'a'azanot Seter, 1979)
- Technical capability for lawful intercept as required by court order
- Strict access controls for intercept systems
- Audit trails for all intercept-related activities

#### Customer Data
- Data retention periods per regulatory requirements
- Customer data protection (billing, call records, location data)
- Notification requirements for data breaches affecting customers
- Secure handling of subscriber identity information

## Energy / Utilities

### Critical Infrastructure Cybersecurity
**Applies to:** Electricity generation and distribution (IEC), natural gas, water (Mekorot), oil refineries.

#### OT/SCADA Security
- Network segmentation between IT and OT environments
- Dedicated monitoring for industrial control systems
- Restricted remote access to OT systems (MFA + VPN minimum)
- Regular vulnerability assessments of SCADA/ICS components
- Patch management adapted for OT availability requirements

#### Physical-Cyber Convergence
- Integrated security operations covering both physical and cyber domains
- Access control systems with cybersecurity protections
- Video surveillance system security
- Environmental monitoring integration

#### Reporting
- INCD mandatory incident reporting for all critical infrastructure events
- Ministry of Energy reporting for energy sector-specific incidents
- Water Authority reporting for water system incidents
- National Infrastructure Forum participation

## Regulator Contact Information

| Regulator | Department | Responsibility |
|-----------|-----------|---------------|
| INCD / CERT-IL | National Cyber Directorate | National cyber incident response |
| Bank of Israel | Banking Supervision | Financial sector cyber regulation |
| ISA | Israel Securities Authority | Listed company cyber disclosure |
| MOH | Digital Health Division | Health sector cyber requirements |
| Ministry of Communications | Telecom Regulation | Telecom sector security |
| Ministry of Energy | Infrastructure Protection | Energy sector security |
| MALMAB | Defense Security | Defense sector security |
| Privacy Protection Authority | Ministry of Justice | Data breach reporting (privacy) |
