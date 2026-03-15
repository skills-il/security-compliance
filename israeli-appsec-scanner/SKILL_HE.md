---
name: israeli-appsec-scanner
description: >-
  Security scanning guidance for Israeli web applications covering OWASP Top 10,
  Israeli Privacy Protection Authority (PPA) compliance, dependency vulnerability
  scanning, secrets detection, and secure coding patterns for Hebrew/RTL apps.
  Use when user asks to "scan for vulnerabilities", "check security compliance",
  "audit Israeli app security", "bodek aviskhut" (Hebrew transliteration), or
  needs help with PPA compliance, secrets detection, or Hebrew input sanitization.
  Provides actionable checklists, automated scanning scripts, and Israeli-specific
  security guidance. Do NOT use for network penetration testing, physical security
  audits, or non-application-layer security concerns.
license: MIT
allowed-tools: 'Bash(python:*)'
compatibility: 'No special requirements. Works with Claude Code, Cursor, Windsurf.'
metadata:
  author: skills-il
  version: 1.0.0
  category: security-compliance
  tags:
    he:
      - אבטחת מידע
      - סריקת פגיעויות
      - OWASP
      - פרטיות
      - הגנת סייבר
      - ישראל
    en:
      - application-security
      - vulnerability-scanning
      - OWASP
      - privacy
      - cybersecurity
      - israel
  display_name:
    he: "סורק אבטחת אפליקציות ישראלי"
    en: Israeli AppSec Scanner
  display_description:
    he: "סריקת אבטחה לאפליקציות ישראליות. בדיקות OWASP Top 10, עמידה בדרישות רשות הגנת הפרטיות, סריקת תלויות, זיהוי סודות, ודפוסי קוד מאובטח לאפליקציות בעברית/RTL."
    en: >-
      Security scanning guidance for Israeli web applications covering OWASP Top 10,
      Israeli Privacy Protection Authority (PPA) compliance, dependency vulnerability
      scanning, secrets detection, and secure coding patterns for Hebrew/RTL apps.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
---

# סורק אבטחת אפליקציות ישראלי

כלי סריקה ובדיקות אבטחה שמותאם לאפליקציות ווב ישראליות. הסקיל מכסה את כל הספקטרום, מבדיקות OWASP Top 10 ועד עמידה בדרישות רשות הגנת הפרטיות, עם דגש מיוחד על וקטורי תקיפה שקשורים לעברית ו-RTL.

## רשימת בדיקות OWASP Top 10 (בהקשר ישראלי)

עברו על כל קטגוריה בשיטתיות. לכל ממצא, סמנו רמת חומרה (קריטי/גבוה/בינוני/נמוך) ותנו המלצת תיקון.

### A01: בעיות בבקרת גישה

- [ ] וודאו שכל נקודות ה-API דורשות אימות (בדקו middleware של Next.js, guards של NestJS)
- [ ] ודאו שבקרת גישה מבוססת תפקידים מכסה admin, user ואנונימי
- [ ] בדקו שנתיבי URL בעברית לא יכולים לעקוף הרשאות מבוססות ניתוב
- [ ] חפשו IDOR על משאבים שגלויים למשתמשים
- [ ] ודאו שהגדרות CORS מגבילות את ה-origins לדומיינים הישראליים הצפויים
- [ ] וודאו שטוקני JWT נבדקים בצד השרת, לא רק בצד הלקוח
- [ ] בדקו directory traversal עם קטעי נתיב מקודדים בעברית (%D7%90 וכו')

### A02: כשלים קריפטוגרפיים

- [ ] ודאו TLS 1.2+ על כל החיבורים (ספקי אחסון ישראליים לפעמים משתמשים בגרסאות ישנות כברירת מחדל)
- [ ] בדקו שסיסמאות מוצפנות עם bcrypt/argon2 (לא MD5/SHA1)
- [ ] ודאו שמספרי תעודת זהות מוצפנים ב-rest
- [ ] ודאו שנתוני כרטיסי אשראי לא נשמרים מקומית (דרישת PCI DSS)
- [ ] בדקו שמפתחות service role של Supabase לא חשופים ללקוח
- [ ] ודאו שטוקנים של שערי תשלום ישראליים (קארדקום, טרנזילה) מאוחסנים בצורה מאובטחת

### A03: הזרקות (Injection)

- [ ] בדקו SQL injection עם טקסט בעברית (`'; DROP TABLE --` עם תווים בעברית)
- [ ] ודאו שימוש ב-parameterized queries לכל פעולות מסד הנתונים עם טקסט עברי
- [ ] בדקו NoSQL injection בשאילתות MongoDB (נפוץ בסטארטאפים ישראליים שמשתמשים ב-MEAN stack)
- [ ] בדקו command injection דרך שמות קבצים שמכילים תווים בעברית
- [ ] ודאו הגנה מפני LDAP injection אם יש אינטגרציה עם ספריות ארגוניות ישראליות
- [ ] בדקו template injection בתבניות אימייל עם תוכן בעברית

### A04: תכנון לא מאובטח

- [ ] ודאו rate limiting על נקודות קצה של שערי SMS ישראליים (מניעת הצפה ב-OTP)
- [ ] חפשו פגמים בלוגיקה העסקית בתהליכי תשלום ישראליים
- [ ] ודאו שטפסים מרובי שלבים (נפוצים באינטגרציות עם שירותי ממשלה) שומרים state בצורה מאובטחת
- [ ] ודאו שמגבלות אורך קלט בעברית מתחשבות בתווי UTF-8 מרובי בתים

### A05: תצורה לא מאובטחת

- [ ] בדקו כותרות HTTP של אבטחה (CSP, X-Frame-Options, HSTS)
- [ ] ודאו שדפי שגיאה לא חושפים stack traces או הודעות דיבאג בעברית
- [ ] ודאו שסיסמאות ברירת מחדל הוחלפו בכל השירותים
- [ ] בדקו שקבוצות אבטחה של ספקי ענן ישראליים (AWS IL region, GCP) מוגדרות כראוי
- [ ] ודאו שמדיניות RLS של Supabase מופעלת על כל הטבלאות
- [ ] ודאו שקבצי `.env` עם credentials של שירותים ישראליים נמצאים ב-`.gitignore`

### A06: רכיבים פגיעים ומיושנים

- [ ] הריצו `npm audit` או `pnpm audit` וטפלו בממצאים קריטיים/גבוהים
- [ ] חפשו פגיעויות ידועות בספריות ספציפיות לעברית (hebrew-date, מעבדי טקסט דו-כיווני)
- [ ] ודאו שתמונות בסיס של קונטיינרים מעודכנות (השתמשו ב-`trivy image`)
- [ ] בדקו גרסאות מיושנות של SDK של שערי תשלום ישראליים

### A07: כשלי זיהוי ואימות

- [ ] ודאו ולידציה של פורמט מספר טלפון ישראלי (+972) בתהליכי אימות
- [ ] בדקו שקודי OTP למספרים ישראליים פגים אחרי 5 דקות לכל היותר
- [ ] בדקו שמדיניות סיסמאות תומכת בתווים בעברית
- [ ] ודאו ניהול סשנים תקין אחרי אימות עם ספקי OAuth ישראליים
- [ ] בדקו הגנה מפני credential stuffing על נקודות קצה של התחברות

### A08: כשלי שלמות תוכנה ונתונים

- [ ] ודאו שלמות חבילות npm עם ולידציית lockfile
- [ ] בדקו אבטחת pipeline של CI/CD (GitHub Actions, Vercel deployment hooks)
- [ ] ודאו שוובהוקים של שירותים ישראליים צד שלישי מאומתים (ולידציית חתימה)
- [ ] ודאו Subresource Integrity (SRI) לסקריפטים חיצוניים

### A09: כשלי לוגים וניטור

- [ ] ודאו שאירועי אימות נרשמים (התחברות, התנתקות, ניסיונות כושלים)
- [ ] בדקו שלוגים קולטים טקסט בעברית נכון (קידוד UTF-8)
- [ ] ודאו שנתיבי ביקורת שנדרשים על ידי רשות הגנת הפרטיות מתוחזקים לגישה למידע אישי
- [ ] ודאו שאחסון לוגים עומד בדרישות שמירת מידע של החוק הישראלי

### A10: זיוף בקשות בצד השרת (SSRF)

- [ ] ודאו ולידציית URL עבור כתובות שהמשתמש מספק (חסימת טווחי רשת פנימיים)
- [ ] בדקו שאינטגרציות עם ממשקי API ממשלתיים ישראליים מוודאים URL-ים של הפניות
- [ ] בדקו SSRF דרך URL-ים מקודדים בעברית ותקיפות IDN homograph

## עמידה בדרישות רשות הגנת הפרטיות

חוק הגנת הפרטיות (1981) והתקנות שלו מטילים דרישות ספציפיות על אפליקציות שמטפלות במידע אישי של תושבי ישראל.

### רישום מאגרי מידע

על פי החוק הישראלי, מאגרי מידע מסוימים שמכילים מידע אישי חייבים להירשם ברשות:

1. **בדקו חובת רישום**: מאגרים עם 10,000+ רשומות, או שמכילים מידע רגיש (רפואי, פיננסי, ביומטרי), או שמשמשים לדיוור ישיר, חייבים רישום
2. **שדות רישום**: שם המאגר, מטרה, קטגוריות מידע, אמצעי אבטחה, מעבדי מידע, העברות חוצות גבולות
3. **חידוש שנתי**: הרישום חייב להתחדש מדי שנה
4. **פטורים**: מאגרים שמשמשים אך ורק לניהול יחסי עובד-מעביד (בתנאים מסוימים)

### דרישות הגנת מידע

```
רשימת בדיקות: עמידה בחוק הגנת הפרטיות

[ ] הסכמה: קבלו הסכמה מדעת לפני איסוף מידע אישי
    - ההסכמה חייבת להיות ספציפית, מושכלת וחופשית
    - טקסט ההסכמה בעברית חייב להיות ברור ומובן
    - הסכמה נפרדת למטרות עיבוד שונות

[ ] הגבלת מטרה: שימוש במידע רק למטרה המוצהרת
    - תעדו את המטרה במדיניות הפרטיות (עברית + אנגלית)
    - אל תשנו ייעוד מידע ללא הסכמה מחודשת

[ ] מזעור מידע: אספו רק מידע הכרחי
    - בדקו כל שדה בטופס מבחינת הכרחיות
    - מספרי תעודת זהות יש לאסוף רק כשיש חובה חוקית

[ ] אמצעי אבטחה: יישמו אמצעים טכניים מתאימים
    - עקבו אחרי "תקנות אבטחת מידע" (2017) של הרשות
    - בצעו הערכות אבטחה שנתיות
    - שמרו לוגים של גישות למשך 24 חודשים לפחות

[ ] זכויות נושאי מידע: תמכו בבקשות גישה, תיקון ומחיקה
    - הגיבו תוך 30 יום לבקשות גישה למידע
    - ספקו מידע בפורמט מובנה וקריא מכונה
    - תמיכה בעברית לכל התקשורת עם נושאי מידע

[ ] הודעה על אירוע אבטחה: הודיעו לרשות ולנפגעים
    - "אירוע אבטחה חמור" חייב דיווח לרשות
    - ההודעה צריכה להיות בעברית לתושבי ישראל
    - תעדו את כל האירועים ושלבי התיקון
```

### העברת מידע חוצת גבולות

החוק הישראלי מגביל העברת מידע אישי מחוץ לישראל. ההעברה מותרת כאשר:

- למדינת היעד רמת הגנה נאותה (מדינות האיחוד האירופי, מוכרות על ידי הרשות)
- נושא המידע הסכים להעברה
- ההעברה דרושה לקיום חוזה
- קיימים ערובות חוזיות מתאימות (סעיפים חוזיים סטנדרטיים)

**תרחישים נפוצים באפליקציות ישראליות:**
- אחסון בענן ב-AWS/GCP: ודאו שיש הסכם עיבוד מידע
- שימוש בכלי SaaS אמריקאיים: ודאו ערובות חוזיות
- שירותי אנליטיקה: שקלו אנונימיזציה של מידע לפני ההעברה

## סריקת תלויות

### npm/pnpm audit

```bash
# הרצת סריקת פגיעויות
pnpm audit

# תיקון אוטומטי היכן שאפשר
pnpm audit --fix

# יצירת דוח JSON מפורט
pnpm audit --json > audit-report.json

# בדיקה לפי רמת חומרה
pnpm audit --audit-level=high
```

### סריקת קונטיינרים עם Trivy

```bash
# סריקת תמונת Docker
trivy image your-app:latest

# סריקה עם סינון חומרה
trivy image --severity HIGH,CRITICAL your-app:latest

# סריקת מערכת קבצים (לפרויקטים מקומיים)
trivy fs --security-checks vuln,secret,config .
```

### סריקת תלויות Python

```bash
# שימוש ב-pip-audit
pip-audit

# עם הצעות תיקון
pip-audit --fix --dry-run

# סריקת קובץ requirements
pip-audit -r requirements.txt
```

## זיהוי סודות

### סריקת credentials של שירותים ישראליים

אפליקציות ישראליות משתמשות בדרך כלל ב-credentials של שירותים שלעולם לא צריכים להיכנס ל-version control:

**שערי תשלום ישראליים:**
- קארדקום: מספרי מסוף, שמות משתמש API, קודי פעולה
- טרנזילה: קודי ספק, סיסמאות מסוף
- PayMe: מזהי מוכר, מפתחות API
- משולם: קודי עמוד, מפתחות API

**שירותים ישראליים:**
- מפתחות API של דואר ישראל
- credentials של ממשקי API בנקאיים (פועלים, לאומי, דיסקונט, מזרחי)
- טוקנים של Gov.il API
- מפתחות API של שערי SMS ישראליים (019, Cellact, InforUMobile)

### שימוש ב-TruffleHog

```bash
# סריקת היסטוריית git
trufflehog git file://. --only-verified

# סריקת ענף ספציפי
trufflehog git file://. --branch main --only-verified

# סריקה עם פלט JSON
trufflehog git file://. --json > secrets-report.json
```

### שימוש ב-Gitleaks

```bash
# סריקת מאגר
gitleaks detect --source . --verbose

# סריקה עם קונפיגורציה מותאמת לשירותים ישראליים
gitleaks detect --source . --config .gitleaks.toml

# יצירת דוח
gitleaks detect --source . --report-format json --report-path gitleaks-report.json
```

## אבטחה ספציפית לעברית/RTL

### תקיפות טקסט דו-כיווני (Trojan Source)

תווי בקרה דו-כיווניים יכולים לגרום לקוד להיראות שונה ממה שהוא באמת עושה. זה רלוונטי במיוחד בבסיסי קוד מעורבים עברית/אנגלית.

**תווים מסוכנים לזהות:**
- U+202A (Left-to-Right Embedding)
- U+202B (Right-to-Left Embedding)
- U+202E (Right-to-Left Override)
- U+2066 עד U+2069 (Isolate characters)

**מניעה:** הריצו את סקריפט הזיהוי שנמצא ב-`scripts/security-audit-checklist.py` כדי לסרוק קבצי קוד לתווים דו-כיווניים חבויים.

### תקיפות הומוגליף בעברית

תווים עבריים מסוימים דומים ויזואלית לתווים לטיניים, מה שמאפשר פישינג וזיוף:

| עברית | דומה ללטינית | Unicode |
|-------|-------------|---------|
| ס (סמך) | o | U+05E1 |
| ו (וו) | l, 1 | U+05D5 |
| ח (חת) | n | U+05D7 |
| ן (נון סופית) | l | U+05DF |

**מניעה:** נרמלו ובדקו תקינות של כל ה-URL-ים והמזהים שגלויים למשתמשים. דחו מחרוזות מעורבות כתב בהקשרים רגישים מבחינת אבטחה.

### ולידציית קלט בעברית

```javascript
// ולידציה לקלט בעברית בלבד
const HEBREW_PATTERN = /^[\u0590-\u05FF\s\-'".,:;!?()]+$/;

// ולידציה לקלט מעורב עברית/אנגלית
const MIXED_PATTERN = /^[\u0590-\u05FFa-zA-Z0-9\s\-'".,:;!?()@#$%&*]+$/;

// ולידציית מספר טלפון ישראלי
const IL_PHONE_PATTERN = /^(\+972|0)(5[0-9]|7[2-9])\d{7}$/;

// ולידציית מספר תעודת זהות עם ספרת ביקורת
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

## דפוסי קוד מאובטח

### שאילתות עם פרמטרים לטקסט עברי

```typescript
// נכון: שאילתה עם פרמטרים (מאובטח)
const { data, error } = await supabase
  .from('skills')
  .select('*')
  .ilike('name_he', `%${searchTerm}%`);

// לא נכון: שרשור מחרוזות (פגיע ל-SQL injection)
// const query = `SELECT * FROM skills WHERE name_he LIKE '%${searchTerm}%'`;
```

### הגנת CSRF לטפסי תשלום ישראליים

```typescript
import { randomBytes } from 'crypto';

function generateCsrfToken(): string {
  return randomBytes(32).toString('hex');
}

function validateCsrfToken(session: string, submitted: string): boolean {
  return session === submitted && session.length === 64;
}
```

### הגבלת קצב לשערי SMS ישראליים

```typescript
// הגבלת בקשות OTP למניעת ניצול לרעה
// SMS ישראלי עולה בערך 0.05-0.15 שקלים להודעה
const OTP_LIMITS = {
  perPhone: { max: 3, windowMs: 15 * 60 * 1000 },    // 3 ב-15 דקות לטלפון
  perIp: { max: 10, windowMs: 60 * 60 * 1000 },       // 10 בשעה ל-IP
  global: { max: 1000, windowMs: 60 * 60 * 1000 },    // 1000 בשעה גלובלי
};
```

## רשימת בדיקות ציות

### חוק הגנת הפרטיות הישראלי

| דרישה | חוק ישראלי | מקבילה ב-GDPR | סטטוס |
|-------|-----------|---------------|-------|
| בסיס חוקי לעיבוד | סעיף 1, חה"פ | סעיף 6 GDPR | [ ] |
| דרישות הסכמה | סעיף 11, חה"פ | סעיף 7 GDPR | [ ] |
| זכות גישה | סעיף 13, חה"פ | סעיף 15 GDPR | [ ] |
| זכות תיקון | סעיף 14, חה"פ | סעיף 16 GDPR | [ ] |
| זכות מחיקה | סעיף 14א, חה"פ | סעיף 17 GDPR | [ ] |
| אמצעי אבטחה | תקנות 2017 | סעיף 32 GDPR | [ ] |
| הודעה על אירוע | תקנה 11א | סעיפים 33-34 GDPR | [ ] |
| העברה חוצת גבולות | סעיף 36, חה"פ | סעיפים 44-49 GDPR | [ ] |
| רישום מאגר | סעיף 8, חה"פ | סעיף 30 GDPR (ROPA) | [ ] |

### PCI DSS לעיבוד תשלומים ישראלי

אם האפליקציה שלכם מעבדת כרטיסי אשראי ישראליים (ישראכרט, לאומי קארד, כאל):

1. **קביעת רמה**: על בסיס נפח עסקאות שנתי
2. **בחירת SAQ**: רוב האפליקציות הישראליות מתאימות ל-SAQ A או SAQ A-EP
3. **ספציפי לישראל**:
   - לשב"א (מערכת הסליקה הישראלית) יש דרישות אבטחה משלה
   - מספרי כרטיסי אשראי ישראליים עוקבים אחרי אלגוריתם Luhn הסטנדרטי
   - הוראת קבע דורשת תיעוד הסכמה נוסף

## הרצת ביקורת האבטחה

השתמשו בסקריפטים המצורפים לבדיקות אוטומטיות:

```bash
# הרצת רשימת בדיקות אבטחה מלאה
python scripts/security-audit-checklist.py --project-dir /path/to/project

# סריקה לאיתור credentials של שירותים ישראליים
bash scripts/secrets-scanner.sh /path/to/project

# יצירת דוח ציות
python scripts/security-audit-checklist.py --project-dir /path/to/project --format json > report.json
```

עיינו בתיקיית `references/` למידע מפורט על חוק הגנת הפרטיות ושיקולי OWASP לאפליקציות עברית/RTL.
