---
name: israeli-cybersecurity-ops
description: >-
  Coordinate Israeli-built cybersecurity tools for security operations including
  threat triage, vulnerability management, compliance checking, and incident
  response. Use when user mentions security operations, "SOC", vulnerability
  scanning, threat triage, compliance assessment, or asks to coordinate Wiz,
  Snyk, Check Point, CyberArk, SentinelOne, Armis, Torq, or Pentera tools.
  Embeds Israeli security best practices including INCD guidelines and Israeli
  Privacy Protection Law compliance. Do NOT use for offensive security testing
  or creating exploits.
license: MIT
compatibility: >-
  Best with MCP servers for Wiz and Snyk. Works standalone for security
  guidance. Claude Code recommended.
metadata:
  author: skills-il
  version: 1.0.0
  category: security-compliance
  tags:
    he:
      - סייבר
      - תפעול-אבטחה
      - Wiz
      - Snyk
      - ציות
      - ישראל
    en:
      - cybersecurity
      - security-ops
      - wiz
      - snyk
      - compliance
      - israel
  mcp-server: 'wiz, snyk'
  display_name:
    he: אבטחת סייבר ישראלית
    en: Israeli Cybersecurity Ops
  display_description:
    he: 'תיאום כלי אבטחה ישראליים — Wiz, Snyk, Check Point ועוד'
    en: >-
      Coordinate Israeli-built cybersecurity tools for security operations
      including threat triage, vulnerability management, compliance checking,
      and incident response. Use when user mentions security operations, "SOC",
      vulnerability scanning, threat triage, compliance assessment, or asks to
      coordinate Wiz, Snyk, Check Point, CyberArk, SentinelOne, Armis, Torq, or
      Pentera tools. Embeds Israeli security best practices including INCD
      guidelines and Israeli Privacy Protection Law compliance. Do NOT use for
      offensive security testing or creating exploits.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
    - antigravity
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
- **Framework:** If compliance — SOC2, ISO27001, Israeli Privacy Law, INCD

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
1. Israeli Privacy Protection Law (IPPI) 1981 + Regulations 2017
2. INCD (Israel National Cyber Directorate) guidelines
3. Banking Supervision (if financial sector)
4. SOC2 / ISO27001 (international)

Phase 2: Control Assessment
5. Map Israeli-specific requirements:
   - Data protection officer (memune piyuach) required?
   - Database registration with Privacy Protection Authority
   - Cross-border data transfer restrictions
   - Data breach notification requirements
   - Health data special protections (if applicable)
6. Check each control against current tool findings

Phase 3: Gap Report
7. Generate report with: Control, Status, Evidence, Gap, Remediation
8. Highlight Israeli-specific requirements separately

## Israeli-Specific Security Context

### INCD (Israel National Cyber Directorate) Guidelines
- Critical infrastructure sectors: Energy, Water, Finance, Health, Communications, Transportation
- Cyber event reporting: Required within hours for critical infrastructure
- Annual risk assessment recommended
- Supply chain security emphasis

### Israeli Privacy Protection Law Key Requirements
- Registration of databases with Privacy Protection Authority
- Consent for data collection and processing
- Right of access and correction (similar to GDPR but predates it)
- Cross-border transfer: Adequate protection required
- Data breach notification: Required since Regulations 2017
- Penalties: Criminal and civil liability

## Examples

### Example 1: Cloud Alert Triage
User says: "Wiz flagged a critical finding in our production AWS account"
Actions: Follow Workflow A — retrieve Wiz finding details, assess blast radius, check for lateral movement indicators, provide containment recommendation.

### Example 2: Dependency Vulnerability
User says: "Snyk found 15 high vulnerabilities in our Node.js app"
Actions: Follow Workflow B — get Snyk details, check reachability, prioritize by exploitability, create remediation plan with specific version upgrades.

### Example 3: Privacy Compliance
User says: "We need to check if we comply with Israeli privacy law"
Actions: Follow Workflow C — map Israeli Privacy Protection Law requirements, check database registration status, review consent mechanisms, assess cross-border data flows.

## Bundled Resources

### Scripts
- `scripts/security_triage.py` — Structured security alert triage tool that calculates composite severity scores from CVSS, asset criticality, data sensitivity, and blast radius. Determines INCD reporting obligations for critical infrastructure and Privacy Authority notification for data breaches. Outputs classification, recommended response steps, and reporting deadlines. Run: `python scripts/security_triage.py --help`

### References
- `references/incd-guidelines.md` — Israel National Cyber Directorate reference covering CERT-IL, sector-specific regulators, critical infrastructure designations, the five-pillar INCD cyber defense framework (Identify/Protect/Detect/Respond/Recover), incident reporting timelines and channels, security best practices, and compliance mapping between Israeli Privacy Law, SOC2, and ISO 27001. Consult when assessing Israeli regulatory requirements or mapping security controls to compliance frameworks.

## Troubleshooting

### Error: "MCP server not connected"
Cause: Wiz or Snyk MCP server not configured
Solution: This skill works without MCP for guidance mode. For full integration, connect Wiz MCP via Claude Desktop settings or Snyk MCP via `snyk mcp` command.

### Error: "Insufficient context for triage"
Cause: Not enough information about the alert or environment
Solution: Ask for: alert ID, affected asset, environment (prod/staging), data classification, and which detection tools are available.