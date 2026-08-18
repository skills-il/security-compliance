# Ministry of Innovation 2023 AI Policy: 12 Principles

Source: "Policy, Regulation and Ethics Principles in the Field of Artificial Intelligence", Ministry of Innovation, Science and Technology and Ministry of Justice, published December 14, 2023.

The policy sets Israel's "Responsible Innovation" framework: voluntary, sector-based, risk-proportional. It is not a statute. It guides how government should regulate AI and how developers and operators should build and deploy it.

## 6 Regulatory Principles

These apply to government and regulators, not to private developers directly. Include them in compliance docs to show alignment with national policy direction.

### 1. Whole-of-government approach
The government treats AI holistically rather than fragmenting rules across ministries. Implication for you: expect coordinated guidance across regulators over time. Track Ministry of Innovation, Ministry of Justice, PPA, Bank of Israel, and MoH communications together.

### 2. Sector-based, risk-based regulation
Regulation is proportional to actual risk in the specific domain. Implication: do not assume "one AI rule fits all". A low-risk chatbot and a medical-diagnosis AI sit under different regimes even inside Israel.

### 3. International alignment (OECD)
Israel aligns with OECD AI principles and monitors EU, US, UK developments. Implication: policies you adopt from OECD or the EU AI Act will generally be accepted by Israeli regulators.

### 4. Balanced and proportionate intervention
Intervention is calibrated to avoid chilling innovation. Implication: regulators favor guidance, sandboxes, and voluntary compliance before new statutes.

### 5. Soft-law tools first
Voluntary standards, guidance notes, and regulatory sandboxes precede binding law. Implication: compliance posture should anticipate soft-law requirements becoming mandatory over time.

### 6. Regular review and evolution
The policy explicitly commits to revisiting itself. Implication: expect updates. Subscribe to Ministry of Innovation and PPA publications.

## 6 Ethical Principles

These apply directly to developers and operators. Map each principle to concrete controls in your AI system.

### 1. Human-centric AI and respect for fundamental rights
Concrete controls:
- Human oversight role defined with authority to override model outputs
- Fundamental rights impact assessment (similar to a fundamental rights DPIA)
- Appeal mechanism for affected individuals
- No system design that undermines dignity, autonomy, or free choice

### 2. Non-discrimination and equality
Concrete controls:
- Bias testing on protected categories (gender, ethnicity, religion, age, disability)
- Fairness metric documented per use case (demographic parity, equalized odds, or domain-specific)
- Mitigation plan for identified bias
- Periodic re-testing on live data

### 3. Transparency and notice
Concrete controls:
- Users notified they are interacting with AI
- Synthetic content labeled
- Model card published with capabilities and limits
- Explanation of automated decisions where legally required or ethically warranted

### 4. Reliability and safety across the AI lifecycle
Concrete controls:
- Test coverage across expected inputs and adversarial edges
- Red-teaming for GenAI systems
- Performance monitoring in production with drift detection
- Safe fallback behavior when confidence is low

### 5. Responsibility and accountability
Concrete controls:
- Clear owner for each AI system (named role, not just team)
- Incident response plan with escalation path
- Audit trail of training data, model versions, deployments
- Vendor accountability clauses for third-party models

### 6. Promoting innovation for social welfare
Concrete controls:
- Positive impact hypothesis documented per system
- Stakeholder engagement where the system affects vulnerable groups
- Participation in voluntary standards and sandboxes where available
- Sharing safety learnings where competitively possible

## How to Use This in Documentation

For each AI system, create a short alignment statement mapping the 6 ethical principles to specific controls. Attach it to your internal governance file and include it in customer-facing AI risk review responses. Reference the policy by its full title and December 14, 2023 publication date.

## What's Next (2026 and beyond)

The Ministry of Innovation is formalising an AI Policy Coordination Center expected to release a Risk Management Toolbox for sector regulators, containing standardised impact-assessment templates and transparency-report patterns. Track its publications alongside those of the PPA, Bank of Israel, and Ministry of Health.

A new multi-year national AI strategy is anticipated after 2026 and is likely to emphasise generative AI, LLM security, and environmental impact (Green AI). A National AI Ethics Committee has also been floated in public consultations. None of this changes the voluntary, sector-based baseline established in 2023, but it does mean more operational guidance is coming.
