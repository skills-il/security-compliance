---
name: israeli-shelter-guide
description: Guide to finding and preparing shelters in Israel including mamad (apartment safe room), mamak (floor safe room), maman (institutional safe room), and miklat (public shelter). Use when a user needs to find the nearest shelter, prepare a safe room per Home Front Command guidelines, understand time-to-shelter by region, set up workplace emergency procedures, or interpret the multi-stage early-warning notifications introduced for ballistic threats. Covers the civil-defence construction specifications and what Israeli Standard 4422 actually governs, time-to-shelter zones (immediate / 15 / 30 / 45 / 60 / 90 seconds), municipal shelter databases, accessibility law, sheltering with pets, vehicle protocols, and what to do if caught outdoors. Do NOT use for real-time alert integrations (use pikud-haoref-alerts) or per-threat safety protocols (use pikud-haoref-safety-protocols).

license: MIT
compatibility: Knowledge-based skill. No tools, APIs, or network access required. Works on any agent that supports SKILL.md format.

---

# Israeli Shelter Guide

Guidance on finding, preparing and using shelters in Israel during rocket and missile alerts. It is based on publicly available Pikud Ha'Oref (Home Front Command) guidance as of August 2026. All life-safety numbers below should be cross-checked against the live Pikud Ha'Oref site or the 104 hotline before acting on them in a real emergency.

## Description

Helps users:
- Identify which type of protected space they have (mamad, mamak, maman, miklat) and what to do in buildings that have none.
- Look up their region's time-to-shelter (immediate / 15 / 30 / 45 / 60 / 90 seconds).
- Understand the multi-stage early warning system Pikud Ha'Oref publishes for missile fire (preliminary advisory, then alert, then release message), including the separate advisory for fire from Lebanon.
- Prepare an emergency kit (ערכת חירום) according to Pikud Ha'Oref recommendations.
- Apply the correct protocol when caught in a vehicle, outdoors, or in a building without a mamad.
- Navigate the process for inspecting or building a private mamad with a licensed engineer.

## Shelter Types

Israel has four types of protected spaces, each designated by a Hebrew acronym:

| Type | Hebrew | Full Name | Location | Typical Use |
|------|--------|-----------|----------|-------------|
| **Mamad** (ממ"ד) | מרחב מוגן דירתי | Apartment Protected Space | Inside individual apartments | Most common in buildings built after 1992 |
| **Mamak** (ממ"ק) | מרחב מוגן קומתי | Floor Protected Space | Shared space on each floor | Older buildings retrofitted with floor-level shelters |
| **Maman** (ממ"מ) | מרחב מוגן מוסדי | Institutional Protected Space | Schools, offices, public institutions | Workplaces and educational facilities |
| **Miklat** (מקלט) | מקלט ציבורי | Public Shelter | Underground or standalone structures | Parks, community centers, public spaces |

Since 1992, Israeli building code requires all new residential construction to include a mamad. Buildings constructed before 1992 may lack a mamad entirely.

### Mamad Specifications

**Get the legal source right before quoting a figure.** Mamad dimensions, wall thicknesses and heights come from תקנות ההתגוננות האזרחית (מפרטים לבניית מקלטים), התש"ן-1990, not from Israeli Standard 4422. IS 4422 governs the blast door, window and frame items fitted into the space. Attributing an area or a thickness to "IS 4422" is a common and wrong citation, and תקנה 201 (location) is routinely quoted where תקנה 208 (thicknesses) is meant.

Headline figures: 9 sq m net minimum and 22.5 cubic metres (תקנה 197א), clear height 2.5 to 2.8 m (תקנה 198(א)), external wall not less than 25 cm of reinforced concrete (תקנה 208). A mamad may not serve as a kitchen, bathroom or toilet. The full dimension table, the hardship floor, the protective-wall rule and the confrontation-area bathroom allowance are in `references/shelter-types-comparison.md`.

Do not quote a blast-door thickness to a user; it is a manufacturer specification, not a regulated figure, and it is on the door's own approval plate. Israeli Standard 4422 is paywalled, so do not paraphrase its clauses from secondary sources.

## Time-to-Shelter by Region

Pikud Ha'Oref calls this the protection time (זמן התגוננות). The official set has exactly six values: immediate, 15, 30, 45 seconds, one minute, and a minute and a half. Most localities are at 90 seconds. The value is fixed for a locality and does not change with the direction the fire comes from.

**Two operational rules worth stating to any user:**

- **The siren duration equals the protection time.** If it is still sounding, you still have time. If it stops before you arrive, lie on the ground and protect your head.
- **Exception on the confrontation line (קו עימות):** in some of these localities the siren runs 15 seconds but required arrival is immediate. Do not read the siren as a countdown there.

| Protection time | Example localities (verified 2026-08-19) |
|---|---|
| Immediate (0 s) | Avivim. This is the only locality in the official table with a genuine zero. |
| 15 seconds | Kiryat Shmona, Metula, Manara, Yiftach, Sderot, Nahal Oz, Be'eri, Kfar Aza |
| 30 seconds | Ashkelon, Safed, Netivot |
| 45 seconds | Ashdod, Akko, Carmiel, Katzrin, Ofakim, Kiryat Gat |
| 60 seconds | Be'er Sheva |
| 90 seconds | Tel Aviv, Jerusalem, Haifa, Netanya, and most of the rest of the country |

**This table changes.** In 2026 Pikud Ha'Oref extended the protection time in 161 localities across the north and Haifa from 60 to 90 seconds, which is why older references still show Haifa at 60. Pre-2024 references also show 180 seconds for Kiryat Shmona and Metula; that figure is long obsolete, and so is treating those two towns as zero-second localities, which they are not. Use `scripts/shelter_finder.py` for the full 1,418-locality table, and re-verify the user's own locality at oref.org.il.

**How to check a zone:** enter the locality in the oref.org.il home-page lookup, adding the street for a city split into several alert zones. Or call 104.

## The Multi-Stage Warning System

For missile fire from distant launch areas, Pikud Ha'Oref publishes three stages. Treat each as a separate instruction and follow it in order.

1. **Preliminary advisory (הנחיה מקדימה)**: "alerts are expected in your area in the coming minutes." Use the time to move closer to the best protected space available to you. Pikud Ha'Oref describes this as "a few minutes" and publishes no fixed figure; do not quote one. It is issued only where the fire originates far enough away, and only when it is possible.
2. **Alert (התרעה)**: app, sirens, the national emergency portal and broadcast media. Enter the best protected space within your protection time, close the blast door by turning the handle through 90 degrees, confirm the window is fully closed, and stay inside.
3. **Release message (הודעת שחרור)**: an explicit message that the event is over. Read the text of every message, because different areas can receive different instructions.

**A preliminary advisory is not an alert, and an alert can arrive without one.** The alert is what determines action.

### Fire from Lebanon: a separate, much shorter advisory

Pikud Ha'Oref also issues a preliminary advisory for rocket and missile fire from Lebanon, carrying the heading "איום מלבנון - התקרבו למרחב המוגן". Because Lebanon is close, the lead time is far shorter than for Iran or Yemen, and it is not uniform:

| Area | Lead time before the alert |
|---|---|
| Confrontation line (קו עימות) | A few seconds, when an advisory is issued at all |
| Northern region | Up to about one minute |
| Rest of the country | Up to about two minutes |

Not every Lebanese launch can be preceded by an advisory. This advisory covers rockets and missiles only, and is distributed by Cell Broadcast, the Pikud Ha'Oref app, and the Pikud Ha'Oref Telegram channels.

### App colour and sound scheme

The Pikud Ha'Oref app pairs every instruction with a colour, an icon and a dedicated sound:

- **Yellow**, dedicated tone: a threat that may reach you. Prepare.
- **Red**, siren tone: the threat is arriving now. Enter the protected space.
- **Green**, a further dedicated tone: the event is over and the danger has passed.

The app distinguishes an alert at your own location from one in an "area of interest" you configured, so configure those deliberately.

### When You May Leave the Protected Space

**Stay in the protected space until Pikud Ha'Oref issues an explicit instruction to leave.** This applies to every rocket and missile alert, at every range, from every origin.

There is no 10-minute rule for leaving a protected space. Older guidance that told users to wait 10 minutes after the last impact and then exit has been superseded, and repeating it will send someone out early. Pikud Ha'Oref states plainly that leaving a protected space before an explicit instruction endangers life.

The only place 10 minutes still appears in Pikud Ha'Oref guidance is the opposite case: someone caught in the open with no building nearby should lie on the ground and protect their head for at least 10 minutes. There it is a minimum to stay down, not a permission to get up.

## How to Find a Shelter

### Option 1: Pikud Ha'Oref App (official)

- Download "Pikud HaOref" (פיקוד העורף) from the App Store or Google Play.
- Shows shelter locations near your GPS position.
- Delivers the preliminary advisory, the alert and the release message, with the colour and sound scheme above.

### Option 2: RedAlert / Tzofar / Tzeva Adom (third-party)

- RedAlert (redalert.me) is widely used as a backup channel; the vendor reports over 3,000,000 downloads and a 4.7 star rating. Treat any speed claim as the vendor's, not a verified fact.
- Tzofar / Tzeva Adom (tzevaadom.co.il) provides alerts via app, website, Chrome extension, Telegram, WhatsApp, and X.
- Pikud Ha'Oref states these apps are supplements, not replacements.

### Option 3: Your Municipality

- Contact your local authority (mo'atza mekomit / iriya). Municipalities maintain lists of public shelters in their jurisdiction.
- Many municipal websites publish shelter maps. State Comptroller report (2026) found significant variance in municipal shelter readiness; do not assume your nearest public shelter is open.

### Option 4: Pikud Ha'Oref Hotline

- **104**, the Pikud Ha'Oref information centre, 24/7.
- **052-9104104** for SMS or WhatsApp, which is also the accessible channel for deaf and hard-of-hearing users.
- There is no separate English-language phone line. Language (Hebrew, Arabic, English, Russian) is selected in the app and on the national emergency portal.
- Do not publish 1207 as a Pikud Ha'Oref number. It appears on third-party aggregators but on no Pikud Ha'Oref channel.

### Option 5: Physical Signs

- Public shelters are marked with brown signs reading "מקלט" (Miklat), and newer areas add blue directional signs.

## Preparing Your Mamad

### Essential Checklist (per Pikud Ha'Oref Recommendations)

1. **Clear the room.** Many families use the mamad as storage or a bedroom; the door and window must close fully. An unusable mamad is the same as having no mamad.
2. **Test the blast door.** Close it fully by turning the handle through 90 degrees, the same action used during an alert. Lubricate the hinges annually. Do not key-lock or bolt a mamad.
3. **Practice closing the window shutter.** Know which direction the handle turns.
4. **Water.** Pikud Ha'Oref specifies 3 liters per person per day for 3 days, so 9 liters per person. Replace the bottles and check the food stock and its expiry every three months.
5. **Non-perishable food** that does not need refrigeration or cooking.
6. **Lighting and communication.** Flashlight, spare batteries, charged power bank.
7. **Battery radio.** Tune to the relevant REGIONAL station, not a national frequency. Frequencies and TV channels: `references/alert-response-guide.md`. Pikud Ha'Oref does not name Galei Zahal 102.3 or Reshet Bet 95.5, which older guidance did.
8. **First aid kit, 3 days of personal medications, printed prescriptions.**
9. **Hygiene supplies, cash, cards, and copies of IDs, insurance and medical information in a sealed bag.**
10. **Per household needs:** formula, nappies, comfort items and small games for children; food, water and a carrier or leash for each pet.

Store the kit, water and food permanently inside the mamad, in a corner that does not block movement.

### NBC Protection

If your mamad has an NBC filtration system:
- Service the system on the manufacturer's schedule. Filters expire; an expired filter provides zero protection.
- Keep gas masks accessible (distributed by Pikud Ha'Oref during heightened alerts).
- During an event, close the blast door and window shutter fully and switch the system to ventilation mode.

## Building a Private Mamad

**Check eligibility first.** The permit-exemption route in סימן ו'1 of תקנות התכנון והבנייה (עבודות ומבנים הפטורים מהיתר) is NOT a general route for any building without a mamad. It covers only a **low-rise dwelling unit** (no more than two storeys above ground) or a **ground-attached dwelling unit** (none above or below it), in each case one that has no mamad. An apartment in a five-storey pre-1992 block is not covered; that case goes through the ordinary building-permit process with the local planning committee. Telling the owner otherwise sends them down a route that does not exist for them.

Where eligible: a licensed request author (architect, engineer or building technician) files online through Pikud Ha'Oref's licensing system at **oref-rishuy.org.il**; the competent authority answers within 14 days (תקנה 30ג(ב)); a registered structural engineer certifies the finished mamad; and notice of completion goes to the licensing authority and the competent authority within 45 days (תקנה 30ד). The route is a temporary order running three years from 26.10.2023, already amended three times, so confirm its current status rather than assuming expiry or extension.

## Buildings Without a Mamad

If your building was built before 1992 and has no mamad:

### Priority Order of Protection

1. **Miklat (public shelter)** if you can reach it within your zone's time limit.
2. **Mamak (floor shelter)** if your building has one.
3. **Internal stairwell**, meaning one with no windows and no external walls.
4. **Interior room** with the most walls and the fewest windows and openings. An internal hallway works. Avoid a room lined with ceramic, porcelain or glass that can shatter.

Do not use a parking garage that Pikud Ha'Oref has not approved as a protected space. An unapproved garage is not shelter.

### Stairwell Protocol

Pikud Ha'Oref's rule counts floors ABOVE you only, and there is no "one floor below" requirement:

- **Building over three storeys:** stay on a flight of stairs that has at least two floors above it.
- **Building under three storeys:** stay on the middle floor's flight of stairs.
- **In both cases:** do not stay on the entrance floor.
- Stay on the flight of stairs itself, not in the open landing area of the floor.
- Sit against the internal wall, below the window line, away from the lift doors.
- Cover your head with your hands. Do NOT use the elevator.

If you use an interior room instead, sit against an internal wall, below the window line, and not facing the door.

## If Caught Outdoors

When a siren sounds and you cannot reach a shelter in time:

1. **Near a building:** enter it and follow the building-without-mamad protocol.
2. **Open area:** lie face down on the ground and protect your head with your hands, away from buildings (falling debris) and vehicles. Lying down is not a formality: Pikud Ha'Oref puts the exposure to fragments at 100% standing and 85% crouching, against 10% lying down. Stay down for at least 10 minutes.
3. **In a vehicle:** with no alert, keep driving and move closer to a better protected space. On an alert, slow down, move right, stop on the shoulder, **switch off the engine**, check the road is clear, exit and enter a nearby miklat or stairwell. With no building nearby, move past the shoulder or guardrail, lie down and protect your head. Watch for other drivers braking for the shoulder too.
4. **Never stop under a bridge.** A bridge does not protect against a nearby impact: it can be hit by the blast and collapse, and blast and fragments from a ground impact spread sideways past its open flanks.
5. **In a tunnel:** if you are already inside the tunnel and can stop safely in a safety bay, you may stop there. If not, stop safely on the roadside outside the tunnel, exit the vehicle, move past the shoulder or guardrail, lie down and protect your head.
6. **If you cannot lie down** because of a physical limitation, crouch as low as you can and protect your head.

## Other Alerts on the Same System

**Not every alert means the rocket protocol.** Pikud Ha'Oref uses the same channels for several threats, and the sound tells you which one:

- **A rising-and-falling siren, or the Tzeva Adom alert:** rocket or missile fire. Enter the protected space within your protection time.
- **A short siren burst followed by spoken text:** any other threat. The text names the threat and the required action. Read it.
- **A short burst then "חדירת כלי טיס עוין":** hostile aircraft or drone. Enter the best protected space you have immediately, and stay there unless a further alert or instruction arrives. This alert can be the only warning; treat any unexplained explosion as an alert.

The app states the threat and the action in the device's configured language (Hebrew, Arabic, English, Russian), and can deliver a 10-second vibration for deaf and hard-of-hearing users, with a torch flash on Android.

**Read the alert before acting on it.** Where the text tells the user to do something other than enter a protected space, follow the text. This skill's priority order is written for the rocket and missile case.

## An Alert in a Crowd or a Public Venue

Noise makes an alert hard to hear, and a crowd rushing at once causes crush injuries. The guidance covers shopping centres, entertainment shows, weddings, synagogues and cultural events:

1. **Organisers must stop the event immediately on the alert and tell the audience.**
2. If lying down is possible, everyone lies on the ground and protects the head with the hands, against a wall or cover if there is one.
3. If lying down is not possible, crouch as low as possible to reduce the body's silhouette, and protect the head with the hands.
4. **At a seated indoor event, stay seated** and protect the head with the hands.

The closer to the ground, the lower the risk from fragments. In an unfamiliar crowded building follow the venue's staff and public-address system rather than running for the street.

## After an Impact Nearby

Some munitions disperse smaller submunitions, and part of them can remain on the ground unexploded after an impact. **They can detonate on contact, and being near them endangers life.** Interceptor and booster fragments land the same way.

The rule is three words: **move away, move others away, report.**

- Move away, keep the curious away, and report any suspicious object to the security forces immediately.
- **Do not photograph** fallen ordnance or unidentified objects, do not stand near them, and never touch them.
- Scan a balcony, yard or playground before children play, and teach them what to do if they find something.

**Life-safety override on the stay-inside rule.** Staying until an explicit instruction governs the missile threat. It is not a reason to remain in a space that has itself become dangerous: fire, smoke, a gas smell, or structural damage. Leave, get clear, and call the service you need. 101 is Magen David Adom, 100 the police, 102 fire and rescue, 103 the electric corporation. 104 is an information centre, not a dispatch line.

## Workplace and School Procedures

### Employer Obligations

Pikud Ha'Oref does not publish the employment-law side and refers employers to the Ministry of Labour, which is where the binding duties live: providing a protected space, appointing a safety officer, drills, and pay during emergency absence.

- Identify the designated protected space and its capacity first, and check people can actually reach it inside the site's protection time.
- Post the emergency procedure in the languages the workforce actually reads, not only Hebrew.
- Route the legal duties themselves (safety-officer appointment, mandatory drill frequency, record keeping) to the Ministry of Labour. Do not assert a drill frequency or a headcount trigger from memory.

### School Protocols

- **Do not tell a parent their school has a maman.** The protected space varies by school and by build date: some have a maman, some use a miklat or a mamak, and the January 2026 State Comptroller report on protection and sheltering in local authorities documents gaps. Have the user confirm with the school and with the local authority's emergency officer.
- Teachers are responsible for orderly movement to the protected space, and pupils with mobility limitations are best placed in classrooms near it.
- Drill frequency is set by the Ministry of Education per school year and security posture. Direct users there rather than quoting a number.

## Accessibility

### People with Disabilities

- The framework statute is חוק שוויון זכויות לאנשים עם מוגבלות, התשנ"ח-1998. The accessibility chapter was added by תיקון מס' 2, התשס"ה-2005, which is where the widely-quoted "2005" comes from. Shelter accessibility itself sits in secondary legislation: תקנות ההתגוננות האזרחית (התאמות נגישות במקלטים), התשע"ו-2016, plus the 2022 regulations on accessibility of emergency evacuation and reception, which require an accessible route to the protected space serving a reception facility.
- Mamad doors are heavy; people with mobility limitations should practice opening them or arrange for assistance.
- Some municipalities maintain designated accessible shelters; contact your local authority.

### Elderly and Mobility-Limited Residents

- **Arrange it in advance**: a neighbour or the vaad bayit who will come, and registration with Pikud Ha'Oref. That is the primary answer. An interior room on the lowest accessible floor is a LAST resort, and it is the weakest option in the priority order above, so use it only when nothing better is reachable.
- Inform neighbors or building committee (vaad bayit) so they can assist during an alert.
- Register with Pikud Ha'Oref for special-needs assistance by calling 104, or by SMS or WhatsApp to 052-9104104.

## Sheltering With Pets

Keep a carrier or leash for each animal in or near the mamad, plus 3 days of food and water for the pet, and put small animals in carriers before the siren where possible. Cats hide when startled, so close interior doors ahead of an expected alert window. Access for animals to a SHARED space (a public miklat, a mamak, a maman) is set by the operating authority or institution, not by Pikud Ha'Oref, so check yours in advance rather than at the door.

## Examples

### Example 1: New oleh in Tel Aviv asks "where do I shelter?"

User says: "I just moved to Florentin, Tel Aviv, and I have no idea what to do when sirens sound."

Expected answer: Tel Aviv is in the 90-second band. The user should (1) identify their building's mamad or stairwell, (2) install the Pikud Ha'Oref app, (3) install RedAlert as a backup, (4) at the next siren follow the 90-second window to reach the mamad or interior stairwell, and (5) stay there until a release message arrives. Confirm zone at oref.org.il.

### Example 2: Family in Sderot has 15 seconds and a toddler

User says: "We have a baby and 15 seconds. The mamad is full of boxes."

Expected answer: Clear the mamad today (it is the single most common failure mode). Pre-position the baby's carrier, formula, diapers, and water inside the mamad. Drill the route from the most-used parts of the home to the mamad door. Confirm the blast door closes fully.

### Example 3: User caught driving on Highway 1 during an alert

User says: "I just got an alert on Highway 1 between Jerusalem and Tel Aviv. What do I do?"

Expected answer: Slow down, move right, stop on the shoulder, switch off the engine, check the road is clear and get out. Enter a nearby building or stairwell if there is one. If not, move past the shoulder or guardrail, lie down and protect your head. Do not stop under a bridge. If already inside a tunnel and a safety bay is reachable, stopping there is permitted. Wait for an explicit instruction from Pikud Ha'Oref before resuming, not a fixed number of minutes.

## Bundled Resources

See the `references/` directory for:
- `references/alert-response-guide.md`, telling the alerts apart, the do-not-run rule, ventilation between alerts, crowded venues, unexploded ordnance, release-message channels, and the full emergency-number list. **Read this one whenever the question is about the moments during or after an alert.**
- `references/shelter-preparation-checklist.md`, printable preparation checklist.
- `references/shelter-types-comparison.md`, comparison of shelter types plus the full mamad dimension table.

See the `scripts/` directory for:
- `scripts/shelter_finder.py`, looks up a locality's protection time and returns the matching sheltering guidance. Accepts Hebrew or English names.
- `scripts/protection_times.json`, all 1,418 localities with their protection time, generated from Pikud Ha'Oref's own district table. Carries its own `snapshot_date`. Refresh it with `python3 scripts/shelter_finder.py --refresh`. Verify against oref.org.il for the user's exact address before acting on it.

## Gotchas

1. **Mamad as storage.** Most families use the mamad for storage, making it impossible to enter quickly. The single most common failure is not being able to close the blast door because of furniture or boxes. An unusable mamad is the same as having no mamad.

2. **Stairwell floor confusion.** The "not top or bottom floor" rule refers to the structural floor of the stairwell, not the user's apartment floor. In a 4-story building, sit on the stairs between floors 1 to 3, not on the roof stairwell or the ground-floor entrance area.

3. **Time-to-shelter is absolute.** 15 seconds means 15 seconds from siren to closed door. If the nearest miklat is a 2-minute walk, you cannot use it in a 30-second zone. Know your actual transit time, not the theoretical distance.

4. **Public shelter locked.** Municipal miklat shelters are sometimes locked during non-emergency periods. They should be opened by local authorities when the security situation escalates. If you find a locked shelter during an alert, report it to your municipality and use the next closest option.

5. **NBC filters need maintenance.** Gas mask filters and NBC systems expire. An expired filter provides zero protection. Check expiration dates annually.

6. **There is no 10-minute rule for leaving a protected space, at any range.** This is the single most dangerous piece of stale guidance still circulating, including in older versions of this skill. The instruction is to stay until Pikud Ha'Oref issues an explicit instruction to leave. If a user quotes the 10-minute rule at you, correct them.

7. **A preliminary advisory is not an alert.** It means "get closer to a protected space", not "enter it now". The alert is the trigger. Equally, an alert can arrive with no advisory ahead of it, and an advisory can arrive with no alert after it. Never present the advisory as a guaranteed countdown, and never quote a fixed number of minutes for it.

8. **Cities are split into alert zones, but that is not the same as being split across protection-time bands.** Tel Aviv, Jerusalem and Haifa each have several alert polygons, so a siren can sound in one part of the city and not another, which is why oref.org.il asks for a street. In the current official table the protection time is uniform within each of those cities. Verify the address rather than assuming either way.

9. **Do not quote a mamad figure to "Israeli Standard 4422".** The areas, thicknesses and heights are in the 1990 civil-defence construction-specification regulations. IS 4422 covers the door, window and frame items. Miscitation here is endemic in secondary sources.

## Recommended MCP Servers

- **pikud-haoref**, wraps the Pikud Ha'Oref public alert feed so an agent can query the live siren status for a given city or geo-coordinate. Useful when an agent needs to confirm an active alert before guiding a user.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Pikud Ha'Oref (Home Front Command) | https://www.oref.org.il | Protection-time lookup, warning stages, release messages, protected-space requirements |
| Pikud Ha'Oref district table (machine-readable) | https://www.oref.org.il/districts/districts_heb.json | Authoritative protection time per locality (`migun_time`, in seconds). This is the table `scripts/protection_times.json` is generated from |
| Preliminary advisory for fire from Lebanon | https://api.oref.org.il/api/v1/articles//heb/articles/info/iron-swords/1140 | Lead times by area, the advisory heading, distribution channels |
| Warning stages and leaving the protected space | https://api.oref.org.il/api/v1/articles//heb/articles/info/iron-swords/1128 | The three stages, and the rule that you stay until an explicit instruction |
| Emergency kit | https://api.oref.org.il/api/v1/articles//heb/articles/info/preparing-protected-space/1201 | Water and food quantities, required and recommended equipment |
| Pikud Ha'Oref licensing system | https://www.oref-rishuy.org.il | Submit a private mamad construction request, track approval |
| Standards Institution of Israel | https://www.sii.org.il/he/standardization/ | Israeli Standard 4422 (blast door, window and frame items). The standard itself is paywalled |
| Civil-defence construction specifications | https://he.wikisource.org/wiki/%D7%AA%D7%A7%D7%A0%D7%95%D7%AA_%D7%94%D7%94%D7%AA%D7%92%D7%95%D7%A0%D7%A0%D7%95%D7%AA_%D7%94%D7%90%D7%96%D7%A8%D7%97%D7%99%D7%AA_(%D7%9E%D7%A4%D7%A8%D7%98%D7%99%D7%9D_%D7%9C%D7%91%D7%A0%D7%99%D7%99%D7%AA_%D7%9E%D7%A7%D7%9C%D7%98%D7%99%D7%9D) | Mamad area and volume (תקנה 197א), height and width (תקנה 198), thicknesses (תקנה 208), protective wall |
| State Comptroller report (January 2026) | https://library.mevaker.gov.il/sites/DigitalLibrary/Documents/2026/Emergency/2026-Emergency-104-Local.pdf | Municipal shelter readiness audit, gaps by locality |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Mamad door will not close | Check for obstructions. Lubricate hinges. If structurally damaged, contact your building committee to arrange a licensed repair. |
| Cannot find public shelter | Use the Pikud Ha'Oref app or call 104. Ask neighbors or the vaad bayit. |
| Do not know your time-to-shelter zone | Visit oref.org.il, enter your city or street. Or call 104. |
| Building has no shelter at all | Use the stairwell protocol. Consider installing a private mamad via oref-rishuy.org.il (engineer or architect required). |
| Shelter is inaccessible (wheelchair) | Contact your municipality for accessible shelter locations. Register with Pikud Ha'Oref via 104. |
| Conflicting messages: app says "stay", someone quotes the 10-minute rule | Follow the app. The 10-minute rule for leaving a protected space no longer exists at any range. Wait for the explicit instruction from Pikud Ha'Oref. |
| Received a preliminary advisory but no alert followed | That happens by design and is not a malfunction. Stay near the protected space, use the time to prepare, and treat the alert, not the advisory, as the trigger. |
| A reference or an older document gives a different protection time for the locality | Trust oref.org.il or `scripts/protection_times.json` over any prose. The table was revised in 2026 for 161 northern and Haifa localities, so older figures are systematically low there. |
