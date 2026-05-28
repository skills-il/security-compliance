---
name: israeli-cyber-regulations
description: Israeli cybersecurity regulatory framework guidance covering INCD (Ma'arach HaSyber) national directives, Bank of Israel Directive 361 (cyber for financial institutions), Directive 364 (the consolidated IT, information security, and cyber framework), ISA requirements for TASE-listed companies, and sector-specific rules for fintech and healthtech. Use when user asks about "cyber regulation Israel", "horaot Bank Israel 361", "INCD compliance", "Ma'arach HaSyber", "ISA cyber requirements", "sector cyber rules Israel", or "רגולציית סייבר". Covers regulatory mapping, gap analysis, compliance checklists, and audit preparation for Israeli cyber frameworks. Do NOT use for privacy law compliance (use israeli-privacy-compliance instead).
license: MIT
compatibility: No network required. Works with Claude Code, Claude.ai, Cursor.
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
| BOI Directive 364 (Nov 2024, effective 18 May 2026) | Banks, insurance, credit card companies | Bank of Israel (BOI) | **Consolidates and supersedes Directives 357, 361, 363**; primary current cyber framework. On its effective date the three legacy directives are repealed. Stronger board accountability, supply-chain expectations |
| BOI Directive 361 | Banks, insurance, credit card companies | Bank of Israel (BOI) | Cyber Defense Management: cyber risk governance, CISO, SOC, penetration testing. Folded into 364 |
| BOI Directive 357 | Banks | Bank of Israel (BOI) | Management of Information Technology (general IT governance, NOT payment-specific). Folded into 364 |
| BOI Directive 366 | Banks | Bank of Israel (BOI) | Reporting of technological-failure and cyber events (the operational incident-reporting hook) |
| BOI Directive 362 | Banks (cloud) | Bank of Israel (BOI) | Cloud Computing approval process (the directive that defines the cloud-approval workflow referenced under 361 Third-Party Risk) |
| ISA Cyber Requirements | TASE-listed companies | Israel Securities Authority (ISA/Rashut) | Disclosure, board oversight, cyber risk reporting |
| MOH Health Cyber | Hospitals, HMOs, health-tech | Ministry of Health | Patient data protection, medical device security |
| CDPA Telecom Rules | Telecom providers | Ministry of Communications | Network security, lawful intercept, data retention |

**Decision logic:**
```
Is the organization designated as critical infrastructure by INCD?
  YES -> INCD mandatory directives apply + sector-specific regulator
Is the organization a bank, insurer, or credit company?
  YES -> BOI Directive 364 applies (consolidating the legacy 357 IT-management, 361 cyber, 363 directives) (+ INCD if critical)
Does the organization provide payment services?
  YES -> BOI payment-service-provider supervision applies, plus the BOI IT/cyber directives (357 IT management, 361 cyber, now under 364)
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
- **Reporting channel:** CERT-IL hotline or secure portal at https://www.gov.il/he/departments/israel_national_cyber_directorate

**Annual INCD compliance checklist:**
- [ ] Risk assessment completed and documented
- [ ] Asset inventory up to date (including OT/IoT)
- [ ] Incident response plan tested (tabletop or live drill)
- [ ] Supply chain security review performed
- [ ] Employee cybersecurity awareness training conducted
- [ ] Backup and recovery procedures validated
- [ ] Third-party penetration test (for critical infrastructure)

### Step 3: Bank of Israel Cyber Directives (357 / 361 / 363, now consolidated under 364)

> **Directive 364 (November 2024) consolidates and supersedes Directives 357, 361, and 363.** Directive 364, "Management of IT, Information Security, and Cyber Protection Risks," is the primary current cyber framework for banks. The legacy directives are still listed in the BOI Proper Conduct index for transitional purposes, but new control programs should map to 364, not to 361 alone. Reporting mechanics for technological failures and cyber incidents sit under **Directive 366**, and cloud-computing approval is governed by **Directive 362**. For consumer audiences (banks, insurance, credit card companies) the substantive control content from 361 carries forward into 364, with stronger board accountability and supply-chain expectations.

Directive 361 (Hora'a 361) governs cybersecurity for banking and financial institutions and is the operative directive most agents reference; treat its controls as a baseline to map against 364.

**Core requirements:**
1. **Board-level cyber governance:** Board must approve cyber strategy and receive quarterly reports
2. **Dedicated CISO:** Must appoint a Chief Information Security Officer reporting to senior management
3. **Security Operations Center (SOC):** 24/7 monitoring for banks with significant digital operations
4. **Penetration testing:** Annual external pen test by certified Israeli firm
5. **Third-party risk:** Due diligence on all technology vendors, cloud providers require BOI approval
6. **Incident reporting:** Report significant technological-failure and cyber events to Banking Supervision per the timelines set in Directive 366 (the reporting directive), not under 361 itself

**Directive 361 compliance matrix:**
| Control Area | Requirement | Evidence Needed |
|-------------|-------------|-----------------|
| Governance | Board-approved cyber policy | Policy document + board minutes |
| Personnel | CISO appointment | Appointment letter, org chart |
| SOC | Continuous monitoring | SOC procedures, alert logs |
| Testing | Annual penetration test | Pen test report, remediation plan |
| Vendor management | Cloud/vendor approval | Approval documentation, SLAs |
| Incident response | Reporting per Directive 366 | IR plan, drill records |
| Business continuity | DR site and testing | BCP document, DR drill results |

### Step 4: Payment and Fintech Security
Payment-service security for banks and fintech is governed by the BOI IT and cyber directives (now consolidated under 364) together with BOI supervision of payment service providers. Note: Directive 357 itself is "Management of Information Technology", a general IT-governance directive, not a payment-specific rule, so do not cite "357" as the payment-security authority. The substantive payment-security expectations are:

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
- BOI Directive 364 (consolidating 361 cyber defense + 357 IT management + 363) (see Steps 3-4)
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
1. Identify: BOI payment-service-provider supervision + the IT/cyber directives (364, consolidating 357/361/363) + INCD baseline
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

## Gotchas

- Bank of Israel Directive 361 requires cloud providers to receive explicit BOI approval before use. Agents may assume any SOC 2-certified cloud provider is automatically compliant for Israeli banks.
- INCD (Ma'arach HaSyber) incident reporting timelines differ by sector: critical infrastructure must report within hours, while private sector reporting is voluntary. Agents may apply a single timeline across all sectors.
- The Israeli Securities Authority (ISA/Rashut) uses a different materiality test for cyber incident disclosure than the US SEC. Agents may apply US materiality standards to TASE-listed companies.
- Israel's DPO (Data Protection Officer) requirement is in force since Amendment 13 (effective August 14, 2025) and covers public bodies and large-scale sensitive data processors. Agents with pre-2025 training data may not know about this requirement.
- **Amendment 13 cross-reference for cyber teams.** While privacy compliance lives in `israeli-privacy-compliance`, cyber incident-response playbooks must align with Amendment 13's requirement to notify the PPA of a serious security incident **immediately** (the law says "immediately", NOT a GDPR-style fixed 72-hour clock), plus notification to affected individuals where there is high risk. Stack this against the BOI sector reporting timelines (Directive 366) and the ISA materiality test.
- **National Cybersecurity Bill (draft, January 2026).** INCD published a draft "Cyber Defense Law" (tazkir) on 22 January 2026 imposing binding controls on "essential organizations" (irgun chiyoni) and codifying CERT-IL / INCD authority, with ISO 27001/27002 offered as a compliance route. Not yet enacted, but track for applicability scoping. Flag clients with critical-infrastructure exposure to expect future statutory expansion of the current INCD methodology.
- Directive 357 is "Management of Information Technology" (general IT governance), NOT a payment-security directive. Agents that cite "Directive 357" as the Israeli payment-security rule are mislabeling it. Payment-service security comes from BOI payment-service-provider supervision plus the IT/cyber directives (consolidated under 364). A pre-launch cybersecurity assessment is part of BOI fintech/payment licensing, not a "357" requirement.


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Israel National Cyber Directorate (INCD) | https://www.gov.il/he/departments/israel_national_cyber_directorate | Official cyber regulations, incident reporting, critical infrastructure rules |
| Protection of Privacy Law (Knesset) | https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/default.aspx | Privacy Protection Law 1981 and 2024 amendments, breach notification |
| Privacy Protection Authority | https://www.gov.il/he/departments/the_privacy_protection_authority | Database registration, data subject rights, enforcement guidelines |
| CERT-IL | https://www.gov.il/he/departments/units/cert_il | National CERT advisories, vulnerability disclosures, sector alerts |
| Bank of Israel cyber directive | https://www.boi.org.il/en/economic-roles/supervision-and-regulation/ | Proper Conduct Directive 361 (cyber defense management for banks) |

## Troubleshooting

### Error: "Unsure which framework applies"
Cause: Organization operates across multiple regulated sectors
Solution: Apply all applicable frameworks. Start with INCD baseline (applies to everyone), then layer sector-specific requirements. For dual-regulated entities (e.g., fintech listed on TASE), combine BOI 364 (the consolidated IT/cyber framework) + ISA requirements.

### Error: "Conflicting requirements between regulators"
Cause: Different regulators set different standards for overlapping areas
Solution: Apply the stricter requirement. Document the rationale. For formal conflicts, consult with legal counsel specializing in Israeli financial regulation (orech din le-regulatziya finansit).

### Error: "No clear cyber regulation for our sector"
Cause: Some sectors lack specific cyber regulation
Solution: Follow INCD voluntary baseline recommendations as minimum standard. If handling personal data, also apply Privacy Protection Law security regulations (2017). Monitor INCD publications for emerging sector guidance.