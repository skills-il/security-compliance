# Domain coverage checklist: Israeli application security and privacy compliance

Anchor for the Expert Review gate. Updated 2026-08-26 (v1.3.0).

## Must cover (core)

| # | Item | Authority | Status |
|---|------|-----------|--------|
| 1 | Amendment 13 in force 14 Aug 2025: expanded "personal information" and "sensitive data" definitions | Privacy Protection Law 1981 as amended | Covered |
| 2 | Registration vs notification: registration only for data brokers with more than 10,000 individuals and public bodies; separate notification for especially-sensitive data on more than 100,000, within 30 days (s.8A(b)); no annual renewal | PPL s.8A; PPA Amendment 13 guide | Covered |
| 3 | Three security levels (basic / medium / high) plus the individually-managed carve-out, with the correct First/Second Schedule triggers and the 100,000-subject and 100-authorized-user thresholds | Information Security Regs 2017, reg. 1 + First/Second Schedules | Covered in references/israeli-privacy-law-guide.md, summarised in both SKILL files (corrected in v1.3.0) |
| 4 | Periodic duties: audit every 24 months (medium and high); risk survey and penetration test every 18 months under Regulation 5 (high only; Regulation 15 is outsourcing); log retention 24 months | Regs 5(c)-(d), 10(d), 16(a), 17 | Covered in references/israeli-privacy-law-guide.md, summarised in both SKILL files (corrected in v1.3.0) |
| 5 | Breach notification: immediate notification of a serious incident; there is no Regulation 11A, the provision is Regulation 11(d) | Information Security Regs 2017, reg. 11(d) | Covered |
| 6 | Statutory damages up to NIS 10,000 without proof of harm under Amendment 13 | Amendment 13 | Covered |
| 7 | Cross-border transfer: a lawful gateway under reg. 1 or 2 AND the reg. 3 written undertaking from the recipient. The undertaking is not an alternative to consent | Transfer of Data Abroad Regs 2001, regs 1-3 | Covered in references/israeli-privacy-law-guide.md, summarised in both SKILL files (corrected in v1.3.0) |
| 8 | Anti-spam: s.30A Communications Law, prior opt-in, in-message sender ID and opt-out, damages up to NIS 1,000 per message without proof of harm | Communications (Telecommunications and Broadcasts) Law s.30A(i)(1) | Covered in the Gotchas of BOTH SKILL.md and SKILL_HE.md (added in v1.3.0) |
| 9 | Direct marketing opt-out under the live provision s.17F (s.17C repealed) | PPL s.17F | Covered |
| 10 | Data-subject rights and the 30-day access response window | PPL ss.13, 14(a) | Covered |
| 11 | OWASP Top 10, with an accurate cross-walk from the 2021 numbering to 2025 | owasp.org/Top10/2025 | Covered (checklist keyed to 2021, cross-walk note at top) |
| 12 | Secrets detection that matches modern prefixed key formats and unquoted `.env` assignment syntax | Vendor key-format docs | Covered in the Gotchas of BOTH SKILL.md and SKILL_HE.md (added in v1.3.0) |
| 13 | Trojan Source / BiDi control characters, homoglyphs, mixed-script rejection | CVE-2021-42574; UAX #9 | Covered |
| 14 | Teudat Zehut check digit (weights 1,2,1,2..., cast out 9s, sum mod 10) | Israeli MoI ID specification | Covered, algorithm independently verified correct |
| 15 | Supply-chain integrity: pin GitHub Actions to a full commit SHA, reference images by digest, rotate secrets exposed to a compromised CI window | GHSA-69fq-xp46-6x23 | Covered |

## Should cover (advanced, not yet in the skill)

These are genuine coverage gaps recorded so a later cycle resurfaces them. They are NOT out of scope.

| # | Item | Authority | Why deferred |
|---|------|-----------|--------------|
| 16 | PPA guidance on applying the PPL to AI systems, and the PETs guidance | gov.il PPA guidance pages | The PPA pages return HTTP 403 to automated clients, so the guidance could not be quoted verbatim in this cycle. Do not assert a date or content until read in a browser. |
| 17 | Expiry of the DPO appointment non-enforcement grace period, and the DPO independence / reporting-line duty | PPA DPO guidance | Two reviewers reported the grace period expired 31 Oct 2025; the date could not be confirmed against a primary source this cycle, so it was deliberately not written. Verify before adding. |
| 18 | EEA-inbound regulations 2023: erasure, notice, accuracy and retention duties on Israeli recipients of EEA data | Privacy Protection (Provisions Regarding Data Transferred to Israel from the EEA) Regs 2023 | Not verified against the regulation text this cycle. |
| 19 | Bank of Israel Proper Conduct of Banking Business Directives 361 and 363; Capital Market Authority cyber circular | Bank of Israel; Capital Market Authority | Applies to fintech/insurtech subset; large addition, next cycle. |
| 20 | SBOM (CycloneDX/SPDX), SLSA provenance attestation, dependency confusion against private registries | OWASP A03:2025 | The A03:2025 category is supply chain; the skill covers the Trivy incident but not SBOM tooling. |
| 21 | OWASP LLM Top 10: prompt injection, tool-call authorization, untrusted model output, secrets in context | OWASP Top 10 for LLM Applications | Increasingly relevant to the codebases this skill scans. |
| 22 | Blind index (keyed HMAC) alongside encrypted Teudat Zehut so encryption at rest survives a lookup requirement | Cryptographic engineering practice | Practical gap in the encryption guidance. |
| 23 | Shva / Ashrait protocol detail, EMV, acquirer-driven PCI scope; current acquirer set is Isracard, CAL and Max (Leumi Card was rebranded Max in 2019) | Acquirer integration docs | The skill's one-line Shva mention is not actionable. |

## Out of scope (explicit)

- **Network penetration testing, physical security, red-teaming.** The skill's description already excludes these, correctly. Re-litigated 2026-08-26: still out of scope, a separate discipline with a separate toolchain.
- **Defence and security bodies (גופי ביטחון).** Carved out of the DPO obligation and much of the PPL; a specialist regime.
- **Accessibility (IS 5568 / Regulation 35).** A separate compliance regime, not application security.
- **Advice on a specific enforcement action or warning letter.** Route the user to counsel.
- **Malware reverse engineering, EDR/SOC operations, cloud infrastructure hardening below the application layer.**

## Authoritative sources

- Privacy Protection Law 1981 and Amendment 13, PPA professional guide (gov.il)
- Information Security Regulations 2017: https://www.nevo.co.il/law_html/law00/144811.htm
- Transfer of Data Abroad Regulations 2001: https://www.nevo.co.il/law_html/law00/71639.htm
- Communications (Telecommunications and Broadcasts) Law s.30A
- OWASP Top 10 2025: https://owasp.org/Top10/2025/ and 2021: https://owasp.org/Top10/2021/
- Trojan Source: https://trojansource.codes/ ; UAX #9: https://unicode.org/reports/tr9/
- Israel National Cyber Directorate: https://www.gov.il/he/departments/israel_national_cyber_directorate
