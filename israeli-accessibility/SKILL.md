---
name: israeli-accessibility
description: >-
  Audit and implement web accessibility compliance per Israeli Standard IS 5568
  and the Equal Rights for Persons with Disabilities Law (Chok Shivyon Zchuyot
  L'Anashim Im Mugbaluyot). Use when user asks about Israeli accessibility
  requirements, "negishot", IS 5568 compliance, WCAG for Hebrew sites,
  RTL accessibility, or Israeli government accessibility audit. Covers
  IS 5568 standard requirements mapped to WCAG 2.1, RTL-specific screen
  reader patterns, Hebrew ARIA labels, and Israeli government audit criteria.
license: MIT
compatibility: 'No network required. Works with Claude Code, Claude.ai, Cursor.'
metadata:
  author: skills-il
  version: 1.0.0
  category: security-compliance
  tags:
    he:
      - נגישות
      - IS-5568
      - WCAG
      - ציות
      - RTL
      - שוויון-זכויות
    en:
      - accessibility
      - is-5568
      - wcag
      - compliance
      - rtl
      - equal-rights
  display_name:
    he: נגישות ישראלית
    en: Israeli Accessibility
  display_description:
    he: ביקורת ויישום נגישות אתרים בהתאם לתקן IS 5568 ולחוק שוויון זכויות
    en: >-
      Audit and implement web accessibility per Israeli Standard IS 5568 and
      the Equal Rights for Persons with Disabilities Law.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
---

# Israeli Accessibility

## Critical Note
This skill provides technical accessibility guidance based on IS 5568 and
Israeli accessibility law. For legal compliance decisions, consult an
accessibility expert certified by the Israeli Standards Institution (Machon
HaTkanim HaYisraeli) or a lawyer specializing in accessibility law.

## Instructions

### Step 1: Understand Israeli Accessibility Law

**The Equal Rights for Persons with Disabilities Law (Chok Shivyon Zchuyot L'Anashim Im Mugbaluyot, 1998)**

This is the foundational Israeli disability rights law. Key amendments related to web accessibility:

| Amendment | Year | Requirement |
|-----------|------|-------------|
| Amendment 2 (Accessibility) | 2005 | Established accessibility obligations for public services |
| Accessibility Regulations | 2013 | Mandated IS 5568 compliance for websites |
| Service Accessibility Regulations | 2013 | Required accessible customer-facing digital services |
| Enforcement updates | 2017+ | Increased enforcement and penalty provisions |

**Who Must Comply:**
| Entity Type | Requirement | Deadline |
|-------------|-------------|----------|
| Government websites | Full IS 5568 AA compliance | Already required |
| Public bodies (Gufim Tziburiyim) | Full IS 5568 AA compliance | Already required |
| Businesses serving the public | IS 5568 AA compliance | Already required |
| Private websites with 50+ employees | IS 5568 AA compliance | Already required |
| E-commerce sites | IS 5568 AA compliance | Already required |
| New websites (all of above) | Must be accessible from launch | Immediate |

**Penalties for Non-Compliance:**
- Civil lawsuits: Individuals with disabilities can sue for damages
- Class action lawsuits: Growing trend in Israel
- Commission for Equal Rights enforcement actions
- Fines: Up to 75,000 NIS per violation for public bodies
- Reputational damage: Israeli disability rights organizations actively monitor compliance

### Step 2: Israeli Standard IS 5568 Requirements

**IS 5568 maps to WCAG 2.1 with Israeli-specific additions:**

IS 5568 is based on WCAG 2.0/2.1 but includes specific requirements for Hebrew and RTL interfaces. The standard defines three conformance levels:

| Level | WCAG Equivalent | Requirements | Israeli Context |
|-------|----------------|--------------|-----------------|
| A | WCAG 2.1 A | Basic accessibility | Minimum legal requirement |
| AA | WCAG 2.1 AA | Standard accessibility | Required for most organizations |
| AAA | WCAG 2.1 AAA | Enhanced accessibility | Government best practice |

**IS 5568 Israeli-Specific Requirements (Beyond Standard WCAG):**

1. **Accessibility Statement (Hatzaharat Negishot):**
   - Required on every compliant website
   - Must be in Hebrew
   - Must include: compliance level, known limitations, contact for accessibility issues
   - Must be accessible from every page (usually in footer)
   - Must include date of last accessibility audit

2. **Accessibility Menu/Widget:**
   - Many Israeli sites implement an accessibility toolbar
   - Common features: font resize, contrast toggle, link highlighting, animation pause
   - Must be keyboard-accessible itself
   - Shortcut key recommendation: Alt+1 for accessibility menu

3. **Hebrew Language Requirements:**
   - `lang="he"` attribute on HTML element
   - `dir="rtl"` attribute on HTML element
   - Proper language switching for mixed content (Hebrew+English)
   - Screen reader pronunciation must work for Hebrew

4. **Contact Information:**
   - Accessibility coordinator contact details must be published
   - Must provide accessible channel for accessibility complaints

### Step 3: RTL-Specific Accessibility Patterns

**HTML Direction and Language:**
```html
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
```

**RTL Keyboard Navigation:**
| Interaction | LTR Behavior | RTL Behavior (IS 5568) |
|------------|-------------|----------------------|
| Tab order | Left to right, top to bottom | Right to left, top to bottom |
| Arrow keys in menus | Right = open submenu, Left = close | Left = open submenu, Right = close |
| Arrow keys in text | Right = forward, Left = back | Left = forward, Right = back |
| Slider increment | Right = increase | Left = increase (logical direction) |
| Progress bar | Fills left to right | Fills right to left |
| Carousel/slider | Next = right arrow | Next = left arrow |
| Breadcrumbs | Home > Section > Page | Home < Section < Page (visual RTL) |

**RTL CSS Accessibility:**
```css
/* Logical properties for RTL-safe layouts */
.element {
  /* Use logical properties instead of physical */
  margin-inline-start: 1rem;  /* Instead of margin-left */
  margin-inline-end: 2rem;    /* Instead of margin-right */
  padding-inline-start: 1rem; /* Instead of padding-left */
  padding-inline-end: 2rem;   /* Instead of padding-right */
  text-align: start;          /* Instead of text-align: left */
  float: inline-start;        /* Instead of float: left */
  border-inline-start: 2px solid; /* Instead of border-left */
}

/* Focus indicators must be clearly visible */
:focus-visible {
  outline: 3px solid #005fcc; /* High contrast focus ring */
  outline-offset: 2px;
}

/* Ensure sufficient color contrast (WCAG AA: 4.5:1 for normal text) */
.text-content {
  color: #1a1a1a; /* Dark text */
  background: #ffffff; /* Light background */
  /* Contrast ratio: 16.9:1 - exceeds AA requirement */
}
```

**RTL Screen Reader Considerations:**
- Hebrew screen readers (NVDA with Hebrew, JAWS Hebrew) read right-to-left
- Mixed content (Hebrew + English/numbers) requires proper `dir` attributes:
```html
<p>המחיר הוא <span dir="ltr">₪99.99</span> כולל מע"מ</p>
<p>צרו קשר: <a href="tel:+972501234567" dir="ltr">050-123-4567</a></p>
<p>כתובת אימייל: <a href="mailto:info@example.co.il" dir="ltr">info@example.co.il</a></p>
```

### Step 4: Hebrew ARIA Labels and Accessible Names

**ARIA Labels in Hebrew:**
```html
<!-- Navigation -->
<nav aria-label="תפריט ראשי">...</nav>
<nav aria-label="ניווט משני">...</nav>
<nav aria-label="פירורי לחם" dir="rtl">...</nav>

<!-- Search -->
<form role="search" aria-label="חיפוש באתר">
  <label for="search-input">חיפוש</label>
  <input id="search-input" type="search" placeholder="חפשו באתר...">
  <button type="submit" aria-label="בצעו חיפוש">
    <svg aria-hidden="true">...</svg>
  </button>
</form>

<!-- Buttons with icons -->
<button aria-label="סגירה" title="סגירה">
  <svg aria-hidden="true"><!-- X icon --></svg>
</button>

<button aria-label="תפריט" aria-expanded="false" aria-controls="mobile-nav">
  <svg aria-hidden="true"><!-- hamburger icon --></svg>
</button>

<!-- Status messages -->
<div role="status" aria-live="polite" aria-label="הודעת מערכת">
  הפעולה בוצעה בהצלחה
</div>

<div role="alert" aria-live="assertive">
  שגיאה: יש למלא את שדה האימייל
</div>

<!-- Form validation -->
<input
  id="email"
  type="email"
  required
  aria-required="true"
  aria-invalid="true"
  aria-describedby="email-error"
>
<span id="email-error" role="alert">כתובת האימייל אינה תקינה</span>
```

**Common Hebrew ARIA Labels Reference:**
| Element | Hebrew ARIA Label |
|---------|------------------|
| Main navigation | תפריט ראשי |
| Footer navigation | תפריט תחתון |
| Search form | חיפוש באתר |
| Close button | סגירה |
| Open menu | פתיחת תפריט |
| Loading | טוען... |
| Required field | שדה חובה |
| Error message | הודעת שגיאה |
| Success message | הפעולה בוצעה בהצלחה |
| Skip to content | דלגו לתוכן הראשי |
| Back to top | חזרה לראש העמוד |
| Previous | הקודם |
| Next | הבא |
| Expand | הרחבה |
| Collapse | כיווץ |
| Sort ascending | מיון עולה |
| Sort descending | מיון יורד |

### Step 5: Accessibility Audit Checklist (IS 5568 AA)

**Perceivable (נתפס):**
- [ ] All images have meaningful `alt` text in Hebrew (or `alt=""` for decorative)
- [ ] Video content has Hebrew captions (כתוביות)
- [ ] Audio content has Hebrew transcript (תמלול)
- [ ] Color contrast meets 4.5:1 for normal text, 3:1 for large text
- [ ] Information is not conveyed by color alone
- [ ] Text can be resized to 200% without loss of content
- [ ] Content is responsive and works on mobile devices

**Operable (ניתן להפעלה):**
- [ ] All functionality available via keyboard (no mouse-only interactions)
- [ ] Tab order follows RTL logical reading order
- [ ] Focus indicators are clearly visible (3px minimum)
- [ ] Skip navigation link in Hebrew: "דלגו לתוכן הראשי"
- [ ] No keyboard traps (user can always Tab away from any element)
- [ ] Animations can be paused/stopped (respect `prefers-reduced-motion`)
- [ ] Time limits can be extended or disabled
- [ ] No content flashes more than 3 times per second

**Understandable (מובן):**
- [ ] `lang="he"` set on HTML element
- [ ] Language changes marked with `lang` attribute (`<span lang="en">`)
- [ ] Form labels are in Hebrew and associated with inputs
- [ ] Error messages are in Hebrew and descriptive
- [ ] Consistent navigation across pages
- [ ] Form submissions have clear feedback in Hebrew

**Robust (חזק):**
- [ ] Valid HTML (passes W3C validator)
- [ ] ARIA roles and properties used correctly
- [ ] Custom widgets follow WAI-ARIA Authoring Practices
- [ ] Works with Hebrew screen readers (NVDA, JAWS, VoiceOver Hebrew)
- [ ] Compatible with accessibility tools and browser extensions

**IS 5568 Additional Requirements:**
- [ ] Accessibility statement page (הצהרת נגישות) published
- [ ] Accessibility coordinator contact information displayed
- [ ] Accessibility menu/toolbar functional
- [ ] Last audit date published in accessibility statement
- [ ] Known limitations documented in accessibility statement

### Step 6: Accessibility Statement Template

**Required Accessibility Statement (Hebrew):**
```html
<article id="accessibility-statement">
  <h1>הצהרת נגישות</h1>

  <p>
    [שם הארגון] מחויב להנגשת האתר לאנשים עם מוגבלויות
    בהתאם לתקן הישראלי IS 5568 ולתקנות שוויון זכויות
    לאנשים עם מוגבלות (התאמות נגישות לשירות), התשע"ג-2013.
  </p>

  <h2>רמת הנגישות</h2>
  <p>
    אתר זה עומד בדרישות תקן IS 5568 ברמה AA.
    האתר נבדק לאחרונה בתאריך [תאריך].
  </p>

  <h2>מגבלות ידועות</h2>
  <ul>
    <li>[מגבלה 1 - תיאור והצעדים לתיקון]</li>
    <li>[מגבלה 2 - תיאור והצעדים לתיקון]</li>
  </ul>

  <h2>יצירת קשר בנושא נגישות</h2>
  <p>
    רכז/ת הנגישות: [שם]<br>
    טלפון: <a href="tel:+972-XX-XXXXXXX" dir="ltr">[מספר טלפון]</a><br>
    אימייל: <a href="mailto:negishot@example.co.il" dir="ltr">negishot@example.co.il</a>
  </p>

  <h2>מידע נוסף</h2>
  <p>
    אנו משתמשים בטכנולוגיות הבאות לצורך הנגשת האתר:
    HTML5, WAI-ARIA, CSS3.
    האתר נבדק ומותאם לדפדפנים: Chrome, Firefox, Safari, Edge.
    האתר נבדק עם קוראי מסך: NVDA, JAWS, VoiceOver.
  </p>
</article>
```

### Step 7: Testing Tools for IS 5568 Compliance

**Automated Testing:**
| Tool | What It Tests | Hebrew/RTL Support |
|------|--------------|-------------------|
| axe DevTools | WCAG 2.1 A/AA rules | Partial (English rules, works on Hebrew content) |
| Lighthouse (Chrome) | WCAG subset, performance | Works on Hebrew sites |
| WAVE | Visual accessibility errors | Works on Hebrew sites |
| Pa11y | CLI accessibility testing | Works on Hebrew sites |
| jest-axe | Unit test accessibility | Works with Hebrew components |

**Manual Testing Required:**
| Test | How | Why |
|------|-----|-----|
| Keyboard navigation (RTL) | Tab through entire site | Verify RTL tab order is logical |
| Screen reader (Hebrew) | NVDA/JAWS with Hebrew TTS | Verify Hebrew content reads correctly |
| VoiceOver (iOS/Mac) | Enable Hebrew in VoiceOver | Test mobile and desktop Hebrew |
| Zoom to 200% | Browser zoom | Verify Hebrew text reflows properly |
| High contrast mode | Windows High Contrast | Check visibility of all elements |
| Color blindness simulation | Chrome DevTools | Verify color is not sole indicator |

**axe-core Integration Example:**
```javascript
// In Playwright or Cypress tests
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('homepage meets IS 5568 AA requirements', async ({ page }) => {
  await page.goto('https://example.co.il');

  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
    .analyze();

  expect(accessibilityScanResults.violations).toEqual([]);
});

test('RTL direction is set correctly', async ({ page }) => {
  await page.goto('https://example.co.il');
  const htmlDir = await page.getAttribute('html', 'dir');
  const htmlLang = await page.getAttribute('html', 'lang');
  expect(htmlDir).toBe('rtl');
  expect(htmlLang).toBe('he');
});
```

## Examples

### Example 1: Full Site Accessibility Audit
**Input**: "Audit our Israeli e-commerce site for IS 5568 compliance"
**Output**: Comprehensive audit report covering all WCAG 2.1 AA criteria plus IS 5568 Israeli-specific requirements. Identifies issues, severity levels, and remediation steps. Includes accessibility statement template and coordinator appointment guidance.

### Example 2: RTL Form Accessibility
**Input**: "Make our Hebrew registration form accessible"
**Output**: Accessible form with Hebrew labels, ARIA attributes, RTL-safe validation messages, keyboard-navigable fields in RTL order, error announcements via aria-live, and proper `dir` handling for mixed Hebrew/English fields (email, phone).

### Example 3: Skip Navigation and Landmarks
**Input**: "Add accessibility landmarks and skip navigation to our Hebrew site"
**Output**: HTML structure with semantic landmarks (main, nav, aside, footer), Hebrew ARIA labels, skip-to-content link ("דלגו לתוכן הראשי"), and proper heading hierarchy for Hebrew content.

## Troubleshooting

- **Issue**: Screen reader reads Hebrew text in wrong direction or garbled
  **Solution**: Ensure `lang="he"` and `dir="rtl"` are set on the `<html>` element. For mixed-language content, wrap English segments in `<span lang="en" dir="ltr">`. Numbers and email addresses should have `dir="ltr"`.

- **Issue**: Keyboard tab order is reversed/illogical in RTL layout
  **Solution**: Tab order follows DOM order, not visual order. Ensure the HTML source order matches the logical reading order for Hebrew (right to left, top to bottom). Do not use `tabindex` values greater than 0. Use CSS logical properties for layout.

- **Issue**: Accessibility toolbar/widget not meeting IS 5568 requirements
  **Solution**: The accessibility toolbar itself must be keyboard-accessible and ARIA-compliant. Ensure it does not introduce new accessibility barriers. Test with screen readers in Hebrew. The toolbar supplements but does not replace built-in accessibility.

- **Issue**: Unclear what IS 5568 level is required for our organization
  **Solution**: Most Israeli businesses serving the public must comply with IS 5568 AA level. Government and public bodies have the strictest requirements. When in doubt, aim for AA compliance. Consult the Commission for Equal Rights of Persons with Disabilities (Nezinut Shivyon Zchuyot L'Anashim Im Mugbaluyot) for specific guidance.
