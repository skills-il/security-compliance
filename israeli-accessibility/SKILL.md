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
