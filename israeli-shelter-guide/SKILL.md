---
name: israeli-shelter-guide
description: Guide to finding and preparing shelters in Israel, including mamad (apartment safe room), mamak (floor safe room), maman (institutional safe room), and miklat (public shelter). Use when a user needs to find the nearest shelter, prepare a safe room according to Home Front Command guidelines, understand time-to-shelter by region, set up workplace emergency procedures, learn the Israeli shelter system as a new immigrant, or interpret the multi-stage early-warning notifications introduced for ballistic threats. Covers Israeli Standard 4422, time-to-shelter zones (immediate / 15 / 30 / 45 / 60 / 90 seconds), municipal shelter databases, accessibility law, sheltering with pets, vehicle protocols, and what to do if caught outdoors. Helps users protect themselves and their families during rocket and ballistic-missile alerts, especially those unfamiliar with the system. Do NOT use for building real-time alert integrations (use pikud-haoref-alerts), for per-threat safety protocols (use pikud-haoref-safety-protocols), or for non-Israeli emergency shelter systems.

license: MIT
compatibility: Knowledge-based skill. No tools, APIs, or network access required. Works on any agent that supports SKILL.md format.

---

# Israeli Shelter Guide

This skill provides guidance on finding, preparing, and using shelters in Israel during rocket and ballistic-missile alerts. It is based on publicly available Pikud Ha'Oref (Home Front Command) guidance as of May 2026. All life-safety numbers below should be cross-checked against the live Pikud Ha'Oref site or the 104 / 1207 hotline before acting on them in a real emergency.

## Description

Helps users:
- Identify which type of protected space they have (mamad, mamak, maman, miklat) and what to do in buildings that have none.
- Look up their region's time-to-shelter (immediate / 15 / 30 / 45 / 60 / 90 seconds).
- Understand the multi-stage early warning system Pikud Ha'Oref now publishes for ballistic threats from Iran (advance warnings, then siren, then explicit release message).
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

### Mamad Specifications (Israeli Standard 4422)

- **Minimum floor area**: 9 square meters (per IS 4422).
- **Expanded option** (2025 amendment): up to 12 sq m + 3 sq m bathroom for new construction.
- **Walls and ceiling**: reinforced concrete, minimum 25 cm thick, double-rebar reinforcement.
- **Ceiling height**: 2.5 to 2.8 m clear, no structural columns through the protected space.
- **Door**: steel blast door, approximately 7 cm thick.
- **Window**: steel-frame window with a blast shutter that closes from inside.
- **Blast wall (קיר הדף)**: required by default; per IS 4422 Amendment 4, can be omitted if a special blast door is installed and the mamad is at least 4 m from the external wall.
- **NBC filtration**: ventilation and filtering system connection point; turn on and set to "ventilation" mode when sheltering.

The full standard is published by the Standards Institution of Israel (sii.org.il, standard 4422 parts 1 and 2).

## Time-to-Shelter by Region

When a siren sounds, you have a limited number of seconds to reach a protected space. Pikud Ha'Oref defines five short bands (immediate, 15, 30, 45, 60 seconds) for border-proximity zones plus a default of 90 seconds (1.5 minutes) for most of the country. Always verify your own address at oref.org.il, since cities can be split across bands.

| Region | Time to Shelter | Example Cities |
|--------|----------------|----------------|
| Lebanon border (kav ha-imut) | 0 seconds (immediate) | Kiryat Shmona, Metula, Manara, Yiftach |
| Upper Galilee / Golan | 30 seconds | Safed, Carmiel, Akko, Katzrin |
| Gaza envelope (Otef Aza) | 0 to 15 seconds | Nir Am, Be'eri, Kissufim, Sderot |
| Western Negev | 15 to 30 seconds | Sderot, Netivot |
| Southern coast | 30 seconds | Ashkelon |
| Central Negev | 45 seconds | Ofakim, Kiryat Gat |
| Southern cities | 60 seconds | Ashdod, Be'er Sheva |
| Central Israel | 90 seconds | Tel Aviv, Jerusalem, Netanya |
| Haifa area | 60 to 90 seconds | Haifa, Krayot |
| Houthi or long-range threats | country-wide siren, 3 to 12 minutes warning | All districts (varies by intercept point) |

**Doctrine update (post-Iron Swords):** the "up to 180 seconds" figure for Kiryat Shmona / Metula from pre-2024 references is no longer accurate. Northern border communities adjacent to the Lebanon line have effectively zero warning time and Pikud Ha'Oref guidance is to remain inside the protected space whenever feasible during active rounds.

**How to check your zone:** visit oref.org.il, open the "התרעות" (Alerts) section, and enter your locality. For split cities use the street address. You can also call 104.

## The Multi-Stage Early Warning System (2025 to 2026)

Pikud Ha'Oref now publishes multiple notifications for ballistic missile threats from Iran. Treat each stage as a separate instruction and follow it in order:

1. **Advance advisory**, roughly 15 minutes before impact: app notification to stay near a protected space and avoid open areas.
2. **Improvement warning**, roughly 10 minutes before impact: app notification that sirens are expected in your area in the coming minutes; finish moving to the protected space and prepare to seal it.
3. **Siren and app alert**, roughly 90 seconds before impact in most areas (less near borders): the standard rising-falling siren plus an app alert. Enter the protected space and close the door.
4. **Release message** (הודעת שחרור): Pikud Ha'Oref issues an explicit message in the app and on Cell Broadcast when it is safe to leave. For ballistic / Iran / Houthi scenarios, do **not** apply the classic 10-minute rule.

### After-Siren Rule (Short-Range vs. Ballistic)

- **Short-range fire (Gaza or Lebanon historical posture):** stay in the protected space for 10 minutes after the last impact.
- **Ballistic / Iran / Houthi scenarios:** the 10-minute rule does NOT apply. Stay put until an explicit release message arrives in the app or via Cell Broadcast. When in doubt, stay put.

## How to Find a Shelter

### Option 1: Pikud Ha'Oref App (official)

- Download "Pikud HaOref" (פיקוד העורף) from the App Store or Google Play.
- Shows shelter locations near your GPS position.
- Delivers the four-stage warnings above plus the release message.

### Option 2: RedAlert / Tzofar / Tzeva Adom (third-party)

- RedAlert (redalert.me) has dedicated push servers and is widely used as a faster alternative; 4.7-star rating with millions of downloads.
- Tzofar / Tzeva Adom (tzevaadom.co.il) provides alerts via app, website, Chrome extension, Telegram, WhatsApp, and X.
- Pikud Ha'Oref states these apps are supplements, not replacements, for the official channels.

### Option 3: Your Municipality

- Contact your local authority (mo'atza mekomit / iriya). Municipalities maintain lists of public shelters in their jurisdiction.
- Many municipal websites publish shelter maps. State Comptroller report (2026) found significant variance in municipal shelter readiness; do not assume your nearest public shelter is open.

### Option 4: Pikud Ha'Oref Hotline

- Hebrew: **1207**
- English and other languages: **104**
- Both available 24/7.

### Option 5: Physical Signs

- Public shelters are marked with brown signs reading "מקלט" (Miklat).
- In newer areas, blue directional signs point to the nearest shelter.

## Preparing Your Mamad

### Essential Checklist (per Pikud Ha'Oref Recommendations)

1. **Clear the room.** Many families use the mamad as storage or a bedroom; the door and window must close fully. An unusable mamad is the same as having no mamad.
2. **Test the blast door.** Close and lock it. Lubricate hinges annually.
3. **Practice closing the window shutter.** Know which direction the handle turns.
4. **Water.** Store 4 liters per person per day for at least 3 days (minimum 12 L per person).
5. **Non-perishable food** that does not need refrigeration or cooking.
6. **Lighting and communication.** Flashlight, spare batteries, charged power bank.
7. **Battery radio.** Galei Zahal (Galatz) 102.3 FM or Reshet Bet 95.5 FM for official updates.
8. **First aid kit and 3-day supply of personal medications.**
9. **Hygiene supplies, cash, and credit cards.**
10. **Documents.** Copies of IDs, insurance, medical info in a sealed bag.
11. **For families with children:** formula or milk substitutes, diapers, pacifiers, comfort items, small games.
12. **For pet owners:** pet food, carrier or leash for each animal.

Pikud Ha'Oref recommends storing the emergency kit, water, and food permanently inside the mamad in a corner that does not block movement.

### NBC Protection

If your mamad has an NBC filtration system:
- Service the system on the manufacturer's schedule. Filters expire; an expired filter provides zero protection.
- Keep gas masks accessible (distributed by Pikud Ha'Oref during heightened alerts).
- During an event, close the blast door and window shutter fully and switch the system to ventilation mode.

## Building a Private Mamad

If your building has no mamad, you may be eligible to add one. The current fast-track process (relaxed under the Iron Swords emergency framework, with an end-of-permit window in late 2026, verify before relying on the relaxation):

1. Appoint a licensed architect, engineer, or building technician as the request author (orech bakasha).
2. Submit the application through Pikud Ha'Oref's licensing system at **oref-rishuy.org.il**, with supporting documents per Regulation 30(ג).
3. Pikud Ha'Oref responds within 14 days (approval or rejection).
4. A structural engineer must certify, after construction, that the mamad meets IS 4422 and that construction did not damage the building's structural frame.
5. Within 45 days of completion, the request author updates the licensing authority and Pikud Ha'Oref per Regulation 30(ד).

Costs and exact procedures vary by municipality. Confirm directly with your local Vaadat HaTichnun (planning committee).

## Buildings Without a Mamad

If your building was built before 1992 and has no mamad:

### Priority Order of Protection

1. **Miklat (public shelter)** if you can reach it within your zone's time limit.
2. **Mamak (floor shelter)** if your building has one.
3. **Interior stairwell** with at least 2 floors above and 1 below you. Do NOT use the top floor or ground floor of the stairwell.
4. **Interior room** with the fewest exterior walls and windows. Bathroom or interior hallway can work.

### Stairwell Protocol

- Sit on the stairs, not on the landing.
- Position yourself against the inner wall (closest to the building center).
- Stay below the window line if there are stairwell windows.
- Cover your head with your hands.
- Do NOT use the elevator.

## If Caught Outdoors

When a siren sounds and you cannot reach a shelter in time:

1. **Near a building:** enter the nearest building and follow the building-without-mamad protocol.
2. **Open area:** lie face down on the ground, cover your head with your hands, stay away from buildings (falling debris) and vehicles.
3. **In a vehicle:** Pikud Ha'Oref guidance is to pull over safely, exit the vehicle, and enter a nearby building or stairwell. If no shelter is reachable, move away from the vehicle and lie face down. If you cannot safely exit (for example heavy traffic on a highway or inside a tunnel), bend below the window line and cover your head. Tunnels have not been formally endorsed as shelters; exit the tunnel as soon as the road allows and find a protected building.
4. **Near a bus stop shelter:** concrete bus stops provide some protection; enter and crouch low.

## Workplace and School Procedures

### Employer Obligations

- Every workplace must have a designated protected space.
- Employers must conduct shelter drills at least once per year.
- Emergency procedures must be posted in Hebrew and other languages relevant to the workforce.
- A safety officer (memune betihut) must be appointed.

### School Protocols

- Schools have a maman (institutional protected space).
- Teachers are responsible for orderly movement to the shelter.
- Practice drills are conducted multiple times per year.
- Students with mobility limitations are assigned ground-floor classrooms near the shelter.

## Accessibility

### People with Disabilities

- Public shelters must be accessible per the Equal Rights for Persons with Disabilities Law (Hok Negishut, 2005).
- Mamad doors are heavy; people with mobility limitations should practice opening them or arrange for assistance.
- Service animals are permitted in all shelters.
- Some municipalities maintain designated accessible shelters; contact your local authority.

### Elderly and Mobility-Limited Residents

- If you cannot reach a shelter within the time limit, use an interior room on the lowest accessible floor.
- Inform neighbors or building committee (vaad bayit) so they can assist during an alert.
- Register with Pikud Ha'Oref for special needs assistance (call 104 or 1207).

## Sheltering With Pets

Pets are welcome in protected spaces. Keep a carrier or leash for each animal in or near the mamad, plus a 3-day supply of food and water for the pet. Place small animals in carriers before the siren if possible. Cats, in particular, hide when startled; close interior doors a few minutes before expected alert windows so they cannot disappear under a bed when the siren sounds.

## Examples

### Example 1: New oleh in Tel Aviv asks "where do I shelter?"

User says: "I just moved to Florentin, Tel Aviv, and I have no idea what to do when sirens sound."

Expected answer: Tel Aviv is in the 90-second band. The user should (1) identify their building's mamad or stairwell, (2) install the Pikud Ha'Oref app, (3) install RedAlert as a backup, (4) at the next siren follow the 90-second window to reach the mamad or interior stairwell, and (5) stay there until a release message arrives. Confirm zone at oref.org.il.

### Example 2: Family in Sderot has 15 seconds and a toddler

User says: "We have a baby and 15 seconds. The mamad is full of boxes."

Expected answer: Clear the mamad today (it is the single most common failure mode). Pre-position the baby's carrier, formula, diapers, and water inside the mamad. Drill the route from the most-used parts of the home to the mamad door. Confirm the blast door closes fully.

### Example 3: User caught driving on Highway 1 during a ballistic alert

User says: "I just got an alert on Highway 1 between Jerusalem and Tel Aviv. What do I do?"

Expected answer: Pull over safely (do not stop in a tunnel). Exit the car if a building or stairwell is reachable. If not, move away from the vehicle and lie face down. Cover your head. After the siren, wait for the release message before resuming driving.

## Bundled Resources

See the `references/` directory for:
- `references/shelter-preparation-checklist.md`, printable preparation checklist.
- `references/shelter-types-comparison.md`, detailed comparison of shelter types.

See the `scripts/` directory for:
- `scripts/shelter_finder.py`, local lookup table that maps a city name (Hebrew or English) to its time-to-shelter band. Treat the table as a best-effort reference and verify against oref.org.il for the user's exact address.

## Gotchas

1. **Mamad as storage.** Most families use the mamad for storage, making it impossible to enter quickly. The single most common failure is not being able to close the blast door because of furniture or boxes. An unusable mamad is the same as having no mamad.

2. **Stairwell floor confusion.** The "not top or bottom floor" rule refers to the structural floor of the stairwell, not the user's apartment floor. In a 4-story building, sit on the stairs between floors 1 to 3, not on the roof stairwell or the ground-floor entrance area.

3. **Time-to-shelter is absolute.** 15 seconds means 15 seconds from siren to closed door. If the nearest miklat is a 2-minute walk, you cannot use it in a 30-second zone. Know your actual transit time, not the theoretical distance.

4. **Public shelter locked.** Municipal miklat shelters are sometimes locked during non-emergency periods. They should be opened by local authorities when the security situation escalates. If you find a locked shelter during an alert, report it to your municipality and use the next closest option.

5. **NBC filters need maintenance.** Gas mask filters and NBC systems expire. An expired filter provides zero protection. Check expiration dates annually.

6. **Do not apply the 10-minute rule to ballistic threats.** That rule is specifically for short-range fire from Gaza or Lebanon. For Iran / Houthi / ballistic scenarios wait for an explicit release message; the army has stated that staying longer than 10 minutes is often required.

7. **The early-warning notifications are not a siren.** The 15-minute and 10-minute app notifications for ballistic threats are advisories to prepare; they are not the "enter shelter now" signal. The siren itself is still the trigger for actually entering the protected space.

8. **Cities are split across zones.** Jerusalem, Tel Aviv, and Haifa each contain neighborhoods with different time-to-shelter bands. Always verify the user's specific street address at oref.org.il.

## Recommended MCP Servers

- **pikud-haoref**, wraps the Pikud Ha'Oref public alert feed so an agent can query the live siren status for a given city or geo-coordinate. Useful when an agent needs to confirm an active alert before guiding a user.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Pikud Ha'Oref (Home Front Command) | https://www.oref.org.il | Time-to-shelter zone lookup, multi-stage warnings, release messages, protected-space requirements |
| Pikud Ha'Oref licensing system | https://www.oref-rishuy.org.il | Submit a private mamad construction request, track approval |
| Standards Institution of Israel | https://www.sii.org.il | Israeli Standard 4422 (mamad), full PDF of the technical specification |
| Israel Planning Administration | https://www.gov.il/he/departments/planning_authority | Building code, mamad permit relaxations, public shelter construction |
| Ministry of the Interior | https://www.gov.il/he/departments/ministry_of_interior | Public shelter registry, municipal shelter maintenance responsibilities |
| Civil Defense Regulations (Knesset) | https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/default.aspx | Civil Defense Law, takanot ha-hitgonenut |
| Kol Zchut: shelters | https://www.kolzchut.org.il/he/שימוש_במקלט_בבית_משותף | Tenant rights, landlord obligations, shared shelter access |
| State Comptroller report (2026) | https://library.mevaker.gov.il/sites/DigitalLibrary/Documents/2026/Emergency/2026-Emergency-104-Local.pdf | Municipal shelter readiness audit, gaps by locality |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Mamad door will not close | Check for obstructions. Lubricate hinges. If structurally damaged, contact your building committee to arrange a licensed repair. |
| Cannot find public shelter | Use the Pikud Ha'Oref app or call 104. Ask neighbors or the vaad bayit. |
| Do not know your time-to-shelter zone | Visit oref.org.il, enter your city or street. Or call 104. |
| Building has no shelter at all | Use the stairwell protocol. Consider installing a private mamad via oref-rishuy.org.il (engineer or architect required). |
| Shelter is inaccessible (wheelchair) | Contact your municipality for accessible shelter locations. Register with Pikud Ha'Oref via 104. |
| Conflicting messages: app says "stay", classic 10-minute rule says "exit" | Follow the app. The 10-minute rule does not apply to ballistic threats. Wait for the explicit release message. |
| Receiving early-warning advisories but no siren | Do NOT leave the area near your protected space. Improve your shelter (water, phone, kit) and wait for the siren or release message. |
