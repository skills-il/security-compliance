#!/usr/bin/env python3
"""
Alert Protocol Lookup

Given an alert category number or name, returns the appropriate safety protocol.
Reference script for AI agents responding to emergency queries.

Usage:
    python alert_protocol_lookup.py 1
    python alert_protocol_lookup.py "earthquake"
    python alert_protocol_lookup.py "רעידת אדמה"
"""

import sys

PROTOCOLS = {
    1: {
        "name_en": "Missiles / Rockets",
        "name_he": "ירי רקטות וטילים",
        "action": "Enter shelter immediately. Close blast door and window shutter. Sit below window line against inner wall. Cover head.",
        "shelter_time": "10 minutes after last impact, or until category 13 all-clear",
        "outdoor": "Lie face down, cover head, away from buildings and vehicles",
        "vehicle": "Pull over, exit, move 10m away, lie face down. If can't exit: bend below windows",
        "critical": "Do NOT assume silence means all-clear. Wait for cat 13 or 10 min minimum."
    },
    2: {
        "name_en": "Hostile Aircraft Intrusion",
        "name_he": "חדירת כלי טיס עוין",
        "action": "Enter shelter. Close all doors and windows. Stay away from windows and exterior walls.",
        "shelter_time": "Until official all-clear (may be longer than missile alerts)",
        "outdoor": "Enter nearest building. If impossible, take cover behind solid structure.",
        "vehicle": "Pull over, enter nearest building if possible",
        "critical": "Drones may carry explosives. Treat as seriously as missile alerts."
    },
    3: {
        "name_en": "Earthquake",
        "name_he": "רעידת אדמה",
        "action": "DROP to hands and knees. COVER under sturdy table. HOLD ON until shaking stops.",
        "shelter_time": "Until shaking stops. Then check for structural damage before moving.",
        "outdoor": "Move to open area. Drop to ground. Cover head. Away from buildings/power lines.",
        "vehicle": "Pull over away from buildings/bridges. Stay in vehicle with seatbelt on.",
        "critical": "Do NOT enter mamad during earthquake! Blast door can trap you if structure shifts."
    },
    4: {
        "name_en": "Tsunami",
        "name_he": "צונאמי",
        "action": "Move inland and to high ground. At least 2km from coast or 30m elevation.",
        "shelter_time": "Until official all-clear. First wave is often not the largest.",
        "outdoor": "Move uphill immediately. If no high ground, go to 3rd+ floor of reinforced building.",
        "vehicle": "Drive inland/uphill. Abandon vehicle if roads are flooded.",
        "critical": "Warning signs: sea rapidly receding, loud ocean roar. Act even without official alert."
    },
    5: {
        "name_en": "Radiological Event",
        "name_he": "אירוע רדיולוגי",
        "action": "Enter building. Close windows/doors/ventilation. Activate NBC filter if available. Seal gaps.",
        "shelter_time": "Follow official instructions. May require evacuation.",
        "outdoor": "Remove outer clothing. Shower with soap. Do not eat outdoor food.",
        "vehicle": "Drive to nearest building. Close vehicle ventilation in the meantime.",
        "critical": "Remove and bag outer clothing if exposed. Do NOT scrub skin hard when washing."
    },
    6: {
        "name_en": "Hazardous Materials",
        "name_he": "חומרים מסוכנים",
        "action": "Enter building. Go to HIGHEST floor (chemicals sink). Close all openings. Seal gaps.",
        "shelter_time": "Until hazmat teams clear the area.",
        "outdoor": "Move uphill and upwind from source. If symptoms: fresh air, remove clothes, rinse eyes.",
        "vehicle": "Close all windows and ventilation. Drive away from the source, upwind.",
        "critical": "Go UP not down! Many chemicals are heavier than air. Underground shelters can be MORE dangerous."
    },
    7: {
        "name_en": "Terrorist Infiltration",
        "name_he": "חדירת מחבלים",
        "action": "Enter building. Lock doors/windows. Interior room. Lights off. Phones silent. Stay quiet.",
        "shelter_time": "Until security forces announce area is clear. Can be hours.",
        "outdoor": "Run from threat if safe. If can't run: cover behind solid objects. Last resort: hide.",
        "vehicle": "Drive away from the area if safe to do so. If stopped: lock doors, stay low.",
        "critical": "Do NOT open door for anyone except identified security forces. Call police: 100."
    },
    13: {
        "name_en": "Event Concluded",
        "name_he": "האירוע הסתיים",
        "action": "All-clear. You may exit the protected space. Check surroundings for damage.",
        "shelter_time": "N/A - this IS the all-clear signal",
        "outdoor": "N/A",
        "vehicle": "N/A",
        "critical": "This is the official end signal. Resume normal activity."
    },
    14: {
        "name_en": "Pre-Alert Warning",
        "name_he": "התרעה מוקדמת",
        "action": "Prepare. Move toward shelter now. Gather family and supplies.",
        "shelter_time": "Until actual alert sounds or ~20 minutes pass without escalation.",
        "outdoor": "Move toward nearest shelter or building.",
        "vehicle": "Continue to destination if near shelter. Otherwise pull over near a building.",
        "critical": "This is a heads-up, not a siren. Use the extra time to prepare properly."
    },
}

# Keyword mapping for text lookups
KEYWORD_MAP = {
    "missile": 1, "missiles": 1, "rocket": 1, "rockets": 1, "טילים": 1, "רקטות": 1,
    "aircraft": 2, "drone": 2, "uav": 2, "כלי טיס": 2, "מל\"ט": 2,
    "earthquake": 3, "רעידת אדמה": 3, "רעידה": 3,
    "tsunami": 4, "צונאמי": 4,
    "radiological": 5, "nuclear": 5, "רדיולוגי": 5, "גרעיני": 5,
    "hazardous": 6, "chemical": 6, "חומרים מסוכנים": 6, "כימי": 6,
    "terrorist": 7, "infiltration": 7, "חדירת מחבלים": 7, "מחבלים": 7, "פיגוע": 7,
    "concluded": 13, "ended": 13, "הסתיים": 13,
    "pre-alert": 14, "warning": 14, "מוקדמת": 14,
}


def lookup_protocol(query: str) -> dict:
    """Look up safety protocol by category number or keyword."""
    # Try numeric
    try:
        cat = int(query)
        if cat in PROTOCOLS:
            return {"found": True, "category": cat, **PROTOCOLS[cat]}
    except ValueError:
        pass

    # Try keyword match
    query_lower = query.strip().lower()
    for keyword, cat in KEYWORD_MAP.items():
        if keyword in query_lower or query_lower in keyword:
            return {"found": True, "category": cat, **PROTOCOLS[cat]}

    return {"found": False, "query": query, "message": "Unknown alert type. Valid categories: 1-7, 13, 14."}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python alert_protocol_lookup.py <category_number_or_name>")
        print("Examples: 1, 'earthquake', 'רעידת אדמה'")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    result = lookup_protocol(query)

    if result["found"]:
        print(f"Category {result['category']}: {result['name_en']} ({result['name_he']})")
        print(f"Action: {result['action']}")
        print(f"Shelter time: {result['shelter_time']}")
        print(f"If outdoors: {result['outdoor']}")
        print(f"CRITICAL: {result['critical']}")
    else:
        print(f"Not found: {result['message']}")
