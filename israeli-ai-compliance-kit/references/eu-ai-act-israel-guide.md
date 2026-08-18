# EU AI Act for Israeli Companies

When and how Regulation (EU) 2024/1689 ("EU AI Act") reaches Israeli AI providers and deployers. Not legal advice.

## Baseline Facts

- Legal instrument: Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence
- Entry into force: August 1, 2024
- Risk-based structure: Prohibited, High-risk (Annex III), Limited-risk, Minimal-risk, plus General-Purpose AI (GPAI) obligations
- Enforcement: Member-state authorities plus the European AI Office for GPAI

## When Israeli Companies Are in Scope

Article 2 defines scope. You are caught if any of these apply:

1. You place an AI system on the EU market as a provider (sell, license, or make available in the EU under your name or brand)
2. You put an AI system into service in the EU under your name or brand
3. The output of your AI system is used in the EU, even if you operate the system from Israel

A pure Israeli-only deployment with only Israeli users does not trigger the Act, even if the underlying model was trained on European data.

## Risk Tiers in Practice

### Prohibited (Article 5)
Examples: social scoring by public authorities, real-time remote biometric identification in publicly accessible spaces for law enforcement (with narrow exceptions), exploiting vulnerabilities of specific groups, emotion recognition in workplace or education contexts. Cannot be placed on the EU market.

### High-Risk (Annex III)
Eight categories:
1. Biometrics
2. Critical infrastructure
3. Education and vocational training
4. Employment, worker management, access to self-employment
5. Access to essential private and public services
6. Law enforcement
7. Migration, asylum, border control
8. Administration of justice and democratic processes

Provider obligations include:
- Risk management system across the lifecycle
- Data governance for training, validation, test data
- Technical documentation
- Logging
- Transparency and information to deployers
- Human oversight
- Accuracy, robustness, cybersecurity
- Quality management system
- Conformity assessment (Annex VI self-assessment or Annex VII notified body, depending on system)
- Registration in the EU database
- CE marking
- Post-market monitoring
- Incident reporting to the relevant authority

Non-EU providers of high-risk systems must appoint an authorized representative established in the EU (Article 22).

### Limited-Risk
Chatbots and synthetic content require transparency disclosures. Users must know they are interacting with AI. Synthetic content must be machine-readable as such.

### Minimal-Risk
Most AI. Voluntary codes of conduct. No mandatory obligations.

### GPAI (General-Purpose AI models)
Obligations on model providers:
- Technical documentation for downstream developers
- Information summary of copyrighted training data
- Copyright policy for text and data mining opt-outs
- Compliance with Union copyright law

GPAI models with systemic risk (above a compute threshold, currently 10^25 FLOPs for training) face additional obligations including model evaluations, adversarial testing, cybersecurity, and serious incident reporting.

## Staggered Timeline

| Date | Status | What applies |
|------|--------|-------------|
| August 1, 2024 | In force | Act enters into force |
| February 2, 2025 | In force | Prohibitions (Article 5) and AI literacy obligations (Article 4) apply |
| August 2, 2025 | In force | GPAI obligations, governance structures, penalties apply. New GPAI models placed on the EU market after this date must comply immediately; providers of pre-existing GPAI models have until August 2, 2027 to comply |
| December 2, 2026 | Upcoming | Article 50(2) synthetic-content transparency obligations apply. Providers of AI systems generating synthetic audio, image, video, or text must mark outputs as artificially generated in a machine-readable format |
| December 2, 2027 | Upcoming (revised, previously August 2, 2026) | Annex III high-risk requirements (Articles 6 to 15) apply to stand-alone high-risk AI systems |
| August 2, 2028 | Upcoming (revised) | High-risk requirements apply to AI systems embedded in products already covered by sector-specific EU legislation (Annex I) |

**Timeline change (Digital Omnibus on AI, May 7, 2026):** the Council and Parliament reached a provisional political agreement to postpone the Annex III high-risk deadline from August 2, 2026 to December 2, 2027, and the Annex I product-embedded deadline to August 2, 2028. The Article 50(2) synthetic-content transparency grace period was compressed so it now takes effect December 2, 2026. GPAI obligations (in force since August 2, 2025) were NOT postponed. The agreement is provisional and pending formal adoption of the amending regulation, so treat these dates as not yet final.

## General-Purpose AI Code of Practice

On July 10, 2025 the European AI Office published the final version of the voluntary Code of Practice for GPAI providers. The Code was endorsed by the European Commission and the AI Board on August 1, 2025 via adequacy decisions. It has three chapters: Transparency, Copyright, and Safety and Security. Signing is voluntary but is the Commission's preferred route for demonstrating compliance with GPAI obligations. For Israeli GPAI providers selling into the EU, signing the Code is usually less work than building a bespoke compliance dossier.

## Decision Framework for Israeli Companies

Run through these questions in order:

1. **Is my system prohibited?** If yes, stop. Do not place on EU market.
2. **Am I a provider placing on the EU market, or will my output be used in the EU?** If no to both, you are outside scope.
3. **Is my system in Annex III (high-risk)?** If yes, plan for full high-risk obligations and EU authorized representative.
4. **Is my system limited-risk (chatbot, deepfake, emotion recognition outside work/school)?** If yes, transparency obligations apply.
5. **Is my model a GPAI?** If it is a foundation model offered for downstream use, GPAI obligations apply. Check compute threshold for systemic-risk tier.
6. **If minimal-risk:** consider voluntary codes of conduct for signaling trust to EU customers.

## Practical Notes for Israeli Teams

- Budget for EU authorized representative early if you expect to ship high-risk systems. This is typically a legal services contract, not an engineering task.
- Conformity assessment for high-risk is the largest cost. Allocate time.
- GPAI training data summaries will be a significant documentation effort. Start tracking training data provenance now.
- Copyright opt-outs: honor machine-readable opt-outs in training data scraping from EU sources.
- The EU AI Act does not preempt Israeli law. You may need to satisfy both regimes simultaneously.

## Gaps and Open Questions

- Harmonized standards for high-risk systems are still being drafted by CEN/CENELEC. Until finalized, use the Act's core requirements as a floor.
- Interaction with GDPR is active and evolving. DPIA under GDPR and risk management under AI Act are related but distinct.
- The European AI Office's guidance on GPAI is still maturing. Track it as it is published.
