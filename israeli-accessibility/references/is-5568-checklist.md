# IS 5568 Accessibility Checklist

## Legal Framework
- **Law**: Equal Rights for Persons with Disabilities (1998)
- **Amendments**: 2005 (accessibility regulations), 2013 (web accessibility)
- **Standard**: IS 5568 (based on WCAG 2.1 AA)
- **Penalty**: Up to 75,000 NIS per violation

## Who Must Comply
- Government websites and public bodies
- Businesses serving the public
- Companies with 50+ employees
- E-commerce sites
- Educational institutions

## IS 5568 Requirements (Beyond WCAG)
1. **Accessibility Statement** (Hatzaharat Negishot) on every page
2. **Accessibility menu/widget** providing quick adjustments
3. **Accessibility coordinator** contact information published
4. `lang="he"` and `dir="rtl"` attributes on html element

## WCAG AA Checklist for Hebrew Sites

### Perceivable
- [ ] All images have Hebrew alt text
- [ ] Video has Hebrew captions
- [ ] Color contrast ratio >= 4.5:1 (text), >= 3:1 (large text)
- [ ] Text resizable to 200% without loss

### Operable
- [ ] All functionality keyboard accessible
- [ ] Tab order follows RTL reading direction (right to left)
- [ ] Skip navigation link ("דלגו לתוכן הראשי")
- [ ] Focus indicators visible (3px minimum)
- [ ] No keyboard traps

### Understandable
- [ ] `lang="he"` on html element
- [ ] Error messages in Hebrew
- [ ] Form labels in Hebrew
- [ ] Consistent navigation across pages

### Robust
- [ ] Valid HTML
- [ ] Correct ARIA roles and labels
- [ ] Works with NVDA/JAWS in Hebrew mode
- [ ] Works with VoiceOver

## RTL-Specific Checks
- [ ] Arrow keys reversed in menus (left = open submenu)
- [ ] CSS uses logical properties (inline-start/end, not left/right)
- [ ] Numbers wrapped in `dir="ltr"` spans
- [ ] Email addresses wrapped in `dir="ltr"` spans
- [ ] Mixed content has proper `dir` attributes

## Testing Tools
- **Automated**: axe DevTools, Lighthouse, WAVE, Pa11y
- **Screen readers**: NVDA (free, Windows), JAWS (Windows), VoiceOver (Mac/iOS)
- **Manual**: Keyboard navigation in RTL mode, zoom 200%, high contrast
