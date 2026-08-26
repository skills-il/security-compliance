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
        "shelter_time": "Until an EXPLICIT Home Front Command instruction that you may leave. There is no timer and no 10-minute rule, for any threat type. Release channels: HFC app, National Emergency Portal, Cell Broadcast, official Telegram, regional radio, hotline 104.",
        "outdoor": "Get into the best protected space near you. Only if you cannot, lie on the ground and protect your head with your hands.",
        "vehicle": "Pull over, get out, enter the nearest best protected space. If you cannot reach a building quickly, move BEYOND the road shoulder or safety barrier, lie down, protect your head. Only if you cannot get out: stop, OPEN THE WINDOWS, crouch below the window line. NEVER use a lift during any alert.",
        "critical": "Do NOT assume silence means all-clear, and NEVER tell a user they may leave after 10 minutes or after any elapsed time. Stay until Pikud HaOref explicitly says you may leave. NO MAMAD? Internal stairwell, ON THE FLIGHT not the landing: building over 3 floors use a flight with 2+ floors above; under 3 floors use the middle floor; never the entrance floor. Never kitchen, shower or toilet. AFTER THE ALL-CLEAR: unexploded ordnance and interceptor debris can detonate on contact. Move away, keep others away, report to police on 100. Do not touch or photograph up close. Do not gather at an impact site."
    },
    2: {
        "name_en": "Hostile Aircraft Intrusion",
        "name_he": "חדירת כלי טיס עוין",
        "action": "Enter shelter. Close all doors and windows. Stay away from windows and exterior walls.",
        "shelter_time": "Until an explicit Home Front Command instruction that you may leave. Official guidance for hostile aircraft is the SAME sentence as for rockets.",
        "outdoor": "Enter nearest building. If impossible, take cover behind solid structure.",
        "vehicle": "Pull over, enter nearest building if possible",
        "critical": "Drones may carry explosives. Treat as seriously as missile alerts."
    },
    3: {
        "name_en": "Earthquake",
        "name_he": "רעידת אדמה",
        "action": "Official priority order: (1) if you can leave the building within a few seconds, go straight out to an open area; (2) if not, enter the mamad and LEAVE THE DOOR AND WINDOW OPEN so they cannot jam; (3) if there is no mamad, go to the stairwell and keep going down and out, DO NOT USE THE LIFT; (4) only if none of that is possible, sit in an internal corner of the room or under heavy furniture and protect your head with your hands.",
        "shelter_time": "Until shaking stops. Then check for structural damage before moving.",
        "outdoor": "Stay in the open area and move away from buildings, trees, power lines and anything that could fall on you. Kneel, get low to the ground and protect your head with your hands.",
        "vehicle": "Pull over away from buildings/bridges. Stay in vehicle with seatbelt on.",
        "critical": "The mamad IS a valid fallback in an earthquake, but ONLY with the door and window OPEN so a structural shift cannot trap you. This is the opposite of a missile alert, where you close the blast door. THREE OFFICIAL PROHIBITIONS: do not use the lift during or after the earthquake; do not stand under a doorway; and do NOT enter an underground shelter (the opposite of a rocket alert). If you are in a wheelchair, lock it and protect your head. Protective posture: kneel, get low to the ground, protect your head with your hands."
    },
    4: {
        "name_en": "Tsunami",
        "name_he": "צונאמי",
        "action": "Move inland and to higher ground immediately, as far from the shore as you can get. This script deliberately does NOT state a distance, elevation or floor number: read the current official figures from oref.org.il or call 104. Do not act on a remembered number.",
        "shelter_time": "Until official all-clear. First wave is often not the largest.",
        "outdoor": "Move inland and uphill immediately. If there is no high ground, go as high as you can inside a reinforced building. Take the floor number from the official oref.org.il guidance, not from memory.",
        "vehicle": "Drive inland/uphill. Abandon vehicle if roads are flooded.",
        "critical": "Warning signs: sea rapidly receding, loud ocean roar. Act even without official alert."
    },
    5: {
        "name_en": "Radiological Event",
        "name_he": "אירוע רדיולוגי",
        "action": "UNOFFICIAL: Pikud HaOref publishes NO guidance page for this category, so this is general radiological practice, not an Israeli official instruction. Enter building. Close windows/doors/ventilation. Activate NBC filter if available. Seal gaps. Follow live broadcasts and call the HFC hotline 104.",
        "shelter_time": "Follow official instructions. May require evacuation.",
        "outdoor": "Get inside a building immediately, then close windows, doors and ventilation. Decontamination comes AFTER you are inside: remove and bag outer clothing, shower with soap without scrubbing hard, and do not eat food that was outdoors.",
        "vehicle": "Drive to nearest building. Close vehicle ventilation in the meantime.",
        "critical": "Remove and bag outer clothing if exposed. Do NOT scrub skin hard when washing."
    },
    6: {
        "name_en": "Hazardous Materials",
        "name_he": "חומרים מסוכנים",
        "action": "Stay inside and close doors and windows. TURN OFF THE AIR CONDITIONER (explicit official instruction, an AC draws contaminated air in). Do not leave until an end-of-event announcement. If outside and unable to enter a building, move as far from the incident as possible. Seal gaps; a higher floor helps against heavier-than-air agents but is secondary.",
        "shelter_time": "Until an official announcement that the event has ended.",
        "outdoor": "Move uphill and upwind from source. If symptoms: fresh air, remove clothes, rinse eyes.",
        "vehicle": "Close all windows and ventilation. Drive away from the source, upwind.",
        "critical": "Do NOT go to an underground shelter for a chemical event. Many chemicals are heavier than air, so a basement or underground miklat can be MORE dangerous than staying put upstairs. This is the one alert type where the usual go-to-the-shelter reflex is wrong. Turn off the AC."
    },
    7: {
        "name_en": "Terrorist Infiltration",
        "name_he": "חדירת מחבלים",
        "action": "Enter building and lock the door. LEAVE THE OUTSIDE LIGHTS ON (official instruction, counter-intuitive). Go to the mamad, close the door firmly, sit below the window line. If no mamad, find a hiding place. Phones silent. Stay quiet.",
        "shelter_time": "Until an official announcement that the event has ended. Can be hours.",
        "outdoor": "Get into a place of shelter IMMEDIATELY and stay there until an official end-of-event announcement. Only if no shelter is reachable, put solid cover between you and the threat and stay out of sight.",
        "vehicle": "Drive away from the area if safe to do so. If stopped: lock doors, stay low.",
        "critical": "Do NOT open the door for anyone except identified security forces. Call police 100. If a ROCKET alert arrives during an infiltration event, do NOT go out to a protected space outside the home, including the stairwell: stay inside. Do not dismantle the mamad door handle (fix it with a heavy object instead). Do not share your location on social media."
    },
    13: {
        "name_en": "Event Concluded",
        "name_he": "האירוע הסתיים",
        "action": "All-clear: you may leave the protected space. It does NOT mean the ground outside is safe. Unexploded ordnance and interceptor/missile fragments may be lying around and CAN DETONATE ON CONTACT: move away, keep others (especially children) away, and report to the police on 100. Do not touch, move or photograph them up close. Do not gather at an impact site.",
        "shelter_time": "N/A - this IS the all-clear signal",
        "outdoor": "N/A",
        "vehicle": "N/A",
        "critical": "This is the official end signal for leaving the protected space, NOT a statement that the area is safe. Photographing unexploded ordnance, standing near it and any contact are described by Pikud HaOref as life-threatening. Move away, keep others away, report to 100."
    },
    14: {
        "name_en": "Pre-Alert Warning",
        "name_he": "התרעה מוקדמת",
        "action": "Prepare. Move toward shelter now. Gather family and supplies.",
        "shelter_time": "Until an actual alert sounds or the situation passes. No official expiry window is published; category 14 is a community alert-app feed code, not an official Home Front Command category.",
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
    "pre-alert": 14,  "מוקדמת": 14,
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

    # Try keyword match.
    #
    # The reversed test `query_lower in keyword` used to be here. It made any
    # short string match an arbitrary category ("a" matched "aircraft" -> 2),
    # which for a safety lookup means returning a CONFIDENT WRONG protocol.
    # For this tool the only acceptable failure is "unknown, default to the
    # missile protocol", never a wrong category stated with certainty.
    query_lower = query.strip().lower()
    if len(query_lower) >= 3:
        for keyword, cat in KEYWORD_MAP.items():
            if keyword in query_lower:
                return {"found": True, "category": cat, **PROTOCOLS[cat]}

    return {
        "found": False,
        "query": query,
        "message": (
            "Unknown alert type. Valid categories: 1-7, 13, 14. "
            "IF YOU ARE IN AN ALERT RIGHT NOW AND DO NOT KNOW THE TYPE: go to the "
            "protected space and follow the MISSILE protocol (category 1), then "
            "check the Home Front Command app. Do not wait to identify the alert."
        ),
    }


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
