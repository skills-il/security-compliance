---
name: israeli-ai-compliance-kit
description: "Guide Israeli ML teams through the AI governance and compliance stack: Ministry of Innovation December 2023 AI policy principles, Privacy Protection Law (PPL) and Amendment 13 applied to ML training data, sector-specific rules (Bank of Israel Directive 364, Ministry of Health AMAR medical-device AI), and EU AI Act exposure for Israeli exporters. Generates model cards, data statements, and DPIA templates tailored to Israeli context. Use when preparing AI governance docs, answering an enterprise customer's AI risk review, classifying a system under the EU AI Act, or building an internal responsible-AI checklist. Prevents costly compliance gaps when shipping AI to regulated markets. Do NOT use for general PPL policy (use israeli-privacy-shield), web app security (use israeli-appsec-scanner), or SOC/threat triage (use israeli-cybersecurity-ops)."
license: MIT
---

# Israeli AI Compliance Kit

## Problem

Israeli ML teams shipping AI products face a fragmented compliance landscape: voluntary principles from the Ministry of Innovation, the Privacy Protection Law with Amendment 13 arriving in August 2025, sector regulators each drafting their own AI guidance, and the EU AI Act reaching anyone selling into Europe. Most teams discover these requirements mid-procurement when an enterprise customer demands a model card, data statement, and DPIA. There is no unified checklist or template set tailored to the Israeli regulatory context.

## Instructions

### Step 1: Scope Your AI System

Before any compliance work, classify the system across four axes. The classification determines which regimes apply.

| Axis | Options | Why it matters |
|------|---------|----------------|
| System type | GenAI (LLM, image, audio), Predictive ML, Rule-based | EU AI Act GPAI obligations target GenAI. Predictive models fall under Annex III if used in high-risk domains |
| Personal data | Yes (training or inference), No | Triggers PPL, Amendment 13 obligations, Data Security Regulations 2017 |
| EU market exposure | Placed on EU market, Output used in EU, Neither | Determines EU AI Act applicability under Article 2 |
| Israeli sector regulator | Banking (BoI), Health (MoH AMAR), Insurance (CMISA), Transport (MoT), Defense (MoD), None | Each regulator has distinct obligations; some predate AI-specific rules |

Output a one-page scoping memo with these four answers before continuing. This memo is the first artifact the customer's AI risk review will ask for.

### Step 2: Israel's Ministry of Innovation AI Policy (December 2023)

The authoritative document is "Policy, Regulation and Ethics Principles in the Field of Artificial Intelligence", published December 14, 2023 jointly by the Ministry of Innovation, Science and Technology and the Ministry of Justice. It establishes Israel's "Responsible Innovation" approach: a voluntary, sector-based, risk-proportional framework rather than a horizontal law like the EU AI Act.

The policy contains 12 principles total, organized into two groups.

6 Regulatory Principles (governance-focused, how government should regulate):
1. Whole-of-government approach
2. Sector-based, risk-based regulation
3. International alignment (OECD principles)
4. Balanced and proportionate intervention
5. Soft-law tools first (voluntary standards, guidance, sandboxes)
6. Regular review and evolution

6 Ethical Principles (values-focused, how AI should be developed and used):
1. Human-centric AI and respect for fundamental rights
2. Non-discrimination and equality
3. Transparency and notice
4. Reliability and safety across the AI lifecycle
5. Responsibility and accountability of developers and operators
6. Promoting innovation for social welfare

For internal governance documentation, map each of your AI system's controls to the 6 ethical principles. This is the closest thing Israel has to a national AI framework, and enterprise customers in Israel are increasingly asking for alignment statements.

### Step 3: Privacy Protection Law (PPL) Applied to ML

The PPL predates LLMs but applies to any ML pipeline processing personal information. Amendment 13 (effective August 14, 2025) modernizes it significantly. Map each pipeline stage to its obligations:

| Pipeline stage | Core PPL obligations | Amendment 13 additions |
|----------------|---------------------|------------------------|
| Data collection | Lawful basis, consent or exemption, notice to data subjects | Expanded "personal information" definition, stricter consent standards |
| Storage | Database registration thresholds, Data Security Regulations 2017 technical and organizational measures | Data Security Officer role for large databases |
| Training | Purpose limitation, minimization | DPO role for orgs processing sensitive data at scale or doing systematic monitoring |
| Inference | Data subject rights (access, correction, deletion) even for inferred attributes | Broader data subject rights, incident reporting |
| Monitoring | Access logs, audit trails | Expanded breach notification obligations |
| Retention | Retention limits proportional to purpose | Clearer deletion obligations |

The PPA draft AI guidance (April 28, 2025) is the first sector-specific signal. Key positions:
- Legal basis is required at every lifecycle stage, including training
- Unauthorized scraping of personal data for AI training is expressly prohibited
- Data subject rights (access, correction, erasure) must be honored even when data is baked into model weights
- Orgs heavily reliant on AI should appoint a DPO even where not strictly mandated

Do NOT use web-scraped Hebrew social content or forum data for training without a documented legal basis. This is the fastest way to draw PPA enforcement attention post-August 2025.

### Step 4: Sector-Specific Rules

| Sector | Regulator | Relevant framework | What it actually requires |
|--------|-----------|-------------------|---------------------------|
| Banking, Fintech | Bank of Israel Supervisor of Banks | Proper Conduct of Banking Business Directive 364 (published 18/11/2024), consolidates former Directives 357, 361, 363 into "Management of IT, Information Security, and Cyber Protection Risks" | Technology-neutral governance, risk management, incident response for IT and cyber. Not AI-specific but applies to AI in banks. Model risk management lives in supervisory guidance |
| Health, Medtech | Ministry of Health Medical Devices Division (AMAR) | AMAR framework applies to AI as software-as-medical-device | Registration, clinical validation, post-market surveillance. Compare to FDA SaMD framework for engineering analogies but not legal substitution |
| Insurance | Capital Markets, Insurance and Savings Authority | Algorithmic decisions in underwriting and claims | Transparency, non-discrimination, appeals process |
| Transport (autonomous) | Ministry of Transport | Test permit framework for autonomous vehicles | Insurance, safety driver, incident reporting |
| Defense and dual-use | Ministry of Defense (DECA / DSDE) | Wassenaar Arrangement export controls (Israel is a participating state) | Export licensing for dual-use AI; applies to model weights and training data in some cases |

If your AI system operates in two or more of these sectors, the strictest regime generally prevails unless regulators have issued specific guidance on overlap.

### Step 5: EU AI Act Exposure for Israeli Companies

Regulation (EU) 2024/1689 entered into force on August 1, 2024 with staggered applicability through 2027. An Israeli company is caught by the Act when:

1. It places an AI system on the EU market (sells, licenses, or makes available to EU users)
2. It puts an AI system into service in the EU under its own name
3. The output of its AI system is used in the EU, even if the system is operated outside the EU

Key obligations by risk tier:

| Tier | Examples | Israeli exporter obligations |
|------|----------|------------------------------|
| Prohibited | Social scoring, real-time remote biometric ID in public for law enforcement, emotion recognition at work or school | Cannot place on EU market |
| High-risk (Annex III) | Biometrics, critical infrastructure, education, employment, essential services, law enforcement, migration, administration of justice | Conformity assessment, risk management system, data governance, technical documentation, logging, transparency, human oversight, accuracy/robustness/cybersecurity, quality management system, registration in EU database, authorized representative in EU |
| Limited-risk | Chatbots, deepfakes, emotion recognition | Transparency obligations (disclose AI use, label synthetic content) |
| Minimal-risk | Most other AI | Voluntary codes of conduct |
| GPAI | Foundation models | Technical documentation, information to downstream deployers, copyright policy, training data summary; systemic-risk models face additional obligations |

Staggered timeline:
- February 2, 2025: Prohibitions and AI literacy obligations apply
- August 2, 2025: GPAI obligations, governance, penalties apply
- August 2, 2026: Most obligations apply to new AI systems (including high-risk)
- August 2, 2027: Remaining obligations for products already regulated under sector-specific EU law

Non-EU providers of high-risk AI systems must appoint an EU authorized representative under Article 22. Budget for this as a legal-ops cost, not an engineering one.

### Step 6: Generate Documentation Artifacts

Four artifacts cover most enterprise and regulatory asks:

1. Model card: based on Mitchell et al. 2019 ("Model Cards for Model Reporting"). Add Israeli-context fields: PPL database registration status, Amendment 13 DPO designation, MoI 2023 principles alignment, sector regulator applicability. Use `scripts/generate_model_card.py` to render from a JSON input.

2. Data statement: based on Bender & Friedman 2018 ("Data Statements for NLP"). For Hebrew datasets, explicitly document speaker or author demographics, dialect and register coverage (modern standard, religious, academic, spoken), nikud presence, code-switching with English or Arabic, source platforms, scraping lawfulness, and PII scrubbing method.

3. DPIA (Data Protection Impact Assessment): aligned to PPL and Amendment 13. Full template in `references/dpia-template.md`. Required fields include purpose, lawful basis, data categories, retention, international transfers (including managed LLM vendors), risk analysis per affected group, mitigations, residual risk, review cadence, DPO sign-off.

4. AI risk assessment: internal governance artifact. Fields include stakeholders, impact categories (individuals, groups, society), mitigation owners, review cadence, escalation path, and incident playbook.

Use `scripts/classify_eu_ai_act_risk.py` to walk through Annex III and produce a risk classification plus next-step checklist.

### Step 7: Internal AI Governance Checklist

Self-assessment before any production deployment:

- [ ] Scoping memo completed (Step 1)
- [ ] Lawful basis documented for all training data sources
- [ ] No unauthorized scraping of personal data (per April 2025 PPA draft guidance)
- [ ] PPL database registration filed if thresholds met
- [ ] DPO designated if Amendment 13 triggers apply (sensitive data at scale, systematic monitoring, public authority, data broker)
- [ ] Model card published and linked from product documentation
- [ ] Data statement published for each training dataset
- [ ] DPIA completed and signed off
- [ ] Human oversight designated and trained
- [ ] Bias and fairness testing documented with results
- [ ] Incident response plan with breach notification workflow
- [ ] Access controls on training data (principle of least privilege)
- [ ] Model versioning with rollback capability
- [ ] Inference logging with retention policy
- [ ] Deletion-on-request workflow tested end to end
- [ ] Vendor due diligence for managed LLM providers (data residency, subprocessors, DPA in place)
- [ ] EU AI Act scoping: is system in scope? If yes, risk tier classified and obligations tracked
- [ ] MoI 2023 ethical principles mapped to controls

## Examples

### Example 1: Enterprise customer asks for AI risk review docs

User says: "A potential customer's security team wants a model card, data statement, and DPIA for our Hebrew summarization API before they sign."

Actions:
1. Run Step 1 scoping (GenAI, personal data in inputs, not sold in EU, no sector regulator)
2. Generate model card via `scripts/generate_model_card.py` with JSON input
3. Draft data statement referencing `references/ppl-for-ml-engineers.md` for Hebrew-specific fields
4. Draft DPIA using `references/dpia-template.md`
5. Map controls to MoI 2023 ethical principles

Result: Three documents ready for customer review, aligned to Israeli and international conventions.

### Example 2: Fintech credit-scoring model launching in Israel

User says: "We are building a credit-scoring model for a licensed Israeli bank. What BoI rules apply?"

Actions:
1. Confirm system type (predictive ML, personal data, no EU market, BoI sector)
2. Reference BoI Directive 364 (2024) for IT, cyber, and data governance obligations
3. Note that Directive 364 is not AI-specific; model risk management flows from broader supervisory guidance, so align with the bank's compliance team
4. Prepare model card with fairness testing across Israeli demographic groups
5. Document PPL lawful basis for training data and Amendment 13 DPO assignment

Result: Scoped compliance plan for the banking customer's internal review.

## Bundled Resources

### Scripts
- `scripts/generate_model_card.py` -- Takes a JSON input describing the model (name, owner, training data, intended use, limitations, metrics) and renders a markdown model card with Israeli-context fields. Run: `python scripts/generate_model_card.py --help`
- `scripts/classify_eu_ai_act_risk.py` -- Walks through Annex III categories via a question tree and outputs a risk classification (prohibited, high-risk, limited-risk, minimal-risk, GPAI) with reasoning and next-step checklist. Run: `python scripts/classify_eu_ai_act_risk.py --help`

### References
- `references/moi-2023-principles.md` -- Full breakdown of the 12 MoI principles (6 regulatory + 6 ethical) with concrete implementation examples per principle. Consult when writing alignment statements for internal governance or customer reviews.
- `references/ppl-for-ml-engineers.md` -- Practical mapping of PPL sections to ML pipeline stages. Consult when documenting lawful basis for each stage.
- `references/eu-ai-act-israel-guide.md` -- When Israeli companies fall under EU AI Act, what GPAI obligations mean, conformity assessment path, timeline. Consult when scoping EU exposure.
- `references/dpia-template.md` -- Full DPIA template aligned to PPL and Amendment 13 with all required fields. Consult when producing DPIA artifacts.

## Recommended MCP Servers

| MCP | Use for |
|-----|---------|
| `israel-law` | Full-text search of 66 Israeli statutes including Privacy Protection Law and Data Security Regulations in Hebrew and English. Use to look up specific PPL sections and Data Security Regulations clauses when drafting compliance memos. |

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Ministry of Innovation 2023 AI Policy (PDF) | https://www.gov.il/BlobFolder/policy/ai_2023/en/Israels%20AI%20Policy%202023.pdf | 12 principles, voluntary framework, sector approach |
| Bank of Israel Proper Conduct Directives | https://www.boi.org.il/en/economic-roles/supervision-and-regulation/proper_conduct/ | Directive 364 (2024) IT and cyber, other sector directives |
| EU AI Act Regulation 2024/1689 | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | Full text, Annex III high-risk list, GPAI obligations, timeline |
| IAPP analysis of PPL Amendment 13 | https://iapp.org/news/a/israel-marks-a-new-era-in-privacy-law-amendment-13-ushers-in-sweeping-reform | Amendment 13 scope, DPO rules, enforcement, August 14 2025 effective date |
| PPA AI draft guidance analysis | https://www.pearlcohen.com/israel-new-draft-guidelines-on-the-application-of-privacy-law-to-ai/ | April 2025 PPA guidance positions on training data and scraping |
| US Trade.gov analysis of Israel AI policy | https://www.trade.gov/market-intelligence/israel-ict-policy-artificial-intelligence-regulation-and-ethics | Independent summary of Israel's AI policy framework |

## Gotchas

- Israel does NOT have a horizontal AI law as of April 2026. The framework is voluntary (MoI December 2023 policy) plus sector-based regulation. AI agents frequently hallucinate an "Israeli AI Act". There is no such statute. Do not cite one in compliance documents.
- Bank of Israel Directives 357, 361, and 363 were consolidated into Directive 364 in November 2024. Older sources still cite the retired directive numbers. Always cite Directive 364 for IT, information security, and cyber protection going forward, not the retired numbers.
- Directive 364 is a CYBER and IT governance directive, not an AI governance directive. Agents often cite it as "BoI's AI rule". It is not. For AI-specific model governance in banks, look to ongoing supervisory guidance and model risk management expectations, not Directive 364.
- PPL database registration is NOT the same as GDPR records of processing. They have different triggers and different registration authorities (Israeli Registrar of Databases vs EU-level Article 30 records). Agents conflate them routinely.
- The EU AI Act's extraterritorial reach catches Israeli companies only when they actually place systems on the EU market or their output is used in the EU. A purely Israeli deployment with Israeli users is outside scope, even if the model was trained on EU data. Do not over-scope Israeli-only products.
- The authoritative Ministry of Innovation document is in Hebrew. English translations paraphrase. For compliance claims, cross-reference the Hebrew text.

## Troubleshooting

### Error: "Customer's AI risk review demands an 'Israeli AI Act compliance statement'"
Cause: The customer's security team has a generic template that assumes every country has a horizontal AI law like the EU.
Solution: Reply with a statement that references (a) MoI December 2023 voluntary principles, (b) PPL and Amendment 13 obligations, (c) applicable sector regulator, (d) EU AI Act status if relevant. Attach model card, data statement, and DPIA as the concrete artifacts.

### Error: "Legal says we need to register our ML training dataset under PPL"
Cause: Database registration thresholds are being reviewed.
Solution: Check the Registrar of Databases thresholds for the specific data categories and number of data subjects. Consult `references/ppl-for-ml-engineers.md` for stage-by-stage mapping. If thresholds are met, file before going to production. Amendment 13 tightens some thresholds and expands DPO requirements.

### Error: "Bank customer wants us to comply with BoI Directive 361"
Cause: Directive 361 was retired and consolidated into Directive 364 in November 2024.
Solution: Reply that Directive 361 has been superseded by Directive 364 "Management of IT, Information Security, and Cyber Protection Risks", published 18/11/2024. Map controls to Directive 364 clauses instead and share with the customer.
