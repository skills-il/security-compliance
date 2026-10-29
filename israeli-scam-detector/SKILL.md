---
name: israeli-scam-detector
description: "Not a security guarantee. Check whether a suspicious Israeli SMS, email, link or phone call is a scam, and get the exact next steps, including after the money is already gone. Covers smishing and phishing impersonating Israeli banks, Bituach Leumi, Rashut HaMisim, Israel Post and gov.il, SIM-swap takeover, and AI voice-cloning and deepfake fraud. Explains the real deadlines under the Payment Services Law 2019 (the Debit Cards Law it replaced is repealed), the 8-business-day refund clock for unauthorised use, and the 24/7 human bank fraud line that owes customers aged 70 or over queue priority, and where Russian-language service is an expectation the regulator voiced rather than a duty. Use when a user asks whether a message or link is real, got a suspicious call, thinks they were scammed, or wants to protect an elderly or Russian-speaking relative. Do NOT use for malware removal, corporate incident response, or to declare a specific message safe."
license: Apache-2.0
---

# Israeli Scam Detector

## Legal notice

This skill is not legal advice, not a substitute for a licensed lawyer, and not a security
guarantee. It explains published Israeli law and official guidance so you can act quickly, but it
cannot tell you how a bank or a court will decide your particular case. It does not verify
messages on your behalf and cannot confirm that any message is safe.

Where the law is unsettled, this skill says so rather than guessing. If money is involved, contact
your bank immediately and consider consulting a lawyer. The National Cyber Directorate states that
any senior citizen over 65 who fell victim to exploitation or economic abuse may approach the
Ministry of Justice legal aid and receive **free legal advice and representation, at *6405**.

## Problem

Nearly every Israeli guide to card fraud still cites חוק כרטיסי חיוב, repealed in 2020, and tells
victims the bank has 30 days to refund and that they must file a police report first. Both are wrong
under the law that governs, and both cost time in the only window that matters. The advice to check
the sender was disowned by the Ministry of Communications, and forged messages now land inside the
genuine thread of GOV.IL and of real companies.

The Bank of Israel, Israel Police and the Ministry of Communications jointly found that fraud
concentrates on people with low financial and digital literacy, and the Bank of Israel flagged
Russian speakers in a directive's explanatory notes after public consultation raised it.

## Instructions

Work in this order: the first step stops the bleeding, and every later step depends on it.

### Step 0: Ask the one question that decides everything else

**Before quoting any deadline, establish which of these happened.** They are governed by different
rules, and confusing them is the most damaging mistake this skill can make.

| Ask the user | Which situation |
|---|---|
| "Did someone else use your card or account details?" (a charge you did not make, a card used by the scammer, details taken and used) | **A. Unauthorised use.** The misuse rules of חוק שירותי תשלום (ss.24 to 27) apply. Go to Step 1A. |
| "Or did you move the money yourself, in your own app or at the bank, because someone talked you into it?" | **B. A transfer you gave.** Ss.24 to 27 do **not** apply. Go to Step 1B. |
| "Have you given card details, a password or a one-time code, or lost the card or phone, but nothing has been charged yet?" | **C. A component is compromised, no misuse yet.** Call the bank now, see below, and skip the ladder in Step 1A. |

**Why this is not a technicality.** s.1 defines שימוש לרעה as use "**בידי מי שאינו זכאי לכך לפי
חוזה שירותי התשלום**". A person deceived into making their own transfer is entitled under the
contract, so the ₪75 + ₪30/day ladder, the ₪450 cap and the eight-business-day refund **do not reach
that case at all.**

Quoting that refund to someone in situation B sends them to their bank with a demand the bank will
correctly refuse, and costs them the hours in which situation B is still winnable.

If both happened, run both branches. **If the user typed or approved a code because the caller said it
would cancel or block something**, it is unclear which row applies, and a bank may treat an approval
made in the user's own app as the user's own payment order. Run A and B together, and have the user
describe exactly what happened (who entered the beneficiary and the amount, and what they believed
they were approving) rather than labelling it. Do not concede to the bank that the statute does not
apply, and do not deny giving the order either: say what happened.

**Situation C is the cheapest to win and the most often missed.** Do **not** quote the ₪75 + ₪30/day
ladder here: where the user handed the component over, s.24(ד) opens *"על אף הוראות סעיף קטן (ג)"*
and removes the whole s.24(ג) limit, which is the question Step 3 says is untested. That is the
argument **for** speed. For a lost or stolen card or phone, s.24(א) makes notice available with nothing
charged (*"גניבה או אבדן של רכיב חיוני"*). For a component handed to a fraudster it is less clear that
notice qualifies before any misuse, so ask for a **freeze** as well: s.25(ב) protects the frozen
period however those points fall, and s.24(ב) ends liability for misuse after notice. Describe what actually happened, for example *"מסרתי קוד למתחזה, אני מוסר הודעה ומבקש להקפיא מיד את
אמצעי התשלום"*. Never call a component stolen if it was handed over: the call is recorded, and s.26
removes every limit where the payer acted with intent to deceive. The freeze is a right: under s.22
the provider must freeze **immediately**, for the period asked, up to 14 days. Ask for the full 14
days and use them to replace the card and reset credentials, because the protection ends with the
freeze while the fraudster still holds the details (ending or returning the instrument also ends
liability, s.25(א)).

### Step 1A: Unauthorised use. Call the bank NOW

Do this before reading anything else, before calling the police, and before gathering evidence.
(Situation C: skip the next paragraph and go straight to the call.)

Under section 24 of חוק שירותי תשלום, התשע"ט-2019, the payer's liability before notice is the
**lower** of two amounts: a fixed ₪75 plus **₪30 for every day** counted from the day the payer
learned of the theft, loss or misuse until notice is given, or the amount charged **before notice**. If
notice is given within 30 days of the first misuse, liability is capped at ₪450. The day of notice
is excluded from the count when notice is given the same day the person found out. On the usual reading
the day the person learned is not counted (Interpretation Law s.10(א)); counting both ends adds ₪30
to the daily limb, before the cap and the lower-amount rule. Do not argue it on the fraud call.

The ₪30 per day clock starts from **the moment you knew**, not from the fraud, and after notice
liability for further misuse is **zero** (s.24(ב)). Notice is the switch, and it means notice to **the
payment service provider** (your bank or card issuer). The word משטרה does not appear in the law;
telling the police starts no clock in this statute.

**The bank must answer, and you can say so.** Since 31 May 2026, הוראת ניהול בנקאי תקין 426 requires
every banking corporation to provide a professional human telephone answer for suspected payment
fraud, available around the clock, every day of the week, **including during the weekly rest hours**.
As a rule the wait must not exceed six minutes.

**Ask for what you are owed:**

| If the caller is | Say this |
|---|---|
| A senior citizen | Directive 426 binds a **תאגיד בנקאי** as the Banking (Customer Service) Law defines it, which also covers a תאגיד עזר and a licensed acquirer (סולק). Do not assume a card company is outside it. Senior priority (s.7) is owed to a customer with an account there, including for a card that institution issued, so if the card is not your bank's, call both. Its אזרח ותיק is age **70** by the population registry, not the 65 used for free legal aid below. |
| A Russian speaker | Ask for a Russian-speaking representative, but do not call it an entitlement. Russian service appears only in 426's explanatory notes, as an *example* of adapting service under Directive 501, because the Bank of Israel found fraud is prevalent among Russian speakers. It is the regulator's stated expectation, not an operative clause. See `references/russian-phrasebook.md`. |
| Unable to reach anyone at all | Note the time and how long you waited. Under s.24(ה), a payer bears **no liability** under s.24(ג) or (ד) if the provider did not allow him to give notice **or cancel the instrument**, at any time, in a reasonable manner. It does not override s.26 (fraud by the payer). |

Find the number yourself: on the back of your own card, or by opening the bank's app or typing its
address yourself. Never use a number that came from the message or from the person who called you.

**If money has already left to another account**, also ask on the same call for an immediate recall
to the beneficiary bank, using the beneficiary-details steps of Step 1B items 2 and 3; here the order was not the user's (s.9). The bank's first
answer may be s.24(ד), and if it is, money still sitting in the receiving account is all that is left
to reach.

**Same-day, not "the day after": unauthorised direct debits.** If the loss came through a
הרשאה לחיוב, s.35 runs a far shorter clock than card misuse. A specific charge can be cancelled by
notice within **3 business days** of the charge, and must be refunded within **1 business day** of
that notice. Raise it on the same call, because three business days disappear quickly. Older charges
are not forfeited: cancel the mandate itself at any time (s.34), a mandate set up without the payer's
enhanced authentication or consent is invalid (s.33(4)), and a charge outside the mandate's terms is
refunded within 1 business day (s.37).

### Step 1B: A transfer you were talked into. Speed at the other end is the only lever

Say plainly that the statutory refund clock does not apply here (unless Step 0 left it open), then
move to what works. This branch is won or lost in hours.

1. **Call the bank now and ask for an immediate recall to the beneficiary bank.** Use the words
   "בקשת החזרת כספים" and ask them to contact the receiving bank directly. The money is only
   recoverable while it is still sitting in the beneficiary account. **First establish whether it has
   actually been executed yet**: some Israeli retail transfers settle immediately and some are queued
   to the next business day, so ask rather than assume. If it has not executed, this is not a favour: s.16(א)(1) lets the payer cancel a payment order (not a card payment, see item 4) while the provider
   can still stop it, and s.16(ב) then obliges it to halt execution *"מיד עם קבלת ההודעה"*. The cut-off
   is the provider's reasonable technical limit or the contractual deadline, which s.16(א)(1) says
   must itself be reasonable ("ובלבד שהוא סביר"), and s.16(ג) requires the contract to state it. Once the
   order **has** executed there is no statutory recall window, and a recall is a request the bank
   owes you nothing on.
2. **Get the beneficiary details in writing**: account number, bank, branch, and the name on the
   account. If the bank declines on privacy grounds, do not stall there: ask the police to obtain
   them, and move straight on to the report.
3. **Report to the police with those beneficiary details**, as early as possible. Wherever money
   went to another account, the police step is time-critical rather than administrative: the receiving account can
   be acted on only by the police or by the receiving bank, never by you, and neither is guaranteed
   or fast, and filing does not by itself freeze anything. The report is how you put the details in
   front of them.
4. **If it was a card purchase from a fake shop that never delivered**, s.17 is a statutory lever:
   once the agreed delivery date has passed (or, before it, the seller has stopped supplying for
   good), tell the seller you cancel as far as you can reach them, then tell the card issuer. It must
   stop executing the order and charging you **from that notice**. That is not a refund of what was
   already debited, so notify before the billing date; it reaches later instalments. A re-charge
   needs 15 days' written reasons (s.17(ב)).
5. **If the money went to a crypto exchange or a payment app, contact that provider in parallel.**
   They freeze on their own terms and usually faster than any bank.
6. **Ask the bank to open a case in writing** and record the reference number.

If the bank ignored its own anomalous-transaction monitoring, that is a **separate claim** for Step
6A; do not lead with it. Recovery depends on whether the money is still there, so neither promise it
nor call it hopeless. Tell the user what to do in the next hour.

### Step 2: Deadlines that follow, in branch A only

- **Refund: 8 business days.** Section 27(א) requires the provider to refund the charge, less the
  amount owed under s.24(ג), as soon as possible and **no later than eight business days** from the
  day of your notice. If someone tells you thirty days, they are quoting the repealed law.
- **Re-debit: 15 days' warning.** The bank may reverse the refund if it concludes the case falls
  under s.24(ד) or s.26, but s.27(ב) requires **written reasons at least 15 days before** the actual
  debit, and it must give you **copies of its documents on request**. The warning may be simultaneous only where the payer acted
  fraudulently.
- **Business days are the bank's own.** s.1 defines יום עסקים "כפי שנקבע בחוזה שירותי תשלום", so
  read the contract before alleging a breach. The ₪30 limb counts every day; the refund counts
  business days.
- **A second route with its own 30-day clock.** A transaction is a פעולת תשלום במסמך חסר under s.29(א)
  if the bank holds neither a document the user signed nor an admissible record of enhanced
  authentication **and** of the user's consent to that payment. Tell the bank in writing, **within 30
  days of its notice of the charge**, that you did not carry out the transaction, and ask for that
  document or record. Use this only where it is true that you did not give the order; in a mixed
  case, write what happened. If it has neither, s.29(ב) requires a refund within eight business days. Keep
  this 30 days apart from the 30-day window for the ₪450 cap.

### Step 3: Where the law is unsettled, in branch A only

**This step is branch A only.** Section 24(ד) presupposes a שימוש לרעה, so it has nothing to say
about a transfer the user gave themselves. If you are in branch B, skip to Step 4; the question of
whether the user is "covered" does not arise, because ss.24 to 27 never applied.

Within branch A: if the person was **deceived into handing over** a code, a card detail or a
password, do not tell them whether they are covered. Explain the position:

Section 24(ד) removes the whole s.24(ג) limit, not only the ₪450 cap, when the payer made the רכיב חיוני available to another
person, and it applies "בין שהשימוש נעשה בידיעת המשלם ובין שנעשה שלא בידיעתו". It lists exactly two
carve-outs: handing it over in reasonable circumstances for safekeeping only or to a payee to
initiate a payment, and cases where it was then stolen from or lost by that person. **Being tricked
is not among the listed carve-outs**, and no case law was located resolving how this applies to
someone deceived into disclosing a one-time code. Where card details were typed into what the user
believed was a merchant's payment page (a fake "delivery fee"), note the first carve-out's second
limb, a component given "למוטב לשם מתן הוראת תשלום"; whether it reaches a fake payee is also untested.
If the bank points to its terms, s.51(א) says the law "לא ניתן להתנות ... אלא לטובת הלקוח".

There is also a threshold question. Under s.1 a component is a רכיב חיוני only if it "פורט בחוזה
שירותי התשלום". Ask the bank, in writing, which component its contract lists. Ask; do not predict the
answer.

**Name the likely first answer, and label it as first, not final:** "I cannot promise an outcome. The
bank may first say you are responsible because you gave the code. That is the first answer, not the
last." Section 27(ב) lets the provider re-debit if it concludes s.24(ד) applies, so a refund is not
the end either: keep every record, demand the written reasons, use the 15 days, and escalate (Step 6A).

### Step 4: Judge the message, using tests that actually work

Apply these in order; the first two matter most.

1. **Did you initiate contact?** If not, treat every detail as attacker-controlled: sender name,
   logo, thread, and any number it gives.
2. **Verify on a channel you navigated to yourself**: type the address, open your own app, or call
   the number on your card. This habit defeats nearly every pattern below.
3. **Check the domain**, where the body publishes one. Israel Post states that genuine messages show
   only `postil.co.il` or `israelpost.co.il`, and that any change of address means impersonators.
   Bituach Leumi states its address always ends in `Gov.il`.
4. **Check the organisation's own inbox.** Bituach Leumi notifies in the personal area under
   ׳מכתבים׳, so a real notice usually exists in two places.
5. **Apply the never rules.** A real representative of a bank, the police or a government body will
   not ask you by phone for a one-time code, a password, card details, or a photo of a personal
   document. Bituach Leumi does not ask for card details in order to pay you benefits. Generalise it:
   a body that owes you money never needs your card number.
6. **Treat three demands as decisive.** Being asked to install an app, click a link or share your
   screen; being asked to move money to a "safe account"; and being asked to keep the call secret
   ("אל תספר לאף אחד", "זה דחוף"). Each is a documented pressure tactic, not a coincidence.

**Two tests that do NOT work, and why:**

- **The sender name proves nothing.** The Ministry of Communications decided in 2020 that Latin
  letters in the SMS CLI field are not a one-to-one identifier of a subscriber.
- **The thread proves nothing.** The National Cyber Directorate has warned that impersonating
  messages appear **inside the existing genuine thread** of GOV.IL, and separately of Pango, by
  exploiting how certain handsets group messages, not by any breach.

So this skill publishes no list of legitimate sender names: it would train the check the attack
defeats.

### Step 5: Match the pattern

The joint Bank of Israel, Israel Police and Ministry of Communications task force focuses on three
patterns. Use them as the top-level triage.

| Pattern | What it looks like | The specific move |
|---|---|---|
| **Phone-number takeover** (SIM Swap and עקוב אחריי) | An unrequested porting (ניוד) SMS, then sudden loss of cellular signal | An unrequested porting message is the attack in progress. Call the carrier from another phone immediately, then the bank. Carriers now push the OTP to the end of the porting message so the text above it is readable, so read it before the code. |
| **Phishing via impersonating sites** | A link to a page that mimics a bank or government service | Never reach a login through a link. Close it and navigate yourself. |
| **Vishing and smishing** | A call or SMS creating urgency about a debt, package, fine or grant | Hang up. Call back on a number you already hold. |

Two newer layers, detailed in `references/scam-patterns.md`:

- **A cloned voice or a deepfake video call** of a relative or manager asking for an urgent transfer.
  Looking and sounding right is no longer evidence. The defence is arranged in advance: a family code
  word and a callback on the number you already hold (מערך הסייבר: עוצרים, מנתקים, מאמתים).
- **Fake police letters**, such as the October 2026 emails posing as להב 433 and threatening legal
  steps, which Israel Police called "הודעת כזב". Do not reply, click or download.

### Step 6: Report, with honest expectations about each route

- **The bank or card issuer, always first.** In branch A it stops the s.24 clock and starts the s.27
  refund clock (the s.35 window already runs from the charge, the s.29 one from the bank's notice of it). In branch B
  it is first because only the bank can send a recall; it owes no statutory refund there.
- **119, מערך הסייבר הלאומי.** Report the link so the Directorate can act on it. It does not recover money.
- **Police, 100 or the online form.** Opens a criminal case. The online filing is a בקשה, not a
  completed complaint, and filing does not by itself freeze anything.
- **מוקד 105.** Only where the **victim** is a minor; a parent may call for a child.
- **Bank of Israel פניות הציבור.** For the bank's own conduct, not the scammer.

What each route will and will not do is in `references/reporting-routes.md`.

### Step 6A: If the bank refuses, escalate in this order

1. **The bank's own פניות הציבור**, in writing (an oral notice is what gets disputed later), citing
   the section you rely on.
2. **Bank of Israel פניות הציבור**, if the answer is unsatisfactory or absent.
3. **תביעות קטנות (small claims court)**, where the law does not require a lawyer, for a four-figure
   loss; in a disputed s.24(ד) case consider one anyway (free legal aid at 65+, Step 8).
   `israeli-small-claims-court` covers the procedure.

### Step 7: The day after

Block the card with **both** the bank and the card company, hunt for unfamiliar new standing orders
(הוראות קבע), and preserve every message and the bank's written confirmation of notice before
tidying up. The full checklist, including the sweep for credit taken in the user's name and
replacing a stolen ID, is in `references/aftermath.md`.

### Step 8: Helping someone else

When helping a parent or grandparent, lead with what can be asked for. **Senior queue priority** is
demandable from a bank for someone aged 70 or over. **Russian-language service** is an expectation
the regulator voiced, not a duty, so ask without promising it. Then set up the family code word,
save the bank's real fraud number in the person's phone, and agree that nobody in the family ever
asks for money by message or by a call the other person did not initiate.

For a person aged 65 or over, Legal Aid Law amendment 30 (in force since March 2026) waives the means
test in a proceeding founded on exploitation of difficulty, weakness, a cognitive or health
condition, or language difficulty, including a proceeding under s.24 of חוק שירותי תשלום where that
condition is met. It is not automatic for every senior. Point them to *6405.

Tell them the National Cyber Directorate has said that merely answering a call does not harm the
phone; elderly users who believe otherwise stop answering, including the bank's callback.

If the user writes in Russian, answer in Russian.

## Gotchas

These are failure modes for the agent, not for the user.

- **Never quote the refund clock before running Step 0.** This is the biggest trap in the domain.
  Every figure in Step 1A is correct and none of it applies to a victim who made the transfer
  themselves. Correct and applicable are different questions, and only Step 0 answers the second.
- **Do not assume the user is the account holder.** Joint, business and a relative's accounts change
  who may give notice and whether the consumer regime applies. Ask; if unclear, give notice anyway
  and route to the bank and a lawyer rather than guessing.

- **Do not cite חוק כרטיסי חיוב or "the bank has 30 days".** The law is repealed outright by s.55 of
  חוק שירותי תשלום; the live provisions are ss.24 and 27, and the refund is 8 business days. The old
  numbers look right, which is why they slip through, and quoting them forfeits the user's credibility.
- **Do not send the user to the police first.** No statutory clock depends on it, while the ₪30
  per day clock keeps running.
- **Do not repeat "check the sender name", even though Bituach Leumi's page lists it.** Present the
  domain check, the personal-area check and the independent callback as the load-bearing tests, and
  do not describe Bituach Leumi as wrong; its other rules are sound.
- **Never say a message is safe.** Still give the action: do not click, and verify through a
  channel you opened yourself.
- **Do not state that Israel Post never sends SMS.** Customs-payment notifications are genuine; the
  domain test in Step 4 is the rule.
- **Keep the attributions apart.** The in-thread SMS warnings come from the National Cyber
  Directorate's Telegram channel; deepfake warnings come from מערך הסייבר, not רשות ניירות ערך.
- **Never tell a user to pay whoever took their account.** Paying an account hijacker or a sextortion
  demand buys nothing the user can rely on. For a hijacked WhatsApp the documented
  route is self-service re-verification, then reporting to WhatsApp, and it never involves payment.
  See `references/reporting-routes.md`.

## Recommended MCP Servers

| MCP | Why it helps here |
|---|---|
| [`kolzchut`](https://agentskills.co.il/he/mcp/kolzchut) | Kol Zchut, Israel's rights knowledge base: current consumer-rights and banking-complaint procedures and identity-theft routes, instead of memory. |

Do not reach for a bank-scraping MCP: a defrauded user should not be wiring new access to their
accounts.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| חוק שירותי תשלום, התשע"ט-2019 | https://www.nevo.co.il/law_html/law01/502_043.htm | ss.24, 26, 27, 34 to 37, 51, 55. The liability ladder, the 8-business-day refund, the 15-day re-debit warning, the repeal |
| הוראת ניהול בנקאי תקין 426 | https://www.boi.org.il/media/k23b3lzq/h2834.pdf | s.3(א) addressee and s.3(ב) repealed, s.4 age 70, s.5(ב) 24/7 human fraud line (weekly rest hours named in the explanatory notes), s.6א six-minute standard, s.7 senior queue priority. Russian-language service is in the explanatory notes only |
| בנק ישראל, משטרה ומשרד התקשורת | https://www.boi.org.il/publications/pressreleases/15-4-26a/ | The three national fraud patterns, the targeting finding, the porting-message change |
| משרד התקשורת, החלטת שימוע 03.06.2020 | https://www.gov.il/he/pages/03062020_2 | Why an alphabetic sender name is not proof of anything |
| מערך הסייבר הלאומי, דיווח על אירוע | https://www.gov.il/he/service/cyber-event-report | 119, the reporting form, what the CERT does and does not do |
| עוצרים. מנתקים. מאמתים. | https://www.gov.il/he/pages/us080726 | The code word and callback protocol for cloned-voice calls |
| אחרי האירוע | https://www.gov.il/he/pages/fool_me_twice | The aftermath checklist, including new standing orders |
| רשות הדואר | https://doar.israelpost.co.il/content/fishing | The two legitimate Post domains |
| ביטוח לאומי | https://www.btl.gov.il/About/newspapers/Pages/hodaaitonotfakesaagetari2026.aspx | Its own verification rules and the no-credit-card rule |
| רשות המסים | https://www.gov.il/he/pages/pa010825-1 | Current impersonation lures, including the fake investigation notice |

## Bundled Resources

| File | Purpose |
|---|---|
| `references/domain-checklist.md` | The coverage contract, every source, and the known-wrong advice this skill must never reproduce |
| `references/russian-phrasebook.md` | What to say on the bank's fraud line, Russian and Hebrew side by side |
| `references/reporting-routes.md` | Each reporting route, what it achieves and what it will not do, plus the hijacked-WhatsApp path |
| `references/aftermath.md` | The day-after checklist: standing orders, credit taken in the user's name, evidence, stolen ID |
| `scripts/liability_clock.py` | Computes s.24(ג) exposure and shows which limb binds. Branch A only |

## Troubleshooting

| Symptom | Likely cause | What to do |
|---|---|---|
| The bank quotes a 30-day refund period | It is applying the repealed חוק כרטיסי חיוב, or the representative is working from old training material | Cite s.27(א) of חוק שירותי תשלום and the eight-business-day period. This is a documented and common error, not necessarily bad faith. |
| The bank demands a police report before refunding | Internal procedure, not a statutory precondition | A report is useful evidence and a bank may ask for a reference number, but no clock in the statute depends on it. Give notice to the bank first regardless, and say you have done so. |
| The refund arrived and was then reversed | The bank concluded s.24(ד) or s.26 applies | It owes written reasons at least 15 days before the debit, and copies of its documents on request (s.27(ב)). Request the documents. |
| Nobody answers the fraud line | Possible breach of Directive 426 | Record the time and wait duration. Note s.24(ה) removes liability where no reasonable way to give notice was provided. Complain to the Bank of Israel's public enquiries unit. |
| The user asks whether they will get their money back after being tricked into disclosing a code | s.24(ד) is untested on deception | Do not predict the outcome. State the provision, state that it is unresolved, and give the immediate action. Note that s.27(ב) lets the bank re-debit if it concludes 24(ד) applies, so tell them to keep records and use the 15-day window. |
| The bank says the eight-business-day refund does not apply | The user is probably in branch B, having made the transfer themselves | Check Step 0. If they gave the payment order, the bank is right and the lever is a recall plus a police report with the beneficiary details, or s.17 for a card purchase that never arrived (Step 1B item 4). If Step 0 left it open, do not concede; describe what happened. |
| The bank froze the user's own card or app after the fraud | s.23 lets it freeze on suspected misuse or fraud, where law requires it or the contract allows it, for reasonable grounds | It must give notice and reasons before the freeze, or as soon as possible after where notice would defeat the purpose, confirm an oral notice in writing, and lift the freeze or issue a replacement instrument once the reasons end. |
