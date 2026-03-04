---
name: israeli-accessibility
description: >-
  Audit and implement web accessibility compliance per Israeli Standard IS 5568
  and the Equal Rights for Persons with Disabilities Law (Chok Shivyon
  Zchuyot). Use when user asks about Israeli accessibility requirements, IS 5568
  compliance, WCAG for Hebrew sites, RTL accessibility, or Israeli government
  accessibility audit. Covers IS 5568 mapped to WCAG 2.1, RTL screen reader
  patterns, and Hebrew ARIA labels.
license: MIT
compatibility: >-
  Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
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
    he: "נגישות ישראלית"
    en: "Israeli Accessibility"
  display_description:
    he: >-
      ביקורת ויישום נגישות אתרים בהתאם לתקן IS 5568 ולחוק שוויון זכויות
      לאנשים עם מוגבלות, כולל דפוסי RTL ותוויות ARIA בעברית
    en: >-
      Audit and implement web accessibility compliance per Israeli Standard
      IS 5568 and the Equal Rights for Persons with Disabilities Law
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
---

# Israeli Accessibility

## Instructions

### Israeli Accessibility Law
The Equal Rights for Persons with Disabilities Law (Chok Shivyon Zchuyot, 1998) with 2005 and 2013 amendments mandates IS 5568 compliance. Government websites, public bodies, businesses serving the public, companies with 50+ employees, and e-commerce sites must all comply at AA level. Penalties up to 75,000 NIS per violation.

### IS 5568 Standard
Based on WCAG 2.1 with Israeli-specific additions: accessibility statement (Hatzaharat Negishot) required on every page, accessibility menu/widget, lang="he" and dir="rtl" attributes, accessibility coordinator contact published.

### RTL Accessibility Patterns
Tab order: right to left, top to bottom. Arrow keys in menus: left opens submenu (reversed from LTR). Use CSS logical properties (margin-inline-start instead of margin-left). Focus indicators must be 3px minimum.

### Hebrew ARIA Labels
Common labels: תפריט ראשי (main nav), חיפוש באתר (search), סגירה (close), דלגו לתוכן הראשי (skip to content), טוען... (loading). Mixed content needs proper dir attributes on numbers and emails.

### Audit Checklist (IS 5568 AA)
Perceivable: alt text in Hebrew, captions, 4.5:1 contrast. Operable: keyboard access, RTL tab order, skip nav. Understandable: lang="he", Hebrew error messages. Robust: valid HTML, correct ARIA.

### Testing
Automated: axe DevTools, Lighthouse, WAVE, Pa11y, jest-axe. Manual: keyboard nav RTL, NVDA/JAWS Hebrew, VoiceOver, zoom 200%, high contrast mode.

## Examples

### Example 1: Audit a Hebrew E-Commerce Site for IS 5568
User says: "Check my Hebrew e-commerce site for Israeli accessibility compliance"
Actions:
1. Verify `<html lang="he" dir="rtl">` is set
2. Check skip navigation link exists and works with keyboard
3. Validate all images have Hebrew alt text (not English)
4. Test form labels are associated with inputs and read correctly in Hebrew
5. Verify color contrast meets WCAG 2.1 AA (4.5:1 for text)
6. Check tab order follows RTL flow (right-to-left, top-to-bottom)
7. Test with NVDA screen reader in Hebrew mode
8. Verify accessibility statement page exists in Hebrew
Result: Compliance report with pass/fail per IS 5568 criterion and remediation guidance

### Example 2: Add Accessibility to a React RTL Application
User says: "Make my React app accessible for Israeli users"
Actions:
1. Add `dir="rtl"` to root element, use CSS logical properties
2. Implement skip-nav component with Hebrew label ("דלג לתוכן הראשי")
3. Add ARIA labels in Hebrew for all interactive elements
4. Implement keyboard navigation (arrow keys reversed for RTL)
5. Add accessibility statement page per Israeli law requirement
6. Configure focus indicators visible in both light and dark themes
Result: React app with IS 5568 compliant accessibility features

## Bundled Resources

### Scripts
- `scripts/a11y_checker.py` -- Validates HTML files against IS 5568 Israeli accessibility requirements including RTL attributes, Hebrew ARIA labels, skip navigation, and form labels. Run: `python scripts/a11y_checker.py --help`

### References
- `references/is-5568-checklist.md` -- Complete IS 5568 compliance checklist covering legal framework (Equal Rights for Persons with Disabilities Act, 1998), WCAG 2.1 AA mapping, RTL-specific requirements, Hebrew ARIA patterns, and testing tools. Consult when performing a full accessibility audit or when you need the detailed per-criterion checklist.

## Troubleshooting

### Error: "Screen reader not reading Hebrew content correctly"
Cause: NVDA/JAWS may not switch to Hebrew speech engine automatically
Solution: Ensure `lang="he"` is set on the HTML element and on any content sections. Use `aria-label` in Hebrew for custom widgets. Test with NVDA's Hebrew speech synthesizer (eSpeak or Vocalizer).

### Error: "Focus indicator not visible in dark theme"
Cause: Default browser focus outline may be invisible on dark backgrounds
Solution: Use a custom focus indicator with sufficient contrast in both themes. Use `outline: 2px solid` with a color that has 3:1 contrast against both light and dark backgrounds. CSS: `*:focus-visible { outline: 2px solid #4A90D9; outline-offset: 2px; }`

### Error: "Tab order incorrect in RTL layout"
Cause: CSS flexbox/grid items may not follow visual RTL order for keyboard navigation
Solution: Ensure `dir="rtl"` is on the container element. Avoid `tabindex` values greater than 0. Use CSS logical properties (`margin-inline-start` instead of `margin-left`) so layout and tab order stay aligned.
