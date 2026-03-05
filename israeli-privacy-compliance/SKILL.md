---
name: israeli-privacy-compliance
description: >-
  Israeli privacy law implementation code patterns for the Protection of Privacy
  Law (Chok Haganat HaPratiyut, 1981). Provides consent management code,
  DSAR workflow implementation, PPA database registration API integration,
  cross-border data transfer patterns, and GDPR dual-compliance bridging code.
  Use when user asks to implement privacy compliance in code, build consent
  forms, handle "bakashat noshe meida" (data subject requests), integrate with
  "rasham maagarei meida" (database registry), or write GDPR-compatible Israeli
  privacy code. Do NOT use for regulatory overview (use israeli-privacy-shield
  instead).
license: MIT
compatibility: 'No network required. Works with Claude Code, Claude.ai, Cursor.'
metadata:
  author: skills-il
  version: 1.0.0
  category: security-compliance
  tags:
    he:
      - פרטיות
      - הגנת-מידע
      - רשם-מאגרי-מידע
      - GDPR
      - קוד
      - ישראל
    en:
      - privacy
      - data-protection
      - ppa-registry
      - gdpr
      - code
      - israel
  display_name:
    he: ציות פרטיות ישראלי
    en: Israeli Privacy Compliance
  display_description:
    he: >-
      דפוסי קוד ליישום חוק הגנת הפרטיות — טפסי הסכמה, בקשות נושא מידע,
      רישום מאגרי מידע, העברות חוצות גבולות, וגישור GDPR
    en: >-
      Israeli privacy law implementation code patterns for the Protection of
      Privacy Law (Chok Haganat HaPratiyut, 1981). Provides consent management
      code, DSAR workflow implementation, PPA database registration API
      integration, cross-border data transfer patterns, and GDPR dual-compliance
      bridging code. Use when user asks to implement privacy compliance in code,
      build consent forms, handle data subject requests, integrate with database
      registry, or write GDPR-compatible Israeli privacy code. Do NOT use for
      regulatory overview (use israeli-privacy-shield instead).
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
    - antigravity
---

# Israeli Privacy Compliance

## Critical Note
This skill provides **implementation code patterns** for Israeli privacy compliance.
It does not replace legal counsel. For regulatory overview and checklists,
use the `israeli-privacy-shield` skill instead.

## Instructions

### Step 1: Consent Management Implementation
Implement consent collection per Protection of Privacy Law requirements.

**Consent form must include:**
- Purpose of data collection (matarat haishuf)
- Types of data collected
- Third-party sharing disclosure
- Cross-border transfer disclosure (if applicable)
- Withdrawal mechanism

**Code pattern — consent record schema:**
```python
consent_record = {
    "subject_id": "hashed_user_id",
    "consent_type": "marketing|essential|analytics",
    "purpose_he": "תיאור מטרת איסוף המידע",
    "purpose_en": "Description of data collection purpose",
    "granted_at": "ISO-8601 timestamp",
    "ip_address": "collected at grant time",
    "withdrawal_at": None,
    "version": "consent_policy_version",
    "legal_basis": "consent|contract|legal_obligation|vital_interest"
}
```

**Cookie consent banner requirements:**
- Must appear before non-essential cookies are set
- Hebrew text required for Israeli users
- Separate toggles for: essential, analytics, marketing
- "Reject all" must be as prominent as "Accept all"

### Step 2: Data Subject Access Request (DSAR) Workflow
Implement handling for "bakashat noshe meida" — data subject requests.

**Required DSAR types under Israeli law:**
1. Access (zchut iyun) — right to view stored data
2. Correction (zchut tikun) — right to fix inaccurate data
3. Deletion — limited right, narrower than GDPR
4. Objection to direct marketing (zchut hista'agut)

**DSAR workflow implementation:**
```
1. Receive request -> verify identity (teuda mezahe / biometric)
2. Log request with timestamp (max response: 30 days)
3. Search all data stores for subject's data
4. Compile response in readable format (Hebrew if requested)
5. Deliver securely to verified identity
6. Log completion and retain audit trail
```

**Code pattern — DSAR handler:**
```python
class DSARHandler:
    VALID_TYPES = ["access", "correction", "deletion", "marketing_objection"]
    MAX_RESPONSE_DAYS = 30

    def process_request(self, request):
        self.verify_identity(request.subject_id, request.id_document)
        self.log_request(request)
        data = self.collect_subject_data(request.subject_id)
        response = self.format_response(data, request.language)
        self.deliver_securely(response, request.delivery_method)
        self.log_completion(request.id)
```

### Step 3: PPA Database Registration Integration
Integrate with Privacy Protection Authority (Rashut LeHaganat HaPratiut) database registry.

**Registration check logic:**
```python
def requires_registration(db_info):
    if db_info["is_public_body"]:
        return True
    if db_info["is_credit_service"]:
        return True
    if db_info["record_count"] >= 10000:
        if db_info["has_sensitive_data"] or db_info["used_for_marketing"]:
            return True
    return False
```

**Registration data model:**
```python
registration_payload = {
    "database_name": "string",
    "owner_entity": "string",  # Israeli business number (CH/PN)
    "purpose": "string",       # matarat ha-maagar
    "data_types": ["personal", "sensitive", "financial"],
    "data_sources": ["direct_collection", "third_party"],
    "recipients": ["internal", "service_providers"],
    "security_level": "basic|medium|high",
    "cross_border": False,
    "retention_period_months": 36
}
```

**PPA portal URL:** `https://www.gov.il/he/departments/privacy_authority`

### Step 4: Cross-Border Data Transfer Patterns
Implement data transfer safeguards for moving data outside Israel.

**Transfer decision tree:**
```
Is destination in EU/EEA?
  YES -> Transfer permitted (Israel has EU adequacy decision)
Is destination recognized as adequate by PPA?
  YES -> Transfer permitted
Has data subject given informed consent for this specific transfer?
  YES -> Transfer permitted with documented consent
Are contractual safeguards in place (similar to SCCs)?
  YES -> Transfer permitted with safeguard documentation
Is transfer necessary for contract performance?
  YES -> Transfer permitted with justification documentation
ELSE -> Transfer NOT permitted
```

**Code pattern — transfer validator:**
```python
ADEQUATE_COUNTRIES = ["EU", "EEA", "UK", "CH", "NZ", "UY", "JP", "KR", "CA", "AR", "IL"]

def validate_transfer(destination_country, transfer_basis, documentation):
    if destination_country in ADEQUATE_COUNTRIES:
        return {"allowed": True, "basis": "adequacy"}
    if transfer_basis == "explicit_consent" and documentation.get("consent_record"):
        return {"allowed": True, "basis": "consent"}
    if transfer_basis == "contractual_safeguards" and documentation.get("scc_signed"):
        return {"allowed": True, "basis": "contractual"}
    if transfer_basis == "contract_necessity" and documentation.get("justification"):
        return {"allowed": True, "basis": "contract_necessity"}
    return {"allowed": False, "reason": "No valid transfer basis"}
```

### Step 5: GDPR Dual-Compliance Bridging
For Israeli companies with EU customers, implement code that satisfies both frameworks.

**Key bridging rules:**
| Aspect | Israeli Law | GDPR | Dual-Compliance Approach |
|--------|------------|------|--------------------------|
| Legal basis | Consent primary | 6 bases | Implement all 6 GDPR bases, default to consent |
| Breach notification | "Without delay" | 72 hours | Use 72-hour deadline (stricter) |
| Right to erasure | Limited | Comprehensive | Implement full GDPR erasure |
| DPO requirement | High-level DBs only | Broader | Appoint DPO if either requires it |
| Registration | Required | ROPA instead | Do both: register + maintain ROPA |

**Code pattern — dual-compliance consent:**
```python
def create_dual_consent(user_region, purpose, data_types):
    consent = {
        "israeli_requirements": {
            "informed": True,
            "specific_purpose": purpose,
            "freely_given": True,
            "documented": True,
        },
        "gdpr_requirements": {
            "legal_basis": "consent",  # Article 6(1)(a)
            "purpose_limitation": purpose,
            "data_minimization": data_types,
            "storage_limitation_days": 365,
            "right_to_withdraw": True,
        },
        "applies_israeli_law": True,
        "applies_gdpr": user_region in ["EU", "EEA", "UK"],
    }
    return consent
```

### Step 6: Privacy-by-Design Code Patterns
Apply privacy-by-design principles to Israeli application code.

**Data minimization pattern:**
```python
# Collect only what you need per declared purpose
FIELD_ALLOWLIST = {
    "registration": ["name", "email", "phone"],
    "purchase": ["name", "email", "shipping_address", "payment_token"],
    "marketing": ["email", "consent_marketing"],
}

def filter_fields(data, purpose):
    allowed = FIELD_ALLOWLIST.get(purpose, [])
    return {k: v for k, v in data.items() if k in allowed}
```

**Pseudonymization pattern:**
```python
import hashlib

def pseudonymize(identifier, salt):
    return hashlib.sha256(f"{salt}:{identifier}".encode()).hexdigest()
```

**Retention enforcement pattern:**
```python
def enforce_retention(db, retention_days=365):
    cutoff = datetime.now() - timedelta(days=retention_days)
    expired = db.query("SELECT id FROM users WHERE last_activity < ?", cutoff)
    for record in expired:
        db.anonymize_or_delete(record.id)
    return len(expired)
```

### Step 7: Audit Trail Implementation
Implement logging for compliance audit readiness.

**Required audit events:**
- Consent granted / withdrawn
- DSAR received / completed
- Data access by staff
- Cross-border transfer executed
- Breach detected / reported
- Retention policy enforced

**Code pattern — audit logger:**
```python
def log_privacy_event(event_type, subject_id, details, operator_id=None):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "subject_id": pseudonymize(subject_id),
        "operator_id": operator_id,
        "details": details,
        "retention_years": 7,
    }
    append_to_immutable_log(entry)
```

## Examples

### Example 1: Building a Consent Management System
User says: "I need to add privacy consent to my Israeli SaaS app"
Actions:
1. Generate consent form component with Hebrew/English toggle
2. Create consent record database schema with all required fields
3. Implement consent withdrawal endpoint
4. Add cookie consent banner with granular controls
Result: Complete consent management system compliant with Israeli Privacy Protection Law.

### Example 2: DSAR Automation Pipeline
User says: "How do I automate data subject access requests for Israeli users?"
Actions:
1. Create DSAR intake form with identity verification
2. Build data collection pipeline across all data stores
3. Generate formatted response with Hebrew support
4. Implement 30-day SLA tracking and alerting
Result: Automated DSAR workflow with identity verification, data aggregation, and audit logging.

### Example 3: Dual Israel-GDPR Compliance
User says: "We have Israeli and European customers, how do I handle both privacy laws?"
Actions:
1. Implement region-aware consent collection
2. Apply stricter requirement from each framework
3. Set up dual breach notification (72-hour for GDPR, immediate for Israeli)
4. Create combined ROPA + database registration
Result: Unified privacy compliance layer satisfying both Israeli and EU requirements.

### Example 4: Cross-Border Transfer Setup
User says: "We need to store Israeli user data in AWS us-east-1"
Actions:
1. Evaluate transfer basis (US is not on adequacy list)
2. Implement contractual safeguards documentation
3. Add explicit consent for US transfer in sign-up flow
4. Create transfer impact assessment record
Result: Documented and code-enforced cross-border transfer with proper legal basis.

## Bundled Resources

### Scripts
- `scripts/check_compliance.py` -- Generates a privacy compliance checklist for your codebase: checks consent implementation, DSAR readiness, cross-border transfer safeguards, and audit logging. Run: `python scripts/check_compliance.py --help`

### References
- `references/privacy-law.md` -- Implementation-focused breakdown of Protection of Privacy Law 1981 and 2017 Security Regulations with code-relevant requirements for consent, DSAR handling, database registration, cross-border transfers, and dual GDPR compliance. Consult when you need specific legal requirements mapped to code patterns.
- `references/ppa-registration.md` -- Step-by-step guide for PPA database registration including required fields, registration criteria decision tree, renewal process, and integration patterns. Consult when implementing database registration workflows.

## Troubleshooting

### Error: "Consent record missing required fields"
Cause: Consent schema does not include all fields required by Israeli law
Solution: Ensure consent records include purpose, timestamp, withdrawal mechanism, and version. Use the consent_record schema from Step 1.

### Error: "DSAR response exceeds 30-day deadline"
Cause: Data aggregation pipeline is too slow or identity verification is stalling
Solution: Pre-index subject data across stores. Implement parallel queries. Set up SLA alerts at 20-day mark.

### Error: "Cross-border transfer blocked"
Cause: No valid transfer basis for destination country
Solution: Check the transfer decision tree in Step 4. For non-adequate countries, obtain explicit consent or sign contractual safeguards before transfer.
