---
name: israeli-ecommerce-compliance
description: >-
  Audit and ensure Israeli e-commerce legal compliance — Consumer Protection
  Law, return policies, price display, accessibility, and cookie consent. Use
  when user asks about "online store compliance Israel", "Chok Hagnat
  HaTzarchan", "consumer protection Israel", "return policy Israel", "IS 5568
  ecommerce", "cookie consent Israel", or "חוק הגנת הצרכן". Covers cooling-off
  period validation, price display requirements, Hebrew terms of service
  generation, accessibility compliance (IS 5568), and business disclosure
  verification. Do NOT use for food-specific compliance (use israeli-food-
  business-compliance) or privacy/GDPR (use israeli-privacy-shield).
license: MIT
allowed-tools: "Bash(python:*) WebFetch"
compatibility: >-
  Works with Claude Code, OpenClaw, Cursor. OpenClaw recommended for automated
  website scanning and periodic compliance checks.
metadata:
  author: skills-il
  version: 1.0.0
  category: security-compliance
  tags:
    he:
      - ציות
      - מסחר-אלקטרוני
      - הגנת-צרכן
      - נגישות
      - משפטי
      - ישראל
    en:
      - compliance
      - ecommerce
      - consumer-protection
      - accessibility
      - legal
      - israel
  display_name:
    he: תאימות חוקית למסחר אלקטרוני ישראלי
    en: Israeli E-Commerce Compliance
  display_description:
    he: ביקורת תאימות חוקית לחנויות מקוונות ישראליות — חוק הגנת הצרכן, מדיניות החזרות, נגישות ועוגיות
    en: >-
      Audit and ensure Israeli e-commerce legal compliance — Consumer Protection
      Law, return policies, price display, accessibility, and cookie consent.
  openclaw:
    requires:
      bins: []
      env: []
    emoji: "✅"
---

# Israeli E-Commerce Compliance

## Instructions

> **Note:** This skill provides compliance guidance. It does not replace legal counsel. Recommend consulting a consumer protection attorney (orech din specializing in mishpat tzarchani) for specific compliance decisions.

### Step 1: Scan for Consumer Protection Law Compliance (Chok Hagnat HaTzarchan)
Verify 14-day cooling-off period for distance selling (mecher merachok):
- Right to cancel within 14 days of receiving product
- Extended to 4 months for people with disabilities, seniors (65+), and new immigrants (<5 years)
- Cancellation fee: up to 5% of transaction or 100 NIS, whichever is lower
- Return shipping: at buyer's expense unless item is defective

Check for required pre-purchase disclosures:
- Full product/service description
- Total price including all fees and taxes
- Delivery timeline and costs
- Cancellation and return policy
- Seller's full details (see Step 5)

### Step 2: Validate Price Display Requirements
- All prices MUST include VAT (18%) — Israeli law requires consumer-facing prices to be inclusive
- Delivery/shipping costs must be clearly stated before checkout
- Total order cost (including all fees) must be shown before payment confirmation
- Currency must be NIS (display as ₪ or ש"ח)
- Discounted items: both original and sale price must be shown
- "From" pricing (e.g., "from 99 NIS") only allowed when the base price actually exists

### Step 3: Generate Hebrew Terms of Service and Return Policy
Generate compliant Hebrew Terms of Service (תנאי שימוש) including:
- Company details (name, registration number, address, contact)
- Product/service descriptions
- Payment terms and accepted methods
- Delivery policy and timeframes
- Return and cancellation policy per Consumer Protection Law
- Warranty terms (if applicable)
- Dispute resolution mechanism

Generate Return Policy (מדיניות החזרות) per legal requirements:
- 14-day cancellation right clearly stated
- Process for requesting cancellation
- Refund timeline (up to 14 days from cancellation notice)
- Exceptions to cancellation right (perishables, custom items, digital content after download)

### Step 4: Check Accessibility Compliance (IS 5568 / Amendment 36)
Israeli websites must comply with IS 5568 accessibility standard (based on WCAG 2.1 AA).
Use browser automation to scan for:
- Alt text on images
- Keyboard navigation support
- Screen reader compatibility
- Color contrast ratios (4.5:1 minimum for normal text)
- Form labels and error messages
- Language declaration (Hebrew RTL)
- Accessibility statement page

Amendment 36 to the Equal Rights for People with Disabilities Law applies to:
- All businesses with 25+ employees
- All businesses providing public services online
- Government services

### Step 5: Verify Business Disclosure (Osek Number, Address, Contact)
Israeli e-commerce sites must prominently display:
- Business name (as registered with Registrar of Companies)
- Registration number (osek murshe number or company number)
- Physical address (not just PO Box)
- Phone number
- Email address
- Full name of business owner or authorized contact

These must appear on the website (typically in footer or "About Us").
Must also appear on every invoice/receipt.

### Step 6: Validate Cookie Consent per Communications Law
Israeli Communications Law (Amendment 2022) requires:
- Cookie consent banner for non-essential cookies
- Clear description of cookie types and purposes
- Opt-in for marketing/analytics cookies (not opt-out)
- Easy way to withdraw consent
- Privacy policy linking to cookie details

Essential cookies (login, shopping cart) don't require consent.
Analytics and marketing cookies require explicit opt-in.

## Examples

### Example 1: Full Compliance Audit for New Online Store
User says: "I'm launching an online clothing store, make sure it's compliant with Israeli law"
Actions:
1. Scan website for Consumer Protection Law compliance (return policy, cooling-off)
2. Validate price display (VAT included, delivery costs visible)
3. Check business disclosure (registration, address, contact visible)
4. Test accessibility (IS 5568 automated checks)
5. Verify cookie consent implementation
6. Generate compliance report with pass/fail per section
Result: Compliance report: 4/6 sections pass. Issues found: return policy doesn't mention extended cancellation for elderly/disabled, cookie banner uses opt-out instead of opt-in. Recommended fixes provided with Hebrew legal text.

### Example 2: Generating Compliant Return Policy
User says: "I need a return policy for my electronics store that's legal in Israel"
Actions:
1. Determine product categories (electronics — standard 14-day applies)
2. Draft Hebrew return policy per Consumer Protection Law
3. Include all mandatory clauses: 14-day cooling-off, extended periods, exceptions
4. Include cancellation fee disclosure (up to 5% or 100 NIS)
5. Add refund timeline commitment (14 days)
Result: Complete Hebrew return policy (מדיניות החזרות) ready to publish. Includes all legally required clauses, clear customer-facing language, and specific exceptions for electronics (e.g., opened software).

### Example 3: Accessibility Audit for Existing Store
User says: "We got a complaint about our website's accessibility, can you check it?"
Actions:
1. Determine if business falls under IS 5568 requirements (25+ employees or public service)
2. Run automated accessibility scan using browser automation
3. Check: alt text, keyboard nav, contrast ratios, form labels, RTL support
4. Identify: 12 images missing alt text, 3 forms without labels, contrast below 4.5:1 on 2 pages
5. Generate prioritized fix list with effort estimates
Result: Accessibility report: 15 issues found (8 critical, 7 moderate). Critical issues: missing form labels (checkout page), insufficient contrast on CTA buttons. Fix guide provided with HTML/CSS corrections.

## Bundled Resources

### References
- `references/consumer-protection-law.md` — Summary of Israeli Consumer Protection Law requirements for e-commerce: distance selling rules, cooling-off periods (standard and extended), cancellation fees, price display requirements, required disclosures, and exceptions. Consult when auditing compliance in Steps 1-2 or generating legal documents in Step 3.

## Troubleshooting

### Error: "Cookie consent not compliant"
Cause: Using opt-out instead of opt-in for non-essential cookies, or consent banner not appearing on all pages.
Solution: Implement opt-in consent per Communications Law Amendment. Ensure banner appears on first visit before any non-essential cookies are set. Include clear categories (essential, analytics, marketing) with individual toggle controls.

### Error: "Accessibility scan incomplete"
Cause: Dynamic content loaded via JavaScript may not be captured by automated scanning.
Solution: Ensure scan waits for full page load including lazy-loaded content. Run additional manual checks for JavaScript-heavy pages. Focus on checkout flow and forms — these are highest-priority accessibility targets.

### Error: "Price display violation"
Cause: Prices shown without VAT or delivery costs hidden until checkout.
Solution: All consumer-facing prices must include 18% VAT. Delivery costs must be shown before the payment confirmation step. Use clear format: "₪X.XX (כולל מע"מ)" for all prices. Ensure cart total includes delivery before asking for payment details.

### Error: "Business disclosure missing"
Cause: Required business details not visible or not on every required page.
Solution: Add business name, registration number, physical address, phone, email, and contact name to footer (appears on all pages). Also verify these appear on order confirmations and invoices. Israeli Consumer Protection Law specifically requires these for distance selling.