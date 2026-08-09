---
name: israeli-cybersecurity-ops
description: Coordinate Israeli-built cybersecurity tools for security operations including threat triage, vulnerability management, compliance checking, and incident response. Use when user mentions security operations, "SOC", vulnerability scanning, threat triage, compliance assessment, or asks to coordinate Wiz, Snyk, Check Point, CyberArk, SentinelOne, Armis, Torq, or Pentera tools. Embeds Israeli security best practices including INCD guidelines and Israeli Privacy Protection Law compliance. Do NOT use for offensive security testing or creating exploits.
license: MIT
compatibility: Best with MCP servers for Wiz and Snyk. Works standalone for security guidance. Claude Code recommended.
---

# Israeli Cybersecurity Ops

## Instructions

### Step 1: Identify Security Workflow
Determine which workflow the user needs:

| Workflow | When | Tools Involved |
|----------|------|---------------|
| Incident Triage | Alert received, need to classify and respond | Wiz, SentinelOne, Snyk |
| Vulnerability Management | Scan results need prioritization | Snyk, Wiz, Pentera |
| Compliance Assessment | Need to check against framework | Wiz (cloud), Snyk (code) |
| Threat Investigation | Suspicious activity, need to investigate | SentinelOne, Check Point |
| Access Review | Need to audit privileged access | CyberArk |

### Step 2: Gather Context
For any security workflow, collect:
- **Environment:** Cloud (AWS/Azure/GCP), On-prem, Hybrid
- **Available tools:** Which MCP servers or APIs are connected
- **Scope:** Specific asset, application, or organization-wide
- **Framework:** If compliance, SOC2, ISO27001, Israeli Privacy Law, INCD

### Step 3: Execute Workflow

#### Workflow A: Incident Triage (Sequential)

Phase 1: Alert Enrichment
1. Retrieve alert details from detection tool (Wiz/SentinelOne)
2. Enrich with asset information (owner, environment, criticality)
3. Check for related alerts in last 24 hours

Phase 2: Classification
4. Assess severity based on:
   - CVSS score (if vulnerability)
   - Asset criticality (production > staging > dev)
   - Data sensitivity (PII, financial, health data)
   - Blast radius (single host vs. network segment)
5. Classify: Critical / High / Medium / Low / False Positive

Phase 3: Response
6. If Critical/High: Immediate containment actions
7. If Medium: Add to sprint/backlog for remediation
8. If Low/FP: Document and close
9. Update tracking system (Monday.com if available)

#### Workflow B: Vulnerability Prioritization

Phase 1: Scan Collection
1. Gather findings from Snyk (code vulnerabilities, dependencies)
2. Gather findings from Wiz (cloud misconfigurations, vulnerabilities)
3. If available: Pentera results (exploitability validation)

Phase 2: Prioritization Matrix
4. Score each finding:
   - Exploitability (is there a public exploit?)
   - Reachability (is the vulnerable component reachable from internet?)
   - Data at risk (what data could be exposed?)
   - Business impact (revenue, reputation, regulatory)
5. Rank: Fix Now / Fix This Sprint / Fix This Quarter / Accept Risk

Phase 3: Remediation Plan
6. For each "Fix Now" item: specific remediation steps
7. Group by team/owner for efficient assignment
8. Create tracking items with deadlines

#### Workflow C: Israeli Compliance Check

Phase 1: Framework Selection
1. Israeli Privacy Protection Law (PPL) 1981 as amended through **Amendment 13** (in force August 14, 2025) + Information Security Regulations 2017. Amendment 13 requires immediate notification of a serious security incident to the PPA (the law says "immediately", not a GDPR-style fixed 72-hour clock), with notification to affected individuals where high risk; mandatory DPO triggers; expanded definitions of "personal information" and "sensitive data"; expanded PPA enforcement powers (administrative fines, cease-processing orders, deletion orders); and a statutory damages head added by Amendment 13 of up to NIS 10,000 without proof of harm; higher no-proof-of-harm ceilings under the older PPL statutory-damages provision are conditional, so consult the PPA's Amendment 13 guide rather than quoting a figure from memory.
2. INCD (Israel National Cyber Directorate / מערך הסייבר הלאומי) guidelines, current canonical methodology is the **Israeli Cyber Defense Methodology (ICDM) 2.0** (published 2021, mapped to NIST CSF 1.1 + SP 800-53 r5, with explicit Zero Trust + Threat-Informed Defense direction). The National Cyber Security Strategy was updated February 2025.
3. Banking Supervision (if financial sector): primary current directive is **BOI Directive 364** (2024-11) which consolidates and supersedes Directives 357, 361, and 363
4. SOC2 / ISO27001 (international); MITRE ATT&CK v18 (October 28, 2025) is current with Detection Strategies and Analytics

Phase 2: Control Assessment
5. Map Israeli-specific requirements:
   - Data protection officer (ממונה הגנת מידע / DPO) required? (Mandatory under Amendment 13 for public bodies; data brokers over 10,000 individuals; organizations whose main activity is large-scale processing of especially-sensitive data; and those carrying out systematic large-scale monitoring. A generic database merely exceeding 10,000 individuals does NOT by itself trigger a DPO.)
   - Risk-based regime under Amendment 13 (database registration is no longer the primary control)
   - Cross-border data transfer restrictions
   - Data breach notification: notify the PPA immediately for a serious security incident, plus affected individuals where high risk
   - Health data special protections (if applicable)
6. Check each control against current tool findings

Phase 3: Gap Report
7. Generate report with: Control, Status, Evidence, Gap, Remediation
8. Highlight Israeli-specific requirements separately

## Israeli-Specific Security Context

### INCD (Israel National Cyber Directorate) Guidelines
- Critical infrastructure sectors: Energy, Water, Finance, Health, Communications, Transportation
- Cyber event reporting: critical infrastructure must report as soon as possible (real-time) via the INCD cyber-event-report service (gov.il/he/service/cyber-event-report) and the 119 hotline; sector-specific directives may set their own timelines
- Annual risk assessment recommended
- Supply chain security emphasis (especially given documented Iranian / Hezbollah / Houthi-attributed targeting of Israeli software supply chains since 2023)

### Israeli Privacy Protection Law Key Requirements (post Amendment 13)
- Risk-based regime; database registration is no longer the primary compliance control
- Mandatory DPO triggers (public bodies, data brokers, systematic-monitoring, large/sensitive databases)
- Consent for data collection and processing
- Right of access and correction (similar to GDPR but predates it)
- Cross-border transfer: Adequate protection required
- Data breach notification: Required since Regulations 2017
- Penalties: Criminal and civil liability

## Examples

### Example 1: Cloud Alert Triage
User says: "Wiz flagged a critical finding in our production AWS account"
Actions: Follow Workflow A, retrieve Wiz finding details, assess blast radius, check for lateral movement indicators, provide containment recommendation.

### Example 2: Dependency Vulnerability
User says: "Snyk found 15 high vulnerabilities in our Node.js app"
Actions: Follow Workflow B, get Snyk details, check reachability, prioritize by exploitability, create remediation plan with specific version upgrades.

### Example 3: Privacy Compliance
User says: "We need to check if we comply with Israeli privacy law"
Actions: Follow Workflow C, map Israeli Privacy Protection Law requirements, check database registration status, review consent mechanisms, assess cross-border data flows.

## Bundled Resources

### Scripts
- `scripts/security_triage.py`, Structured security alert triage tool that calculates composite severity scores from CVSS, asset criticality, data sensitivity, and blast radius. Determines INCD reporting obligations for critical infrastructure and Privacy Authority notification for data breaches. Outputs classification, recommended response steps, and reporting deadlines. Run: `python scripts/security_triage.py --help`

### References
- `references/incd-guidelines.md`, Israel National Cyber Directorate reference covering CERT-IL, sector-specific regulators, critical infrastructure designations, the five-pillar INCD cyber defense framework (Identify/Protect/Detect/Respond/Recover), incident reporting timelines and channels, security best practices, and compliance mapping between Israeli Privacy Law, SOC2, and ISO 27001. Consult when assessing Israeli regulatory requirements or mapping security controls to compliance frameworks.

## Gotchas

- **Vendor ownership changes (2025-2026).** Wiz was acquired by Google for ~$32B (closed March 11, 2026) and now ships under Google Cloud Security alongside Mandiant; multi-cloud commitment preserved. CyberArk was acquired by Palo Alto Networks for ~$25B (closed February 11, 2026); CyberArk is now part of Palo Alto's identity platform (Cortex / Strata). Check Point product naming has shifted (Quantum SASE → Harmony SASE; Horizon Playblocks → Infinity Playblocks). Agents that quote pre-2026 vendor framing miss integration patterns and TOS implications. Wiz acquired by Google means the Wiz MCP can be expected to evolve toward Google Cloud Security MCP family.
- Israeli security tools (Wiz, Snyk, Check Point) may have Hebrew-language dashboards or alerts. Agents should not assume all output is in English when parsing tool responses.
- CERT-IL (the Israeli national CERT) provides free incident response assistance to private sector organizations, unlike many national CERTs. Agents may not recommend this free resource when advising on incident response.
- Israeli SOC teams typically operate Sunday-Thursday with reduced Friday coverage. Agents may generate 24/7 staffing plans based on Monday-Friday assumptions.
- CyberArk, a commonly used PAM tool in Israeli enterprises, uses Hebrew role names in many Israeli deployments. Agents should expect bilingual access control configurations.
- Israeli critical infrastructure designations by INCD are not publicly listed. Agents cannot determine if an organization is designated as critical infrastructure without the organization confirming it.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| INCD (Israel National Cyber Directorate) | https://www.gov.il/en/departments/israel_national_cyber_directorate | Critical infrastructure guidance, cyber event reporting |
| CERT-IL | https://www.gov.il/en/departments/guides/cyber_incident | Incident reporting, free IR assistance |
| Privacy Protection Authority | https://www.gov.il/en/departments/the_privacy_protection_authority | Database registration, breach notification rules |
| Wiz Documentation | https://docs.wiz.io | Cloud security findings, compliance frameworks |
| Snyk Documentation | https://docs.snyk.io | SAST, SCA, container scanning |
| OWASP Top 10 | https://owasp.org/www-project-top-ten/ | Vulnerability classification baseline |

## Troubleshooting

### Error: "MCP server not connected"
Cause: Wiz or Snyk MCP server not configured
Solution: This skill works without MCP for guidance mode. For full integration, connect Wiz MCP via Claude Desktop settings or Snyk MCP via `snyk mcp` command.

### Error: "Insufficient context for triage"
Cause: Not enough information about the alert or environment
Solution: Ask for: alert ID, affected asset, environment (prod/staging), data classification, and which detection tools are available.