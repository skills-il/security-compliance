# INCD (Israel National Cyber Directorate) Guidelines Reference

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
| Financial | Bank of Israel | Supervisor of Banks, Directive 357 |
| Insurance | Capital Markets Authority | Cyber regulation circular |
| Health | Ministry of Health | Health information security standards |
| Energy | National Infrastructure | Infrastructure protection division |
| Water | Water Authority | SCADA/ICS security requirements |
| Telecom | Ministry of Communications | License conditions |
| Government | INCD directly | Government ICT Authority standards |

## Critical Infrastructure Protection

### Designated Sectors
Israel designates the following as critical infrastructure:
1. **Energy** — Electricity (IEC), natural gas, fuel
2. **Water** — Mekorot, desalination plants, water utilities
3. **Finance** — Banks, stock exchange, payment systems
4. **Health** — Hospitals, HMOs (kupot cholim), medical devices
5. **Communications** — Telecom operators, internet infrastructure
6. **Transportation** — Airports, ports, railways, road systems
7. **Government** — Central and local government IT systems

### Requirements for Critical Infrastructure
- **Mandatory cyber incident reporting** to INCD
- **Risk assessment** — annual comprehensive assessment required
- **Security controls** — aligned with INCD framework
- **Incident response plan** — tested annually
- **Security officer** — dedicated CISO required
- **Supply chain security** — vendor risk management
- **Business continuity** — DR/BC plans for cyber scenarios

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
- **Cyber attacks** — successful or attempted
- **Malware infections** — especially ransomware
- **Data breaches** — unauthorized access to sensitive data
- **Service disruptions** — caused by cyber events
- **Vulnerabilities** — critical vulnerabilities in widely-used systems

### Reporting Timeline
| Severity | Reporting Deadline | To Whom |
|----------|-------------------|---------|
| Critical (active attack on critical infra) | Immediately | INCD hotline |
| High (successful breach, data exposure) | Within hours | CERT-IL portal |
| Medium (malware contained, no data loss) | Within 24 hours | CERT-IL portal |
| Low (attempted attack, blocked) | Best effort | CERT-IL portal |

### Reporting Channels
- **CERT-IL Portal:** Online incident reporting form
- **Hotline:** Phone reporting for urgent incidents
- **Email:** For non-urgent reports and inquiries
- **Sector regulators:** Some sectors have parallel reporting requirements

## Security Best Practices (INCD Recommended)

### For Organizations
1. **Multi-factor authentication** on all external-facing and privileged accounts
2. **Patch management** — critical patches within 24 hours, high within 7 days
3. **Network segmentation** — isolate critical systems from general network
4. **Backup strategy** — 3-2-1 rule (3 copies, 2 media types, 1 offsite)
5. **Email security** — SPF, DKIM, DMARC implementation
6. **Endpoint protection** — EDR on all endpoints
7. **Security awareness** — regular training for all employees
8. **Incident response** — documented and tested plan
9. **Supply chain** — assess and monitor vendor security
10. **Cloud security** — CSPM tools, proper IAM configuration

### For Software Development
1. **Secure SDLC** — security integrated into development lifecycle
2. **Code review** — security-focused code review process
3. **Dependency scanning** — automated SCA for third-party components
4. **SAST/DAST** — static and dynamic application security testing
5. **Container security** — image scanning, runtime protection
6. **API security** — authentication, rate limiting, input validation
7. **Secrets management** — no hardcoded credentials, use vaults

### For Cloud Environments
1. **Identity** — least privilege, MFA, regular access review
2. **Data** — encryption at rest and in transit, key management
3. **Network** — security groups, NACLs, VPN for management
4. **Monitoring** — cloud-native logging, CSPM tools (Wiz recommended)
5. **Compliance** — continuous compliance monitoring
6. **Incident response** — cloud-specific IR procedures

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
