---
name: israeli-ai-compliance-kit
description: "Guide Israeli ML teams through the AI governance and compliance stack: Ministry of Innovation December 2023 AI policy principles, Privacy Protection Law (PPL) and Amendment 13 applied to ML training data, sector-specific rules (Bank of Israel Directive 364, Ministry of Health AMAR medical-device AI), and EU AI Act exposure for Israeli exporters. Generates model cards, data statements, and DPIA templates tailored to Israeli context. Use when preparing AI governance docs, answering an enterprise customer's AI risk review, classifying a system under the EU AI Act, or building an internal responsible-AI checklist. Prevents costly compliance gaps when shipping AI to regulated markets. Do NOT use for general PPL policy (use israeli-privacy-shield), web app security (use israeli-appsec-scanner), or SOC/threat triage (use israeli-cybersecurity-ops)."
license: MIT
---

# Israeli AI Compliance Kit

## Problem

Israeli ML teams shipping AI products face a fragmented compliance landscape: voluntary principles from the Ministry of Innovation, the Privacy Protection Law with Amendment 13 in force since August 14, 2025, sector regulators each drafting their own AI guidance, and the EU AI Act rolling out in staggered phases through 2027 that reach anyone selling into Europe. Most teams discover these requirements mid-procurement when an enterprise customer demands a model card, data statement, and DPIA. There is no unified checklist or template set tailored to the Israeli regulatory context.

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

The Ministry of Innovation is formalising an AI Policy Coordination Center that is expected to release a Risk Management Toolbox for sector regulators (standardised impact-assessment templates and transparency-report patterns). Track its publications alongside PPA, Bank of Israel, and MoH circulars.

Two newer reference points to fold into governance docs:
- The Innovation Authority published the National Program for Artificial Intelligence overview in May 2025, integrating activities across the Ministry of Innovation, Finance, Defense (DDR&D), Council for Higher Education, the National Digital Agency, and the Ministries of Foreign Affairs and Justice.
- In January 2026 the US State Department and Israel announced a Strategic Partnership on AI, Research, and Critical Technologies, which gives Israeli AI exporters a more concrete signal to align with NIST AI RMF in dual-track US/EU compliance stories.

A new multi-year national AI strategy is anticipated after 2026, likely emphasising generative AI, LLM security, and environmental impact.

### Step 3: Privacy Protection Law (PPL) Applied to ML

The PPL predates LLMs but applies to any ML pipeline processing personal information. Amendment 13 came into force on August 14, 2025 and modernises it significantly. The PPA granted a temporary grace period on the new DPO obligation until October 31, 2025 to let organisations prepare; that grace period has expired, so DPO appointment where triggers apply is now fully enforceable. Map each pipeline stage to its obligations:

| Pipeline stage | Core PPL obligations | Amendment 13 additions |
|----------------|---------------------|------------------------|
| Data collection | Lawful basis, consent or exemption, notice to data subjects | Expanded "personal information" definition, stricter consent standards |
| Storage | Database registration thresholds, Data Security Regulations 2017 technical and organizational measures | Data Security Officer role for large databases |
| Training | Purpose limitation, minimization | DPO role for orgs processing sensitive data at scale or doing systematic monitoring |
| Inference | Data subject rights (access, correction, deletion) even for inferred attributes | Broader data subject rights, incident reporting |
| Monitoring | Access logs, audit trails | Expanded breach notification obligations |
| Retention | Retention limits proportional to purpose | Clearer deletion obligations |

The PPA draft AI guidance, published April 30, 2025 with public consultation closing June 5, 2025, is the first sector-specific signal. As of May 2026 it remains formally in draft and has not been finalised into a binding directive, but PPA officials have stated they will enforce it as if it were statutory. Treat it as the PPA's operative compliance standard and align with it as if binding. Key positions:
- Legal basis is required at every lifecycle stage, including training
- Unauthorized scraping of personal data for AI training is expressly prohibited
- Data subject rights (access, correction, erasure) must be honored even when data is baked into model weights
- Orgs heavily reliant on AI should appoint a DPO under Amendment 13, whom the PPA treats as the most suitable figure to handle AI-related privacy questions
- Generative-AI usage policy: organisations should adopt an internal policy covering which tools are permitted, who may use them, what data may be uploaded, and retention limits on prompts

In February 2026 the PPA went further and published a final opinion on consent under Israeli privacy law, which the PPA treats as binding. The opinion explicitly addresses AI: scraping personal data from the internet to train AI models without informed consent is described as unlawful privacy infringement, and the PPA states that publishing data on social media does not constitute informed consent for AI training. Even with the AI guidance still formally in draft, the consent opinion now closes the "but the AI rules are just draft" defence on the scraping question.

Do NOT use web-scraped Hebrew social content or forum data for training without a documented legal basis. This is the fastest way to draw PPA enforcement attention under Amendment 13, the draft AI guidance, and the February 2026 consent opinion.

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
- February 2, 2025 (now in force): Prohibitions (Article 5) and AI literacy obligations (Article 4) apply
- August 2, 2025 (now in force): GPAI obligations, governance structures, and penalties apply. New GPAI models placed on the EU market after this date must comply immediately; providers of GPAI models already on the market before August 2, 2025 have until August 2, 2027 to bring their models and documentation into compliance
- December 2, 2026 (upcoming): Article 50(2) synthetic-content transparency obligations apply. Providers of AI systems generating synthetic audio, image, video, or text must mark outputs as artificially generated in a machine-readable format
- December 2, 2027 (revised, previously August 2, 2026): Annex III high-risk requirements under Articles 6-15 apply to stand-alone high-risk AI systems
- August 2, 2028 (revised): High-risk requirements apply to AI systems embedded in products already regulated under sector-specific EU law (Annex I)

Note: the "Digital Omnibus on AI" agreement of May 7, 2026 (Council + Parliament provisional political agreement, pending formal adoption) postponed the Annex III high-risk deadline from August 2, 2026 to December 2, 2027, and the Annex I product-embedded deadline to August 2, 2028. It also compressed the Article 50(2) transparency grace period so it now takes effect December 2, 2026. GPAI obligations (in force since August 2, 2025) were NOT postponed. Formal adoption by Parliament and Council is expected in June or July 2026, ahead of the original August 2, 2026 deadline; if formal adoption slips past August 2, 2026 the unamended timeline reactivates. Treat these dates as provisional and confirm against the EU Official Journal before relying on them in customer commitments.

The European AI Office published the final General-Purpose AI Code of Practice on July 10, 2025, endorsed by the Commission and the AI Board on August 1, 2025. The Code is voluntary but is the Commission's preferred route for demonstrating compliance with GPAI obligations. It has three chapters: Transparency, Copyright, and Safety and Security. Israeli GPAI providers selling into the EU should consider signing onto the Code rather than building a bespoke compliance story.

Non-EU providers of high-risk AI systems must appoint an EU authorized representative under Article 22. Budget for this as a legal-ops cost, not an engineering one.

### Step 5.5: Voluntary International Frameworks Worth Aligning With

Because Israel's MoI 2023 policy favours soft-law and OECD alignment, voluntary international frameworks accepted by Israeli regulators double as useful scaffolding for enterprise AI risk reviews:

| Framework | What it is | Why Israeli teams should care |
|-----------|-----------|-------------------------------|
| ISO/IEC 42001:2023 | First certifiable AI management system standard (AIMS). Published December 2023. Plan-do-check-act structure with 38 controls covering risk management, impact assessment, lifecycle management, third-party oversight. | Certification is increasingly asked for in enterprise procurement. Controls map cleanly to EU AI Act high-risk obligations and PPA guidance. Treat as the AI-specific counterpart to ISO/IEC 27001. |
| NIST AI RMF 1.0 | US National Institute of Standards and Technology framework (January 2023) organised around Govern, Map, Measure, Manage. Augmented by the Generative AI Profile (NIST-AI-600-1, July 2024) and the Cyber AI Profile (preliminary draft NIST IR 8596 published December 16, 2025; comment period closed January 30, 2026; final expected later in 2026). RMF 1.1 addenda and an AI in Critical Infrastructure profile (concept note April 7, 2026) are also in flight. | OECD-aligned and widely accepted by US enterprise customers, and now reinforced by the January 2026 US-Israel Strategic Partnership on AI. The risk taxonomy fits alongside MoI 2023 ethical principles in compliance docs. |
| OECD AI Principles | OECD Recommendation of the Council on AI, adopted 2019, updated 2024. | Explicitly referenced by Israel's MoI 2023 policy as a baseline. Alignment is essentially free in your governance docs. |
| EU GPAI Code of Practice | Voluntary compliance route for EU AI Act GPAI obligations (July 2025, Commission-endorsed August 2025). | If you ship a foundation model into the EU, this is the lowest-friction compliance pathway. |

Pick one or two as the backbone of your documentation and cross-reference the rest. You rarely need all four at once.

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
- [ ] No unauthorized scraping of personal data (per the April 2025 PPA AI guidance, which the PPA enforces as its operative standard, plus the February 2026 PPA final consent opinion which is binding)
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
- [ ] EU AI Act scoping: is system in scope? If yes, risk tier classified and obligations tracked. For GPAI, consider signing the EU GPAI Code of Practice
- [ ] MoI 2023 ethical principles mapped to controls
- [ ] Voluntary framework alignment (ISO/IEC 42001, NIST AI RMF, or OECD AI Principles) stated in governance docs
- [ ] Internal generative-AI usage policy documented (permitted tools, allowed data, retention limits on prompts)

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
| EU General-Purpose AI Code of Practice | https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai | Voluntary compliance route for GPAI obligations (July 2025 final, Commission-endorsed August 2025) |
| EU Council statement on the Digital Omnibus on AI | https://www.consilium.europa.eu/en/press/press-releases/2026/05/07/artificial-intelligence-council-and-parliament-agree-to-simplify-and-streamline-rules/ | May 7, 2026 provisional agreement postponing Annex III high-risk obligations to December 2, 2027 |
| ISO/IEC 42001:2023 AI management system | https://www.iso.org/standard/42001 | Certifiable AIMS standard, 38 controls, plan-do-check-act |
| NIST AI Risk Management Framework | https://www.nist.gov/itl/ai-risk-management-framework | AI RMF 1.0 plus Generative AI Profile (NIST-AI-600-1, July 2024) |
| NIST IR 8596 Cyber AI Profile (preliminary draft) | https://csrc.nist.gov/pubs/ir/8596/iprd | Draft published December 16, 2025; comments closed January 30, 2026; final expected later in 2026 |
| PPA February 2026 consent opinion (analysis) | https://www.lexology.com/library/detail.aspx?g=e303b2da-16c8-4842-b742-36c5f8a99d23 | Final binding opinion; scraping personal data for AI training without informed consent is unlawful |
| Israel National Program for AI (2025) | https://innovationisrael.org.il/wp-content/uploads/2025/05/AI-National-Program-en-14.5.25.pdf | Multi-ministry program overview, May 2025 |
| US-Israel Strategic Partnership on AI (January 2026) | https://www.state.gov/releases/office-of-the-spokesperson/2026/01/joint-statement-of-the-united-states-and-israel-on-the-launch-of-a-strategic-partnership-on-artificial-intelligence-research-and-critical-technologies | Bilateral signal reinforcing NIST AI RMF alignment for Israeli exporters |

## Gotchas

- Israel does NOT have a horizontal AI law as of May 2026. The framework is voluntary (MoI December 2023 policy) plus sector-based regulation. AI agents frequently hallucinate an "Israeli AI Act". There is no such statute. Do not cite one in compliance documents.
- Bank of Israel Directives 357, 361, and 363 were consolidated into Directive 364 in November 2024. Older sources still cite the retired directive numbers. Always cite Directive 364 for IT, information security, and cyber protection going forward, not the retired numbers.
- Directive 364 is a CYBER and IT governance directive, not an AI governance directive. Agents often cite it as "BoI's AI rule". It is not. For AI-specific model governance in banks, look to ongoing supervisory guidance and model risk management expectations, not Directive 364.
- PPL database registration is NOT the same as GDPR records of processing. They have different triggers and different registration authorities (Israeli Registrar of Databases vs EU-level Article 30 records). Agents conflate them routinely.
- The EU AI Act's extraterritorial reach catches Israeli companies only when they actually place systems on the EU market or their output is used in the EU. A purely Israeli deployment with Israeli users is outside scope, even if the model was trained on EU data. Do not over-scope Israeli-only products.
- The authoritative Ministry of Innovation document is in Hebrew. English translations paraphrase. For compliance claims, cross-reference the Hebrew text.
- The PPA's April 2025 AI guidance is still formally in DRAFT as of May 2026. Public consultation closed June 5, 2025 and no final binding directive has been published, but PPA officials have said they will enforce it as if it were statutory. Treat it as the PPA's operative compliance standard and align with it as if binding. When phrasing it for a customer, you can note the formal draft status, but do not treat that as a reason to ignore it. Watch gov.il/privacy for finalisation.
- The PPA's February 2026 final opinion on consent IS binding (no draft caveat). It directly states that scraping personal data to train AI without informed consent is unlawful, and that social-media publication is not consent for AI training. Older docs that hedge the scraping rule as "draft only" are stale; the consent opinion now backs the scraping rule on a final, separately-published footing.
- The EU General-Purpose AI Code of Practice (July 2025) is voluntary but endorsed by the Commission. Signing it is the lowest-friction GPAI compliance route. Do not conflate it with mandatory obligations: the Code supports compliance with the Act, it does not replace it.
- Amendment 13 is now in force (since August 14, 2025). The PPA's earlier grace period on DPO appointment expired October 31, 2025. Older internal memos saying "Amendment 13 is coming" are stale. Update them.
- The EU AI Act high-risk timeline moved. The "Digital Omnibus on AI" agreement of May 7, 2026 postponed Annex III high-risk obligations from August 2, 2026 to December 2, 2027 (and Annex I product-embedded systems to August 2, 2028), while compressing Article 50(2) synthetic-content transparency to December 2, 2026. GPAI obligations were NOT postponed. The agreement is a provisional political agreement pending formal adoption, so phrase these dates as provisional. Older docs citing "August 2, 2026 for high-risk" are stale.

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
