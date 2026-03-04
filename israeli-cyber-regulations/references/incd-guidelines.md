# INCD (Ma'arach HaSyber) Framework Reference

## Overview

The Israel National Cyber Directorate (INCD / Ma'arach HaSyber HaLeumi) is the national authority responsible for defending Israel's cyberspace. Established under the Prime Minister's Office, INCD sets cybersecurity policy, coordinates incident response through CERT-IL, and issues guidelines for both public and private sectors.

**Official portal:** `https://www.gov.il/he/departments/israel_national_cyber_directorate`

## Organizational Structure

### CERT-IL (National Cyber Emergency Response Team)
- **Role:** Receives, analyzes, and responds to cyber incidents across all sectors
- **Hotline:** Available 24/7 for incident reporting
- **Services:** Threat intelligence sharing, incident investigation, forensic assistance
- **Free for:** All Israeli organizations (public and private)

### Government ICT Authority (Rashut HaTkshov HaMemshalti)
- **Role:** Sets IT and cybersecurity standards for government ministries and agencies
- **Mandate:** All government systems must comply with Rashut HaTkshov directives
- **Oversight:** Regular audits of government ICT systems

### Sector-Specific Coordination
INCD coordinates with sector regulators:
- **Banking:** Bank of Israel — Banking Supervision Division
- **Capital Markets:** Israel Securities Authority (ISA)
- **Health:** Ministry of Health — Digital Health Division
- **Energy:** Ministry of Energy — Infrastructure Protection
- **Telecom:** Ministry of Communications
- **Defense:** MALMAB (Directorate of Security of the Defense Establishment)

## Five-Pillar Cyber Defense Framework

### Pillar 1: Identify (Zihui)
**Objective:** Understand the organizational environment to manage cyber risk.

Key activities:
- **Asset inventory:** Catalog all hardware, software, data stores, and network components
- **Risk assessment:** Annual threat and vulnerability assessment
- **Supply chain mapping:** Identify all third-party dependencies and their risk profile
- **Data classification:** Categorize data by sensitivity (public, internal, confidential, restricted)
- **Business impact analysis:** Determine critical assets and acceptable downtime

### Pillar 2: Protect (Hagana)
**Objective:** Implement safeguards to ensure delivery of critical services.

Key controls:
- **Access control:** Role-based access, least privilege, MFA for privileged accounts
- **Encryption:** Data at rest and in transit encryption per classification level
- **Secure configuration:** Hardened baselines for servers, endpoints, and network devices
- **Patch management:** Critical patches within 48 hours, regular patches within 30 days
- **Employee training:** Annual cybersecurity awareness training for all staff
- **Network segmentation:** Separate critical systems from general network

### Pillar 3: Detect (Gilui)
**Objective:** Identify cybersecurity events in a timely manner.

Key capabilities:
- **Continuous monitoring:** Log collection and analysis from all critical systems
- **Anomaly detection:** Behavioral analysis for unusual network and user activity
- **Threat intelligence:** Integration with CERT-IL feeds and commercial threat intel
- **Vulnerability scanning:** Regular automated scans of internal and external assets
- **Penetration testing:** Annual external penetration test (mandatory for critical infrastructure)

### Pillar 4: Respond (Tguva)
**Objective:** Take action regarding a detected cybersecurity incident.

Key procedures:
- **Incident response plan:** Documented, tested, and updated annually
- **Containment:** Procedures for isolating affected systems
- **Communication:** Internal escalation paths and external notification procedures
- **CERT-IL coordination:** Contact CERT-IL for assistance and intelligence sharing
- **Evidence preservation:** Chain of custody procedures for forensic evidence
- **Post-incident review:** Lessons learned within 30 days of incident closure

### Pillar 5: Recover (Shichzur)
**Objective:** Restore capabilities and services impacted by a cybersecurity incident.

Key activities:
- **Business continuity plan:** Documented recovery procedures for all critical systems
- **Backup validation:** Regular testing of backup integrity and restoration procedures
- **DR testing:** Annual disaster recovery drill with documented results
- **Communication plan:** Stakeholder notification during and after recovery
- **Improvement cycle:** Incorporate lessons learned into preventive controls

## Critical Infrastructure Designations

INCD designates the following sectors as critical infrastructure with mandatory cybersecurity requirements:

| Sector | Examples | Lead Regulator |
|--------|----------|---------------|
| Energy | IEC, natural gas, refineries | Ministry of Energy |
| Water | Mekorot, municipal water authorities | Water Authority |
| Finance | Major banks, payment clearinghouses | Bank of Israel |
| Health | Major hospitals, HMO systems | Ministry of Health |
| Communications | Bezeq, Cellcom, Partner, HOT | Ministry of Communications |
| Transportation | Airports, ports, Israel Railways | Ministry of Transport |
| Government | Ministries, agencies, local authorities | Rashut HaTkshov |

### Obligations for Critical Infrastructure
- Mandatory incident reporting to CERT-IL
- Annual risk assessment per INCD methodology
- External penetration testing annually
- 24/7 monitoring capability (SOC or equivalent)
- Participation in national cyber drills when called
- Supply chain security assessment for critical vendors

## Incident Reporting Procedures

### Reporting Timeline
| Severity | Report To | Deadline | Method |
|----------|----------|----------|--------|
| Critical (active attack, data exfil) | CERT-IL | Immediately (within hours) | Hotline + secure portal |
| High (confirmed breach, service impact) | CERT-IL | Within 24 hours | Secure portal |
| Medium (attempted attack, contained) | CERT-IL | Within 72 hours | Secure portal |
| Low (reconnaissance, probing) | CERT-IL | Best effort | Secure portal |

### What to Report
- Nature of the incident (type, vector, scope)
- Affected systems and data
- Current status (ongoing, contained, resolved)
- Impact assessment (data exposure, service disruption)
- Actions taken so far
- Assistance requested from CERT-IL

### CERT-IL Assistance
CERT-IL provides free assistance including:
- Incident investigation and forensic analysis
- Malware analysis
- Threat intelligence and indicators of compromise (IOCs)
- Coordination with international CERTs
- Recovery guidance

## INCD Baseline Recommendations

For organizations not designated as critical infrastructure, INCD recommends the following minimum controls:

1. **Endpoint protection:** Anti-malware on all endpoints, kept up to date
2. **Firewall:** Network firewall with deny-by-default policy
3. **Patch management:** Regular patching of OS and applications
4. **Access control:** Unique user accounts, strong passwords, MFA where possible
5. **Backup:** Regular backups stored offline or in separate network segment
6. **Email security:** Anti-phishing and anti-spam filters
7. **Awareness:** Basic cybersecurity training for all employees
8. **Incident plan:** Basic incident response procedure documented
9. **Encryption:** Encrypt sensitive data at rest and in transit
10. **Vendor management:** Assess cybersecurity posture of key vendors

## Compliance Mapping

| INCD Requirement | ISO 27001 | SOC 2 | NIST CSF |
|-----------------|-----------|-------|----------|
| Asset inventory | A.8.1 | CC6.1 | ID.AM |
| Risk assessment | 6.1.2, A.8.2 | CC3.2 | ID.RA |
| Access control | A.9 | CC6.1-6.3 | PR.AC |
| Encryption | A.10.1 | CC6.1, CC6.7 | PR.DS |
| Monitoring | A.12.4 | CC7.1-7.3 | DE.CM |
| Incident response | A.16 | CC7.3-7.5 | RS.RP |
| Business continuity | A.17 | A1.2 | RC.RP |
| Awareness training | A.7.2.2 | CC1.4 | PR.AT |
