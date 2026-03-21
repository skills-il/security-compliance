#!/usr/bin/env python3
"""
Shelter Finder Helper

Provides time-to-shelter lookup by city name and basic shelter type guidance.
This is a reference script for AI agents to use when helping users find shelter info.

Usage:
    python shelter_finder.py "tel aviv"
    python shelter_finder.py "אשקלון"
"""

import sys

# Time-to-shelter zones (seconds) - based on Home Front Command data
# Source: oref.org.il regional countdown values
SHELTER_TIMES = {
    # Gaza envelope - 0-15 seconds
    "nir am": 15, "ניר עם": 15,
    "beeri": 15, "בארי": 15,
    "kissufim": 15, "כיסופים": 15,
    "nahal oz": 15, "נחל עוז": 15,
    "kfar aza": 15, "כפר עזה": 15,
    # Western Negev - 15-30 seconds
    "sderot": 15, "שדרות": 15,
    "netivot": 30, "נתיבות": 30,
    # Southern coast - 30 seconds
    "ashkelon": 30, "אשקלון": 30,
    # Central Negev - 45 seconds
    "ofakim": 45, "אופקים": 45,
    "kiryat gat": 45, "קריית גת": 45,
    # Southern cities - 60 seconds
    "ashdod": 60, "אשדוד": 60,
    "beer sheva": 60, "באר שבע": 60,
    "beersheba": 60,
    # Central Israel - 90 seconds
    "tel aviv": 90, "תל אביב": 90,
    "jerusalem": 90, "ירושלים": 90,
    "netanya": 90, "נתניה": 90,
    "rishon lezion": 90, "ראשון לציון": 90,
    "petah tikva": 90, "פתח תקווה": 90,
    "ramat gan": 90, "רמת גן": 90,
    "holon": 90, "חולון": 90,
    "bnei brak": 90, "בני ברק": 90,
    "bat yam": 90, "בת ים": 90,
    "herzliya": 90, "הרצליה": 90,
    "kfar saba": 90, "כפר סבא": 90,
    "raanana": 90, "רעננה": 90,
    "modiin": 90, "מודיעין": 90,
    "rehovot": 90, "רחובות": 90,
    # Haifa area - 60 seconds
    "haifa": 60, "חיפה": 60,
    "krayot": 60, "קריות": 60,
    "kiryat ata": 60, "קריית אתא": 60,
    "kiryat bialik": 60, "קריית ביאליק": 60,
    "kiryat motzkin": 60, "קריית מוצקין": 60,
    "akko": 60, "עכו": 60,
    "acre": 60,
    "nahariya": 60, "נהריה": 60,
    # Upper Galilee / Golan - up to 180 seconds
    "kiryat shmona": 60, "קריית שמונה": 60,
    "metula": 60, "מטולה": 60,
    "safed": 60, "צפת": 60,
    "tiberias": 90, "טבריה": 90,
}


def get_shelter_time(city: str) -> dict:
    """Look up time-to-shelter for a given city name (Hebrew or English)."""
    city_lower = city.strip().lower()
    city_stripped = city.strip()

    # Try exact match (case-insensitive for English, exact for Hebrew)
    if city_lower in SHELTER_TIMES:
        return {"city": city, "seconds": SHELTER_TIMES[city_lower], "found": True}
    if city_stripped in SHELTER_TIMES:
        return {"city": city, "seconds": SHELTER_TIMES[city_stripped], "found": True}

    # Try substring match
    for key, seconds in SHELTER_TIMES.items():
        if city_lower in key.lower() or key.lower() in city_lower:
            return {"city": city, "seconds": seconds, "found": True, "matched": key}

    return {
        "city": city,
        "found": False,
        "message": "City not in local database. Check oref.org.il or call 104 for your zone."
    }


def shelter_guidance(seconds: int) -> str:
    """Return shelter guidance based on time-to-shelter."""
    if seconds <= 15:
        return "IMMEDIATE: Enter mamad/shelter instantly. No time to reach a distant shelter."
    elif seconds <= 30:
        return "Very short: Enter the nearest mamad or miklat. No time for distant shelters."
    elif seconds <= 60:
        return "Short: Enter mamad if available. Nearby miklat possible if within 30 seconds walk."
    elif seconds <= 90:
        return "Standard: Enter mamad or nearby miklat. Stairwell protocol if no mamad."
    else:
        return "Extended: More time available, but still move to shelter immediately."


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shelter_finder.py <city_name>")
        sys.exit(1)

    city = " ".join(sys.argv[1:])
    result = get_shelter_time(city)

    if result["found"]:
        print(f"City: {result['city']}")
        print(f"Time to shelter: {result['seconds']} seconds")
        print(f"Guidance: {shelter_guidance(result['seconds'])}")
    else:
        print(f"City: {result['city']}")
        print(f"Status: {result['message']}")
