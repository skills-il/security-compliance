# PPA Database Registration Guide

## Overview
The Privacy Protection Authority (Rashut LeHaganat HaPratiut), under the Ministry
of Justice, maintains the registry of databases (rasham maagarei meida) in Israel.

## Registration Decision Tree

```
Does the database contain personal data?
  NO -> Registration not required
  YES -> Continue

Is the database owned by a public body (guf tzibburi)?
  YES -> Registration REQUIRED
  NO -> Continue

Is the database used for credit/financial information services?
  YES -> Registration REQUIRED
  NO -> Continue

Does the database have 10,000+ records?
  NO -> Registration not required
  YES -> Continue

Is the data used for direct marketing (diour yashir)?
  YES -> Registration REQUIRED
  NO -> Continue

Does the database contain sensitive data?
  (health, genetics, sexual orientation, political views, criminal record)
  YES -> Registration REQUIRED
  NO -> Registration not required
```

## Registration Process

### Step 1: Prepare Registration Data
Gather the following information:
- Legal entity name and Israeli business number (mispar chevra / mispar amuta)
- Database name (descriptive, in Hebrew)
- Purpose of the database (matarat ha-maagar)
- Types of personal data stored
- Sources of data (direct collection, third parties, public sources)
- Who has access to the data (internal staff, service providers)
- Security level applied (basic, medium, high)
- Whether data is transferred outside Israel

### Step 2: Submit via PPA Portal
- Portal: https://www.gov.il/he/departments/privacy_authority
- Submit Form 1 (Tofes 1) with all required details
- Pay applicable registration fee

### Step 3: Receive Registration Number
- PPA reviews submission and issues registration number
- Registration number must be referenced in privacy policy

### Step 4: Maintain Registration
- Update registration when purpose or scope changes
- Renew periodically as required
- Report any material changes to the PPA

## Integration Patterns

### Registration Check in Application Code
```python
def check_registration_status(db_config):
    """Check if a database requires PPA registration."""
    if db_config.get("is_public_body"):
        return {"required": True, "reason": "Public body database"}
    if db_config.get("is_credit_service"):
        return {"required": True, "reason": "Credit information service"}
    record_count = db_config.get("record_count", 0)
    if record_count >= 10000:
        if db_config.get("used_for_marketing"):
            return {"required": True, "reason": "10K+ records with direct marketing"}
        if db_config.get("has_sensitive_data"):
            return {"required": True, "reason": "10K+ records with sensitive data"}
    return {"required": False, "reason": "Does not meet registration criteria"}
```

### Registration Data Model
```python
registration_record = {
    "database_name": "string",
    "registration_number": "string (from PPA)",
    "owner_entity": "string (Israeli business number)",
    "purpose": "string (matarat ha-maagar)",
    "data_types": ["personal", "sensitive", "financial"],
    "data_sources": ["direct_collection", "third_party", "public"],
    "recipients": ["internal_staff", "service_providers"],
    "security_level": "basic | medium | high",
    "cross_border_transfer": False,
    "retention_period_months": 36,
    "registered_date": "ISO-8601",
    "renewal_due_date": "ISO-8601",
}
```

## Common Pitfalls

1. **Forgetting to update registration** when database purpose changes
2. **Not counting records across systems** — the 10,000 threshold applies to the
   total across all systems that share the same purpose
3. **Sensitive data misclassification** — health data includes mental health;
   financial data includes salary information
4. **Missing registration number in privacy policy** — must be publicly disclosed
