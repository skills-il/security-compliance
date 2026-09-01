---
name: israeli-scam-detector
description: "Not legal advice and not a security guarantee. Check whether a suspicious Israeli SMS, email, link or phone call is a scam, and get the exact next steps, including after the money is already gone. Covers smishing and phishing impersonating Israeli banks, Bituach Leumi, Rashut HaMisim, Israel Post and gov.il, SIM-swap takeover, and the 2026 wave of AI voice-cloning and deepfake fraud. Explains the real deadlines under the Payment Services Law 2019 (the Debit Cards Law it replaced is repealed), the 8-business-day refund clock, and the 24/7 human bank fraud line that owes senior citizens queue priority and offers Russian-language service. Use when a user asks whether a message or link is real, got a suspicious call, thinks they were scammed, or wants to protect an elderly or Russian-speaking relative. Do NOT use for malware removal, corporate incident response, or to declare a specific message safe."
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

Nearly every Israeli guide to card fraud still cites חוק כרטיסי חיוב, a law that was repealed in
2020, and tells victims the bank has 30 days to refund them and that they must file a police
report first. Both are wrong under the law that actually governs, and both cost the victim time
during the only window that matters. Meanwhile the identification advice everyone repeats, check
who the sender is, was disowned by the Ministry of Communications itself, and forged messages now
land inside the genuine message thread of GOV.IL and of real companies.

The people hit hardest are the ones least served by that bad advice. The Bank of Israel, Israel
Police and the Ministry of Communications jointly found that fraud targets everyone but
concentrates on people with low financial and digital literacy, and the Bank of Israel amended a
banking directive specifically because fraud is prevalent among Russian speakers.

## Instructions

Work in this order. The order is the point: the first step stops the bleeding and every later step
depends on having done it.

### Step 0: Ask the one question that decides everything else

**Before quoting any deadline, establish which of these happened.** They are governed by different
rules, and confusing them is the most damaging mistake this skill can make.

| Ask the user | Which situation |
|---|---|
| "Did someone else use your card or account details?" (a charge you did not make, a card used by the scammer, details taken and used) | **A. Unauthorised use.** Chapter ו' of חוק שירותי תשלום applies. Go to Step 1A. |
| "Or did you move the money yourself, in your own app or at the bank, because someone talked you into it?" | **B. A transfer you gave.** Chapter ו' does **not** apply. Go to Step 1B. |

**Why this matters, and why it is not a technicality.** Chapter ו' is headed
"שימוש לרעה באמצעי תשלום", and s.1 defines שימוש לרעה as use of the instrument
"**בידי מי שאינו זכאי לכך לפי חוזה שירותי התשלום**", meaning use by someone **not entitled** under
the contract. A person deceived into making their own transfer is entitled under the contract. So
the ₪75 plus ₪30 per day ladder, the ₪450 cap and the eight-business-day refund **do not reach that
case at all.**

Quoting an eight-business-day refund entitlement to someone in situation B sends them to their bank
with a demand the bank will correctly refuse, and costs them the hours in which situation B is
actually still winnable. Never state that entitlement before you know which situation you are in.

If both happened, run both branches.

### Step 1A: Unauthorised use. Call the bank NOW

Do this before reading anything else, before calling the police, and before gathering evidence.

Under section 24 of חוק שירותי תשלום, התשע"ט-2019, the payer's liability before notice is the
**lower** of two amounts: a fixed ₪75 plus **₪30 for every day** counted from the day the payer
learned of the theft, loss or misuse until notice is given, or the amount actually transacted. If
notice is given within 30 days of the first misuse, liability is capped at ₪450. The day of notice
is excluded from the count when notice is given the same day the person found out.

Two consequences that change behaviour:

- The ₪30 per day clock starts from **the moment you knew**, not from the fraud. Every day of
  hesitation has a price.
- After notice is given, liability for further misuse is **zero** (s.24(ב)). Notice is the switch.

"Notice" in the statute means notice to **the payment service provider**, meaning your bank or card
issuer. The word משטרה does not appear anywhere in the law. Telling the police does not start any
clock in this statute.

**The bank must answer, and you can say so.** Since 31 May 2026, הוראת ניהול בנקאי תקין 426 requires
every banking corporation to provide a professional human telephone answer for suspected payment
fraud, available around the clock, every day of the week, **including during the weekly rest hours**.
As a rule the wait must not exceed six minutes.

**Ask for what you are owed:**

| If the caller is | Say this |
|---|---|
| A senior citizen (אזרח ותיק) | Directive 426 requires the bank to give senior citizens **priority in the queue** on the fraud line. Ask for it. |
| A Russian speaker | The same directive names Russian-language service, because the Bank of Israel found fraud is prevalent among Russian speakers. Ask for a Russian-speaking representative. See `references/russian-phrasebook.md`. |
| Unable to reach anyone at all | Note the time and how long you waited. Under s.24(ה), a payer bears **no liability at all** if the provider did not allow him to give notice in a reasonable manner at any time. |

Find the number yourself: on the back of your own card, or by opening the bank's app or typing its
address yourself. Never use a number that came from the message or from the person who called you.

**Same-day, not "the day after": unauthorised direct debits.** If the loss came through a
הרשאה לחיוב, s.35 runs a far shorter clock than card misuse. A specific charge can be cancelled by
notice within **3 business days** of the charge, and must be refunded within **1 business day** of
that notice. Raise it on the same call, because three business days disappear quickly.

### Step 1B: A transfer you were talked into. Speed at the other end is the only lever

Say plainly that the statutory refund clock does not apply here, then move immediately to what does
work. This branch is won or lost in hours, so do not spend them arguing about entitlement.

1. **Call the bank now and ask for an immediate recall to the beneficiary bank.** Use the words
   "בקשת החזרת כספים" and ask them to contact the receiving bank directly. The money is only
   recoverable while it is still sitting in the beneficiary account. **There is no statutory recall
   window**: "hours" is a fact about how fast mule accounts are emptied, not a legal deadline, so
   nobody owes you an extension.
2. **Get the beneficiary details in writing**: account number, bank, branch, and the name on the
   account. If the bank declines on privacy grounds, do not stall there: ask the police to obtain
   them, and move straight on to the report.
3. **Report to the police with those beneficiary details**, so the account can be frozen. Here,
   unlike in branch A, the police step is time-critical rather than administrative, because freezing
   the destination account is a police action and not a bank one.
4. **If the money went to a crypto exchange or a payment app, contact that provider in parallel.**
   They freeze on their own terms and usually faster than any bank.
5. **Ask the bank to open a case in writing** and record the reference number.

If the bank ignored its own anomalous-transaction monitoring, that is a **separate claim against the
bank**, not a recall. Preserve it for Step 6A, but do not lead with it: leading with it delays the
only step that is still time-critical.

Be honest about the odds without being defeatist: recovery depends on whether the money is still
there, which is why every hour matters. Do not promise it, and do not tell the user it is hopeless
either. Tell them what to do in the next hour.

### Step 2: Deadlines that follow, in branch A only

- **Refund: 8 business days.** Section 27(א) requires the provider to refund the charge, less the
  amount owed under s.24(ג), as soon as possible and **no later than eight business days** from the
  day of your notice. If someone tells you thirty days, they are quoting the repealed law.
- **Re-debit: 15 days' warning.** The bank may reverse the refund if it concludes the case falls
  under s.24(ד) or s.26, but s.27(ב) requires **written reasons at least 15 days before** the actual
  debit, and it must give you **copies of its documents on request**. That window and those
  documents are your opening to contest. The warning may be simultaneous only where the payer acted
  fraudulently.

### Step 3: Where the law is unsettled, in branch A only

**This step is branch A only.** Section 24(ד) presupposes a שימוש לרעה, so it has nothing to say
about a transfer the user gave themselves. If you are in branch B, skip to Step 4; the question of
whether the user is "covered" does not arise, because chapter ו' never applied.

Within branch A: if the person was **deceived into handing over** a code, a card detail or a
password, do not tell them whether they are covered. Explain the position and let them decide with proper advice:

Section 24(ד) removes the liability cap when the payer made the רכיב חיוני available to another
person, and it applies "בין שהשימוש נעשה בידיעת המשלם ובין שנעשה שלא בידיעתו". It lists exactly two
carve-outs: handing it over in reasonable circumstances for safekeeping only or to a payee to
initiate a payment, and cases where it was then stolen from or lost by that person. **Being tricked
is not among the listed carve-outs**, and no case law was located resolving how this applies to
someone deceived into disclosing a one-time code.

So: state the text, state that the point is untested, and still give the action. Being unable to
say "you are covered" is never a reason to fail to say "call the bank now, the clock is running."

**Name the likely first answer, and label it as first, not final.** A user who is told only the odds
gives up; a user who is told the odds plus the next concrete action keeps going. Say something close
to: "I cannot promise you an outcome. The bank's first answer may well be that you are responsible
because you gave the code. That is the first answer, not the last one. Ask for the refusal in
writing with its reasons, keep every document, and escalate." Section 27(ב) shows the law itself
contemplates the bank reaching that conclusion, which is exactly why the written reasons and the
15 days matter.

**Prepare the user without predicting for them.** Section 27(ב) expressly permits the provider to
re-debit if it concludes the case falls under s.24(ד), so a refund arriving is not the end of the
matter. Tell the user to plan for that: keep every record, demand the written reasons the section
requires, use the 15 days before the debit, and escalate (Step 6A). Refusing to predict the outcome
is honest. Letting the user assume it will be fine is not.

### Step 4: Judge the message, using tests that actually work

Apply these in order. The first two are the ones that matter.

1. **Did you initiate contact?** If you did not open the app or dial the number yourself, treat
   every detail in front of you as attacker-controlled, including the sender name, the logo, the
   thread it sits in, and any number it tells you to call.
2. **Verify on a channel you navigated to yourself.** Type the address, open the app you already
   have, or call the number on your own card. This single habit defeats nearly every pattern below.
3. **Check the domain**, where the body publishes one. Israel Post states that genuine messages show
   only `postil.co.il` or `israelpost.co.il`, and that any change of address means impersonators.
   Bituach Leumi states its address always ends in `Gov.il`.
4. **Check the organisation's own inbox.** Bituach Leumi notifies in the personal area under
   ׳מכתבים׳; most banks and government services do the same. A real notice usually exists in two
   places.
5. **Apply the never rules.** A real representative of a bank, the police or a government body will
   not ask you by phone for a one-time code, a password, card details, or a photo of a personal
   document. Bituach Leumi does not ask for card details in order to pay you benefits. Generalise it:
   a body that owes you money never needs your card number.
6. **Treat three demands as decisive.** Being asked to install an app, click a link or share your
   screen; being asked to move money to a "safe account"; and being asked to keep the call secret
   ("אל תספר לאף אחד", "זה דחוף"). Each is a documented pressure tactic, not a coincidence.

**Two tests that do NOT work, and why:**

- **The sender name proves nothing.** The Ministry of Communications decided in 2020 that it does
  not regard Latin letters in the SMS CLI field as a one-to-one identifier of a subscriber, and that
  a user receiving a message with a textual sender name should exercise judgment about the source.
  It went further, saying the concept of forgery is not even relevant to an alphabetic CLI because
  it is not a unique identifier in the first place.
- **The thread proves nothing.** The National Cyber Directorate has warned that impersonating
  messages appear **inside the existing genuine thread** of GOV.IL, and separately of Pango, and
  explained this exploits how certain handsets group messages rather than any breach.

This is why this skill does not publish a list of legitimate sender names. Such a list would train
exactly the check that the attack defeats.

### Step 5: Match the pattern

The joint Bank of Israel, Israel Police and Ministry of Communications task force focuses on three
patterns. Use them as the top-level triage.

| Pattern | What it looks like | The specific move |
|---|---|---|
| **Phone-number takeover** (SIM Swap and עקוב אחריי) | An unrequested porting (ניוד) SMS, then sudden loss of cellular signal | An unrequested porting message is the attack in progress. Call the carrier from another phone immediately, then the bank. Carriers now push the OTP to the end of the porting message so the text above it is readable, so read it before the code. |
| **Phishing via impersonating sites** | A link to a page that mimics a bank or government service | Never reach a login through a link. Close it and navigate yourself. |
| **Vishing and smishing** | A call or SMS creating urgency about a debt, package, fine or grant | Hang up. Call back on a number you already hold. |

Add the 2026 AI layer:

- **A cloned voice** of a relative or a manager asking for an urgent transfer. The countermeasure is
  social and must be arranged in advance: a family code word for emergencies known only to the
  family, and a callback on the number you already have. The National Cyber Directorate's rule is
  "לא פועלים מתוך לחץ. מנתקים ומתקשרים לבן משפחה במספר המוכר", under the heading
  עוצרים, מנתקים, מאמתים: stop, hang up, verify.
- **Deepfake video calls.** Looking and sounding right is no longer evidence of identity.
- **Deepfake investment videos** using the faces of well-known Israeli finance figures. Attribute
  these warnings to מערך הסייבר, not to רשות ניירות ערך.

### Step 6: Report, with honest expectations about each route

| Route | What it is for | What it will NOT do |
|---|---|---|
| **The bank or card issuer** | Always first, but for different reasons by branch. In branch A it starts every statutory clock. In branch B no statutory clock exists; it is first because only the bank can send a recall to the beneficiary bank. | In branch B it owes you no statutory refund. Do not demand one. |
| **119, מערך הסייבר הלאומי** | National CERT: triage, guidance, and taking down malicious infrastructure. Report the link so the next person does not lose money. | It does not recover your money and does not replace a police report. It does not fix computer faults. |
| **Police, 100 or the online form** | Opens a criminal case. In an emergency call 100; otherwise file online or at the station nearest your area of residence. | The online filing is a בקשה, not a completed complaint; you may still be summoned. It does not freeze a transfer. |
| **מוקד 105** | Harm to a **minor**, ages 0 to 18 only. | Not the adult scam line, despite the word הונאה appearing in its intake list. |
| **Bank of Israel פניות הציבור** | Complaints about **the bank's own conduct**: no answer on the fraud line, a refused refund, a re-debit without the 15 days' notice. | It does not investigate the scammer or recover money from them. |

### Step 6A: If the bank refuses, escalate in this order

A statute the user cannot enforce is worth nothing, so give them the ladder:

1. **The bank's own פניות הציבור**, in writing. Written is not optional: an oral phone notice is
   exactly what gets disputed later. Reference the section you are relying on.
2. **Bank of Israel פניות הציבור**, if the bank's answer is unsatisfactory or absent.
3. **תביעות קטנות (small claims court)**, which needs no lawyer and is the right forum for a
   four-figure loss. `israeli-small-claims-court` covers the procedure.

### Step 7: The day after

- Block the card, and notify **both** the bank and the card company.
- Hunt for **unfamiliar new standing orders** (הוראות קבע) and direct debits. This is the step people
  skip, and it bleeds money for months.
- **Sweep for credit taken in the user's name.** Anyone holding a one-time code and account access
  routinely goes further than a single charge: check for a new digital loan, a raised card limit, a
  newly enrolled device, and whether the phone number or email on the account was changed. Force a
  device de-enrolment and a full credentials reset.
- **Preserve evidence before tidying up.** Do not delete the SMS, the call log or the chat.
  Screenshot the transaction, the beneficiary details and the calling number. Get the bank's
  confirmation of your notice **in writing**, by email or in-app message.
- Turn on purchase alerts, change reused passwords, enable two-factor authentication.
- If ID details were exposed, note that replacing a stolen תעודת זהות does **not** require a police
  complaint; a תצהיר suffices. There is no Israeli equivalent of a US fraud alert, so ask the credit
  data register (מאגר נתוני אשראי) at the Bank of Israel what options actually exist here.

### Step 8: Helping someone else

When the user is helping a parent or grandparent, lead with the two entitlements rather than generic
advice, because they are concrete and demandable: **senior queue priority** and **Russian-language
service** on the bank's fraud line. Then set up the family code word, save the bank's real fraud
number in the person's phone under a name they will recognise, and agree the rule that nobody in the
family ever asks for money by message or by a call the other person did not initiate.

Reassure them about one thing specifically: the National Cyber Directorate has stated that merely
answering the call does not harm the phone. Elderly users who believe otherwise often stop answering
every call, including the bank's callback.

If the user writes in Russian, answer in Russian.

## Gotchas

These are failure modes for the agent, not for the user.

- **Never quote the refund clock before running Step 0.** This is the biggest trap in the domain.
  Chapter ו' reaches only שימוש לרעה, defined as use by someone NOT entitled under the payment
  services contract. A victim talked into transferring money from their own app was entitled, so the
  ladder, the cap and the eight-business-day refund do not apply to them. Every figure in Step 1A is
  correct and none of it is applicable to branch B. Correct and applicable are different questions,
  and only Step 0 answers the second one.
- **Do not assume the user is the account holder.** Joint accounts, business accounts and a relative
  helping a parent each change who may give notice and whether the consumer liability regime reaches
  the account at all. Ask whose account it is, and if it is a company account or the user is not the
  holder, say the position may differ and route them to the bank and a lawyer rather than guessing.

- **Do not cite חוק כרטיסי חיוב.** It is repealed outright by s.55 of חוק שירותי תשלום. Its numbers
  survive in circulation and look right, which is exactly why the citation slips through. The live
  provisions are ss.24 and 27 of the 2019 law. Quoting the dead statute to a bank forfeits the user's
  credibility at the moment they need it.
- **Do not repeat "the bank has 30 days".** That was the repealed regime. It is 8 business days, and
  repeating the old figure hands the bank three weeks the user is entitled to.
- **Do not tell the user to go to the police first.** It feels responsible and it is wrong: no clock
  in the statute is triggered by a police report, while the ₪30 per day clock keeps running.
- **Do not repeat "check the sender name", even though official bodies say it.** Bituach Leumi's own
  page lists it, and it is not sufficient on its own; the Ministry of Communications has ruled that
  an alphabetic sender ID is not a unique identifier. Present the domain check, the personal-area
  check and the independent callback as the load-bearing tests. Do not describe Bituach Leumi as
  wrong; its other rules are sound.
- **Never say a message is safe.** The skill has no way to verify one. When it cannot confirm, it
  must still give the action: do not click, and verify through a channel you opened yourself.
- **Do not state that Israel Post never sends SMS.** Customs-payment notifications are a genuine
  Post service. The overstatement is dangerous because it teaches users to distrust a real message
  and to trust the next forgery that mimics a denial.
- **Keep the attributions apart.** The SMS-in-genuine-thread warnings come from the National Cyber
  Directorate's official Telegram channel and have no gov.il permalink; say so. Deepfake warnings
  about Israeli finance figures come from מערך הסייבר, not from רשות ניירות ערך.
- **Do not answer the deceived-OTP question.** Section 24(ד) is untested on that point. State the
  text, state the uncertainty, give the action.

## Recommended MCP Servers

| MCP | Why it helps here |
|---|---|
| [`kolzchut`](https://agentskills.co.il/he/mcp/kolzchut) | Kol Zchut is Israel's authoritative rights and entitlements knowledge base. Use it to pull the current consumer-rights and banking-complaint procedures, and the routes for identity-theft aftermath, rather than relying on memory. |

Do not reach for a bank-scraping MCP here. A user who has just been defrauded should not be wiring
new access to their accounts, and this skill never needs to read their transactions.

## Reference Links

| Source | URL | What to check |
|---|---|---|
| חוק שירותי תשלום, התשע"ט-2019 | https://www.nevo.co.il/law_html/law01/502_043.htm | ss.24, 26, 27, 34 to 37, 51, 55. The liability ladder, the 8-business-day refund, the 15-day re-debit warning, the repeal |
| הוראת ניהול בנקאי תקין 426 | https://www.boi.org.il/media/k23b3lzq/h2834.pdf | 24/7 human fraud line including Shabbat, six-minute standard, senior queue priority, Russian-language service |
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
| `references/domain-checklist.md` | The coverage contract this skill is maintained against, with every source and the known-wrong advice it must never reproduce |
|  `references/russian-phrasebook.md` | What to say on the bank's fraud line, in Russian and Hebrew side by side, including the demands for Russian-language service and senior queue priority |
| `references/reporting-routes.md` | Each reporting route, what it achieves, and what it will not do |
| `scripts/liability_clock.py` | Computes the s.24(ג) exposure from the date the user found out and the date of notice, and shows which limb of the test binds |

## Troubleshooting

| Symptom | Likely cause | What to do |
|---|---|---|
| The bank quotes a 30-day refund period | It is applying the repealed חוק כרטיסי חיוב, or the representative is working from old training material | Cite s.27(א) of חוק שירותי תשלום and the eight-business-day period. This is a documented and common error, not necessarily bad faith. |
| The bank demands a police report before refunding | Internal procedure, not a statutory precondition | A report is useful evidence and a bank may ask for a reference number, but no clock in the statute depends on it. Give notice to the bank first regardless, and say you have done so. |
| The refund arrived and was then reversed | The bank concluded s.24(ד) or s.26 applies | It owes written reasons at least 15 days before the debit, and copies of its documents on request (s.27(ב)). Request the documents. |
| Nobody answers the fraud line | Possible breach of Directive 426 | Record the time and wait duration. Note s.24(ה) removes liability where no reasonable way to give notice was provided. Complain to the Bank of Israel's public enquiries unit. |
| The message sits inside a real GOV.IL thread | Not evidence of authenticity | The National Cyber Directorate has documented this. Verify by navigating to the service yourself. |
| The user asks whether they will get their money back after being tricked into disclosing a code | s.24(ד) is untested on deception | Do not predict the outcome. State the provision, state that it is unresolved, and give the immediate action. Note that s.27(ב) lets the bank re-debit if it concludes 24(ד) applies, so tell them to keep records and use the 15-day window. |
| The bank says the eight-business-day refund does not apply | The user is probably in branch B, having made the transfer themselves | Check Step 0. If they gave the payment order, the bank is right and the lever is a recall to the beneficiary bank plus a police freeze, not a statutory refund demand. |
| The account is a joint account, a business account, or the user is not the holder | The consumer liability regime may not reach it, and who may give notice differs | Do not guess. Give notice to the bank immediately regardless, then route to the bank and a lawyer for the position. |
