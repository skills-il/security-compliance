---
name: israeli-cyber-regulations
description: >-
  Israeli cybersecurity regulatory framework guidance covering INCD (Ma'arach
  HaSyber) national directives, Bank of Israel Directive 361 (cyber for
  financial institutions), Directive 357 (payment security), ISA requirements
  for TASE-listed companies, and sector-specific rules for fintech and
  healthtech. Use when user asks about "cyber regulation Israel", "horaot
  Bank Israel 361", "INCD compliance", "Ma'arach HaSyber", "ISA cyber
  requirements", "sector cyber rules Israel", or "רגולציית סייבר". Covers
  regulatory mapping, gap analysis, compliance checklists, and audit
  preparation for Israeli cyber frameworks. Do NOT use for privacy law
  compliance (use israeli-privacy-compliance instead).
license: MIT
compatibility: 'No network required. Works with Claude Code, Claude.ai, Cursor.'
metadata:
  author: skills-il
  version: 1.0.0
  category: security-compliance
  tags:
    he:
      - סייבר
      - אבטחה
      - INCD
      - בנק-ישראל
      - רגולציה
    en:
      - cyber
      - security
      - incd
      - boi
      - regulations
  display_name:
    he: רגולציית סייבר ישראלית
    en: Israeli Cyber Regulations
  display_description:
    he: >-
      מסגרת רגולציית סייבר ישראלית — הנחיות מערך הסייבר הלאומי, הוראות בנק
      ישראל 361 ו-357, דרישות רשות ניירות ערך, וכללים מגזריים לפינטק ובריאות
    en: >-
      Israeli cybersecurity regulatory framework guidance covering INCD
      (Ma'arach HaSyber) national directives, Bank of Israel Directive 361
      (cyber for financial institutions), Directive 357 (payment security),
      ISA requirements for TASE-listed companies, and sector-specific rules
      for fintech and healthtech. Use when user asks about cyber regulation
      Israel, INCD compliance, Bank of Israel directives, ISA cyber
      requirements, or sector cyber rules. Do NOT use for privacy law
      compliance (use israeli-privacy-compliance instead).
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
    - antigravity
---

# Israeli Cyber Regulations

## Critical Note
This skill provides **regulatory guidance** for Israeli cybersecurity frameworks.
It does not replace legal counsel or professional security auditing.
For privacy law compliance (data protection, consent, PPA registration),
use the `israeli-privacy-compliance` skill instead.

## Instructions

### Step 1: Identify Applicable Regulatory Framework
Determine which Israeli cybersecurity regulations apply to the user's organization.

| Framework | Applies To | Regulator | Key Focus |
|-----------|-----------|-----------|-----------|
| INCD National Directives | All organizations, mandatory for critical infrastructure | Ma'arach HaSyber (INCD) | Risk management, incident reporting, baseline controls |
| BOI Directive 361 | Banks, insurance, credit card companies | Bank of Israel (BOI) | Cyber risk governance, SOC, penetration testing |
| BOI Directive 357 | Payment service providers, fintech | Bank of Israel (BOI) | Payment security, transaction monitoring, fraud prevention |
| ISA Cyber Requirements | TASE-listed companies | Israel Securities Authority (ISA/Rashut) | Disclosure, board oversight, cyber risk reporting |
| MOH Health Cyber | Hospitals, HMOs, health-tech | Ministry of Health | Patient data protection, medical device security |
| CDPA Telecom Rules | Telecom providers | Ministry of Communications | Network security, lawful intercept, data retention |

**Decision logic:**
```
Is the organization designated as critical infrastructure by INCD?
  YES -> INCD mandatory directives apply + sector-specific regulator
Is the organization a bank, insurer, or credit company?
  YES -> BOI Directive 361 applies (+ INCD if critical)
Does the organization provide payment services?
  YES -> BOI Directive 357 applies
Is the organization listed on TASE?
  YES -> ISA cyber disclosure requirements apply
Is the organization in healthcare?
  YES -> MOH health cyber directives apply
ALL organizations -> INCD voluntary baseline recommendations apply
```

### Step 2: INCD (Ma'arach HaSyber) Framework Assessment
The Israel National Cyber Directorate (INCD) sets national cybersecurity policy.

**INCD Five-Pillar Framework:**
| Pillar | Hebrew | Key Requirements |
|--------|--------|-----------------|
| Identify | זיהוי | Asset inventory, risk assessment, supply chain mapping |
| Protect | הגנה | Access control, encryption, secure configuration, training |
| Detect | גילוי | Monitoring, anomaly detection, log analysis, threat intelligence |
| Respond | תגובה | Incident response plan, containment, communication, CERT-IL coordination |
| Recover | שחזור | Business continuity, backup validation, lessons learned |

**INCD incident reporting requirements:**
- **Critical infrastructure:** Report to CERT-IL within hours of detection
- **Government bodies:** Mandatory reporting per Government ICT Authority (Rashut HaTkshov)
- **Private sector:** Voluntary but strongly recommended; CERT-IL provides free assistance
- **Reporting channel:** CERT-IL hotline or secure portal at `https://www.gov.il/he/departments/israel_national_cyber_directorate`

**Annual INCD compliance checklist:**
- [ ] Risk assessment completed and documented
- [ ] Asset inventory up to date (including OT/IoT)
- [ ] Incident response plan tested (tabletop or live drill)
- [ ] Supply chain security review performed
- [ ] Employee cybersecurity awareness training conducted
- [ ] Backup and recovery procedures validated
- [ ] Third-party penetration test (for critical infrastructure)

### Step 3: Bank of Israel Directive 361 — Cyber for Financial Institutions
Directive 361 (Hora'a 361) governs cybersecurity for banking and financial institutions.

**Core requirements:**
1. **Board-level cyber governance:** Board must approve cyber strategy and receive quarterly reports
2. **Dedicated CISO:** Must appoint a Chief Information Security Officer reporting to senior management
3. **Security Operations Center (SOC):** 24/7 monitoring for banks with significant digital operations
4. **Penetration testing:** Annual external pen test by certified Israeli firm
5. **Third-party risk:** Due diligence on all technology vendors, cloud providers require BOI approval
6. **Incident reporting:** Report significant cyber events to Banking Supervision within 24 hours

**Directive 361 compliance matrix:**
| Control Area | Requirement | Evidence Needed |
|-------------|-------------|-----------------|
| Governance | Board-approved cyber policy | Policy document + board minutes |
| Personnel | CISO appointment | Appointment letter, org chart |
| SOC | Continuous monitoring | SOC procedures, alert logs |
| Testing | Annual penetration test | Pen test report, remediation plan |
| Vendor management | Cloud/vendor approval | Approval documentation, SLAs |
| Incident response | Reporting within 24h | IR plan, drill records |
| Business continuity | DR site and testing | BCP document, DR drill results |

### Step 4: BOI Directive 357 — Payment Security
Directive 357 (Hora'a 357) covers security for payment services and fintech operations.

**Key requirements:**
- **Transaction monitoring:** Real-time fraud detection for all payment channels
- **Strong authentication:** Multi-factor authentication for high-value transactions
- **Encryption:** End-to-end encryption for payment data in transit and at rest
- **PCI DSS alignment:** Israeli payment providers must meet PCI DSS standards
- **API security:** Secure API design for Open Banking interfaces
- **Consumer notification:** Alert customers of suspicious transaction activity

**Fintech-specific considerations:**
- New fintech licensees under BOI supervision must submit cyber assessment before launch
- Payment initiation services require enhanced transaction monitoring
- Digital wallet providers must implement device binding and biometric verification
- Cross-border payment services face additional AML/CFT cyber controls

### Step 5: ISA Requirements for TASE-Listed Companies
The Israel Securities Authority (Rashut Niyarot Erech) requires listed companies to address cyber risk.

**Disclosure requirements:**
1. **Annual report:** Disclose material cyber risks in annual filing (Doch Shnati)
2. **Immediate report:** File immediate disclosure (Divuach Miyadi) for material cyber incidents
3. **Board oversight:** Board must demonstrate awareness of cyber risk management
4. **Risk factors:** Cyber risks must appear in risk factor section if material

**Materiality test for cyber incidents:**
```
Would a reasonable investor consider this information important?
  - Data breach affecting customers -> likely material
  - Ransomware disrupting operations -> likely material
  - Minor phishing attempt contained -> likely not material
  - Vendor breach with no data exposure -> case-by-case
File immediate report if: operational disruption > 24h, customer data exposed,
  financial loss > 1% of equity, or regulatory investigation triggered
```

**ISA compliance checklist:**
- [ ] Cyber risk section in annual report reviewed and current
- [ ] Board received cyber briefing in past 12 months
- [ ] Immediate reporting procedure defined and tested
- [ ] Cyber insurance coverage assessed and disclosed (if material)

### Step 6: Sector-Specific Rules
Apply additional requirements based on industry vertical.

**Fintech / Banking:**
- BOI Directive 361 + 357 (see Steps 3-4)
- Open Banking security standards (per BOI roadmap)
- AML/CFT cyber controls per IMPA (Israel Money Laundering Prohibition Authority)

**Healthtech / Digital Health:**
- MOH Circular on health information security
- Patient data: Israeli Privacy Protection Law + MOH-specific rules
- Medical devices: CE/FDA cyber requirements + MOH registration
- Telemedicine: Secure video, authentication, audit trails per MOH guidelines

**Defense / Aerospace:**
- DSDE (Directorate of Security of the Defense Establishment) / MALMAB oversight
- Classified information handling per Security of Defense Information regulations
- Supply chain security for defense contractors

**Telecom / ISPs:**
- Ministry of Communications network security requirements
- Lawful intercept capabilities per Wiretap Law (Chok Ha'a'azanot)
- Customer data retention and protection obligations

**Energy / Utilities:**
- INCD mandatory directives for critical infrastructure
- SCADA/OT security requirements
- Physical-cyber convergence controls

### Step 7: Build Regulatory Compliance Roadmap
Create a prioritized action plan based on identified gaps.

**Priority framework:**
| Priority | Criteria | Timeline |
|----------|----------|----------|
| Critical | Regulatory mandate with enforcement deadline | 0-30 days |
| High | Required by regulator, no immediate deadline | 30-90 days |
| Medium | Best practice recommended by INCD | 90-180 days |
| Low | Enhancement beyond minimum requirements | 180-365 days |

**Roadmap template:**
```
1. Identify all applicable frameworks (Step 1)
2. Map current controls to requirements
3. Perform gap analysis
4. Prioritize gaps by regulatory risk
5. Assign owners and deadlines
6. Implement controls
7. Document evidence for audit
8. Schedule periodic review (quarterly for financial, annually minimum)
```

## Examples

### Example 1: Fintech Startup Pre-Launch
User says: "We're launching a payment app in Israel, what cyber regulations apply?"
Actions:
1. Identify: BOI Directive 357 (payment security) + INCD baseline
2. Map requirements: transaction monitoring, MFA, encryption, PCI DSS
3. Check if TASE listing planned (ISA requirements)
4. Build pre-launch compliance checklist with BOI submission requirements
Result: Prioritized regulatory compliance roadmap for fintech launch with BOI submission timeline.

### Example 2: Bank Annual Cyber Audit
User says: "We need to prepare for our BOI Directive 361 annual review"
Actions:
1. Review Directive 361 compliance matrix against current controls
2. Verify: board approval, CISO reporting, SOC operations, pen test results
3. Check vendor management documentation and cloud approvals
4. Prepare gap report with remediation plan and evidence package
Result: Complete Directive 361 audit preparation package with evidence checklist and gap remediation plan.

### Example 3: TASE-Listed Company Cyber Incident
User says: "We had a data breach, do we need to file with ISA?"
Actions:
1. Apply materiality test: customer data exposed, operational impact, financial loss
2. Assess immediate disclosure obligation under ISA rules
3. Check INCD/CERT-IL reporting requirements
4. Draft disclosure timeline: ISA immediate report + CERT-IL notification + customer notification
Result: Incident disclosure decision with regulatory reporting timeline and draft notification framework.

### Example 4: Healthtech Compliance Assessment
User says: "Our healthtech startup handles patient data, what cyber rules apply?"
Actions:
1. Identify: MOH health cyber directives + INCD baseline + Privacy Protection Law
2. Map patient data requirements: encryption, access controls, audit trails
3. Check medical device classification (if applicable)
4. Build compliance matrix combining MOH, INCD, and privacy requirements
Result: Multi-framework compliance matrix with healthtech-specific controls and MOH submission requirements.

## Bundled Resources

### References
- `references/incd-guidelines.md` -- Comprehensive guide to INCD (Ma'arach HaSyber) framework including the five-pillar cyber defense model, CERT-IL reporting procedures, critical infrastructure designations, and national cybersecurity baseline requirements. Consult when assessing INCD compliance or preparing incident reports.
- `references/sector-rules.md` -- Sector-specific cybersecurity regulation details for financial services (BOI 361/357), healthtech (MOH), defense (MALMAB), telecom, and energy. Includes control matrices, reporting deadlines, and regulator contact information. Consult when mapping sector-specific requirements.

## Troubleshooting

### Error: "Unsure which framework applies"
Cause: Organization operates across multiple regulated sectors
Solution: Apply all applicable frameworks. Start with INCD baseline (applies to everyone), then layer sector-specific requirements. For dual-regulated entities (e.g., fintech listed on TASE), combine BOI 357 + ISA requirements.

### Error: "Conflicting requirements between regulators"
Cause: Different regulators set different standards for overlapping areas
Solution: Apply the stricter requirement. Document the rationale. For formal conflicts, consult with legal counsel specializing in Israeli financial regulation (orech din le-regulatziya finansit).

### Error: "No clear cyber regulation for our sector"
Cause: Some sectors lack specific cyber regulation
Solution: Follow INCD voluntary baseline recommendations as minimum standard. If handling personal data, also apply Privacy Protection Law security regulations (2017). Monitor INCD publications for emerging sector guidance.
