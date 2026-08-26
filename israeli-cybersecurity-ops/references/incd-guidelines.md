# INCD (Israel National Cyber Directorate) Guidelines Reference

*Last reviewed 2026-08-26 (skill v1.3.0). Claims without a citation in this file are
practice guidance, not statutory obligations. Where this file and SKILL.md disagree, SKILL.md wins.*

## Overview

The Israel National Cyber Directorate (INCD, Ma'arach HaCyber HaLeumi) is the
national authority responsible for defending Israel's cyberspace. It operates
under the Prime Minister's Office and provides guidelines, threat intelligence,
and incident response coordination.

**Website:** https://www.gov.il/en/departments/israel_national_cyber_directorate

## Organizational Structure

### CERT-IL (National CERT)
- Israel's national Computer Emergency Response Team
- Handles cyber incident reports from all sectors
- Provides threat intelligence and advisories
- Contact for incident reporting: https://www.gov.il/he/departments/israel_national_cyber_directorate
- 24/7 hotline available for critical incidents

### Sector-Specific Regulators
| Sector | Regulator | Cyber Authority |
|--------|-----------|----------------|
| Financial | Bank of Israel | Supervisor of Banks, Proper Conduct of Banking Business Directive 364 (11/2024), which consolidates and supersedes Directives 357, 361 and 363 |
| Insurance | Capital Market, Insurance and Savings Authority | Has its own cyber requirements. Obtain the current circular from the Authority; its number and date are not asserted here |
| Health | Ministry of Health | Health information security standards |
| Energy | National Infrastructure | Infrastructure protection division |
| Water | Water Authority | SCADA/ICS security requirements |
| Telecom | Ministry of Communications | License conditions |
| Government | INCD directly | Government ICT Authority standards |

## Critical Infrastructure Protection

### Designated Sectors

**Individual critical-infrastructure designations by the INCD are NOT publicly listed.**
You cannot determine whether a given organisation is designated without that organisation
confirming its own status, and the named organisations below are illustrative examples of
the sectors, not a published designation list. Ask the organisation; do not infer.

The sectors generally understood to contain designated infrastructure:
1. **Energy**, Electricity (IEC), natural gas, fuel
2. **Water**, Mekorot, desalination plants, water utilities
3. **Finance**, Banks, stock exchange, payment systems
4. **Health**, Hospitals, HMOs (kupot cholim), medical devices
5. **Communications**, Telecom operators, internet infrastructure
6. **Transportation**, Airports, ports, railways, road systems
7. **Government**, Central and local government IT systems

### Requirements for Critical Infrastructure

Mandatory cyber incident reporting to the INCD is established. The remaining items below are
**recommended practice**, not citable statutory obligations: an earlier version of this file
listed them as "required", which upgraded guidance into mandates that no source here
supports. Where an organisation is designated, its actual obligations come from the specific
directive that binds it, which is not public. Obtain that directive from the organisation
or its regulator rather than relying on this list.

- **Mandatory cyber incident reporting** to INCD (established)
- **Risk assessment**, comprehensive and periodic (recommended; cadence per the binding directive)
- **Security controls**, aligned with the INCD framework (recommended)
- **Incident response plan**, tested periodically (recommended)
- **Security officer**, a dedicated CISO (recommended; separate from the Privacy Protection
  Law ממונה על הגנת הפרטיות / DPO, which is a different role with different triggers)
- **Supply chain security**, vendor risk management (recommended)
- **Business continuity**, DR/BC plans for cyber scenarios (recommended)

## INCD Cyber Defense Framework

### Framework Structure
The INCD framework is structured around five pillars:

#### 1. Identify
- Asset inventory (hardware, software, data, personnel)
- Risk assessment methodology
- Business environment understanding
- Governance structure for cybersecurity
- Legal and regulatory requirements mapping

#### 2. Protect
- Access control (identity management, authentication)
- Data security (encryption, DLP, classification)
- Security awareness training
- Protective technology (firewalls, IPS, endpoint protection)
- Secure development practices
- Maintenance and patch management

#### 3. Detect
- Continuous monitoring (SIEM, SOC)
- Anomaly detection
- Security event analysis
- Threat intelligence integration
- Detection processes and procedures

#### 4. Respond
- Incident response plan
- Communication plan (internal and external)
- Analysis and investigation
- Containment and mitigation
- Improvements from incidents

#### 5. Recover
- Recovery planning
- Improvements from lessons learned
- Communication during recovery
- Backup and restoration procedures

## Incident Reporting Requirements

### Who Must Report
- Critical infrastructure operators (mandatory)
- Government agencies (mandatory)
- All other organizations (voluntary but strongly encouraged)

### What to Report
- **Cyber attacks**, successful or attempted
- **Malware infections**, especially ransomware
- **Data breaches**, unauthorized access to sensitive data
- **Service disruptions**, caused by cyber events
- **Vulnerabilities**, critical vulnerabilities in widely-used systems

### Reporting Timeline

**There is no published INCD severity-tiered deadline schedule. Do not invent one.**
An earlier version of this file carried a four-row table ("Immediately / within hours /
within 24 hours / best effort"). It had no source and no such tiering is published by the
INCD. It has been removed. What is actually established:

| Duty | Timing | Channel |
|------|--------|---------|
| INCD, critical infrastructure | As soon as possible, in real time | Cyber event report service at gov.il/he/service/cyber-event-report, and the 119 hotline (24/7) |
| INCD, everyone else | Voluntary | Same channels. CERT-IL assistance is free to private-sector organisations |
| Privacy Protection Authority, serious security incident affecting personal data | **Immediately**. An initial report is required; waiting for the investigation to finish is expressly non-compliant | Written notification to the Authority |
| Sector regulator, if the entity is supervised | Per that regulator's own directive | Supervisor of Banks (Directive 364), Capital Market Insurance and Savings Authority, Ministry of Health |

Sector-specific directives may set their own timelines, and those override the general
position for entities they bind. **These duties run independently.** Reporting to CERT-IL
does not discharge the Privacy Protection Authority duty, and neither discharges a sector
regulator's duty. CERT-IL assistance is incident response help, not a regulatory filing.

### Reporting Channels
- **INCD cyber event report service:** https://www.gov.il/he/service/cyber-event-report
- **Hotline:** 119, answered 24/7
- **Sector regulators:** a supervised entity (bank, insurer, pension manager, HMO, hospital)
  owes a separate report to its own regulator. Confirm which regulator supervises the entity;
  this is the most commonly missed mandatory report in an Israeli incident.

## Security Best Practices (INCD Recommended)

### For Organizations
1. **Multi-factor authentication** on all external-facing and privileged accounts
2. **Patch management**, risk-based and prompt for critical vulnerabilities. (An earlier version of this file stated "critical within 24 hours, high within 7 days" as INCD guidance. Those figures had no citation and are not attributed to the INCD here. Set your own SLA, or follow the one your sector regulator imposes.)
3. **Network segmentation**, isolate critical systems from general network
4. **Backup strategy**, 3-2-1 rule (3 copies, 2 media types, 1 offsite)
5. **Email security**, SPF, DKIM, DMARC implementation
6. **Endpoint protection**, EDR on all endpoints
7. **Security awareness**, regular training for all employees
8. **Incident response**, documented and tested plan
9. **Supply chain**, assess and monitor vendor security
10. **Cloud security**, CSPM tools, proper IAM configuration

### For Software Development
1. **Secure SDLC**, security integrated into development lifecycle
2. **Code review**, security-focused code review process
3. **Dependency scanning**, automated SCA for third-party components
4. **SAST/DAST**, static and dynamic application security testing
5. **Container security**, image scanning, runtime protection
6. **API security**, authentication, rate limiting, input validation
7. **Secrets management**, no hardcoded credentials, use vaults

### For Cloud Environments
1. **Identity**, least privilege, MFA, regular access review
2. **Data**, encryption at rest and in transit, key management
3. **Network**, security groups, NACLs, VPN for management
4. **Monitoring**, cloud-native logging, CSPM tools (Wiz recommended)
5. **Compliance**, continuous compliance monitoring
6. **Incident response**, cloud-specific IR procedures

## Israeli Cybersecurity Ecosystem

### Key Israeli Cybersecurity Companies
| Company | Focus | Integration |
|---------|-------|-------------|
| Wiz | Cloud security (CSPM, CNAPP) | MCP server available |
| Snyk | Application security (SAST, SCA) | MCP server available |
| Check Point | Network security, threat prevention | API available |
| CyberArk | Privileged access management | API available |
| SentinelOne | Endpoint detection and response | API available |
| Armis | Asset visibility, IoT/OT security | API available |
| Torq | Security automation (SOAR) | 500+ integrations |
| Pentera | Automated penetration testing | API available |
| Claroty | OT/IoT security | API available |
| Cato Networks | SASE/SSE | API available |
| Orca Security | Cloud security (agentless) | API available |

### CyberSpark (Be'er Sheva)
- Israel's national cyber innovation hub
- Located in Be'er Sheva, Negev
- Hosts: Ben-Gurion University cyber center, INCD, major companies
- Incubator for cybersecurity startups

## Compliance Mapping

### Israeli Privacy Protection Law to Security Controls
| Privacy Requirement | Security Control | Tools |
|--------------------|-----------------|-------|
| Data security (basic) | Access control, logging | IAM, SIEM |
| Data security (medium) | + Encryption, security officer | KMS, DLP |
| Data security (high) | + Annual audit, DPO, pen testing | Pentera, audit |
| Breach notification | Incident detection and response | SIEM, EDR, IR plan |
| Cross-border transfer | Data flow monitoring, DLP | DLP, CASB |
| Database registration | Data inventory, classification | Data catalog |

### SOC2 to Israeli Tools Mapping
| SOC2 Trust Principle | Israeli Tool Coverage |
|---------------------|---------------------|
| Security | Wiz (cloud), SentinelOne (endpoint), Check Point (network) |
| Availability | Monitoring, DR/BC planning |
| Processing Integrity | Snyk (code quality), CI/CD security |
| Confidentiality | CyberArk (access), encryption tools |
| Privacy | Privacy controls, DLP, data classification |

### ISO 27001 Implementation
Israeli organizations pursuing ISO 27001 should:
1. Map INCD framework controls to ISO 27001 Annex A
2. Use INCD risk assessment methodology as basis
3. Align incident response with both INCD reporting and ISO requirements
4. Leverage Israeli cybersecurity tools for continuous control monitoring
