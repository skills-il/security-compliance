#!/usr/bin/env python3
"""
Shelter Finder Helper

Looks up the Pikud Ha'Oref protection time (zman hitgonenut) for a locality and
returns the matching sheltering guidance.

The lookup table lives in scripts/protection_times.json, generated from Pikud
Ha'Oref's own machine-readable district table:
https://www.oref.org.il/districts/districts_heb.json

That table is revised several times a year (161 northern and Haifa localities
moved from 60 to 90 seconds in 2026). This snapshot is dated inside the JSON.
It is a convenience, never an authority: verify the user's exact address at
oref.org.il or call 104 before acting on any value here.

Usage:
    python3 shelter_finder.py "tel aviv"
    python3 shelter_finder.py "אשקלון"
    python3 shelter_finder.py --refresh     # re-download the official table
"""

import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "protection_times.json")
OFFICIAL_URL = "https://www.oref.org.il/districts/districts_heb.json"

# English aliases for the largest localities. Hebrew names come from the official
# table and need no aliasing.
ALIASES = {
    "tel aviv": "תל אביב", "jerusalem": "ירושלים", "haifa": "חיפה",
    "netanya": "נתניה", "ashdod": "אשדוד", "ashkelon": "אשקלון",
    "beer sheva": "באר שבע", "beersheba": "באר שבע", "be'er sheva": "באר שבע",
    "sderot": "שדרות", "netivot": "נתיבות", "ofakim": "אופקים",
    "kiryat gat": "קריית גת", "kiryat shmona": "קריית שמונה",
    "metula": "מטולה", "manara": "מנרה", "yiftach": "יפתח", "avivim": "אביבים",
    "safed": "צפת", "tzfat": "צפת", "carmiel": "כרמיאל", "karmiel": "כרמיאל",
    "akko": "עכו", "acre": "עכו", "nahariya": "נהריה", "katzrin": "קצרין",
    "tiberias": "טבריה", "nazareth": "נצרת", "afula": "עפולה",
    "kiryat ata": "קריית אתא", "kiryat bialik": "קריית ביאליק",
    "kiryat motzkin": "קריית מוצקין", "kiryat yam": "קריית ים",
    "rishon lezion": "ראשון לציון", "petah tikva": "פתח תקווה",
    "ramat gan": "רמת גן", "holon": "חולון", "bat yam": "בת ים",
    "bnei brak": "בני ברק", "herzliya": "הרצליה", "kfar saba": "כפר סבא",
    "raanana": "רעננה", "rehovot": "רחובות", "modiin": "מודיעין",
    "eilat": "אילת", "dimona": "דימונה", "arad": "ערד",
}


def load_table():
    with open(DATA_FILE, encoding="utf-8") as fh:
        raw = json.load(fh)
    table = {}
    for seconds, names in raw["seconds_to_localities"].items():
        for name in names:
            table[name] = int(seconds)
    return raw, table


def refresh():
    """Re-download the official district table and rewrite protection_times.json."""
    import collections
    import urllib.request
    from datetime import date

    with urllib.request.urlopen(OFFICIAL_URL, timeout=30) as resp:
        records = json.loads(resp.read().decode("utf-8"))
    # Rows that are national notices, not places. They sit at migun_time 0 and a
    # substring query would otherwise return "immediate" for them.
    PSEUDO = {"כל הארץ", "ברחבי הארץ", "בחלק מהאזורים בארץ"}
    agg = {}
    for rec in records:
        label = (rec.get("label_he") or "").strip()
        if not label:
            continue
        name = label.split(" - ")[0].split(",")[0].strip()
        if name in PSEUDO:
            continue
        # A locality split across zones must resolve to its SHORTEST time. Today
        # no locality is split, but the table is revised several times a year and
        # last-record-wins would silently hand the losing zone extra seconds.
        agg[name] = min(rec["migun_time"], agg.get(name, rec["migun_time"]))
    by_band = collections.defaultdict(list)
    for name, seconds in sorted(agg.items()):
        by_band[str(seconds)].append(name)
    out = {
        "source": OFFICIAL_URL,
        "snapshot_date": date.today().isoformat(),
        "note": "Protection time (zman hitgonenut) in seconds, by locality. Pikud "
                "Ha'Oref revises this table several times a year; re-verify at "
                "oref.org.il before acting on it.",
        "seconds_to_localities": {k: by_band[k] for k in sorted(by_band, key=int)},
    }
    with open(DATA_FILE, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
    print(f"Refreshed {len(agg)} localities into {DATA_FILE}")


def get_shelter_time(city):
    """Look up the protection time for a locality name (Hebrew or English)."""
    raw, table = load_table()
    query = city.strip()
    key = ALIASES.get(query.lower(), query)

    if key in table:
        return {"city": city, "seconds": table[key], "found": True,
                "matched": key, "snapshot": raw["snapshot_date"]}

    partial = [name for name in table if key and key in name]
    if len(partial) == 1:
        return {"city": city, "seconds": table[partial[0]], "found": True,
                "matched": partial[0], "snapshot": raw["snapshot_date"]}
    if len(partial) > 1:
        bands = {table[name] for name in partial}
        if len(bands) == 1:
            return {"city": city, "seconds": bands.pop(), "found": True,
                    "matched": ", ".join(partial[:5]), "snapshot": raw["snapshot_date"]}
        return {"city": city, "found": False, "candidates": partial[:10],
                "message": "Several localities match and they are not in the same band. "
                           "Ask the user for the exact locality, or check oref.org.il."}

    return {"city": city, "found": False,
            "message": "Locality not in the bundled table. Check oref.org.il or call 104."}


def shelter_guidance(seconds):
    """Return sheltering guidance for a protection time, in seconds."""
    if seconds == 0:
        return ("Immediate. You must already be in the protected space. Stay inside it "
                "during active rounds; a public shelter you have to walk to is not reachable.")
    if seconds <= 15:
        return ("15 seconds. Only the mamad, mamak or an internal stairwell in your own "
                "building is reachable. Do not plan on a public shelter.")
    if seconds <= 30:
        return ("30 seconds. The nearest mamad or a miklat in the same building. "
                "Measure your real transit time, not the map distance.")
    if seconds <= 45:
        return "45 seconds. Mamad, or a miklat you have timed at under 30 seconds on foot."
    if seconds <= 60:
        return "60 seconds. Mamad or a nearby miklat. Internal stairwell if the building has neither."
    return ("90 seconds. Mamad or a nearby miklat. Internal stairwell protocol if the "
            "building has neither.")


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 1
    if sys.argv[1] == "--refresh":
        refresh()
        return 0

    result = get_shelter_time(" ".join(sys.argv[1:]))
    print(f"Locality: {result['city']}")
    if result["found"]:
        print(f"Matched: {result['matched']}")
        print(f"Protection time: {result['seconds']} seconds")
        print(f"Guidance: {shelter_guidance(result['seconds'])}")
        print(f"Table snapshot: {result['snapshot']}. Verify at oref.org.il or call 104.")
    else:
        print(f"Status: {result['message']}")
        if result.get("candidates"):
            print("Candidates: " + ", ".join(result["candidates"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
