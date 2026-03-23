---
name: israeli-appsec-scanner
description: Security scanning guidance for Israeli web applications covering OWASP Top 10, Israeli Privacy Protection Authority (PPA) compliance, dependency vulnerability scanning, secrets detection, and secure coding patterns for Hebrew/RTL apps. Use when user asks to "scan for vulnerabilities", "check security compliance", "audit Israeli app security", "bodek aviskhut" (Hebrew transliteration), or needs help with PPA compliance, secrets detection, or Hebrew input sanitization. Provides actionable checklists, automated scanning scripts, and Israeli-specific security guidance. Do NOT use for network penetration testing, physical security audits, or non-application-layer security concerns.
license: MIT
allowed-tools: Bash(python:*)
compatibility: No special requirements. Works with Claude Code, Cursor, Windsurf.
---

# Israeli AppSec Scanner

Security scanning and compliance guidance tailored for Israeli web applications. This skill covers the full spectrum of application security, from OWASP Top 10 verification to Israeli Privacy Protection Authority (PPA) compliance, with special attention to Hebrew/RTL-specific attack vectors.

## OWASP Top 10 Checklist (Israeli Context)

Work through each category systematically. For each finding, note the severity (Critical/High/Medium/Low) and provide a remediation recommendation.

### A01: Broken Access Control

- [ ] Verify all API endpoints enforce authentication (check Next.js middleware, NestJS guards)
- [ ] Confirm role-based access control covers admin, user, and anonymous roles
- [ ] Test that Hebrew URL paths cannot bypass route-based authorization
- [ ] Check for Insecure Direct Object References (IDOR) on user-facing resources
- [ ] Verify CORS configuration restricts origins to expected Israeli domains
- [ ] Ensure JWT tokens are validated server-side, not just client-side
- [ ] Test directory traversal with Hebrew-encoded path segments (%D7%90 etc.)

### A02: Cryptographic Failures

- [ ] Verify TLS 1.2+ on all connections (Israeli hosting providers sometimes default to older versions)
- [ ] Check that passwords are hashed with bcrypt/argon2 (not MD5/SHA1)
- [ ] Confirm Israeli national ID numbers (teudat zehut) are encrypted at rest
- [ ] Verify credit card data is never stored locally (PCI DSS requirement)
- [ ] Check that Supabase service role keys are never exposed to the client
- [ ] Ensure Israeli payment gateway tokens (Cardcom, Tranzila) use secure storage

### A03: Injection

- [ ] Test SQL injection with Hebrew text input (`'; DROP TABLE --` with Hebrew characters)
- [ ] Verify parameterized queries for all database operations involving Hebrew text
- [ ] Check for NoSQL injection in MongoDB queries (common in Israeli startups using MEAN stack)
- [ ] Test command injection through file upload names containing Hebrew characters
- [ ] Verify LDAP injection protection if integrating with Israeli corporate directories
- [ ] Check for template injection in email templates with Hebrew content

### A04: Insecure Design

- [ ] Verify rate limiting on Israeli SMS gateway endpoints (prevent OTP bombing)
- [ ] Check for business logic flaws in Israeli payment processing flows
- [ ] Ensure multi-step forms (common in Israeli government service integrations) maintain state securely
- [ ] Verify that Hebrew input length limits account for UTF-8 multi-byte characters

### A05: Security Misconfiguration

- [ ] Check HTTP security headers (CSP, X-Frame-Options, HSTS)
- [ ] Verify error pages do not leak stack traces or Hebrew debug messages
- [ ] Confirm default credentials are changed on all services
- [ ] Check that Israeli cloud provider (AWS IL region, GCP) security groups are properly configured
- [ ] Verify Supabase Row Level Security (RLS) policies are enabled on all tables
- [ ] Ensure `.env` files with Israeli service credentials are in `.gitignore`

### A06: Vulnerable and Outdated Components

- [ ] Run `npm audit` or `pnpm audit` and address critical/high findings
- [ ] Check for known vulnerabilities in Hebrew-specific libraries (hebrew-date, bidirectional text processors)
- [ ] Verify container base images are up to date (use `trivy image`)
- [ ] Check for outdated Israeli payment SDK versions

### A07: Identification and Authentication Failures

- [ ] Verify Israeli phone number format validation (+972) in authentication flows
- [ ] Check that OTP codes for Israeli mobile numbers have appropriate expiry (5 minutes max)
- [ ] Test password policies accommodate Hebrew characters
- [ ] Verify session management after authentication with Israeli OAuth providers
- [ ] Check for credential stuffing protection on login endpoints

### A08: Software and Data Integrity Failures

- [ ] Verify npm package integrity with lockfile validation
- [ ] Check CI/CD pipeline security (GitHub Actions, Vercel deployment hooks)
- [ ] Ensure third-party Israeli service webhooks are verified (signature validation)
- [ ] Verify Subresource Integrity (SRI) for external scripts

### A09: Security Logging and Monitoring Failures

- [ ] Confirm authentication events are logged (login, logout, failed attempts)
- [ ] Verify logs capture Hebrew text correctly (UTF-8 encoding)
- [ ] Check that Israeli PPA-required audit trails are maintained for personal data access
- [ ] Ensure log storage complies with Israeli data retention requirements

### A10: Server-Side Request Forgery (SSRF)

- [ ] Verify URL validation for user-supplied URLs (block internal network ranges)
- [ ] Check that Israeli government API integrations validate redirect URLs
- [ ] Test for SSRF through Hebrew-encoded URLs and IDN homograph attacks

## Israeli Privacy Protection Authority (PPA) Compliance

Israel's Privacy Protection Law (1981) and its regulations impose specific requirements on applications handling personal data of Israeli residents.

### Database Registration

Under Israeli law, certain databases containing personal data must be registered with the PPA:

1. **Determine registration requirement**: Databases with 10,000+ records, or containing sensitive data (health, financial, biometric), or used for direct marketing must be registered
2. **Registration fields**: Database name, purpose, data categories, security measures, data processors, cross-border transfers
3. **Annual renewal**: Registration must be renewed annually
4. **Exemptions**: Databases used solely for managing employee-employer relations (under certain conditions)

### Data Protection Requirements

```
CHECKLIST: Israeli Privacy Protection Law Compliance

[ ] Consent: Obtain informed consent before collecting personal data
    - Consent must be specific, informed, and freely given
    - Hebrew consent text must be clear and understandable
    - Separate consent for different processing purposes

[ ] Purpose limitation: Use data only for the stated purpose
    - Document the purpose in your privacy policy (Hebrew + English)
    - Do not repurpose data without fresh consent

[ ] Data minimization: Collect only necessary data
    - Review each form field for necessity
    - Israeli ID numbers should only be collected when legally required

[ ] Security measures: Implement appropriate technical measures
    - Follow PPA's "Information Security Regulations" (2017)
    - Conduct annual security assessments
    - Maintain access logs for at least 24 months

[ ] Data subject rights: Support access, correction, deletion requests
    - Respond within 30 days to data access requests
    - Provide data in a structured, machine-readable format
    - Hebrew language support for all data subject communications

[ ] Breach notification: Notify PPA and affected individuals
    - "Serious security incident" must be reported to PPA
    - Notification should be in Hebrew for Israeli residents
    - Document all incidents and remediation steps
```

### Cross-Border Data Transfer

Israeli law restricts transfer of personal data outside Israel. Permitted when:

- The destination country has adequate data protection (EU countries, recognized by PPA)
- The data subject consented to the transfer
- The transfer is necessary for contract performance
- Appropriate contractual safeguards are in place (Standard Contractual Clauses)

**Common scenarios for Israeli apps:**
- Cloud hosting on AWS/GCP: Ensure data processing agreement is in place
- Using US-based SaaS tools: Verify contractual safeguards
- Analytics services: Consider data anonymization before transfer

## Dependency Scanning

### npm/pnpm Audit

```bash
# Run vulnerability scan
pnpm audit

# Fix automatically where possible
pnpm audit --fix

# Generate detailed JSON report
pnpm audit --json > audit-report.json

# Check specific severity levels
pnpm audit --audit-level=high
```

### Container Scanning with Trivy

```bash
# Scan Docker image
trivy image your-app:latest

# Scan with severity filter
trivy image --severity HIGH,CRITICAL your-app:latest

# Scan filesystem (for local projects)
trivy fs --security-checks vuln,secret,config .

# Generate SARIF report for GitHub integration
trivy image --format sarif --output trivy-results.sarif your-app:latest
```

### Python Dependency Scanning

```bash
# Using pip-audit
pip-audit

# With fix suggestions
pip-audit --fix --dry-run

# Scan requirements file
pip-audit -r requirements.txt
```

### Snyk Integration

```bash
# Authenticate
snyk auth

# Test for vulnerabilities
snyk test

# Monitor project (continuous)
snyk monitor

# Test specific package
snyk test --package-manager=npm
```

## Secrets Detection

### Scanning for Israeli Service Credentials

Israeli applications commonly use service credentials that must never be committed to version control:

**Israeli Payment Gateways:**
- Cardcom: Terminal numbers, API usernames, operation codes
- Tranzila: Supplier codes, terminal passwords
- PayMe: Seller IDs, API keys
- Meshulam: Page codes, API keys

**Israeli Services:**
- Israel Post API keys
- Israeli bank API credentials (Poalim, Leumi, Discount, Mizrahi)
- Gov.il API tokens
- Israeli SMS gateways (019, Cellact, InforUMobile) API keys

### Using TruffleHog

```bash
# Scan git history
trufflehog git file://. --only-verified

# Scan specific branch
trufflehog git file://. --branch main --only-verified

# Scan with JSON output
trufflehog git file://. --json > secrets-report.json
```

### Using Gitleaks

```bash
# Scan repository
gitleaks detect --source . --verbose

# Scan with custom config for Israeli services
gitleaks detect --source . --config .gitleaks.toml

# Generate report
gitleaks detect --source . --report-format json --report-path gitleaks-report.json
```

**Recommended `.gitleaks.toml` additions for Israeli services:**

```toml
[[rules]]
id = "cardcom-terminal"
description = "Cardcom Terminal Number"
regex = '''(?i)(cardcom|terminal)[\s]*[=:]\s*["']?\d{6,8}["']?'''
tags = ["israeli-payment"]

[[rules]]
id = "tranzila-supplier"
description = "Tranzila Supplier Code"
regex = '''(?i)(tranzila|supplier)[\s]*[=:]\s*["']?[a-zA-Z0-9]{4,20}["']?'''
tags = ["israeli-payment"]

[[rules]]
id = "israeli-sms-api"
description = "Israeli SMS Gateway API Key"
regex = '''(?i)(cellact|inforu|019sms)[\s_-]*(api|key|token)[\s]*[=:]\s*["']?[a-zA-Z0-9]{16,}["']?'''
tags = ["israeli-service"]
```

## Hebrew/RTL-Specific Security

### Unicode Bidirectional Text Attacks (Trojan Source)

Bidirectional control characters can make code appear different from what it actually does. This is especially relevant in Hebrew/English mixed codebases.

**Dangerous characters to detect:**
- U+202A (Left-to-Right Embedding)
- U+202B (Right-to-Left Embedding)
- U+202C (Pop Directional Formatting)
- U+202D (Left-to-Right Override)
- U+202E (Right-to-Left Override)
- U+2066 (Left-to-Right Isolate)
- U+2067 (Right-to-Left Isolate)
- U+2068 (First Strong Isolate)
- U+2069 (Pop Directional Isolate)

**Detection script:**
```python
import re
import sys

BIDI_CHARS = re.compile(
    '[\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069]'
)

def scan_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            matches = BIDI_CHARS.findall(line)
            if matches:
                print(f"WARNING: {filepath}:{line_num} contains "
                      f"{len(matches)} bidirectional control character(s)")
```

### Hebrew Homoglyph Attacks

Some Hebrew characters visually resemble Latin characters, enabling phishing and spoofing:

| Hebrew | Latin Lookalike | Unicode |
|--------|----------------|---------|
| ס (samekh) | o | U+05E1 |
| ו (vav) | l, 1 | U+05D5 |
| ח (het) | n | U+05D7 |
| ן (final nun) | l | U+05DF |

**Mitigation:** Normalize and validate all user-facing URLs and identifiers. Reject mixed-script strings in security-sensitive contexts (usernames, URLs, email addresses).

### RTL Override in URLs

Attackers can use RTL override characters (U+202E) to disguise malicious URLs:

```
Example: A URL containing U+202E can make "evil.com/gnp.exe" appear as "evil.com/exe.png"
```

**Mitigation:**
- Strip all bidirectional override characters from URLs before processing
- Validate URL structure after Unicode normalization
- Display punycode for internationalized domain names in security-sensitive contexts

### Hebrew Input Validation Patterns

```javascript
// Validate Hebrew-only input (letters, spaces, common punctuation)
const HEBREW_PATTERN = /^[\u0590-\u05FF\s\-'".,:;!?()]+$/;

// Validate mixed Hebrew/English input
const MIXED_PATTERN = /^[\u0590-\u05FFa-zA-Z0-9\s\-'".,:;!?()@#$%&*]+$/;

// Sanitize Hebrew input for XSS prevention
function sanitizeHebrewInput(input) {
  // Remove bidirectional control characters
  let sanitized = input.replace(/[\u202a-\u202e\u2066-\u2069]/g, '');
  // Standard HTML entity encoding
  sanitized = sanitized
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;');
  return sanitized;
}

// Validate Israeli phone number
const IL_PHONE_PATTERN = /^(\+972|0)(5[0-9]|7[2-9])\d{7}$/;

// Validate Israeli ID number (Teudat Zehut) with check digit
function validateIsraeliId(id) {
  if (!/^\d{9}$/.test(id)) return false;
  let sum = 0;
  for (let i = 0; i < 9; i++) {
    let digit = parseInt(id[i]) * ((i % 2) + 1);
    if (digit > 9) digit -= 9;
    sum += digit;
  }
  return sum % 10 === 0;
}
```

## Secure Coding Patterns

### Parameterized Queries for Hebrew Text

```typescript
// CORRECT: Parameterized query (safe)
const { data, error } = await supabase
  .from('skills')
  .select('*')
  .ilike('name_he', `%${searchTerm}%`);

// INCORRECT: String concatenation (vulnerable to SQL injection)
// const query = `SELECT * FROM skills WHERE name_he LIKE '%${searchTerm}%'`;

// For raw SQL when parameterized queries are needed:
const { data } = await supabase.rpc('search_skills', {
  search_term: searchTerm  // Parameter is safely escaped
});
```

### CSRF Protection for Israeli Payment Forms

```typescript
// Generate CSRF token for payment form
import { randomBytes } from 'crypto';

function generateCsrfToken(): string {
  return randomBytes(32).toString('hex');
}

// Validate on form submission
function validateCsrfToken(session: string, submitted: string): boolean {
  return session === submitted && session.length === 64;
}

// In payment form (Hebrew UI)
// <input type="hidden" name="_csrf" value={csrfToken} />
```

### Rate Limiting for Israeli SMS Gateways

```typescript
// Rate limit OTP requests to prevent abuse
// Israeli SMS costs ~0.05-0.15 NIS per message
const OTP_LIMITS = {
  perPhone: { max: 3, windowMs: 15 * 60 * 1000 },    // 3 per 15 min per phone
  perIp: { max: 10, windowMs: 60 * 60 * 1000 },       // 10 per hour per IP
  global: { max: 1000, windowMs: 60 * 60 * 1000 },    // 1000 per hour globally
};

// Implementation with Redis
async function checkOtpRateLimit(phone: string, ip: string): Promise<boolean> {
  const phoneKey = `otp:phone:${phone}`;
  const ipKey = `otp:ip:${ip}`;

  const phoneCount = await redis.incr(phoneKey);
  if (phoneCount === 1) await redis.expire(phoneKey, 900);
  if (phoneCount > OTP_LIMITS.perPhone.max) return false;

  const ipCount = await redis.incr(ipKey);
  if (ipCount === 1) await redis.expire(ipKey, 3600);
  if (ipCount > OTP_LIMITS.perIp.max) return false;

  return true;
}
```

## Compliance Checklist

### Israeli Privacy Protection Law (GDPR-Equivalent)

| Requirement | Israeli Law | GDPR Equivalent | Status |
|------------|------------|-----------------|--------|
| Legal basis for processing | Section 1, PPL | Art. 6 GDPR | [ ] |
| Consent requirements | Section 11, PPL | Art. 7 GDPR | [ ] |
| Right of access | Section 13, PPL | Art. 15 GDPR | [ ] |
| Right to correction | Section 14, PPL | Art. 16 GDPR | [ ] |
| Right to deletion | Section 14A, PPL | Art. 17 GDPR | [ ] |
| Data security measures | Regulations 2017 | Art. 32 GDPR | [ ] |
| Breach notification | Regulation 11A | Art. 33-34 GDPR | [ ] |
| Cross-border transfers | Section 36, PPL | Art. 44-49 GDPR | [ ] |
| Database registration | Section 8, PPL | Art. 30 GDPR (ROPA) | [ ] |
| DPO appointment | Mandatory for certain entities (Amendment 13, Aug 2025): public bodies, data brokers, large-scale sensitive data processors | Art. 37 GDPR | [ ] |

### SOC 2 Considerations for Israeli Startups

Israeli startups selling to US enterprises often need SOC 2 compliance:

1. **Trust Service Criteria**: Security, Availability, Processing Integrity, Confidentiality, Privacy
2. **Common control gaps in Israeli startups**:
   - Lack of formal change management process
   - Missing access review procedures
   - Incomplete logging and monitoring
   - No formal incident response plan
3. **Israeli-specific considerations**:
   - IDF service background checks are not a substitute for formal employment screening
   - Israeli holiday calendar affects SLA calculations
   - Hebrew documentation may need English translations for auditors

### PCI DSS for Israeli Payment Processing

If your application processes Israeli credit cards (Isracard, Leumi Card, CAL):

1. **Level determination**: Based on annual transaction volume
2. **SAQ selection**: Most Israeli web apps qualify for SAQ A or SAQ A-EP
3. **Israeli specifics**:
   - Shva (the Israeli payment clearing system) has its own security requirements
   - Israeli credit card numbers follow standard Luhn algorithm
   - Israeli recurring payment ("hora'at keva") requires additional consent documentation

## Running the Security Audit

Use the included scripts to perform automated checks:

```bash
# Run the full security audit checklist
python scripts/security-audit-checklist.py --project-dir /path/to/project

# Scan for Israeli service credentials
bash scripts/secrets-scanner.sh /path/to/project

# Generate a compliance report
python scripts/security-audit-checklist.py --project-dir /path/to/project --format json > report.json
```

Refer to the `references/` directory for detailed guidance on Israeli privacy law and OWASP considerations for Hebrew/RTL applications.

## Gotchas

- Israeli Privacy Protection Law (1981) has different breach notification rules than GDPR. There is no 72-hour deadline; the law says "without delay". Agents may incorrectly apply GDPR timelines to Israeli incidents.
- Hebrew UTF-8 characters are 2 bytes each. Input length validation that counts bytes instead of characters will reject valid Hebrew input at half the expected length.
- Israeli ID numbers (Teudat Zehut) use a Luhn-variant check digit algorithm, not standard Luhn. Agents may implement the wrong validation and accept invalid IDs.
- The Israeli Privacy Protection Authority (PPA) database registration threshold is 10,000 records, not 5,000. Agents may cite incorrect thresholds from outdated training data.
- Bidirectional (BiDi) text attacks are especially dangerous in Hebrew/English mixed codebases. Standard security scanners do not detect RTL override characters (U+202E) that can disguise malicious code.
