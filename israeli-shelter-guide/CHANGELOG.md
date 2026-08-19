# Changelog

## 1.3.0 - 2026-08-19

Safety-critical correction pass. Every operational instruction was re-sourced from Pikud Ha'Oref's own content API and from primary regulations, replacing the secondary sources earlier versions relied on.

### Corrected (life-safety)
- **Removed the 10-minute after-siren rule.** Pikud Ha'Oref's instruction is to stay in the protected space until an explicit instruction to leave, at every range and from every origin. The previous short-range / ballistic split was obsolete and would have sent users out early. Ten minutes now appears only where Pikud Ha'Oref still uses it: as a minimum to stay lying down in the open.
- **Corrected six of nine city protection times** against the official district table: Kiryat Shmona and Metula are 15 seconds not immediate, Sderot is 15, Ashdod is 45 not 60, Haifa is 90 not 60 to 90, Akko, Carmiel and Katzrin are 45 not 30, Netivot is 30. Avivim is the only locality in the table at zero.
- **Removed 1207 as a Pikud Ha'Oref hotline.** The number appears on no Pikud Ha'Oref channel. Added 104 and the SMS/WhatsApp line 052-9104104, and removed the false claim of a separate English phone line.
- **Corrected the stairwell protocol.** The official rule counts floors above only (two above in a building over three storeys, the middle floor's flight below that) and has no "one floor below" requirement. Added the internal-stairwell requirement, the stay-on-the-flight rule, and the prohibition on unapproved parking garages.
- **Corrected the emergency water figure** to 3 litres per person per day for 3 days (9 litres), from 4 litres per day (12 litres).
- **Replaced the radio frequencies.** Pikud Ha'Oref names Kol BaRama, Kol Chai, Radio Darom, Galei Yisrael and Kan Moreshet, not Galei Zahal 102.3 or Reshet Bet 95.5.
- **Removed the invented 15-minute and 10-minute advisory timings.** Pikud Ha'Oref publishes three warning stages and describes the advisory only as "a few minutes".

### Added
- The preliminary advisory for fire from Lebanon, in force since 26 May 2026, with its per-area lead times and the rule that the alert, not the advisory, determines action.
- The app colour and sound scheme introduced 18 May 2026 (yellow, red, green).
- The 2026 extension of protection time in 161 northern and Haifa localities from 60 to 90 seconds.
- The siren-duration-equals-protection-time rule and the confrontation-line exception.
- Vehicle detail: switch off the engine, never shelter under a bridge, and the tunnel safety-bay rule.
- `scripts/protection_times.json`, all 1,418 localities generated from Pikud Ha'Oref's district table, with a `--refresh` mode on `shelter_finder.py`.

### Corrected (legal citations)
- Mamad dimensions, wall and ceiling thicknesses and ceiling height are attributed to תקנות ההתגוננות האזרחית (מפרטים לבניית מקלטים), התש"ן-1990, not to Israeli Standard 4422. Removed the unsourced 7 cm door thickness and the incorrect "12 sq m plus 3 sq m bathroom" expansion figure.
- Scoped the permit-exemption route for adding a mamad to low-rise and ground-attached dwelling units, which is what סימן ו'1 actually covers. It was previously presented as available to any building without a mamad.
- Accessibility framework corrected to חוק שוויון זכויות לאנשים עם מוגבלות, התשנ"ח-1998 with the 2005 accessibility chapter, and shelter accessibility placed in the 2016 regulations.
- Employer and school drill obligations no longer state a frequency or a headcount trigger; Pikud Ha'Oref publishes none and defers to the Ministry of Labour.

## 1.2.2 - 2026-08-13

Re-sourced the time-to-shelter bands to the Pikud HaOref protected-space article, which states them verbatim, after they had been left asserted in the body with no evidence. Added that the time is fixed per locality and does not vary with the direction of fire.

All notable changes to this skill are documented here.

## [1.2.1] - 2026-08-13

### Changed

- כל רשומות ה-evidence קיבלו ציטוט מילולי שנשלף בפועל מהמקור. טענות שלא נמצא להן מקור קריא הוסרו או צומצמו.
- קישור מנהל התכנון עודכן ל-gov.il/he/departments/iplan (הכתובת הקודמת מחזירה 403).

### Removed

- ההפניות לתקנה 30(ג) ו-30(ד) בתהליך בניית ממ"ד, בהיעדר מקור רשמי קריא שניתן לצטט ממנו.
- שורות "חוק ההתגוננות האזרחית (כנסת)" ו"כל זכות, מקלטים" מטבלת הקישורים, בהיעדר גישה קריאה לעמודים.
