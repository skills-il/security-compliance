---
name: israeli-privacy-shield
description: Israeli Privacy Protection Law compliance guidance including Amendment 13 (effective August 14, 2025), database registration, consent requirements, data security, cross-border transfers, breach notification, privacy protection officer appointment, and AI governance. Use when user asks about Israeli privacy law, "haganat pratiut", "tikun 13", data protection in Israel, GDPR compliance for Israeli companies, privacy policy requirements, or database registration. Covers the Privacy Protection Law 1981, Amendment 13, and 2017 Security Regulations. Do NOT use for EU GDPR-only questions without Israeli context.
license: MIT
compatibility: No network required. Works with Claude Code, Claude.ai, Cursor.
---

# Israeli Privacy Shield

## Critical Note
This skill provides compliance GUIDANCE. It does not replace legal counsel.
Recommend consulting a privacy attorney (orech din specializing in prati'ut)
for specific compliance decisions.

## Instructions

### Step 1: Assess Security Level
The 2017 regulations define three security levels:

| Level | Criteria | Key Requirements |
|-------|----------|-----------------|
| Basic | < 10,000 records, non-sensitive | Access controls, logging, backup |
| Medium | 10,000+ records OR sensitive data | + Encryption, security officer appointment |
| High | Government, health, financial, 100K+ records, or authorized access for 100+ people | + Incident response plan, DPO, plus a security risk assessment and a penetration test at least once every 18 months with documented findings and remediation |

Sensitive data includes: Health, genetics, sexual orientation, political views, criminal record.

### Step 2: Database Registration Check
Under the Amendment 13 regime, registration with the Privacy Protection Authority (PPA) is required only if:
- Database owned or managed by a public body, OR
- Database contains data on 10,000+ individuals AND the primary purpose is collecting and disclosing personal data to third parties as a business or for value (data brokers)

The broad pre-Amendment requirement covering any database with sensitive data (and the old "Form 1" five-trigger list) no longer applies.

**Notification tier (separate from registration).** Even where registration is not required, a controller holding especially-sensitive data on more than 100,000 individuals must notify the PPA within 30 days, including the controller's and privacy officer's details and the database definition document.

Registration and notification are handled through the PPA: https://www.gov.il/en/departments/the_privacy_protection_authority

### Step 3: Consent Requirements
Israeli law requires consent for:
- Collection of personal data
- Use beyond the original purpose
- Transfer to third parties
- Cross-border transfer

Consent must be: Informed, specific, freely given
Exceptions: Legal obligation, vital interests, public interest, legitimate interest (limited)

### Step 4: Cross-Border Transfer Rules
Personal data transfer outside Israel requires:
- Recipient country has adequate protection (EU, UK, few others), OR
- Contractual safeguards (similar to GDPR SCCs), OR
- Data subject consent (informed and specific), OR
- Listed exemptions (necessary for contract, legal proceedings, etc.)

Note: Israel has EU adequacy decision, transfer TO EU is generally straightforward.

### Step 5: Breach Notification
Israel requires IMMEDIATE notification of a Severe Security Incident under the 2017 Data Security Regulations (no fixed-hours deadline):
1. **Notify the Privacy Protection Authority immediately upon discovering a Severe Security Incident.** The Data Security Regulations (2017) require notification "immediately" (miyad), there is NO fixed 72-hour deadline in Israeli law. Cover what happened, the categories and rough number of affected individuals, the likely impact, and the steps taken. The PPA may then direct the controller to notify affected data subjects.
2. **Notify affected data subjects only if the PPA directs you to.** Under the Data Security Regulations that duty arises from a PPA direction after you report, NOT from the controller's own GDPR-style "high-risk" self-assessment. If directed, the notice must be in clear, plain Hebrew covering the breach, the data affected, the consequences, and protective steps.
3. **Severe Security Incident standard:** an incident (unauthorized access, disclosure, loss, alteration, or destruction of personal data) that poses a risk to the rights of the affected individuals.
4. **Document:** all incidents, response actions, and decisions, regardless of whether they cross the reporting threshold.

### Step 6: Compliance Checklist
For each assessed entity, verify:
- [ ] Database registration (if required)
- [ ] Privacy policy published (Hebrew, accessible)
- [ ] Consent mechanisms in place
- [ ] Security measures per level (basic/medium/high)
- [ ] Data processing agreements with processors
- [ ] Cross-border transfer safeguards
- [ ] Breach response plan with notification template
- [ ] Data subject request workflow (Section 13 access, Section 14 correction, 30-day response)
- [ ] DPIA process for high-risk processing (large-scale sensitive data, systematic monitoring, AI decisions)
- [ ] Minors' data policy (parental consent under Capacity and Guardianship Law, ed-tech safeguards)
- [ ] Employee training
- [ ] Privacy Protection Officer appointed (if required under Amendment 13)
- [ ] AI governance policy for automated decision-making (if applicable)
- [ ] Personal data inventory includes IP addresses, geolocation, and online identifiers

### Step 7: Amendment 13 (Effective August 14, 2025)

Amendment 13 is the most significant reform of Israeli privacy law since 1981. It took effect on August 14, 2025 and expands the Privacy Protection Authority's enforcement powers, broadens the definition of personal data, and introduces new obligations for data brokers and AI systems.

**Expanded definition of personal data.** Amendment 13 explicitly includes digital identifiers:
- IP addresses
- Geolocation data
- Device identifiers and online identifiers
- Biometric and genetic data (already sensitive)

Standard web analytics, session logs, and mobile app telemetry now fall within the scope of the Privacy Protection Law.

**Mandatory Privacy Protection Officer (PPO / DPO).** Under Amendment 13, the following entities must appoint a Privacy Protection Officer:
- Public bodies (government ministries, municipalities, universities, HMOs and similar), except national-security entities
- External suppliers and processors acting for those public bodies
- Data brokers, with a concrete threshold: a controller whose database holds personal data on more than 10,000 individuals AND whose main purpose is collecting personal data to disclose it to third parties as a business or for value (including direct-mailing services)
- Entities that systematically monitor individuals on a large scale, or whose core business includes processing especially-sensitive data on a large scale

The PPO is the contact point with the Privacy Protection Authority and is responsible for monitoring compliance. Note: the PPA announced it would not enforce the appointment obligation until October 31, 2025.

**AI governance for automated decision-making.** Amendment 13 requires transparency and oversight for AI systems that make decisions affecting individuals (credit scoring, hiring, insurance, fraud detection). Requirements include:
- Documentation of the decision logic and data inputs
- Ability to explain outcomes to affected individuals
- Human oversight for high-impact decisions
- Bias and accuracy monitoring

**Enforcement powers and fines.** Amendment 13 significantly expands the Authority's administrative powers:
- Direct supervisory inspections without prior notice
- Per-violation fines from NIS 1,000 up to NIS 320,000, doubled to NIS 640,000 in severe cases
- Aggregate fines up to approximately NIS 3.2 million for serious violations, capped at 5% of the controller's annual turnover for the most serious cases (a separate, lower annual ceiling applies to small/micro businesses)
- For large-scale databases, a per-data-subject component of up to NIS 100 per affected individual
- A private civil right of action (Section 29A): statutory damages up to NIS 50,000 per person without proof of harm, or up to NIS 100,000 only if the violation was intended to harm, separate from the administrative fine.
- Ability to issue binding compliance orders


**Recent enforcement.** Among the early Amendment-13 actions, the PPA fined an individual (a former National Insurance Institute employee) NIS 75,000 for unauthorized retrieval of sensitive data from Bituach Leumi databases. Enforcement is live.

**What changed for database registration.** Amendment 13 narrowed registration to public bodies and to data brokers (databases of 10,000+ individuals whose primary purpose is selling/disclosing personal data to third parties). The broad pre-Amendment "any sensitive database" rule no longer applies. The separate 100,000-record especially-sensitive notification tier (file with the Authority within 30 days) is described above.

### Step 8: Data Subject Rights (DSR) Workflow

The Privacy Protection Law grants individuals enforceable rights. A controller must have a documented workflow so requests do not slip past the statutory deadline (which is short and judicially enforceable).

**Rights granted by the PPL:**

| Right | Statute | Practical form |
|-------|---------|----------------|
| Inspection (access) | Section 13 | Receive a copy of personal data held in the database, in Hebrew, English, or Arabic |
| Correction | Section 14 | Request correction or deletion of inaccurate, incomplete, unclear, or out-of-date data |
| Removal from direct-mail database | Section 17F | Demand removal; controller must comply and confirm |
| Withdrawal of consent | Section 8C (Amendment 13) | Must be as easy as granting consent |

**Response timeline.** Under the Privacy Protection Regulations, controllers must respond to inspection and correction requests **within 30 days**. If the controller fails to respond within 30 days, the data subject may appeal to a Magistrate's Court (this is the fastest enforcement path open to individuals, faster than waiting for PPA enforcement).

**Workflow template:**
1. **Intake channel** that is published in the privacy policy (email to the DPO, in-app form, or postal address). The PPO is the named contact when one is required under Amendment 13.
2. **Identity verification** proportionate to the sensitivity (do not over-collect to verify; a national-ID copy is excessive for a basic profile-data request).
3. **Log the request** with timestamp on receipt. The 30-day clock starts from receipt, not from when the team gets around to it.
4. **Triage by right type:** access vs correction vs direct-mail removal vs withdrawal. Each has a different operational path.
5. **Response template in Hebrew, English, or Arabic** as the user chose. Refusals must be reasoned and cite the legal basis.
6. **Document the response** in the request log. This is your evidence of compliance.

**Refusal grounds (narrow):** refuse inspection only on specific statutory grounds (unjustified trade-secret disclosure, prejudice to an active investigation). Default to disclosure when in doubt.

### Step 9: Data Protection Impact Assessment (DPIA)

A DPIA is a structured pre-processing assessment that documents privacy risks, alternatives considered, and mitigations. The PPL does not contain a GDPR-Article-35-style explicit DPIA mandate, but the PPA's published guidance on AI systems treats DPIA as the recommended best practice for demonstrating compliance. Where a Privacy Protection Officer is appointed under Amendment 13, the PPO is the natural owner of the DPIA process as part of monitoring overall compliance.

**When to conduct a DPIA (PPA AI Guidelines + Amendment 13 framing):**
- Before deploying AI systems that process data on a wide scale
- Before deploying AI systems that include sensitive data
- Before deploying processing that poses high risk to data subjects' rights
- Before large-scale systematic monitoring of individuals (CCTV at scale, location tracking, behavioral profiling)
- Before automated decisions affecting individuals (credit, hiring, insurance, fraud detection)

**DPIA contents:**
1. Description of the processing: purpose, data categories, data sources, retention, recipients
2. Necessity and proportionality: is each category necessary for the stated purpose?
3. Risks to data subjects: probability + severity, including bias and discrimination for AI systems
4. Mitigations: technical (encryption, access controls, minimization) and organizational (training, audit)
5. Residual risk: what remains after mitigations and whether it is acceptable
6. Consultation: with the PPO and, for high residual risk, optional prior consultation with the PPA
7. Sign-off and review cycle (annual or on material change)

Keep DPIAs in the documentation evidence pack. The PPA's unannounced inspection powers under Amendment 13 mean an undocumented DPIA is functionally a missing DPIA.

### Step 10: Minors' and Children's Data

The Privacy Protection Law does not have a dedicated minors' provision, but other statutes and PPA guidance create heightened obligations whenever a controller processes data on individuals under 18.

**Consent rules:**
- The Legal Capacity and Guardianship Law, 1962 provides that legal acts of a minor (under 18) may be cancelled if performed without parental or guardian consent. Privacy consent obtained from a minor is therefore exposed to retroactive invalidation. Default rule: **obtain parental consent for processing personal data of users under 18**, especially for marketing, analytics, and behavioral profiling.
- Age verification mechanism matters: a simple "I am 18" checkbox is not a defensible consent record for a children-targeted service.

**Biometric data:**
- Under the Inclusion of Biometric Means of Identification in Identity Documents and in an Information Database Law, 5770-2009 (the biometric ID-card framework), fingerprints are not collected from applicants under age 12; only facial photographing is performed. Other biometric processing involving minors is subject to heightened restrictions and typically requires both parental and minor consent (for ages where the minor can understand).

**Ed-tech and school services:**
- The PPA treats schools and ed-tech vendors as high-scrutiny processors. The PPA's January 2020 audit of educational websites and applications for minors found defects in 23 of 24 audited entities. The takeaway: ed-tech is on the enforcement priority list, and "everybody does it this way" is not a defense.

**Practical controls for products with minor users:**
- Tag minor accounts/profiles in the data inventory.
- Disable behavioral advertising and cross-site tracking for minor profiles by default.
- Log parental-consent evidence (timestamp, IP, method).
- When schools are the controller, the school obtains parental consent; the vendor supports that flow.
- Offer a parental access/deletion channel and respond within the same 30-day DSR window.

## GDPR vs Israeli Law Key Differences
| Aspect | Israeli Law (post Amendment 13) | GDPR |
|--------|------------|------|
| Legal basis | Consent primary, limited exceptions | 6 legal bases |
| Privacy officer requirement | Public bodies (and their processors), data brokers (10,000+ records), large-scale sensitive-data processors, and large-scale systematic monitors | Broader requirement |
| Breach notification | Immediately to the PPA on a Severe Security Incident (no fixed hours); data subjects as the PPA directs | 72 hours |
| Administrative fines | Up to ~NIS 3.2M for serious violations + criminal liability | Up to 4% global revenue |
| Right to erasure | Limited | Comprehensive (right to be forgotten) |
| Database registration | Public bodies and data brokers only (10,000+ records) | Not required (replaced by ROPA) |
| Personal data scope | Includes IP, geolocation, online identifiers (Amendment 13) | Includes online identifiers |
| AI governance | Required for automated decision-making (Amendment 13) | Article 22 automated decision-making rules |
| Extra-territorial scope | Limited | Broad |

## Examples

### Example 1: SaaS Startup Compliance
User says: "I'm building a SaaS with Israeli customers, what privacy requirements apply?"
Result: Assessment of security level, database registration need, privacy policy requirements, recommended consent mechanisms.

### Example 2: Data Breach Response
User says: "We discovered a data breach affecting Israeli users"
Result: Step-by-step breach response: contain, assess, notify authority, notify users if significant harm, document.

### Example 3: Cross-Border Data Transfer
User says: "We need to transfer Israeli customer data to our US servers"
Actions:
1. Assess data types for sensitivity level
2. Check if destination country has adequate protection
3. Determine transfer mechanism (adequacy, consent, contractual clauses)
4. Document compliance steps
Result: Transfer compliance checklist with specific steps for US data transfer under Israeli Privacy Protection Law.

## Bundled Resources

### Scripts
- `scripts/compliance_checker.py`, Runs a full Privacy Protection Law compliance assessment: determines security level (basic/medium/high), checks database registration requirements, and generates a compliance checklist with all applicable controls. Run: `python scripts/compliance_checker.py --help`

### References
- `references/privacy-law-requirements.md`, Detailed breakdown of the Privacy Protection Law 1981 and 2017 Security Regulations including database registration process, security level requirements, consent rules, cross-border transfer rules, breach notification procedures, and penalties. Consult when you need specific legal requirements, section numbers, or GDPR comparison details beyond what the instructions cover.
- `references/consent-banner-implementation.md`, Copy-pasteable TypeScript/React code for an Amendment 13 + GDPR compliant consent banner: pub-sub store with SSR sentinel, localStorage + companion cookie (12-month TTL, `CONSENT_VERSION`-bumped re-prompt), cross-tab sync via `storage` event, server-side cookie check for SSR gating, Sentry pre-init hydration pattern and mid-session Replay attach, essential-event allowlist, dismissal-as-refusal handling. Consult when the user wants to ship the consent UI itself, not just understand the law.

## Implementing a Compliant Consent Surface

The Privacy Protection Law after Amendment 13, GDPR for EU visitors, and the 2017 Security Regulations all require **explicit, opt-in, granular consent** before collecting personal data beyond what is strictly necessary to deliver the service. The consent surface is where that requirement becomes code. A banner copy-pasted from a generic template almost always fails one of the legal tests below. This section covers the UI patterns that satisfy all three legal frames at once.

### State Model

Model consent as three layers:

1. **Essential** (always on, never toggled): session auth, CSRF, consent cookie itself, bot protection (Turnstile), accessibility preferences, anything required to deliver the requested service. The user has no choice here, by design.
2. **Optional categories** (explicit opt-in): analytics, session replay (Clarity / Hotjar / FullStory), error monitoring with user data (Sentry Session Replay), marketing, personalization.
3. **No consent yet** (first visit): distinct from "rejected all" and from "accepted all". Treat as null.

The persisted state is a tagged version + category map + timestamp:

```ts
interface ConsentState {
  version: number;          // bump to force re-prompt when adding a category
  categories: {
    analytics: boolean;
    session_replay: boolean;
    error_monitoring: boolean;
    // add categories as needed; each gets its own opt-in
  };
  timestamp: string;        // ISO; used for 12-month re-prompt
}
```

### Persistence

Store the state in **both** `localStorage` and a companion cookie. `localStorage` is the source of truth for the client; the cookie exists so Server Components can gate SSR work (e.g. `incrementBundleViews` inside `after()`) without a client round-trip. The cookie only needs a single bit (`0` or `1`) because Server Components rarely distinguish individual categories.

```ts
// lib/consent/store.ts
export const CONSENT_VERSION = 1;
export const CONSENT_STORAGE_KEY = 'site_consent_v1';
export const CONSENT_COOKIE_NAME = 'site_consent';
export const CONSENT_REPROMPT_MS = 365 * 24 * 60 * 60 * 1000;

function writeCookie(state: ConsentState | null) {
  const maxAge = Math.floor(CONSENT_REPROMPT_MS / 1000);
  const secure = location.protocol === 'https:' ? '; Secure' : '';
  if (!state) {
    document.cookie = `${CONSENT_COOKIE_NAME}=; Path=/; Max-Age=0; SameSite=Lax${secure}`;
    return;
  }
  const value = state.categories.analytics ? '1' : '0';
  document.cookie = `${CONSENT_COOKIE_NAME}=${value}; Path=/; Max-Age=${maxAge}; SameSite=Lax${secure}`;
}
```

**Re-prompt rules.** `readStorage()` returns `null` if the stored `version` mismatches `CONSENT_VERSION` or the timestamp is older than 12 months. Bumping `CONSENT_VERSION` when adding a new tracker category forces a fresh prompt, this is how you stay compliant when you add a new analytics vendor.

### SSR Safety: The SSR_SENTINEL Pattern

Naive `useSyncExternalStore` with a `null` server snapshot renders the banner in the initial SSR HTML, which means a) the banner is visible for a moment before hydration replaces it, and b) search engines index pages with the consent dialog overlaying the content. The fix is a sentinel object that is identity-compared to distinguish the server/hydration render from "user hasn't decided yet":

```ts
export const SSR_SENTINEL: ConsentState = Object.freeze({
  version: -1,
  categories: ALL_CATEGORIES_OFF,
  timestamp: '1970-01-01T00:00:00.000Z',
});

// In the provider:
const rawState = useSyncExternalStore(
  consentStore.subscribe,
  consentStore.getSnapshot,
  consentStore.getServerSnapshot,  // returns SSR_SENTINEL
);
const isHydrated = rawState !== SSR_SENTINEL;
const state = isHydrated ? rawState : null;

const needsPrompt = isHydrated && state === null;
```

Only when `isHydrated` is true AND `state` is `null` does the banner render. The sentinel is identity-compared with `!==`, which is why it is frozen and exported as a module constant.

### Cross-Tab Sync

Users open multiple tabs. If they reject consent in one, the others must respect that immediately. Listen for the `storage` event, which fires across tabs sharing the same origin:

```ts
function onStorageEvent(e: StorageEvent) {
  if (e.key === null || e.key === CONSENT_STORAGE_KEY) notify();
}
// Attach in subscribe() when first listener is added, detach when last leaves.
```

### Dismissal-As-Refusal

GDPR Article 4(11) and the EDPB guidance require that dismissing a consent banner counts as refusal. Amendment 13 is aligned. That means:

- **Escape key** = reject all
- **Close button (X)** = reject all
- **Clicking outside the banner** = leave banner visible (do NOT treat as accept)

```tsx
// ESC handler inside the banner component
useEffect(() => {
  if (!promptOpen) return;
  function onKey(e: KeyboardEvent) {
    if (e.key === 'Escape') rejectAll();
  }
  window.addEventListener('keydown', onKey);
  return () => window.removeEventListener('keydown', onKey);
}, [promptOpen, rejectAll]);
```

### Visual Equal Weight for Reject and Accept

GDPR Recital 42 + multiple DPA enforcement decisions require that Reject and Accept carry equal visual weight. In practice:

- Same button style (both primary, or both outline)
- Same width
- Same position (side by side, not one hidden behind "Customize")
- "Customize" is a third action, not a replacement for "Reject"

```tsx
<div className="grid grid-cols-3 gap-2">
  <Button size="sm" variant="outline" onClick={rejectAll}>{dict.rejectAll}</Button>
  <Button size="sm" variant="outline" onClick={openPreferences}>{dict.customize}</Button>
  <Button size="sm" onClick={acceptAll}>{dict.acceptAll}</Button>
</div>
```

### Gating the Trackers

The consent state must actually prevent non-consented trackers from running. A banner that does not stop scripts is worse than no banner (it creates a paper trail of false compliance).

```tsx
// components/consent/consent-gated-trackers.tsx
export function ConsentGatedTrackers() {
  const { isAllowed } = useConsent();
  return (
    <>
      {isAllowed('analytics') && <Analytics />}
      {isAllowed('analytics') && <SpeedInsights />}
      {isAllowed('session_replay') && <ClarityScript />}
    </>
  );
}
```

Also gate the client-side `trackEvent` helper, events emitted before consent is granted should be dropped, not queued:

```ts
const ESSENTIAL_EVENTS = new Set([
  'consent_banner_shown', 'consent_accepted', 'consent_rejected',
  'consent_customized', 'consent_reopened', 'auth_sign_in',
]);

export function trackEvent(event: string, data?: Record<string, unknown>) {
  if (!ESSENTIAL_EVENTS.has(event) && !window.__consent?.analytics) return;
  // ...send to analytics backend
}
```

The essential-event allowlist is for legally transactional events (the consent choice itself, auth), not a general escape hatch.

### Sentry Integration: Two Pieces

Sentry is unusual because `Sentry.init()` runs in `instrumentation-client.ts` **before** React hydrates, which is before `useConsent()` can tell you what the user wants. Two pieces:

**1. Hydrate `window.__consent` from storage BEFORE `Sentry.init()`.** Without this, any errors thrown during early hydration are captured even if the user previously rejected consent.

```ts
// instrumentation-client.ts
import { hydrateWindowFromStorage } from '@/lib/consent/store';

hydrateWindowFromStorage();  // sets window.__consent from localStorage

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  integrations: window.__consent?.session_replay ? [Sentry.replayIntegration()] : [],
  beforeSend(event) {
    return window.__consent?.error_monitoring ? event : null;
  },
});
```

**2. Attach Replay mid-session when the user later grants consent.** Don't re-run `Sentry.init()`, that breaks the existing client. Use `Sentry.addIntegration()`:

```ts
// lib/consent/sentry-gate.ts
import * as Sentry from '@sentry/nextjs';

export function enableSentryReplay() {
  const client = Sentry.getClient();
  if (!client) return;
  if (client.getIntegrationByName?.('Replay')) return;  // idempotent
  Sentry.addIntegration(Sentry.replayIntegration());
}
```

The React provider calls `enableSentryReplay()` the first time `state.categories.session_replay` flips to true. Dynamic-import it so the Replay bundle is not shipped to users who rejected it:

```ts
useEffect(() => {
  if (state?.categories.session_replay) {
    import('./sentry-gate').then((m) => m.enableSentryReplay());
  }
}, [state?.categories.session_replay]);
```

### Server Component Gating

Server Components can read the companion cookie directly:

```ts
// lib/consent/server.ts
import { cookies } from 'next/headers';
import { CONSENT_COOKIE_NAME } from './store';

export async function isAnalyticsAllowedServerSide(): Promise<boolean> {
  const store = await cookies();
  return store.get(CONSENT_COOKIE_NAME)?.value === '1';
}
```

Use it to gate `after()` calls that increment analytics counters:

```tsx
if (await isAnalyticsAllowedServerSide()) {
  after(() => incrementBundleViews(slug));
}
```

### Audit Trail

Amendment 13 and GDPR require you to demonstrate consent on demand. Emit five analytics events through your existing pipeline:

- `consent_banner_shown` (first show only)
- `consent_accepted`
- `consent_rejected`
- `consent_customized`
- `consent_reopened` (user re-opens from the footer link)

Store them through the same `analytics_events` pipeline you already have, no new table needed. These are the events the allowlist in `trackEvent` lets through even when consent is denied, precisely so you have the refusal on record.

See `references/consent-banner-implementation.md` for complete copy-pasteable code covering the pub-sub store, the `ConsentProvider`, the banner, the preferences dialog, the tracker gate, and the Sentry hydration hook.

## Consent UI Anti-Patterns

Israeli DPA enforcement, GDPR DPAs, and the French CNIL have published repeated guidance on UI patterns that look compliant but are not. Any of these will cost you on enforcement even if the underlying law text is satisfied.

| Anti-pattern | Why it fails | Fix |
|-------------|--------------|-----|
| Pre-checked boxes for analytics / marketing | Consent must be explicit opt-in. CJEU *Planet49* (C-673/17) is the binding precedent. | Default unchecked; user must actively flip the switch. |
| "Accept" button styled larger/colored, "Reject" styled as a text link | Fails the equal-weight test. | Same component, same size, same visual prominence. |
| "Reject" hidden behind a "Customize" or "Learn more" submenu | Forces extra clicks to refuse, not to accept. | Reject + Accept on the first screen, side by side. |
| "By continuing to use the site, you accept cookies" banners | Implicit consent is invalid under GDPR and Amendment 13. | Banner blocks nothing visually, but trackers do not run until explicit choice. |
| Cookie wall ("You must accept cookies to read this article") | EDPB guidance treats conditioning service on consent to non-essential cookies as invalid. | Provide full service regardless of the choice; degrade only genuinely analytics-dependent features (e.g. hide a session-replay-powered debug button). |
| Single "Accept all" with no granular option on the first screen | GDPR Article 7(2) requires granularity for distinct purposes. | Either expose the per-category toggles on the first screen, or ensure "Customize" reaches them in one click. |
| Re-prompting every session | Consent fatigue, treated by DPAs as a dark pattern. | Re-prompt only on `CONSENT_VERSION` bump or after 12 months. |
| Burying the "withdraw consent" path | Amendment 13 Article 8C + GDPR Article 7(3) require withdrawal to be as easy as granting. | "Privacy preferences" link in the footer that opens the same dialog. |
| Storing a consent cookie without an expiry / with multi-year TTL | User has not re-consented; stale consent is no consent. | 12-month max. Bump `CONSENT_VERSION` whenever you add a tracker. |
| Loading the analytics SDK script and calling it with `consent=denied` instead of not loading it | Loading itself is a data transfer (IP, UA, referer). | Gate the `<script>` tag, not just the SDK's internal flag. |

The banner you ship is one layer. The other layers, a published privacy policy in Hebrew, a named Privacy Protection Officer where required under Amendment 13, a data subject request handling process, a breach response plan, and the database registration for public bodies and data brokers, all have to exist independently. No consent UI substitutes for those.

## Gotchas

- Amendment 13 took effect on August 14, 2025 and is live law, not a pending proposal. Agents trained on pre-2025 data may treat Amendment 13 as a future change or miss it entirely. Always assume it applies when advising on Israeli privacy compliance today.
- Amendment 13 expands "personal data" to include IP addresses, geolocation, and online identifiers. This pulls standard web analytics and mobile telemetry into scope. Agents may still apply the older narrower definition and underestimate what counts as personal data.
- Administrative fines under Amendment 13 can reach ~NIS 3.2 million (capped at 5% of annual turnover in the worst cases), plus Section 29A statutory damages up to NIS 50,000 without proof of harm (NIS 100,000 only with intent to harm) and criminal liability.
- Israel does NOT have a GDPR-style 72-hour breach deadline. Under the Data Security Regulations (2017, predating Amendment 13), a "Severe Security Incident" is reported to the PPA "immediately" (miyad) on discovery, and the PPA may direct notifying affected data subjects. Agents often wrongly import GDPR's 72-hour rule, do not.
- Israeli Privacy Protection Law predates GDPR (1981 vs 2016) and still has key differences even after Amendment 13: a narrower right to erasure, and database registration still exists (though narrowed to public bodies and data brokers, plus a separate 100,000-record especially-sensitive notification tier). Agents may incorrectly apply GDPR rules to Israeli contexts.
- Israel has an EU adequacy decision, meaning data transfers FROM Israel TO the EU are generally straightforward. Agents may incorrectly flag Israel-to-EU transfers as requiring additional safeguards.
- The 2017 Security Regulations define three security levels (basic/medium/high) based on record count and data sensitivity. Agents may apply a one-size-fits-all approach instead of the tiered model.
- Penalties under Israeli privacy law include criminal liability (up to 5 years imprisonment) in addition to administrative fines. Agents may understate the severity by comparing only to GDPR's monetary penalties.

## Troubleshooting

### Error: "Unsure about security level"
Cause: Borderline case between basic/medium/high
Solution: When in doubt, apply the higher level. The cost difference is small compared to non-compliance risk.

### Error: "Borderline DPO appointment threshold"
Cause: The 10,000-individual threshold for the data-broker DPO trigger is a count of distinct individuals in the database, but the legal text is silent on counting methodology (active vs historical accounts, deduplicated identities vs raw rows, multi-database aggregation).
Solution: Count distinct individuals across all linked databases under the same controller, including historical records you have not purged. When the count is near the threshold, appoint a DPO defensively; the cost of appointing is low compared to the cost of an enforcement finding that you were over-threshold and unrepresented. Document the counting methodology so a PPA inspector can audit it.

### Error: "Cross-border transfer to a country without an adequacy decision"
Cause: The destination country (US, India, Singapore, most non-EU jurisdictions) does not have PPA-recognized adequate protection, so the default ban on transfer applies.
Solution: Pick the strongest available alternative basis in this order: (1) controller-to-controller or controller-to-processor data transfer agreement with privacy obligations equivalent to Israeli law (Israeli equivalent of GDPR SCCs), (2) explicit informed consent of the data subject naming the destination country and the risks, (3) statutory exception (contract performance, legal proceedings, vital interests). Do NOT rely on "legitimate interest" alone for cross-border transfer; the PPA reads that exception narrowly. Document the basis in the data inventory.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| Privacy Protection Authority (gov.il) | https://www.gov.il/en/departments/the_privacy_protection_authority | Enforcement, database registration and notification, guidance |
| Amendment 13 page (gov.il) | https://www.gov.il/he/pages/13_amendment | Overview of the reform and its obligations |
| Amendment 13 professional guide (gov.il) | https://www.gov.il/he/pages/guide_tikon13_professional | Detailed implementation guidance for controllers and processors |
| Amendment 13 FAQ (gov.il) | https://www.gov.il/he/pages/tikun13_qa | Common questions on registration, DPO, breach reporting |
| Protection of Privacy Law, 5741-1981 | https://www.gov.il/he/pages/the_privacy_protection_law | Primary statute text |

gov.il pages may return HTTP 403 to automated clients; open them in a browser.

## Recommended MCP Servers

- `israel-law` MCP, surfaces Israeli primary legislation and regulations (including the Protection of Privacy Law and related regulations). Use it to pull the current statutory text when a compliance question turns on exact wording. Verify the live gov.il pages above for PPA guidance and forms, which an MCP statute index does not cover.