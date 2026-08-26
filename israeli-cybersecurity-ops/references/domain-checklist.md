# Domain coverage checklist: Israeli cybersecurity operations

Anchor for the Expert Review gate. Updated 2026-08-26 (v1.3.0).

## Must cover (core)

| # | Item | Authority | Status |
|---|------|-----------|--------|
| 1 | Privacy Protection Law as amended by Amendment 13 (in force 14 Aug 2025): immediate notification of a serious security incident, expanded definitions, expanded enforcement powers, statutory damages up to NIS 10,000 without proof of harm | PPL 1981 as amended; Information Security Regs 2017 reg. 11(d) | Covered |
| 2 | The breach clock is "immediately", NOT a GDPR-style 72 hours. Waiting to complete the investigation before reporting is non-compliant | Information Security Regs 2017, reg. 11(d) | Covered |
| 3 | DPO appointment triggers, and the fact that a database merely exceeding 10,000 individuals does not by itself trigger one | Amendment 13 | Covered |
| 4 | INCD reporting channels: the cyber-event-report service on gov.il AND the 119 hotline, 24/7 | gov.il/he/service/cyber-event-report | Covered |
| 5 | Israeli Cyber Defense Methodology (ICDM) 2.0, mapped to NIST CSF and SP 800-53 r5 | INCD | Covered |
| 6 | Critical infrastructure sectors and the fact that INCD designations are not publicly listed, so the organisation must confirm its own status | INCD | Covered |
| 7 | Banking sector: BOI Directive 364 (2024-11) consolidating 357, 361 and 363 | Bank of Israel, Supervisor of Banks | Covered |
| 8 | Triage inputs must be validated. An out-of-range CVSS or an unrecognised asset/data/blast category must warn rather than silently produce a score | Operational (tool correctness) | Covered (added in v1.3.0) |
| 8b | The INCD duty, the Privacy Protection Authority duty and a sector regulator's duty run INDEPENDENTLY. A CERT-IL report is assistance, not a regulatory filing | Amendment 13; sector directives | Covered (added in v1.3.0) |
| 8c | Sector-regulator reporting must be in the decision path. A supervised bank, insurer, pension manager, HMO or hospital is frequently NOT INCD-designated, so is_critical_infra=false must not read as "no report owed" | BOI Directive 364; Capital Market Authority; Ministry of Health | Covered (added in v1.3.0, `sector` parameter) |
| 8d | Ransomware payment is a legal decision. Payment to an entity linked to a designated terrorist organisation risks liability under the Counter-Terrorism Law 2016 and the Prohibition on Money Laundering Law, plus foreign sanctions | Counter-Terrorism Law 5776-2016; Prohibition on Money Laundering Law 5760-2000 | Covered (added in v1.3.0) |
| 8e | Preserve volatile evidence BEFORE containment | Forensic practice; PPA/INCD may request evidence | Covered (added in v1.3.0) |
| 8f | Triage scoring must not have a structural ceiling that prevents non-vulnerability incidents from reaching CRITICAL | Tool correctness | Covered (added in v1.3.0, weights renormalise when CVSS does not apply) |
| 9 | Vendor ownership changes: Wiz acquired by Google (closed 11 Mar 2026), CyberArk acquired by Palo Alto Networks (closed 11 Feb 2026), Check Point product renames | Vendor announcements | Covered |
| 10 | CERT-IL offers free incident response assistance to the private sector | INCD / CERT-IL | Covered |

## Should cover (advanced, not yet in the skill)

Recorded so a later cycle resurfaces them. NOT out of scope. Each was deliberately omitted this cycle because it could not be confirmed against a primary source: gov.il returns HTTP 403 to automated clients, and the Knesset bill APIs returned no matching record for the queries tried. Do not write any of these until read in a browser.

| # | Item | Why deferred |
|---|------|--------------|
| 11 | The proposed national Cybersecurity Law (חוק הגנת הסייבר הלאומית). Secondary sources report it passed a first reading in June 2026 and sits in the Foreign Affairs and Defense Committee, and that it would impose mandatory significant-incident reporting on essential organisations with administrative and criminal sanctions. **It is a bill, not law.** Neither its status nor its content could be confirmed against a Knesset primary source this cycle. Never describe it as being in force. | Unverified against a primary source |
| 12 | The Iron Swords temporary law on severe cyber attacks in the digital-services and hosting sector, reported to be extended to 31 January 2027, with a provider duty to report to the authorised administrator. Reported reporting timeframes could not be verified and must not be cited. | Unverified against a primary source |
| 13 | Whether any INCD binding directive has been issued in the last 12 months. INCD's directives index is on gov.il and unreadable to automated clients, so absence of evidence only. | Source unreachable |
| 14 | The Privacy Protection Authority's guidance on applying the law to AI systems, and its Privacy-Enhancing Technologies guidance. Directly relevant to a SOC running AI tooling. | Unverified against a primary source |
| 15 | Encryption Control Order (צו הפיקוח על מצרכים ושירותים, עיסוק באמצעי הצפנה) licensing, relevant to Israeli security-product vendors | Not researched this cycle |
| 16 | The specific number and date of the Capital Market, Insurance and Savings Authority cyber circular. The Authority is now named in the reporting path and in `SUPERVISED_SECTORS`, so the duty is surfaced; only the circular identifier is missing and it is deliberately not asserted anywhere | Identifier unverified against a primary source |

## Out of scope (explicit)

- **Offensive security testing and exploit development.** Already excluded by the description, correctly. Re-litigated 2026-08-26: still out of scope.
- **Application-layer secure coding, OWASP checklists and secrets scanning.** Handled by the sibling skill `israeli-appsec-scanner`; keeping them separate avoids two drifting copies of the same privacy-law content.
- **Physical security and personnel vetting.**
- **Advice on a specific enforcement action or warning letter.** Route to counsel.

## Authoritative sources

- Israel National Cyber Directorate: https://www.gov.il/he/departments/israel_national_cyber_directorate
- INCD cyber event reporting service: https://www.gov.il/he/service/cyber-event-report (119 hotline, 24/7)
- Privacy Protection Authority: https://www.gov.il/he/departments/the_privacy_protection_authority
- Information Security Regulations 2017: https://www.nevo.co.il/law_html/law00/144811.htm
- Bank of Israel Proper Conduct of Banking Business directives
