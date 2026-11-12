# ============================================================
# SUNO SAATHI MAGIC ENGINE V16.6 - STABLE COMPLETE
# Physics + Chemistry | English/Hindi/Hinglish | Unit aware
# ============================================================

import re
import math

VERSION = "16.6"

# ---------- NORMALIZATION ----------
HINDI_NUMBERS = {
    "शून्य":"0", "एक":"1", "दो":"2", "तीन":"3", "चार":"4",
    "पांच":"5", "पाँच":"5", "छह":"6", "छः":"6", "सात":"7",
    "आठ":"8", "नौ":"9", "दस":"10", "ग्यारह":"11", "बारह":"12",
    "तेरह":"13", "चौदह":"14", "पंद्रह":"15", "पन्द्रह":"15",
    "सोलह":"16", "सत्रह":"17", "अठारह":"18", "उन्नीस":"19",
    "बीस":"20", "पच्चीस":"25", "तीस":"30", "चालीस":"40",
    "पचास":"50", "सौ":"100"
}
HINDI_TERMS = {
    "बल":"force", "कार्य":"work", "काम":"work", "शक्ति":"power",
    "वेग":"speed", "चाल":"speed", "दूरी":"distance", "समय":"time",
    "द्रव्यमान":"mass", "त्वरण":"acceleration", "ऊंचाई":"height",
    "ऊँचाई":"height", "गतिज ऊर्जा":"kinetic energy",
    "स्थितिज ऊर्जा":"potential energy", "मोल":"moles",
    "मोलर द्रव्यमान":"molar mass", "मोलरता":"molarity",
    "घनत्व":"density", "संवेग":"momentum", "कण":"particles",
    "निकालो":"calculate", "ज्ञात करो":"calculate", "गणना":"calculate",
    "कितना":"calculate"
}

def normalize_query(query):
    q = str(query).lower().strip()
    # Hindi numerals to Arabic numerals
    devanagari_digits = "०१२३४५६७८९"
    for i, d in enumerate(devanagari_digits):
        q = q.replace(d, str(i))
    for word, number in sorted(HINDI_NUMBERS.items(), key=lambda x: -len(x[0])):
        q = q.replace(word, number)
    for word, replacement in sorted(HINDI_TERMS.items(), key=lambda x: -len(x[0])):
        q = q.replace(word, replacement)
    q = q.replace("किलो ग्राम", "kg").replace("किलोग्राम", "kg")
    q = q.replace("ग्राम", "g").replace("मीटर", "m")
    q = q.replace("सेकंड", "s").replace("मिनट", "min")
    q = re.sub(r"\b(find|calculate|solve|compute| निकालो| ज्ञात करो)\b", " ", q)
    q = re.sub(r"\s+", " ", q)
    return q.strip()

# ---------- TOPIC DETECTION ----------
TOPIC_PATTERNS = [
    ("molarity", r"\b(molarity|molar concentration)\b"),
    ("particles", r"\b(particles|number of particles|molecules)\b"),
    ("moles", r"\b(moles|mol)\b"),
    ("density", r"\b(density)\b"),
    ("momentum", r"\b(momentum)\b"),
    ("kinetic_energy", r"\b(kinetic energy|ke)\b"),
    ("potential_energy", r"\b(potential energy|pe)\b"),
    ("power", r"\b(power)\b"),
    ("work", r"\b(work)\b"),
    ("force", r"\b(force)\b"),
    ("speed", r"\b(speed|velocity)\b"),
]

def detect_topic(q):
    for topic, pattern in TOPIC_PATTERNS:
        if re.search(pattern, q):
            return topic
    return None

# ---------- QUANTITY EXTRACTION ----------
# Numeric + unit pairs, preserving units for chemistry.
NUM_UNIT_RE = re.compile(
    r"([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[-+]?\d+)?)\s*"
    r"(kg/mol|g/mol|mg/mol|km/h|m/s|cm/s|kg|mg|g|km|cm|mm|m|"
    r"min|minutes?|hrs?|hours?|s|sec|seconds?|n|j|w|l|ml|mol|"
    r"m\^?2|m\^?3|pa|kpa|particles?)?\b", re.I
)

def extract_values(q):
    values = []
    for match in NUM_UNIT_RE.finditer(q):
        raw_num, raw_unit = match.groups()
        try:
            number = float(raw_num)
        except ValueError:
            continue
        unit = (raw_unit or "").lower()
        unit = unit.replace("minutes", "min").replace("minute", "min")
        unit = unit.replace("hours", "h").replace("hour", "h").replace("hrs", "h")
        unit = unit.replace("seconds", "s").replace("second", "s").replace("sec", "s")
        values.append({"value": number, "unit": unit, "start": match.start(), "end": match.end()})
    return values

def find_labeled(q, label):
    # Examples: mass 5 kg, acceleration 2 m/s2
    patterns = {
        "mass": r"(?<!molar )\bmass\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(kg|g|mg)?",
        "acceleration": r"acceleration\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(m/s\^?2)?",
        "distance": r"distance\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(km|m|cm|mm)?",
        "time": r"time\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(min|h|s)?",
        "height": r"height\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(km|m|cm|mm)?",
        "force": r"force\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(n)?",
        "molar_mass": r"molar mass\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(kg/mol|g/mol|mg/mol)?",
        "volume": r"volume\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(l|ml)?",
        "amount": r"(?:moles|amount)\s*[:=]?\s*(-?\d+(?:\.\d+)?)\s*(mol)?",
    }
    pat = patterns.get(label)
    if not pat:
        return None
    m = re.search(pat, q)
    if not m:
        return None
    val = float(m.group(1))
    unit = (m.group(2) or "").lower()
    return val, unit

def convert(value, unit, dimension):
    """Convert to SI/base units for supported dimensions."""
    u = unit.lower()
    factors = {
        "mass": {"kg":1, "g":0.001, "mg":1e-6},
        "distance": {"m":1, "km":1000, "cm":0.01, "mm":0.001},
        "time": {"s":1, "min":60, "h":3600},
        "speed": {"m/s":1, "km/h":1/3.6, "cm/s":0.01},
        "force": {"n":1},
        "work": {"j":1},
        "power": {"w":1},
        "volume": {"l":0.001, "ml":1e-6, "m3":1},
        "molar_mass": {"kg/mol":1, "g/mol":0.001, "mg/mol":1e-6},
    }
    if u == "" and dimension in ("mass","distance","time","volume","molar_mass"):
        defaults = {"mass":"kg","distance":"m","time":"s","volume":"l","molar_mass":"g/mol"}
        u = defaults[dimension]
    if dimension not in factors or u not in factors[dimension]:
        return value
    return value * factors[dimension][u]

def labeled_value(q, label, dimension=None, default_unit=None):
    found = find_labeled(q, label)
    if not found:
        return None
    val, unit = found
    if dimension:
        if not unit and default_unit:
            unit = default_unit
        val = convert(val, unit, dimension)
    return val

def values_by_unit(vals, unit):
    return [v["value"] for v in vals if v["unit"] == unit]

def first_dimension(vals, dimension):
    allowed = {
        "mass": {"kg","g","mg"},
        "distance": {"m","km","cm","mm"},
        "time": {"s","min","h"},
        "speed": {"m/s","km/h","cm/s"},
        "force": {"n"},
        "work": {"j"},
        "power": {"w"},
        "volume": {"l","ml"},
        "molar_mass": {"kg/mol","g/mol","mg/mol"},
    }.get(dimension, set())
    for x in vals:
        if x["unit"] in allowed:
            return x["value"], x["unit"]
    return None

# ---------- ENGINE ----------
def suno_magic(query):
    original = str(query)
    q = normalize_query(original)
    topic = detect_topic(q)
    vals = extract_values(q)

    def success(result, unit, formula, explanation=None, extra=None):
        out = {
            "success": True, "topic": topic,
            "values": {}, "result": round(float(result), 10),
            "unit": unit, "formula": formula,
            "explanation": explanation or f"{formula} = {result} {unit}"
        }
        if extra:
            out.update(extra)
        return out

    def fail(message, missing=None):
        return {"success":False, "topic":topic, "error":message,
                "missing":missing or []}

    # Labeled extraction first; unit pairs as fallback.
    def get(label, dimension=None, default_unit=None):
        x = labeled_value(q, label, dimension, default_unit)
        if x is not None:
            return x
        unit_dim = {"mass":"mass","distance":"distance","time":"time",
                    "speed":"speed","force":"force","work":"work",
                    "power":"power","volume":"volume","molar_mass":"molar_mass"}
        d = dimension or unit_dim.get(label)
        got = first_dimension(vals, d) if d else None
        if got:
            return convert(got[0], got[1], d)
        return None

    if topic == "force":
        m = get("mass","mass")
        a = get("acceleration")
        if m is None or a is None:
            return fail("Force ke liye mass (kg) aur acceleration (m/s²) chahiye.", ["mass","acceleration"])
        r = m*a
        return success(r,"N","F = m × a",f"F = {m} × {a} = {r} N",{"values":{"mass_kg":m,"acceleration":a}})
    if topic == "work":
        f = get("force","force")
        d = get("distance","distance")
        if f is None or d is None:
            return fail("Work ke liye force (N) aur distance (m) chahiye.",["force","distance"])
        r=f*d
        return success(r,"J","W = F × d",f"W = {f} × {d} = {r} J",{"values":{"force_N":f,"distance_m":d}})
    if topic == "power":
        w = get("work","work")
        t = get("time","time")
        if w is None or t is None:
            return fail("Power ke liye work (J) aur time (s) chahiye.",["work","time"])
        if t == 0: return fail("Time zero nahi ho sakta.")
        r=w/t
        return success(r,"W","P = W / t",f"P = {w} / {t} = {r} W",{"values":{"work_J":w,"time_s":t}})
    if topic == "speed":
        d=get("distance","distance")
        t=get("time","time")
        # If distance/time not explicitly labeled, take first distance and time units.
        if d is None or t is None:
            return fail("Speed ke liye distance aur time chahiye.",["distance","time"])
        if t==0: return fail("Time zero nahi ho sakta.")
        r=d/t
        return success(r,"m/s","v = d / t",f"v = {d} / {t} = {r} m/s",{"values":{"distance_m":d,"time_s":t}})
    if topic == "kinetic_energy":
        m=get("mass","mass"); v=get("speed","speed")
        if v is None:
            # use bare labeled velocity or speed value
            found=find_labeled(q,"speed")
            if found: v=found[0]
        if m is None or v is None:
            return fail("Kinetic Energy ke liye mass aur speed chahiye.",["mass","speed"])
        r=0.5*m*v*v
        return success(r,"J","KE = ½mv²",f"KE = 0.5 × {m} × {v}² = {r} J",{"values":{"mass_kg":m,"speed_m_s":v}})
    if topic == "potential_energy":
        m=get("mass","mass"); h=get("height","distance")
        g=9.8
        if m is None or h is None:
            return fail("Potential Energy ke liye mass aur height chahiye.",["mass","height"])
        r=m*g*h
        return success(r,"J","PE = mgh",f"PE = {m} × 9.8 × {h} = {r} J",{"values":{"mass_kg":m,"height_m":h,"g":g}})
    if topic == "density":
        m=get("mass","mass"); volume=get("volume","volume")
        if m is None or volume is None:
            # infer numeric kg and L/ml
            masses=first_dimension(vals,"mass"); volumes=first_dimension(vals,"volume")
            if m is None and masses: m=convert(*masses,"mass")
            if volume is None and volumes: volume=convert(*volumes,"volume")
        if m is None or volume is None: return fail("Density ke liye mass aur volume chahiye.",["mass","volume"])
        if volume==0: return fail("Volume zero nahi ho sakta.")
        r=m/volume
        return success(r,"kg/m³","ρ = m / V",f"ρ = {m} / {volume} = {r} kg/m³",{"values":{"mass_kg":m,"volume_m3":volume}})
    if topic == "momentum":
        m=get("mass","mass"); v=get("speed","speed")
        if m is None or v is None: return fail("Momentum ke liye mass aur speed chahiye.",["mass","speed"])
        r=m*v
        return success(r,"kg·m/s","p = mv",f"p = {m} × {v} = {r}",{"values":{"mass_kg":m,"speed_m_s":v}})
    if topic == "moles":
        # Keep mass and molar mass in matching units: g/(g/mol), kg/(kg/mol).
        mass_found=find_labeled(q,"mass")
        mm_found=find_labeled(q,"molar_mass")
        if mass_found and mm_found:
            mass, mu=mass_found; mm, mmu=mm_found
            if not mu: mu="g" if mmu in ("g/mol","mg/mol") else "kg"
            if not mmu: mmu="g/mol" if mu in ("g","mg") else "kg/mol"
            mass_g = convert(mass,mu,"mass") * 1000
            mm_gmol = convert(mm,mmu,"molar_mass") * 1000
            # both converted to grams and g/mol
            if mm_gmol==0: return fail("Molar mass zero nahi ho sakta.")
            r=mass_g/mm_gmol
            return success(r,"mol","n = mass / molar mass",f"n = {mass_g} g / {mm_gmol} g/mol = {r} mol",{"values":{"mass_g":mass_g,"molar_mass_g_mol":mm_gmol}})
        if len(vals)>=2:
            masses=[x for x in vals if x["unit"] in ("g","kg","mg")]
            mms=[x for x in vals if x["unit"] in ("g/mol","kg/mol","mg/mol")]
            if masses and mms:
                mg=convert(masses[0]["value"],masses[0]["unit"],"mass")*1000
                mmg=convert(mms[0]["value"],mms[0]["unit"],"molar_mass")*1000
                if mmg==0:return fail("Molar mass zero nahi ho sakta.")
                r=mg/mmg
                return success(r,"mol","n = mass / molar mass",f"n = {mg} g / {mmg} g/mol = {r} mol")
        return fail("Moles ke liye mass aur molar mass chahiye.",["mass","molar mass"])
    if topic == "molarity":
        n=get("amount"); volume=get("volume","volume")
        if n is None:
            mols=[x["value"] for x in vals if x["unit"]=="mol"]
            if mols:n=mols[0]
        if volume is None:
            liters=[x for x in vals if x["unit"] in ("l","ml")]
            if liters: volume=convert(liters[0]["value"],liters[0]["unit"],"volume")
        if n is None or volume is None:return fail("Molarity ke liye moles aur volume chahiye.",["moles","volume"])
        if volume==0:return fail("Volume zero nahi ho sakta.")
        r=n/volume # mol/m3; convert to mol/L
        r=r/1000
        return success(r,"mol/L","M = n / V",f"M = {n} / {volume*1000} = {r} mol/L")
    if topic == "particles":
        n=get("amount")
        if n is None:
            mols=[x["value"] for x in vals if x["unit"]=="mol"]
            if mols:n=mols[0]
        if n is None:return fail("Particles ke liye moles (mol) chahiye.",["moles"])
        r=n*6.02214076e23
        return success(r,"particles","N = n × NA",f"N = {n} × 6.022×10²³ = {r}")
    return fail("Topic samajh nahi aaya. Physics/Chemistry quantity ka naam likhein.")

# ---------- TESTS ----------

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Suno Saathi Magic V16.6")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class SolveRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Suno Saathi Magic V16.6 Online"}

@app.get("/health")
def health():
    return {"status": "ok", "version": "V16.6"}

@app.post("/solve")
def solve(request: SolveRequest):
    return suno_magic(request.query)
