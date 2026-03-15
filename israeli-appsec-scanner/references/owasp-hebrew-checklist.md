# OWASP Top 10 with Hebrew/RTL-Specific Considerations

This reference extends the standard OWASP Top 10 (2021) with attack vectors and mitigation strategies specific to Hebrew-language and RTL (Right-to-Left) web applications.

## A01: Broken Access Control

### Standard Checks

- Enforce least privilege for all access paths
- Deny by default (except public resources)
- Disable directory listing
- Rate limit API access
- Invalidate sessions on logout

### Hebrew/RTL Specifics

**URL Path Encoding Bypass:**
Hebrew characters in URL paths are encoded as UTF-8 percent-encoded sequences (e.g., alef = %D7%90). Some routing frameworks may not correctly normalize these, creating bypass opportunities.

```
# Test cases
/admin/%D7%90         # Hebrew alef in path
/api/%2e%2e/admin     # Standard traversal
/api/..%c0%af/admin   # Overlong UTF-8 encoding
```

**Authorization header with Hebrew usernames:**
If your system uses Hebrew usernames in tokens or headers, verify that comparison functions handle Unicode normalization consistently (NFC vs. NFD).

**Mitigation:**
- Normalize all URL paths to NFC before route matching
- Use URL-safe identifiers (slugs) rather than Hebrew strings in paths
- Test access control with Hebrew-encoded paths

## A02: Cryptographic Failures

### Standard Checks

- Use TLS 1.2+ for all data in transit
- Encrypt sensitive data at rest
- Use strong, up-to-date algorithms
- Manage keys securely

### Hebrew/RTL Specifics

**Character encoding in hashing:**
Hebrew text can have different byte representations depending on normalization form. Ensure consistent normalization before hashing or comparing hashed values.

```python
import unicodedata

# ALWAYS normalize Hebrew text before hashing
text_nfc = unicodedata.normalize('NFC', hebrew_text)
hashed = hashlib.sha256(text_nfc.encode('utf-8')).hexdigest()
```

**Israeli ID number encryption:**
Israeli ID numbers (teudat zehut) are 9-digit numbers with a check digit. They are considered sensitive PII under Israeli law and should be encrypted at rest.

```typescript
// Encrypt Israeli ID before storage
import { createCipheriv, randomBytes } from 'crypto';

function encryptIsraeliId(idNumber: string, key: Buffer): string {
  const iv = randomBytes(16);
  const cipher = createCipheriv('aes-256-gcm', key, iv);
  let encrypted = cipher.update(idNumber, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  const tag = cipher.getAuthTag();
  return `${iv.toString('hex')}:${tag.toString('hex')}:${encrypted}`;
}
```

## A03: Injection

### Standard Checks

- Use parameterized queries
- Validate and sanitize all input
- Use ORM where possible
- Escape special characters in output

### Hebrew/RTL Specifics

**Hebrew SQL Injection:**
Hebrew characters in SQL injection payloads can bypass naive input filters that only check for ASCII special characters.

```sql
-- Standard injection
'; DROP TABLE users; --

-- Hebrew-mixed injection (may bypass ASCII-only filters)
'; DROP TABLE users; -- נכון?

-- Unicode-encoded injection
%27%3B%20DROP%20TABLE%20users%3B%20--%20%D7%A0%D7%9B%D7%95%D7%9F
```

**NoSQL Injection with Hebrew:**
MongoDB queries with Hebrew values can be exploited if input is not validated.

```javascript
// VULNERABLE: Direct user input in query
db.users.find({ name_he: req.body.name });

// Input: { "$gt": "" } will match all records

// SAFE: Validate input type
if (typeof req.body.name !== 'string') {
  throw new Error('Invalid input');
}
db.users.find({ name_he: req.body.name });
```

**Template Injection in Hebrew Emails:**
If using template engines for Hebrew email content, ensure user input cannot inject template directives.

```
// VULNERABLE: Handlebars with Hebrew user input
const template = `שלום {{userName}}, ברוכים הבאים!`;

// If userName = "{{constructor.constructor('return process')()}}"
// This could execute arbitrary code

// SAFE: Use proper escaping
const template = `שלום {{{safeUserName}}}, ברוכים הבאים!`;
// And sanitize before passing to template
```

**Mitigation:**
- Use parameterized queries regardless of input language
- Validate input character ranges (allow only expected Hebrew Unicode ranges)
- Test injection with mixed Hebrew/ASCII payloads

## A04: Insecure Design

### Standard Checks

- Use threat modeling
- Implement secure design patterns
- Use reference architectures
- Conduct design reviews

### Hebrew/RTL Specifics

**SMS OTP Rate Limiting (Israeli Numbers):**
Israeli mobile numbers (+972-5X) are frequently targeted for OTP bombing. Design rate limits specifically for this vector.

```
Rate limit design:
- Per phone number: 3 OTP requests per 15 minutes
- Per IP address: 10 OTP requests per hour
- Global: 1000 OTP requests per hour
- Exponential backoff after first rate limit hit
- Block phone number for 24 hours after 10 failed verifications
```

**Multi-step Government Service Forms:**
Israeli government integrations often involve multi-step forms. Each step must maintain state securely.

```
Insecure: Storing form progress in client-side localStorage
  - User can modify intermediate values
  - Data persists even after session expiry

Secure: Server-side session with signed tokens
  - Store form state server-side (Redis/database)
  - Client holds only a signed reference token
  - Validate previous steps before allowing progression
  - Set expiry on incomplete form sessions
```

**Hebrew Input Length Validation:**
Hebrew characters are multi-byte in UTF-8 (2-3 bytes each). A field that allows 100 bytes may only hold 33-50 Hebrew characters. Design validation at the character level, not byte level.

```javascript
// WRONG: Byte-level validation
if (Buffer.byteLength(input, 'utf8') > 100) { /* reject */ }

// RIGHT: Character-level validation
if ([...input].length > 100) { /* reject */ }
```

## A05: Security Misconfiguration

### Standard Checks

- Remove default credentials
- Harden all configurations
- Disable unnecessary features
- Set security headers

### Hebrew/RTL Specifics

**Content Security Policy for Hebrew Content:**
CSP policies need to account for Hebrew font loading and RTL CSS.

```
Content-Security-Policy:
  default-src 'self';
  font-src 'self' https://fonts.googleapis.com https://fonts.gstatic.com;
  style-src 'self' 'unsafe-inline';
  script-src 'self';
  img-src 'self' data:;
  connect-src 'self' https://your-api.co.il;
```

Note: If using Google Fonts for Hebrew fonts (e.g., Heebo, Assistant), include their domains in `font-src` and `style-src`.

**Error Pages in Hebrew:**
Custom error pages should be in Hebrew (for Hebrew-language applications) but must not leak sensitive information.

```
Common leaks in error pages:
- Stack traces with file paths
- Database connection strings
- Internal API URLs
- Server software versions
- Debug information in Hebrew comments
```

**Supabase RLS Policies:**
Ensure Row Level Security policies handle Hebrew text fields correctly. String comparison in RLS policies should use the correct collation.

```sql
-- Verify RLS is enabled
SELECT tablename, rowsecurity
FROM pg_tables
WHERE schemaname = 'public';

-- Example RLS policy that works with Hebrew text
CREATE POLICY "Users can view their own profile"
ON profiles FOR SELECT
USING (auth.uid() = id);
```

## A06: Vulnerable and Outdated Components

### Standard Checks

- Regularly scan dependencies
- Remove unused dependencies
- Monitor security advisories
- Use only maintained components

### Hebrew/RTL Specifics

**Hebrew-specific libraries to monitor:**
- `hebrew-date` / `hebcal`: Date conversion libraries (check for recent updates)
- `bidirectional-text`: RTL text processing (check for known vulnerabilities)
- `intl-messageformat`: i18n library (verify Hebrew locale handling)
- Hebrew NLP libraries: May include trained models with embedded data

**Israeli payment SDK versions:**
Keep Israeli payment gateway SDKs updated:
- Cardcom SDK
- Tranzila integration library
- PayMe SDK
- Meshulam integration

Check each vendor's changelog for security patches.

## A07: Identification and Authentication Failures

### Standard Checks

- Use strong password policies
- Implement MFA
- Do not ship default credentials
- Implement account lockout

### Hebrew/RTL Specifics

**Israeli Phone Number Validation:**
Israeli phone numbers must be validated for authentication flows (OTP, SMS verification).

```javascript
// Valid Israeli phone formats
const IL_MOBILE = /^(\+972|0)(5[0-9])\d{7}$/;     // Mobile
const IL_LANDLINE = /^(\+972|0)([2-4,8-9])\d{7}$/; // Landline

// Normalize before validation
function normalizeIlPhone(phone) {
  // Remove spaces, dashes, parentheses
  let normalized = phone.replace(/[\s\-()]/g, '');
  // Convert local to international
  if (normalized.startsWith('0')) {
    normalized = '+972' + normalized.substring(1);
  }
  return normalized;
}
```

**Hebrew Characters in Passwords:**
Modern password policies should accept Hebrew characters, but ensure consistent encoding.

```
Policy:
- Accept Hebrew characters (Unicode range 0590-05FF)
- Normalize to NFC before hashing
- Length check should count characters, not bytes
- Do not use Hebrew characters in password strength estimation
  (most strength estimators do not have Hebrew dictionaries)
```

**Israeli OAuth Providers:**
When using Israeli identity providers (gov.il, Israeli banks), validate the redirect URI strictly.

## A08: Software and Data Integrity Failures

### Standard Checks

- Verify software integrity (checksums, signatures)
- Use trusted repositories
- Validate CI/CD pipeline integrity
- Implement code review

### Hebrew/RTL Specifics

**Webhook Verification for Israeli Services:**
Israeli service providers may use different webhook signing methods. Always verify signatures.

```typescript
// Example: Verifying an Israeli payment gateway webhook
import { createHmac } from 'crypto';

function verifyWebhook(
  payload: string,
  signature: string,
  secret: string
): boolean {
  const expected = createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expected)
  );
}
```

**Subresource Integrity for Hebrew Fonts:**
If loading Hebrew fonts from CDNs, use SRI hashes.

```html
<link rel="stylesheet"
  href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700"
  integrity="sha384-..."
  crossorigin="anonymous">
```

## A09: Security Logging and Monitoring Failures

### Standard Checks

- Log all authentication events
- Log access control failures
- Implement alerting
- Retain logs appropriately

### Hebrew/RTL Specifics

**Hebrew Text in Logs:**
Ensure your logging infrastructure supports UTF-8 Hebrew text correctly.

```
Common issues:
- Log aggregators truncating multi-byte characters
- Search/filter not working on Hebrew text
- Hebrew text appearing as mojibake in log viewers
- RTL text causing display issues in log UIs

Solutions:
- Use structured logging (JSON format)
- Ensure UTF-8 encoding throughout the pipeline
- Test log search with Hebrew queries
- Store Hebrew user names and inputs correctly
```

**Israeli PPA Audit Trail Requirements:**
The 2017 security regulations require logging access to personal data. Your audit trail should include:

```json
{
  "timestamp": "2026-03-15T10:30:00Z",
  "user_id": "uuid",
  "action": "read",
  "resource": "profiles",
  "resource_id": "uuid",
  "ip_address": "1.2.3.4",
  "user_agent": "...",
  "data_fields_accessed": ["name_he", "email", "phone"]
}
```

Retain these logs for a minimum of 24 months.

## A10: Server-Side Request Forgery (SSRF)

### Standard Checks

- Validate and sanitize all URLs
- Enforce allow lists for remote resources
- Disable HTTP redirections
- Do not send raw responses to clients

### Hebrew/RTL Specifics

**IDN Homograph Attacks with Hebrew:**
Internationalized Domain Names (IDN) using Hebrew characters can be crafted to look like legitimate domains.

```
Example attack vectors:
- Using Hebrew samekh (ס) to mimic Latin 'o'
  gооgle.com (with Hebrew ס) vs google.com

- Using Hebrew vav (ו) to mimic Latin 'l' or '1'
  paypa1.com vs paypal.com

Mitigation:
- Convert IDN domains to Punycode before processing
- Reject mixed-script domains in user input
- Display Punycode alongside IDN in security contexts
```

**Hebrew URL Encoding:**
URLs containing Hebrew text must be properly encoded. Verify that URL parsing libraries handle Hebrew percent-encoding correctly.

```python
from urllib.parse import quote, unquote

# Encoding Hebrew in URLs
hebrew_path = quote("שלום", safe='')
# Result: %D7%A9%D7%9C%D7%95%D7%9D

# Decoding
original = unquote('%D7%A9%D7%9C%D7%95%D7%9D')
# Result: שלום

# SSRF check: Normalize URL before validating
from urllib.parse import urlparse

def is_safe_url(url):
    parsed = urlparse(url)
    # Reject internal IPs
    if parsed.hostname in ('localhost', '127.0.0.1', '0.0.0.0'):
        return False
    # Reject private ranges
    # ... (standard SSRF checks)
    # Reject Hebrew-encoded URLs that resolve to internal hosts
    decoded_host = unquote(parsed.hostname or '')
    if decoded_host in ('localhost', '127.0.0.1'):
        return False
    return True
```

## Quick Reference: Hebrew Security Testing Payloads

Use these payloads when testing Hebrew/RTL-specific vulnerabilities:

### XSS Payloads with Hebrew

```
<script>alert('שלום')</script>
"><img src=x onerror=alert('XSS')>שלום
<div dir="rtl" onmouseover="alert(1)">טקסט</div>
javascript:alert('שלום')//
```

### SQL Injection with Hebrew

```
' OR '1'='1' -- שלום
'; EXEC xp_cmdshell('whoami') -- עברית
" UNION SELECT name_he FROM skills --
```

### Bidirectional Text Injection

```
Test with U+202E (RTL Override):
normal_text + \u202E + reversed_text

Test with U+2067 (RTL Isolate):
text_before + \u2067 + isolated_text + \u2069 + text_after
```

### Path Traversal with Hebrew

```
../%D7%90%D7%93%D7%9E%D7%99%D7%9F  (../אדמין)
/api/..%2f..%2fadmin
/files/%2e%2e%2f%2e%2e%2fetc%2fpasswd
```

## Tools for Hebrew/RTL Security Testing

| Tool | Purpose | Hebrew Support |
|------|---------|---------------|
| OWASP ZAP | Web app scanner | Good (UTF-8 payloads) |
| Burp Suite | Security testing proxy | Good (manual encoding) |
| sqlmap | SQL injection testing | Good (custom tamper scripts) |
| Semgrep | Static analysis | Good (custom rules for Hebrew patterns) |
| ESLint Security | JS/TS static analysis | Good (with custom rules) |
| Trivy | Container/dependency scanning | N/A (binary analysis) |

## Additional Resources

- OWASP Top 10 (2021): https://owasp.org/Top10/
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/
- Israeli PPA Guidelines: https://www.gov.il/en/departments/the_privacy_protection_authority
- Unicode Bidirectional Algorithm: https://unicode.org/reports/tr9/
- Trojan Source Paper: https://trojansource.codes/
