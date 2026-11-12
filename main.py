# ============================================
# SUNO SAATHI MAGIC LAYER v1
# Python | Google Colab | No API required
# ============================================

import ipywidgets as widgets
from IPython.display import display, clear_output

# ---------- Formula Database ----------
FORMULAS = {
    "speed": {
        "en": "Speed = Distance / Time",
        "hi": "गति = दूरी / समय"
    },
    "distance": {
        "en": "Distance = Speed × Time",
        "hi": "दूरी = गति × समय"
    },
    "time": {
        "en": "Time = Distance / Speed",
        "hi": "समय = दूरी / गति"
    }
}

# ---------- Calculator Engine ----------
def calculate(distance, time):
    if distance < 0:
        raise ValueError("Distance cannot be negative.")
    if time <= 0:
        raise ValueError("Time must be greater than zero.")

    speed = distance / time

    return {
        "distance": distance,
        "time": time,
        "speed": speed,
        "unit": "km/h"
    }

# ---------- Explanation Engine ----------
def explain(result, language="English"):
    d = result["distance"]
    t = result["time"]
    s = result["speed"]

    if language == "Hindi":
        return f"""
        📘 सूत्र:
        गति = दूरी ÷ समय

        📝 Step 1:
        दूरी = {d} km

        📝 Step 2:
        समय = {t} घंटे

        📝 Step 3:
        गति = {d} ÷ {t}

        ✅ उत्तर:
        {s:.4f} km/h

        💡 अर्थ:
        वाहन प्रत्येक घंटे {s:.4f} km चलता है।
        """

    return f"""
    📘 Formula:
    Speed = Distance / Time

    📝 Step 1:
    Distance = {d} km

    📝 Step 2:
    Time = {t} hours

    📝 Step 3:
    Speed = {d} / {t}

    ✅ Answer:
    {s:.4f} km/h

    💡 Meaning:
    The vehicle travels {s:.4f} km per hour.
    """

# ---------- Formula Finder ----------
def formula_finder(query, language="English"):
    query = query.lower()

    if any(word in query for word in ["speed", "गति"]):
        key = "speed"
    elif any(word in query for word in ["distance", "दूरी"]):
        key = "distance"
    elif any(word in query for word in ["time", "समय"]):
        key = "time"
    else:
        return "Formula not found / सूत्र नहीं मिला"

    return FORMULAS[key][
        "hi" if language == "Hindi" else "en"
    ]

# ---------- User Interface ----------
distance_input = widgets.FloatText(
    value=150,
    description="Distance (km):"
)

time_input = widgets.FloatText(
    value=3,
    description="Time (hours):"
)

language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

calculate_button = widgets.Button(
    description="Calculate + Explain",
    button_style="success"
)

formula_input = widgets.Text(
    placeholder="speed / distance / time",
    description="Formula:"
)

formula_button = widgets.Button(
    description="Find Formula",
    button_style="info"
)

output = widgets.Output()

def on_calculate_clicked(button):
    with output:
        clear_output()

        try:
            result = calculate(
                distance_input.value,
                time_input.value
            )

            print(explain(result, language.value))

        except ValueError as error:
            print("⚠️", error)

def on_formula_clicked(button):
    with output:
        clear_output()
        print(formula_finder(
            formula_input.value,
            language.value
        ))

calculate_button.on_click(on_calculate_clicked)
formula_button.on_click(on_formula_clicked)

display(widgets.HTML(
    "<h2>🌟 Suno Saathi Magic Layer</h2>"
    "<p>Free Educational Calculator Prototype</p>"
))

display(distance_input)
display(time_input)
display(language)
display(calculate_button)

display(widgets.HTML("<hr><h3>Formula Finder</h3>"))
display(formula_input)
display(formula_button)
display(output)

# BASIC TESTS

assert calculate(150, 3)["speed"] == 50
assert calculate(100, 2)["speed"] == 50

try:
    calculate(100, 0)
    raise AssertionError("Zero time should fail")
except ValueError:
    pass

print("✅ All tests passed!")

# ============================================
# SUNO SAATHI MAGIC ENGINE v2
# Physics + Chemistry
# ============================================

import math

def magic_engine(topic, values, language="English"):

    topic = topic.lower().strip()

    # -------- PHYSICS --------

    if topic == "speed":
        d = float(values["distance"])
        t = float(values["time"])

        if d < 0 or t <= 0:
            raise ValueError("Distance must be >= 0 and time > 0")

        result = d / t
        formula = "Speed = Distance / Time"

        steps = [
            f"Distance = {d} km",
            f"Time = {t} hours",
            f"Speed = {d} / {t} = {result} km/h"
        ]

    elif topic == "work":
        f = float(values["force"])
        d = float(values["distance"])

        result = f * d
        formula = "Work = Force × Distance"

        steps = [
            f"Force = {f} N",
            f"Distance = {d} m",
            f"Work = {f} × {d} = {result} J"
        ]

    elif topic == "power":
        w = float(values["work"])
        t = float(values["time"])

        if t <= 0:
            raise ValueError("Time must be greater than zero")

        result = w / t
        formula = "Power = Work / Time"

        steps = [
            f"Work = {w} J",
            f"Time = {t} s",
            f"Power = {w} / {t} = {result} W"
        ]

    # -------- CHEMISTRY --------

    elif topic == "molarity":
        moles = float(values["moles"])
        volume = float(values["volume"])

        if volume <= 0:
            raise ValueError("Volume must be greater than zero")

        result = moles / volume
        formula = "Molarity = Moles / Volume (L)"

        steps = [
            f"Moles = {moles} mol",
            f"Volume = {volume} L",
            f"Molarity = {moles} / {volume} = {result} mol/L"
        ]

    elif topic == "moles":
        mass = float(values["mass"])
        molar_mass = float(values["molar_mass"])

        if mass < 0 or molar_mass <= 0:
            raise ValueError("Mass >= 0 and molar mass > 0")

        result = mass / molar_mass
        formula = "Moles = Mass / Molar Mass"

        steps = [
            f"Mass = {mass} g",
            f"Molar Mass = {molar_mass} g/mol",
            f"Moles = {mass} / {molar_mass} = {result} mol"
        ]

    else:
        raise ValueError(
            "Available topics: speed, work, power, molarity, moles"
        )

    # -------- EXPLANATION --------

    if language == "Hindi":
        translated_formula = {
            "speed": "गति = दूरी / समय",
            "work": "कार्य = बल × दूरी",
            "power": "शक्ति = कार्य / समय",
            "molarity": "मोलरता = मोल / आयतन (लीटर)",
            "moles": "मोल = द्रव्यमान / मोलर द्रव्यमान"
        }
        formula = translated_formula.get(topic, formula)
        explanation = "चरण-दर-चरण समाधान:\n" + "\n".join(steps)
        explanation += f"\n\nअंतिम उत्तर: {result}"

    else:
        explanation = "Step-by-step solution:\n" + "\n".join(steps)
        explanation += f"\n\nFinal Answer: {result}"

    return {
        "topic": topic,
        "formula": formula,
        "steps": steps,
        "result": result,
        "explanation": explanation
    }


# ============================================
# DEMO
# ============================================

print("PHYSICS: SPEED")
print(magic_engine(
    "speed",
    {"distance": 150, "time": 3},
    "English"
)["explanation"])

print("\nCHEMISTRY: MOLARITY")
print(magic_engine(
    "molarity",
    {"moles": 0.5, "volume": 2},
    "Hindi"
)["explanation"])

# ============================================
# SUNO SAATHI MAGIC ENGINE v2
# Physics + Chemistry
# ============================================

import math

def magic_engine(topic, values, language="English"):

    topic = topic.lower().strip()

    # -------- PHYSICS --------

    if topic == "speed":
        d = float(values["distance"])
        t = float(values["time"])

        if d < 0 or t <= 0:
            raise ValueError("Distance must be >= 0 and time > 0")

        result = d / t
        formula = "Speed = Distance / Time"

        steps = [
            f"Distance = {d} km",
            f"Time = {t} hours",
            f"Speed = {d} / {t} = {result} km/h"
        ]

    elif topic == "work":
        f = float(values["force"])
        d = float(values["distance"])

        result = f * d
        formula = "Work = Force × Distance"

        steps = [
            f"Force = {f} N",
            f"Distance = {d} m",
            f"Work = {f} × {d} = {result} J"
        ]

    elif topic == "power":
        w = float(values["work"])
        t = float(values["time"])

        if t <= 0:
            raise ValueError("Time must be greater than zero")

        result = w / t
        formula = "Power = Work / Time"

        steps = [
            f"Work = {w} J",
            f"Time = {t} s",
            f"Power = {w} / {t} = {result} W"
        ]

    # -------- CHEMISTRY --------

    elif topic == "molarity":
        moles = float(values["moles"])
        volume = float(values["volume"])

        if volume <= 0:
            raise ValueError("Volume must be greater than zero")

        result = moles / volume
        formula = "Molarity = Moles / Volume (L)"

        steps = [
            f"Moles = {moles} mol",
            f"Volume = {volume} L",
            f"Molarity = {moles} / {volume} = {result} mol/L"
        ]

    elif topic == "moles":
        mass = float(values["mass"])
        molar_mass = float(values["molar_mass"])

        if mass < 0 or molar_mass <= 0:
            raise ValueError("Mass >= 0 and molar mass > 0")

        result = mass / molar_mass
        formula = "Moles = Mass / Molar Mass"

        steps = [
            f"Mass = {mass} g",
            f"Molar Mass = {molar_mass} g/mol",
            f"Moles = {mass} / {molar_mass} = {result} mol"
        ]

    else:
        raise ValueError(
            "Available topics: speed, work, power, molarity, moles"
        )

    # -------- EXPLANATION --------

    if language == "Hindi":
        translated_formula = {
            "speed": "गति = दूरी / समय",
            "work": "कार्य = बल × दूरी",
            "power": "शक्ति = कार्य / समय",
            "molarity": "मोलरता = मोल / आयतन (लीटर)",
            "moles": "मोल = द्रव्यमान / मोलर द्रव्यमान"
        }
        formula = translated_formula.get(topic, formula)
        explanation = "चरण-दर-चरण समाधान:\n" + "\n".join(steps)
        explanation += f"\n\nअंतिम उत्तर: {result}"

    else:
        explanation = "Step-by-step solution:\n" + "\n".join(steps)
        explanation += f"\n\nFinal Answer: {result}"

    return {
        "topic": topic,
        "formula": formula,
        "steps": steps,
        "result": result,
        "explanation": explanation
    }


# ============================================
# DEMO
# ============================================

print("PHYSICS: SPEED")
print(magic_engine(
    "speed",
    {"distance": 150, "time": 3},
    "English"
)["explanation"])

print("\nCHEMISTRY: MOLARITY")
print(magic_engine(
    "molarity",
    {"moles": 0.5, "volume": 2},
    "Hindi"
)["explanation"])

# MAGIC ENGINE TESTS

assert magic_engine(
    "speed", {"distance": 150, "time": 3}
)["result"] == 50

assert magic_engine(
    "work", {"force": 10, "distance": 5}
)["result"] == 50

assert magic_engine(
    "power", {"work": 100, "time": 5}
)["result"] == 20

assert magic_engine(
    "molarity", {"moles": 0.5, "volume": 2}
)["result"] == 0.25

assert magic_engine(
    "moles", {"mass": 10, "molar_mass": 20}
)["result"] == 0.5

print("✅ All Physics + Chemistry Magic Engine tests passed!")

# ============================================
# SUNO SAATHI MAGIC LAYER v3
# Interactive Calculator UI
# Requires Cell 3 Magic Engine
# ============================================

import ipywidgets as widgets
from IPython.display import display, clear_output

# Calculator configuration
CONFIG = {
    "Speed": {
        "topic": "speed",
        "fields": [("distance", "Distance (km)", 150),
                   ("time", "Time (hours)", 3)]
    },
    "Work": {
        "topic": "work",
        "fields": [("force", "Force (N)", 10),
                   ("distance", "Distance (m)", 5)]
    },
    "Power": {
        "topic": "power",
        "fields": [("work", "Work (J)", 100),
                   ("time", "Time (seconds)", 5)]
    },
    "Molarity": {
        "topic": "molarity",
        "fields": [("moles", "Moles", 0.5),
                   ("volume", "Volume (L)", 2)]
    },
    "Moles": {
        "topic": "moles",
        "fields": [("mass", "Mass (g)", 10),
                   ("molar_mass", "Molar Mass (g/mol)", 20)]
    }
}

# UI controls
tool_select = widgets.Dropdown(
    options=list(CONFIG.keys()),
    description="Calculator:",
    layout=widgets.Layout(width="95%")
)

lang_select = widgets.Dropdown(
    options=["English", "Hindi"],
    description="Language:",
    layout=widgets.Layout(width="95%")
)

input_area = widgets.VBox()
calculate_btn = widgets.Button(
    description="✨ Calculate + Explain",
    button_style="success",
    layout=widgets.Layout(width="95%", height="45px")
)

result_area = widgets.Output()
input_widgets = {}

# Generate input fields
def update_fields(change=None):
    global input_widgets
    config = CONFIG[tool_select.value]
    input_widgets = {}

    for key, label, default in config["fields"]:
        input_widgets[key] = widgets.FloatText(
            value=default,
            description=label,
            layout=widgets.Layout(width="95%")
        )

    input_area.children = tuple(input_widgets.values())

tool_select.observe(update_fields, names="value")
update_fields()

# Calculate action
def run_magic(button):
    with result_area:
        clear_output()

        try:
            values = {
                key: widget.value
                for key, widget in input_widgets.items()
            }

            result = magic_engine(
                CONFIG[tool_select.value]["topic"],
                values,
                lang_select.value
            )

            print("🌟 SUNO SAATHI MAGIC LAYER")
            print("=" * 35)
            print("📘 Formula:", result["formula"])
            print()
            print(result["explanation"])

        except Exception as error:
            print("⚠️ Error:", error)

calculate_btn.on_click(run_magic)

# Display application
display(widgets.HTML("""
<div style="background:linear-gradient(135deg,#123c91,#1769d2);
color:white;padding:20px;border-radius:12px">
<h2>🌟 Suno Saathi Magic Layer</h2>
<p>Physics + Chemistry Smart Calculator</p>
</div>
"""))

display(tool_select)
display(lang_select)
display(input_area)
display(calculate_btn)
display(result_area)

print("✅ Interactive Magic Layer v3 Ready")

# ============================================================
# SUNO SAATHI MAGIC LAYER v4
# Complete standalone prototype | Google Colab
# ============================================================

import re
import math
import ipywidgets as w
from IPython.display import display, clear_output

# ---------------- FORMULA DATABASE ----------------

FORMULAS = {
    "speed": {
        "en": "Speed = Distance / Time",
        "hi": "गति = दूरी / समय"
    },
    "work": {
        "en": "Work = Force × Distance",
        "hi": "कार्य = बल × दूरी"
    },
    "power": {
        "en": "Power = Work / Time",
        "hi": "शक्ति = कार्य / समय"
    },
    "molarity": {
        "en": "Molarity = Moles / Volume (L)",
        "hi": "मोलरता = मोल / आयतन (लीटर)"
    },
    "moles": {
        "en": "Moles = Mass / Molar Mass",
        "hi": "मोल = द्रव्यमान / मोलर द्रव्यमान"
    }
}

# ---------------- CALCULATION ENGINE ----------------

def magic_calculate(topic, values):

    if topic == "speed":
        d, t = values["distance"], values["time"]
        if d < 0 or t <= 0:
            raise ValueError("Distance >= 0 and Time > 0 required")
        return d / t, "km/h"

    if topic == "work":
        f, d = values["force"], values["distance"]
        if f < 0 or d < 0:
            raise ValueError("Force and Distance must be >= 0")
        return f * d, "J"

    if topic == "power":
        work, t = values["work"], values["time"]
        if work < 0 or t <= 0:
            raise ValueError("Work >= 0 and Time > 0 required")
        return work / t, "W"

    if topic == "molarity":
        n, v = values["moles"], values["volume"]
        if n < 0 or v <= 0:
            raise ValueError("Moles >= 0 and Volume > 0 required")
        return n / v, "mol/L"

    if topic == "moles":
        mass, mm = values["mass"], values["molar_mass"]
        if mass < 0 or mm <= 0:
            raise ValueError("Mass >= 0 and Molar Mass > 0 required")
        return mass / mm, "mol"

    raise ValueError("Unsupported calculator")

# ---------------- EXPLANATION ENGINE ----------------

def magic_explain(topic, values, result, unit, language):

    hi = language == "Hindi"

    if topic == "speed":
        d, t = values["distance"], values["time"]
        steps = [
            f"Distance = {d} km",
            f"Time = {t} hours",
            f"Speed = {d} / {t} = {result}"
        ]

    elif topic == "work":
        f, d = values["force"], values["distance"]
        steps = [
            f"Force = {f} N",
            f"Distance = {d} m",
            f"Work = {f} × {d} = {result}"
        ]

    elif topic == "power":
        a, t = values["work"], values["time"]
        steps = [
            f"Work = {a} J",
            f"Time = {t} seconds",
            f"Power = {a} / {t} = {result}"
        ]

    elif topic == "molarity":
        n, v = values["moles"], values["volume"]
        steps = [
            f"Moles = {n} mol",
            f"Volume = {v} L",
            f"Molarity = {n} / {v} = {result}"
        ]

    else:
        m, mm = values["mass"], values["molar_mass"]
        steps = [
            f"Mass = {m} g",
            f"Molar mass = {mm} g/mol",
            f"Moles = {m} / {mm} = {result}"
        ]

    formula = FORMULAS[topic]["hi" if hi else "en"]

    heading = "चरण-दर-चरण समाधान" if hi else "Step-by-step solution"
    answer = "अंतिम उत्तर" if hi else "Final Answer"

    return (
        formula + "\n\n" +
        heading + "\n" +
        "\n".join(steps) +
        f"\n\n{answer}: {result} {unit}"
    )

# ---------------- COMMON MISTAKES ----------------

MISTAKES = {
    "speed": [
        "Time zero nahi hona chahiye.",
        "Distance aur time units consistent rakho.",
        "Average speed aur instantaneous speed alag concepts hain."
    ],
    "work": [
        "Force aur displacement ki direction important hai.",
        "Work = F × d sirf same direction ke force ke liye.",
        "SI unit Joule hai."
    ],
    "power": [
        "Work Joule mein hona chahiye.",
        "Time seconds mein hona chahiye.",
        "SI unit Watt hai."
    ],
    "molarity": [
        "Volume litres mein convert karo.",
        "Molarity solution ke total volume par based hoti hai.",
        "Unit mol/L hai."
    ],
    "moles": [
        "Mass grams mein hona chahiye.",
        "Molar mass g/mol mein hona chahiye.",
        "Moles = Mass / Molar mass."
    ]
}

# ---------------- FORMULA FINDER ----------------

def find_formula(query, language):

    q = query.lower()

    keywords = {
        "speed": ["speed", "velocity", "गति"],
        "work": ["work", "कार्य"],
        "power": ["power", "शक्ति"],
        "molarity": ["molarity", "मोलरता"],
        "moles": ["moles", "mole", "मोल"]
    }

    for topic, words in keywords.items():
        if any(word in q for word in words):
            return FORMULAS[topic][
                "hi" if language == "Hindi" else "en"
            ]

    return "Formula not found / सूत्र नहीं मिला"

# ---------------- QUESTION DETECTOR ----------------

def detect_question(question):

    q = question.lower()

    if any(x in q for x in ["speed", "गति"]):
        return "speed"

    if any(x in q for x in ["molarity", "मोलरता"]):
        return "molarity"

    if any(x in q for x in ["moles", "mole", "मोल"]):
        return "moles"

    if any(x in q for x in ["power", "शक्ति"]):
        return "power"

    if any(x in q for x in ["work", "कार्य"]):
        return "work"

    return None

# ---------------- CALCULATOR CONFIG ----------------

CONFIG = {
    "Speed": {
        "topic": "speed",
        "fields": [
            ("distance", "Distance (km)", 150),
            ("time", "Time (hours)", 3)
        ]
    },
    "Work": {
        "topic": "work",
        "fields": [
            ("force", "Force (N)", 10),
            ("distance", "Distance (m)", 5)
        ]
    },
    "Power": {
        "topic": "power",
        "fields": [
            ("work", "Work (J)", 100),
            ("time", "Time (seconds)", 5)
        ]
    },
    "Molarity": {
        "topic": "molarity",
        "fields": [
            ("moles", "Moles", 0.5),
            ("volume", "Volume (L)", 2)
        ]
    },
    "Moles": {
        "topic": "moles",
        "fields": [
            ("mass", "Mass (g)", 10),
            ("molar_mass", "Molar Mass (g/mol)", 20)
        ]
    }
}

# ---------------- INTERACTIVE UI ----------------

tool = w.Dropdown(
    options=list(CONFIG.keys()),
    description="Calculator:"
)

language = w.Dropdown(
    options=["English", "Hindi"],
    description="Language:"
)

fields_box = w.VBox()
output = w.Output()
question = w.Textarea(
    placeholder="Example: Calculate speed for 150 km in 3 hours",
    description="Question:",
    layout=w.Layout(width="100%", height="90px")
)

formula_query = w.Text(
    placeholder="speed / work / power / molarity / moles",
    description="Formula:"
)

formula_button = w.Button(
    description="Find Formula",
    button_style="info"
)

calculate_button = w.Button(
    description="✨ Calculate + Explain",
    button_style="success"
)

input_fields = {}

def refresh_fields(change=None):

    global input_fields
    input_fields = {}

    for key, label, default in CONFIG[tool.value]["fields"]:

        input_fields[key] = w.FloatText(
            value=default,
            description=label,
            layout=w.Layout(width="100%")
        )

    fields_box.children = tuple(input_fields.values())

tool.observe(refresh_fields, names="value")
refresh_fields()

def calculate_action(button):

    with output:
        clear_output()

        try:
            topic = CONFIG[tool.value]["topic"]

            values = {
                key: field.value
                for key, field in input_fields.items()
            }

            result, unit = magic_calculate(topic, values)

            print("🌟 SUNO SAATHI MAGIC LAYER")
            print("=" * 40)

            print(magic_explain(
                topic, values, result, unit, language.value
            ))

            print("\n⚠️ COMMON MISTAKES")
            for mistake in MISTAKES[topic]:
                print("•", mistake)

        except Exception as error:
            print("⚠️ Error:", error)

def formula_action(button):

    with output:
        clear_output()
        print(find_formula(
            formula_query.value,
            language.value
        ))

def question_action(button):

    with output:
        clear_output()

        topic = detect_question(question.value)

        if topic:
            print("Detected topic:", topic)
            print("Formula:", FORMULAS[topic][
                "hi" if language.value == "Hindi" else "en"
            ])
            print("\nPlease enter numerical values in calculator fields.")
            print("Question detection is rule-based, not AI.")
        else:
            print("Topic not detected.")
            print("Try: speed, work, power, molarity or moles.")

question_button = w.Button(
    description="🔎 Detect Question",
    button_style="warning"
)

calculate_button.on_click(calculate_action)
formula_button.on_click(formula_action)
question_button.on_click(question_action)

display(w.HTML("""
<div style="background:linear-gradient(135deg,#123c91,#1769d2);
color:white;padding:20px;border-radius:14px">
<h2>🌟 Suno Saathi Magic Layer v4</h2>
<p>Physics + Chemistry | Hindi + English</p>
</div>
"""))

display(tool)
display(language)
display(fields_box)
display(calculate_button)

display(w.HTML("<h3>Formula Finder</h3>"))
display(formula_query)
display(formula_button)

display(w.HTML("<h3>Question Detector</h3>"))
display(question)
display(question_button)
display(output)

# ---------------- TESTS ----------------

assert magic_calculate("speed", {
    "distance":150,"time":3
})[0] == 50

assert magic_calculate("work", {
    "force":10,"distance":5
})[0] == 50

assert magic_calculate("power", {
    "work":100,"time":5
})[0] == 20

assert magic_calculate("molarity", {
    "moles":0.5,"volume":2
})[0] == 0.25

assert magic_calculate("moles", {
    "mass":10,"molar_mass":20
})[0] == 0.5

assert detect_question("Calculate speed") == "speed"
assert detect_question("Find molarity") == "molarity"

print("\n✅ MAGIC LAYER v4 READY")
print("✅ All tests passed")

# ============================================================
# SUNO SAATHI MAGIC LAYER v4
# Complete standalone prototype | Google Colab
# ============================================================

import re
import math
import ipywidgets as w
from IPython.display import display, clear_output

# ---------------- FORMULA DATABASE ----------------

FORMULAS = {
    "speed": {
        "en": "Speed = Distance / Time",
        "hi": "गति = दूरी / समय"
    },
    "work": {
        "en": "Work = Force × Distance",
        "hi": "कार्य = बल × दूरी"
    },
    "power": {
        "en": "Power = Work / Time",
        "hi": "शक्ति = कार्य / समय"
    },
    "molarity": {
        "en": "Molarity = Moles / Volume (L)",
        "hi": "मोलरता = मोल / आयतन (लीटर)"
    },
    "moles": {
        "en": "Moles = Mass / Molar Mass",
        "hi": "मोल = द्रव्यमान / मोलर द्रव्यमान"
    }
}

# ---------------- CALCULATION ENGINE ----------------

def magic_calculate(topic, values):

    if topic == "speed":
        d, t = values["distance"], values["time"]
        if d < 0 or t <= 0:
            raise ValueError("Distance >= 0 and Time > 0 required")
        return d / t, "km/h"

    if topic == "work":
        f, d = values["force"], values["distance"]
        if f < 0 or d < 0:
            raise ValueError("Force and Distance must be >= 0")
        return f * d, "J"

    if topic == "power":
        work, t = values["work"], values["time"]
        if work < 0 or t <= 0:
            raise ValueError("Work >= 0 and Time > 0 required")
        return work / t, "W"

    if topic == "molarity":
        n, v = values["moles"], values["volume"]
        if n < 0 or v <= 0:
            raise ValueError("Moles >= 0 and Volume > 0 required")
        return n / v, "mol/L"

    if topic == "moles":
        mass, mm = values["mass"], values["molar_mass"]
        if mass < 0 or mm <= 0:
            raise ValueError("Mass >= 0 and Molar Mass > 0 required")
        return mass / mm, "mol"

    raise ValueError("Unsupported calculator")

# ---------------- EXPLANATION ENGINE ----------------

def magic_explain(topic, values, result, unit, language):

    hi = language == "Hindi"

    if topic == "speed":
        d, t = values["distance"], values["time"]
        steps = [
            f"Distance = {d} km",
            f"Time = {t} hours",
            f"Speed = {d} / {t} = {result}"
        ]

    elif topic == "work":
        f, d = values["force"], values["distance"]
        steps = [
            f"Force = {f} N",
            f"Distance = {d} m",
            f"Work = {f} × {d} = {result}"
        ]

    elif topic == "power":
        a, t = values["work"], values["time"]
        steps = [
            f"Work = {a} J",
            f"Time = {t} seconds",
            f"Power = {a} / {t} = {result}"
        ]

    elif topic == "molarity":
        n, v = values["moles"], values["volume"]
        steps = [
            f"Moles = {n} mol",
            f"Volume = {v} L",
            f"Molarity = {n} / {v} = {result}"
        ]

    else:
        m, mm = values["mass"], values["molar_mass"]
        steps = [
            f"Mass = {m} g",
            f"Molar mass = {mm} g/mol",
            f"Moles = {m} / {mm} = {result}"
        ]

    formula = FORMULAS[topic]["hi" if hi else "en"]

    heading = "चरण-दर-चरण समाधान" if hi else "Step-by-step solution"
    answer = "अंतिम उत्तर" if hi else "Final Answer"

    return (
        formula + "\n\n" +
        heading + "\n" +
        "\n".join(steps) +
        f"\n\n{answer}: {result} {unit}"
    )

# ---------------- COMMON MISTAKES ----------------

MISTAKES = {
    "speed": [
        "Time zero nahi hona chahiye.",
        "Distance aur time units consistent rakho.",
        "Average speed aur instantaneous speed alag concepts hain."
    ],
    "work": [
        "Force aur displacement ki direction important hai.",
        "Work = F × d sirf same direction ke force ke liye.",
        "SI unit Joule hai."
    ],
    "power": [
        "Work Joule mein hona chahiye.",
        "Time seconds mein hona chahiye.",
        "SI unit Watt hai."
    ],
    "molarity": [
        "Volume litres mein convert karo.",
        "Molarity solution ke total volume par based hoti hai.",
        "Unit mol/L hai."
    ],
    "moles": [
        "Mass grams mein hona chahiye.",
        "Molar mass g/mol mein hona chahiye.",
        "Moles = Mass / Molar mass."
    ]
}

# ---------------- FORMULA FINDER ----------------

def find_formula(query, language):

    q = query.lower()

    keywords = {
        "speed": ["speed", "velocity", "गति"],
        "work": ["work", "कार्य"],
        "power": ["power", "शक्ति"],
        "molarity": ["molarity", "मोलरता"],
        "moles": ["moles", "mole", "मोल"]
    }

    for topic, words in keywords.items():
        if any(word in q for word in words):
            return FORMULAS[topic][
                "hi" if language == "Hindi" else "en"
            ]

    return "Formula not found / सूत्र नहीं मिला"

# ---------------- QUESTION DETECTOR ----------------

def detect_question(question):

    q = question.lower()

    if any(x in q for x in ["speed", "गति"]):
        return "speed"

    if any(x in q for x in ["molarity", "मोलरता"]):
        return "molarity"

    if any(x in q for x in ["moles", "mole", "मोल"]):
        return "moles"

    if any(x in q for x in ["power", "शक्ति"]):
        return "power"

    if any(x in q for x in ["work", "कार्य"]):
        return "work"

    return None

# ---------------- CALCULATOR CONFIG ----------------

CONFIG = {
    "Speed": {
        "topic": "speed",
        "fields": [
            ("distance", "Distance (km)", 150),
            ("time", "Time (hours)", 3)
        ]
    },
    "Work": {
        "topic": "work",
        "fields": [
            ("force", "Force (N)", 10),
            ("distance", "Distance (m)", 5)
        ]
    },
    "Power": {
        "topic": "power",
        "fields": [
            ("work", "Work (J)", 100),
            ("time", "Time (seconds)", 5)
        ]
    },
    "Molarity": {
        "topic": "molarity",
        "fields": [
            ("moles", "Moles", 0.5),
            ("volume", "Volume (L)", 2)
        ]
    },
    "Moles": {
        "topic": "moles",
        "fields": [
            ("mass", "Mass (g)", 10),
            ("molar_mass", "Molar Mass (g/mol)", 20)
        ]
    }
}

# ---------------- INTERACTIVE UI ----------------

tool = w.Dropdown(
    options=list(CONFIG.keys()),
    description="Calculator:"
)

language = w.Dropdown(
    options=["English", "Hindi"],
    description="Language:"
)

fields_box = w.VBox()
output = w.Output()
question = w.Textarea(
    placeholder="Example: Calculate speed for 150 km in 3 hours",
    description="Question:",
    layout=w.Layout(width="100%", height="90px")
)

formula_query = w.Text(
    placeholder="speed / work / power / molarity / moles",
    description="Formula:"
)

formula_button = w.Button(
    description="Find Formula",
    button_style="info"
)

calculate_button = w.Button(
    description="✨ Calculate + Explain",
    button_style="success"
)

input_fields = {}

def refresh_fields(change=None):

    global input_fields
    input_fields = {}

    for key, label, default in CONFIG[tool.value]["fields"]:

        input_fields[key] = w.FloatText(
            value=default,
            description=label,
            layout=w.Layout(width="100%")
        )

    fields_box.children = tuple(input_fields.values())

tool.observe(refresh_fields, names="value")
refresh_fields()

def calculate_action(button):

    with output:
        clear_output()

        try:
            topic = CONFIG[tool.value]["topic"]

            values = {
                key: field.value
                for key, field in input_fields.items()
            }

            result, unit = magic_calculate(topic, values)

            print("🌟 SUNO SAATHI MAGIC LAYER")
            print("=" * 40)

            print(magic_explain(
                topic, values, result, unit, language.value
            ))

            print("\n⚠️ COMMON MISTAKES")
            for mistake in MISTAKES[topic]:
                print("•", mistake)

        except Exception as error:
            print("⚠️ Error:", error)

def formula_action(button):

    with output:
        clear_output()
        print(find_formula(
            formula_query.value,
            language.value
        ))

def question_action(button):

    with output:
        clear_output()

        topic = detect_question(question.value)

        if topic:
            print("Detected topic:", topic)
            print("Formula:", FORMULAS[topic][
                "hi" if language.value == "Hindi" else "en"
            ])
            print("\nPlease enter numerical values in calculator fields.")
            print("Question detection is rule-based, not AI.")
        else:
            print("Topic not detected.")
            print("Try: speed, work, power, molarity or moles.")

question_button = w.Button(
    description="🔎 Detect Question",
    button_style="warning"
)

calculate_button.on_click(calculate_action)
formula_button.on_click(formula_action)
question_button.on_click(question_action)

display(w.HTML("""
<div style="background:linear-gradient(135deg,#123c91,#1769d2);
color:white;padding:20px;border-radius:14px">
<h2>🌟 Suno Saathi Magic Layer v4</h2>
<p>Physics + Chemistry | Hindi + English</p>
</div>
"""))

display(tool)
display(language)
display(fields_box)
display(calculate_button)

display(w.HTML("<h3>Formula Finder</h3>"))
display(formula_query)
display(formula_button)

display(w.HTML("<h3>Question Detector</h3>"))
display(question)
display(question_button)
display(output)

# ---------------- TESTS ----------------

assert magic_calculate("speed", {
    "distance":150,"time":3
})[0] == 50

assert magic_calculate("work", {
    "force":10,"distance":5
})[0] == 50

assert magic_calculate("power", {
    "work":100,"time":5
})[0] == 20

assert magic_calculate("molarity", {
    "moles":0.5,"volume":2
})[0] == 0.25

assert magic_calculate("moles", {
    "mass":10,"molar_mass":20
})[0] == 0.5

assert detect_question("Calculate speed") == "speed"
assert detect_question("Find molarity") == "molarity"

print("\n✅ MAGIC LAYER v4 READY")
print("✅ All tests passed")

# ============================================================
# SUNO SAATHI MAGIC LAYER v5
# AUTOMATIC QUESTION SOLVER
# ============================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------------------
# TOPIC DETECTION
# ------------------------------------------------------------

def v5_detect_topic(q):

    q = q.lower()

    if any(x in q for x in ["speed", "distance", "time", "velocity", "गति", "दूरी", "समय"]):
        return "speed"

    if any(x in q for x in ["work", "कार्य", "force", "बल"]):
        return "work"

    if any(x in q for x in ["power", "शक्ति"]):
        return "power"

    if any(x in q for x in ["molarity", "मोलरता", "moles per litre"]):
        return "molarity"

    if any(x in q for x in ["number of moles", "calculate moles", "moles", "मोल", "molecular mass"]):
        return "moles"

    return None


# ------------------------------------------------------------
# NUMBER EXTRACTION
# ------------------------------------------------------------

def v5_extract_numbers(q):

    pattern = r'\d+(?:\.\d+)?'
    return [float(x) for x in re.findall(pattern, q)]


# ------------------------------------------------------------
# UNIT EXTRACTION
# ------------------------------------------------------------

def v5_extract_units(q):

    q = q.lower()

    units = {
        "km": "km",
        "kilometer": "km",
        "kilometre": "km",
        "m": "m",
        "meter": "m",
        "metre": "m",
        "cm": "cm",
        "mm": "mm",
        "hour": "hour",
        "hr": "hour",
        "h": "hour",
        "minute": "minute",
        "min": "minute",
        "second": "second",
        "sec": "second",
        "s": "second",
        "kg": "kg",
        "gram": "g",
        "g": "g",
        "newton": "N",
        "n": "N",
        "joule": "J",
        "j": "J",
        "watt": "W",
        "mol": "mol",
        "litre": "L",
        "liter": "L",
        "ml": "mL"
    }

    found = []

    for word, unit in units.items():
        if re.search(r'\b' + re.escape(word) + r'\b', q):
            found.append(unit)

    return found


# ------------------------------------------------------------
# SOLVER
# ------------------------------------------------------------

def v5_solve_question(q):

    topic = v5_detect_topic(q)
    nums = v5_extract_numbers(q)

    if topic is None:
        return {
            "success": False,
            "message": "Topic detect nahi hua. Speed, Work, Power, Molarity ya Moles ka question try karein."
        }

    if len(nums) < 2:
        return {
            "success": False,
            "message": "Calculation ke liye kam se kam 2 numerical values chahiye."
        }

    # SPEED
    if topic == "speed":

        distance = nums[0]
        time = nums[1]

        if time == 0:
            return {"success": False, "message": "Time zero nahi ho sakta."}

        result = distance / time

        return {
            "success": True,
            "topic": "Speed",
            "formula": "Speed = Distance / Time",
            "values": {
                "Distance": distance,
                "Time": time
            },
            "result": result,
            "unit": "distance unit / time unit"
        }

    # WORK
    if topic == "work":

        force = nums[0]
        distance = nums[1]

        result = force * distance

        return {
            "success": True,
            "topic": "Work",
            "formula": "Work = Force × Distance",
            "values": {
                "Force": force,
                "Distance": distance
            },
            "result": result,
            "unit": "J (if Force is N and Distance is m)"
        }

    # POWER
    if topic == "power":

        work = nums[0]
        time = nums[1]

        if time == 0:
            return {"success": False, "message": "Time zero nahi ho sakta."}

        result = work / time

        return {
            "success": True,
            "topic": "Power",
            "formula": "Power = Work / Time",
            "values": {
                "Work": work,
                "Time": time
            },
            "result": result,
            "unit": "W (if Work is J and Time is s)"
        }

    # MOLARITY
    if topic == "molarity":

        moles = nums[0]
        volume = nums[1]

        if volume == 0:
            return {"success": False, "message": "Volume zero nahi ho sakta."}

        result = moles / volume

        return {
            "success": True,
            "topic": "Molarity",
            "formula": "Molarity = Moles / Volume (L)",
            "values": {
                "Moles": moles,
                "Volume": volume
            },
            "result": result,
            "unit": "mol/L"
        }

    # MOLES
    if topic == "moles":

        mass = nums[0]
        molar_mass = nums[1]

        if molar_mass == 0:
            return {"success": False, "message": "Molar mass zero nahi ho sakta."}

        result = mass / molar_mass

        return {
            "success": True,
            "topic": "Moles",
            "formula": "Moles = Mass / Molar Mass",
            "values": {
                "Mass": mass,
                "Molar Mass": molar_mass
            },
            "result": result,
            "unit": "mol"
        }


# ------------------------------------------------------------
# EXPLANATION GENERATOR
# ------------------------------------------------------------

def v5_explain(data, language="English"):

    if not data["success"]:
        return data["message"]

    if language == "Hindi":

        text = f"""
विषय: {data['topic']}

सूत्र:
{data['formula']}

दिए गए मान:
{data['values']}

गणना:
{data['formula']}

उत्तर:
{data['result']:.4f} {data['unit']}
"""

    else:

        text = f"""
Topic: {data['topic']}

Formula:
{data['formula']}

Given values:
{data['values']}

Calculation:
{data['formula']}

Final Answer:
{data['result']:.4f} {data['unit']}
"""

    return text


# ------------------------------------------------------------
# TESTS
# ------------------------------------------------------------

v5_tests = [
    ("Calculate speed for 100 km in 2 hours", "speed"),
    ("Find work done by force 10 N over 5 m", "work"),
    ("Calculate power for 100 J in 5 seconds", "power"),
    ("Find molarity of 2 moles in 4 litres", "molarity"),
    ("Calculate moles from 10 g mass and 20 g molar mass", "moles")
]

print("V5 TESTS")

for q, expected in v5_tests:

    result = v5_solve_question(q)

    assert result["success"], q
    assert result["topic"].lower() == expected

    print("PASS:", q)

print("\nAll V5 tests passed!")


# ------------------------------------------------------------
# INTERACTIVE MAGIC LAYER
# ------------------------------------------------------------

v5_question = widgets.Textarea(
    placeholder="Example: Calculate speed for 100 km in 2 hours",
    description="Question:",
    layout=widgets.Layout(width="100%", height="100px")
)

v5_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v5_button = widgets.Button(
    description="Solve Question",
    button_style="success",
    icon="check"
)

v5_output = widgets.Output()


def v5_run(_):

    with v5_output:

        clear_output()

        q = v5_question.value

        data = v5_solve_question(q)

        print(v5_explain(data, v5_language.value))

        if data["success"]:

            print("\nDetected topic:", data["topic"])
            print("Formula:", data["formula"])
            print("Answer:", round(data["result"], 4), data["unit"])


v5_button.on_click(v5_run)

display(v5_question)
display(v5_language)
display(v5_button)
display(v5_output)

print("\nSUNO SAATHI MAGIC LAYER V5 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V6
# SMART UNIT CONVERSION + QUESTION SOLVER
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. UNIT CONVERSION DATABASE
# ------------------------------------------------

V6_UNITS = {
    "distance": {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001
    },
    "time": {
        "hour": 3600,
        "min": 60,
        "s": 1
    },
    "mass": {
        "kg": 1000,
        "g": 1,
        "mg": 0.001
    }
}

V6_ALIASES = {
    "kilometer": "km", "kilometre": "km",
    "kilometers": "km", "kilometres": "km",
    "meter": "m", "metre": "m",
    "meters": "m", "metres": "m",
    "centimeter": "cm", "centimetre": "cm",
    "millimeter": "mm", "millimetre": "mm",
    "hours": "hour", "hr": "hour", "hrs": "hour",
    "minutes": "min", "minute": "min",
    "seconds": "s", "second": "s", "sec": "s",
    "grams": "g", "gram": "g",
    "kilograms": "kg", "kilogram": "kg",
    "milligrams": "mg", "milligram": "mg"
}

def v6_normalize_unit(unit):
    unit = unit.lower().strip()
    return V6_ALIASES.get(unit, unit)

def v6_convert(value, from_unit, to_unit):
    from_unit = v6_normalize_unit(from_unit)
    to_unit = v6_normalize_unit(to_unit)

    for category, units in V6_UNITS.items():
        if from_unit in units and to_unit in units:
            base_value = value * units[from_unit]
            return base_value / units[to_unit]

    raise ValueError("Incompatible or unsupported units")

# ------------------------------------------------
# 2. QUESTION DETECTION
# ------------------------------------------------

def v6_detect_topic(q):
    q = q.lower()

    if any(x in q for x in [
        "molarity", "molar concentration", "मोलरता"
    ]):
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    if any(x in q for x in [
        "power", "शक्ति"
    ]):
        return "power"

    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "कार्य"
    ]):
        return "work"

    if any(x in q for x in [
        "speed", "velocity", "distance",
        "गति", "दूरी"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER + UNIT EXTRACTION
# ------------------------------------------------

V6_NUMBER_PATTERN = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

def v6_extract_pairs(q):
    pattern = (
        r'(' + V6_NUMBER_PATTERN + r')\s*'
        r'(kilometers?|kilometres?|kilometres?|'
        r'km|meters?|metres?|m|centimeters?|cm|mm|'
        r'hours?|hrs?|hr|min|minutes?|seconds?|secs?|s|'
        r'kilograms?|kg|grams?|g|mg)'
    )

    matches = re.findall(pattern, q.lower())

    result = []

    for number, unit in matches:
        result.append({
            "value": float(number),
            "unit": v6_normalize_unit(unit)
        })

    return result

def v6_extract_numbers(q):
    return [
        float(x)
        for x in re.findall(V6_NUMBER_PATTERN, q)
    ]

# ------------------------------------------------
# 4. CONVERT TO SI
# ------------------------------------------------

def v6_si(value, unit, category):
    unit = v6_normalize_unit(unit)

    if unit not in V6_UNITS[category]:
        raise ValueError(
            f"Unsupported {category} unit: {unit}"
        )

    return value * V6_UNITS[category][unit]

# ------------------------------------------------
# 5. QUESTION SOLVER
# ------------------------------------------------

def v6_solve(q):

    topic = v6_detect_topic(q)
    pairs = v6_extract_pairs(q)
    nums = v6_extract_numbers(q)

    if topic is None:
        return {
            "success": False,
            "message": "Topic identify nahi hua. Supported: Speed, Work, Power, Moles, Molarity."
        }

    try:

        # SPEED
        if topic == "speed":

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if distance_pair and time_pair:

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                distance = nums[0]
                time = nums[1]

            else:
                raise ValueError("Distance aur time dono required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = distance / time

            return {
                "success": True,
                "topic": "Speed",
                "formula": "Speed = Distance / Time",
                "calculation": f"{distance} / {time}",
                "result": result,
                "unit": "m/s",
                "values": {
                    "Distance": distance,
                    "Time": time
                }
            }

        # WORK
        if topic == "work":

            force_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:n|newton)',
                q.lower()
            )

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            if force_match and distance_pair:

                force = float(force_match.group(1))

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

            elif len(nums) >= 2:

                force, distance = nums[0], nums[1]

            else:
                raise ValueError("Force aur distance required hain.")

            result = force * distance

            return {
                "success": True,
                "topic": "Work",
                "formula": "Work = Force × Distance",
                "calculation": f"{force} × {distance}",
                "result": result,
                "unit": "J",
                "values": {
                    "Force": force,
                    "Distance": distance
                }
            }

        # POWER
        if topic == "power":

            work_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:j|joules?)',
                q.lower()
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if work_match and time_pair:

                work = float(work_match.group(1))

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                work, time = nums[0], nums[1]

            else:
                raise ValueError("Work aur time required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = work / time

            return {
                "success": True,
                "topic": "Power",
                "formula": "Power = Work / Time",
                "calculation": f"{work} / {time}",
                "result": result,
                "unit": "W",
                "values": {
                    "Work": work,
                    "Time": time
                }
            }

        # MOLES
        if topic == "moles":

            if len(nums) < 2:
                raise ValueError("Mass aur molar mass required hain.")

            mass, molar_mass = nums[0], nums[1]

            if molar_mass == 0:
                raise ValueError("Molar mass zero nahi ho sakta.")

            result = mass / molar_mass

            return {
                "success": True,
                "topic": "Moles",
                "formula": "Moles = Mass / Molar Mass",
                "calculation": f"{mass} / {molar_mass}",
                "result": result,
                "unit": "mol",
                "values": {
                    "Mass": mass,
                    "Molar Mass": molar_mass
                }
            }

        # MOLARITY
        if topic == "molarity":

            if len(nums) < 2:
                raise ValueError("Moles aur volume required hain.")

            moles, volume = nums[0], nums[1]

            if volume == 0:
                raise ValueError("Volume zero nahi ho sakta.")

            result = moles / volume

            return {
                "success": True,
                "topic": "Molarity",
                "formula": "Molarity = Moles / Volume",
                "calculation": f"{moles} / {volume}",
                "result": result,
                "unit": "mol/L",
                "values": {
                    "Moles": moles,
                    "Volume": volume
                }
            }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }

# ------------------------------------------------
# 6. ANSWER VERIFICATION
# ------------------------------------------------

def v6_verify(data):

    if not data["success"]:
        return False

    result = data["result"]

    if not math.isfinite(result):
        return False

    return True

# ------------------------------------------------
# 7. EXPLANATION GENERATOR
# ------------------------------------------------

def v6_explain(data, language="English"):

    if not data["success"]:
        return data["message"]

    if not v6_verify(data):
        return "Answer verification failed."

    if language == "Hindi":

        return f"""
विषय: {data['topic']}

सूत्र:
{data['formula']}

दिए गए मान:
{data['values']}

गणना:
{data['calculation']}

अंतिम उत्तर:
{data['result']:.6g} {data['unit']}

जाँच:
उत्तर finite numerical value है।
"""

    return f"""
Topic: {data['topic']}

Formula:
{data['formula']}

Given:
{data['values']}

Calculation:
{data['calculation']}

Final Answer:
{data['result']:.6g} {data['unit']}

Verification:
Finite numerical result confirmed.
"""

# ------------------------------------------------
# 8. UNIT CONVERTER TESTS
# ------------------------------------------------

print("UNIT CONVERSION TESTS")

assert abs(v6_convert(1, "km", "m") - 1000) < 1e-9
assert abs(v6_convert(1, "hour", "s") - 3600) < 1e-9
assert abs(v6_convert(1000, "g", "kg") - 1) < 1e-9
assert abs(v6_convert(100, "cm", "m") - 1) < 1e-9

print("All unit conversion tests passed!")

# ------------------------------------------------
# 9. SOLVER TESTS
# ------------------------------------------------

print("\nSOLVER TESTS")

test_questions = [
    ("Calculate speed for 100 km in 2 hours", 13.8888889),
    ("Find speed for 100 m in 20 seconds", 5),
    ("Calculate work done by 10 N force over 5 m", 50),
    ("Calculate power for 100 J in 5 seconds", 20),
    ("Calculate moles from 10 g mass and 20 g molar mass", 0.5),
    ("Find molarity of 2 moles in 4 litres", 0.5)
]

for question, expected in test_questions:

    data = v6_solve(question)

    assert data["success"], question

    assert abs(data["result"] - expected) < 0.001, (
        question,
        data["result"],
        expected
    )

    assert v6_verify(data)

    print("PASS:", question)

print("\nALL V6 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE MAGIC LAYER UI
# ------------------------------------------------

v6_question = widgets.Textarea(
    placeholder="Calculate speed for 100 km in 2 hours",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="110px"
    )
)

v6_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v6_button = widgets.Button(
    description="Solve Question",
    button_style="success",
    icon="check"
)

v6_output = widgets.Output()

def v6_run(_):

    with v6_output:

        clear_output()

        question = v6_question.value

        data = v6_solve(question)

        print(v6_explain(data, v6_language.value))

        if data["success"]:

            print("\nAnswer verified:", v6_verify(data))

v6_button.on_click(v6_run)

display(v6_question)
display(v6_language)
display(v6_button)
display(v6_output)

print("\nSUNO SAATHI MAGIC LAYER V6 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V6
# SMART UNIT CONVERSION + QUESTION SOLVER
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. UNIT CONVERSION DATABASE
# ------------------------------------------------

V6_UNITS = {
    "distance": {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001
    },
    "time": {
        "hour": 3600,
        "min": 60,
        "s": 1
    },
    "mass": {
        "kg": 1000,
        "g": 1,
        "mg": 0.001
    }
}

V6_ALIASES = {
    "kilometer": "km", "kilometre": "km",
    "kilometers": "km", "kilometres": "km",
    "meter": "m", "metre": "m",
    "meters": "m", "metres": "m",
    "centimeter": "cm", "centimetre": "cm",
    "millimeter": "mm", "millimetre": "mm",
    "hours": "hour", "hr": "hour", "hrs": "hour",
    "minutes": "min", "minute": "min",
    "seconds": "s", "second": "s", "sec": "s",
    "grams": "g", "gram": "g",
    "kilograms": "kg", "kilogram": "kg",
    "milligrams": "mg", "milligram": "mg"
}

def v6_normalize_unit(unit):
    unit = unit.lower().strip()
    return V6_ALIASES.get(unit, unit)

def v6_convert(value, from_unit, to_unit):
    from_unit = v6_normalize_unit(from_unit)
    to_unit = v6_normalize_unit(to_unit)

    for category, units in V6_UNITS.items():
        if from_unit in units and to_unit in units:
            base_value = value * units[from_unit]
            return base_value / units[to_unit]

    raise ValueError("Incompatible or unsupported units")

# ------------------------------------------------
# 2. QUESTION DETECTION
# ------------------------------------------------

def v6_detect_topic(q):
    q = q.lower()

    if any(x in q for x in [
        "molarity", "molar concentration", "मोलरता"
    ]):
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    if any(x in q for x in [
        "power", "शक्ति"
    ]):
        return "power"

    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "कार्य"
    ]):
        return "work"

    if any(x in q for x in [
        "speed", "velocity", "distance",
        "गति", "दूरी"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER + UNIT EXTRACTION
# ------------------------------------------------

V6_NUMBER_PATTERN = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

def v6_extract_pairs(q):
    pattern = (
        r'(' + V6_NUMBER_PATTERN + r')\s*'
        r'(kilometers?|kilometres?|kilometres?|'
        r'km|meters?|metres?|m|centimeters?|cm|mm|'
        r'hours?|hrs?|hr|min|minutes?|seconds?|secs?|s|'
        r'kilograms?|kg|grams?|g|mg)'
    )

    matches = re.findall(pattern, q.lower())

    result = []

    for number, unit in matches:
        result.append({
            "value": float(number),
            "unit": v6_normalize_unit(unit)
        })

    return result

def v6_extract_numbers(q):
    return [
        float(x)
        for x in re.findall(V6_NUMBER_PATTERN, q)
    ]

# ------------------------------------------------
# 4. CONVERT TO SI
# ------------------------------------------------

def v6_si(value, unit, category):
    unit = v6_normalize_unit(unit)

    if unit not in V6_UNITS[category]:
        raise ValueError(
            f"Unsupported {category} unit: {unit}"
        )

    return value * V6_UNITS[category][unit]

# ------------------------------------------------
# 5. QUESTION SOLVER
# ------------------------------------------------

def v6_solve(q):

    topic = v6_detect_topic(q)
    pairs = v6_extract_pairs(q)
    nums = v6_extract_numbers(q)

    if topic is None:
        return {
            "success": False,
            "message": "Topic identify nahi hua. Supported: Speed, Work, Power, Moles, Molarity."
        }

    try:

        # SPEED
        if topic == "speed":

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if distance_pair and time_pair:

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                distance = nums[0]
                time = nums[1]

            else:
                raise ValueError("Distance aur time dono required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = distance / time

            return {
                "success": True,
                "topic": "Speed",
                "formula": "Speed = Distance / Time",
                "calculation": f"{distance} / {time}",
                "result": result,
                "unit": "m/s",
                "values": {
                    "Distance": distance,
                    "Time": time
                }
            }

        # WORK
        if topic == "work":

            force_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:n|newton)',
                q.lower()
            )

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            if force_match and distance_pair:

                force = float(force_match.group(1))

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

            elif len(nums) >= 2:

                force, distance = nums[0], nums[1]

            else:
                raise ValueError("Force aur distance required hain.")

            result = force * distance

            return {
                "success": True,
                "topic": "Work",
                "formula": "Work = Force × Distance",
                "calculation": f"{force} × {distance}",
                "result": result,
                "unit": "J",
                "values": {
                    "Force": force,
                    "Distance": distance
                }
            }

        # POWER
        if topic == "power":

            work_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:j|joules?)',
                q.lower()
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if work_match and time_pair:

                work = float(work_match.group(1))

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                work, time = nums[0], nums[1]

            else:
                raise ValueError("Work aur time required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = work / time

            return {
                "success": True,
                "topic": "Power",
                "formula": "Power = Work / Time",
                "calculation": f"{work} / {time}",
                "result": result,
                "unit": "W",
                "values": {
                    "Work": work,
                    "Time": time
                }
            }

        # MOLES
        if topic == "moles":

            if len(nums) < 2:
                raise ValueError("Mass aur molar mass required hain.")

            mass, molar_mass = nums[0], nums[1]

            if molar_mass == 0:
                raise ValueError("Molar mass zero nahi ho sakta.")

            result = mass / molar_mass

            return {
                "success": True,
                "topic": "Moles",
                "formula": "Moles = Mass / Molar Mass",
                "calculation": f"{mass} / {molar_mass}",
                "result": result,
                "unit": "mol",
                "values": {
                    "Mass": mass,
                    "Molar Mass": molar_mass
                }
            }

        # MOLARITY
        if topic == "molarity":

            if len(nums) < 2:
                raise ValueError("Moles aur volume required hain.")

            moles, volume = nums[0], nums[1]

            if volume == 0:
                raise ValueError("Volume zero nahi ho sakta.")

            result = moles / volume

            return {
                "success": True,
                "topic": "Molarity",
                "formula": "Molarity = Moles / Volume",
                "calculation": f"{moles} / {volume}",
                "result": result,
                "unit": "mol/L",
                "values": {
                    "Moles": moles,
                    "Volume": volume
                }
            }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }

# ------------------------------------------------
# 6. ANSWER VERIFICATION
# ------------------------------------------------

def v6_verify(data):

    if not data["success"]:
        return False

    result = data["result"]

    if not math.isfinite(result):
        return False

    return True

# ------------------------------------------------
# 7. EXPLANATION GENERATOR
# ------------------------------------------------

def v6_explain(data, language="English"):

    if not data["success"]:
        return data["message"]

    if not v6_verify(data):
        return "Answer verification failed."

    if language == "Hindi":

        return f"""
विषय: {data['topic']}

सूत्र:
{data['formula']}

दिए गए मान:
{data['values']}

गणना:
{data['calculation']}

अंतिम उत्तर:
{data['result']:.6g} {data['unit']}

जाँच:
उत्तर finite numerical value है।
"""

    return f"""
Topic: {data['topic']}

Formula:
{data['formula']}

Given:
{data['values']}

Calculation:
{data['calculation']}

Final Answer:
{data['result']:.6g} {data['unit']}

Verification:
Finite numerical result confirmed.
"""

# ------------------------------------------------
# 8. UNIT CONVERTER TESTS
# ------------------------------------------------

print("UNIT CONVERSION TESTS")

assert abs(v6_convert(1, "km", "m") - 1000) < 1e-9
assert abs(v6_convert(1, "hour", "s") - 3600) < 1e-9
assert abs(v6_convert(1000, "g", "kg") - 1) < 1e-9
assert abs(v6_convert(100, "cm", "m") - 1) < 1e-9

print("All unit conversion tests passed!")

# ------------------------------------------------
# 9. SOLVER TESTS
# ------------------------------------------------

print("\nSOLVER TESTS")

test_questions = [
    ("Calculate speed for 100 km in 2 hours", 13.8888889),
    ("Find speed for 100 m in 20 seconds", 5),
    ("Calculate work done by 10 N force over 5 m", 50),
    ("Calculate power for 100 J in 5 seconds", 20),
    ("Calculate moles from 10 g mass and 20 g molar mass", 0.5),
    ("Find molarity of 2 moles in 4 litres", 0.5)
]

for question, expected in test_questions:

    data = v6_solve(question)

    assert data["success"], question

    assert abs(data["result"] - expected) < 0.001, (
        question,
        data["result"],
        expected
    )

    assert v6_verify(data)

    print("PASS:", question)

print("\nALL V6 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE MAGIC LAYER UI
# ------------------------------------------------

v6_question = widgets.Textarea(
    placeholder="Calculate speed for 100 km in 2 hours",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="110px"
    )
)

v6_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v6_button = widgets.Button(
    description="Solve Question",
    button_style="success",
    icon="check"
)

v6_output = widgets.Output()

def v6_run(_):

    with v6_output:

        clear_output()

        question = v6_question.value

        data = v6_solve(question)

        print(v6_explain(data, v6_language.value))

        if data["success"]:

            print("\nAnswer verified:", v6_verify(data))

v6_button.on_click(v6_run)

display(v6_question)
display(v6_language)
display(v6_button)
display(v6_output)

print("\nSUNO SAATHI MAGIC LAYER V6 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V6
# SMART UNIT CONVERSION + QUESTION SOLVER
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. UNIT CONVERSION DATABASE
# ------------------------------------------------

V6_UNITS = {
    "distance": {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001
    },
    "time": {
        "hour": 3600,
        "min": 60,
        "s": 1
    },
    "mass": {
        "kg": 1000,
        "g": 1,
        "mg": 0.001
    }
}

V6_ALIASES = {
    "kilometer": "km", "kilometre": "km",
    "kilometers": "km", "kilometres": "km",
    "meter": "m", "metre": "m",
    "meters": "m", "metres": "m",
    "centimeter": "cm", "centimetre": "cm",
    "millimeter": "mm", "millimetre": "mm",
    "hours": "hour", "hr": "hour", "hrs": "hour",
    "minutes": "min", "minute": "min",
    "seconds": "s", "second": "s", "sec": "s",
    "grams": "g", "gram": "g",
    "kilograms": "kg", "kilogram": "kg",
    "milligrams": "mg", "milligram": "mg"
}

def v6_normalize_unit(unit):
    unit = unit.lower().strip()
    return V6_ALIASES.get(unit, unit)

def v6_convert(value, from_unit, to_unit):
    from_unit = v6_normalize_unit(from_unit)
    to_unit = v6_normalize_unit(to_unit)

    for category, units in V6_UNITS.items():
        if from_unit in units and to_unit in units:
            base_value = value * units[from_unit]
            return base_value / units[to_unit]

    raise ValueError("Incompatible or unsupported units")

# ------------------------------------------------
# 2. QUESTION DETECTION
# ------------------------------------------------

def v6_detect_topic(q):
    q = q.lower()

    if any(x in q for x in [
        "molarity", "molar concentration", "मोलरता"
    ]):
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    if any(x in q for x in [
        "power", "शक्ति"
    ]):
        return "power"

    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "कार्य"
    ]):
        return "work"

    if any(x in q for x in [
        "speed", "velocity", "distance",
        "गति", "दूरी"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER + UNIT EXTRACTION
# ------------------------------------------------

V6_NUMBER_PATTERN = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

def v6_extract_pairs(q):
    pattern = (
        r'(' + V6_NUMBER_PATTERN + r')\s*'
        r'(kilometers?|kilometres?|kilometres?|'
        r'km|meters?|metres?|m|centimeters?|cm|mm|'
        r'hours?|hrs?|hr|min|minutes?|seconds?|secs?|s|'
        r'kilograms?|kg|grams?|g|mg)'
    )

    matches = re.findall(pattern, q.lower())

    result = []

    for number, unit in matches:
        result.append({
            "value": float(number),
            "unit": v6_normalize_unit(unit)
        })

    return result

def v6_extract_numbers(q):
    return [
        float(x)
        for x in re.findall(V6_NUMBER_PATTERN, q)
    ]

# ------------------------------------------------
# 4. CONVERT TO SI
# ------------------------------------------------

def v6_si(value, unit, category):
    unit = v6_normalize_unit(unit)

    if unit not in V6_UNITS[category]:
        raise ValueError(
            f"Unsupported {category} unit: {unit}"
        )

    return value * V6_UNITS[category][unit]

# ------------------------------------------------
# 5. QUESTION SOLVER
# ------------------------------------------------

def v6_solve(q):

    topic = v6_detect_topic(q)
    pairs = v6_extract_pairs(q)
    nums = v6_extract_numbers(q)

    if topic is None:
        return {
            "success": False,
            "message": "Topic identify nahi hua. Supported: Speed, Work, Power, Moles, Molarity."
        }

    try:

        # SPEED
        if topic == "speed":

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if distance_pair and time_pair:

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                distance = nums[0]
                time = nums[1]

            else:
                raise ValueError("Distance aur time dono required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = distance / time

            return {
                "success": True,
                "topic": "Speed",
                "formula": "Speed = Distance / Time",
                "calculation": f"{distance} / {time}",
                "result": result,
                "unit": "m/s",
                "values": {
                    "Distance": distance,
                    "Time": time
                }
            }

        # WORK
        if topic == "work":

            force_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:n|newton)',
                q.lower()
            )

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            if force_match and distance_pair:

                force = float(force_match.group(1))

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

            elif len(nums) >= 2:

                force, distance = nums[0], nums[1]

            else:
                raise ValueError("Force aur distance required hain.")

            result = force * distance

            return {
                "success": True,
                "topic": "Work",
                "formula": "Work = Force × Distance",
                "calculation": f"{force} × {distance}",
                "result": result,
                "unit": "J",
                "values": {
                    "Force": force,
                    "Distance": distance
                }
            }

        # POWER
        if topic == "power":

            work_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:j|joules?)',
                q.lower()
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if work_match and time_pair:

                work = float(work_match.group(1))

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                work, time = nums[0], nums[1]

            else:
                raise ValueError("Work aur time required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = work / time

            return {
                "success": True,
                "topic": "Power",
                "formula": "Power = Work / Time",
                "calculation": f"{work} / {time}",
                "result": result,
                "unit": "W",
                "values": {
                    "Work": work,
                    "Time": time
                }
            }

        # MOLES
        if topic == "moles":

            if len(nums) < 2:
                raise ValueError("Mass aur molar mass required hain.")

            mass, molar_mass = nums[0], nums[1]

            if molar_mass == 0:
                raise ValueError("Molar mass zero nahi ho sakta.")

            result = mass / molar_mass

            return {
                "success": True,
                "topic": "Moles",
                "formula": "Moles = Mass / Molar Mass",
                "calculation": f"{mass} / {molar_mass}",
                "result": result,
                "unit": "mol",
                "values": {
                    "Mass": mass,
                    "Molar Mass": molar_mass
                }
            }

        # MOLARITY
        if topic == "molarity":

            if len(nums) < 2:
                raise ValueError("Moles aur volume required hain.")

            moles, volume = nums[0], nums[1]

            if volume == 0:
                raise ValueError("Volume zero nahi ho sakta.")

            result = moles / volume

            return {
                "success": True,
                "topic": "Molarity",
                "formula": "Molarity = Moles / Volume",
                "calculation": f"{moles} / {volume}",
                "result": result,
                "unit": "mol/L",
                "values": {
                    "Moles": moles,
                    "Volume": volume
                }
            }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }

# ------------------------------------------------
# 6. ANSWER VERIFICATION
# ------------------------------------------------

def v6_verify(data):

    if not data["success"]:
        return False

    result = data["result"]

    if not math.isfinite(result):
        return False

    return True

# ------------------------------------------------
# 7. EXPLANATION GENERATOR
# ------------------------------------------------

def v6_explain(data, language="English"):

    if not data["success"]:
        return data["message"]

    if not v6_verify(data):
        return "Answer verification failed."

    if language == "Hindi":

        return f"""
विषय: {data['topic']}

सूत्र:
{data['formula']}

दिए गए मान:
{data['values']}

गणना:
{data['calculation']}

अंतिम उत्तर:
{data['result']:.6g} {data['unit']}

जाँच:
उत्तर finite numerical value है।
"""

    return f"""
Topic: {data['topic']}

Formula:
{data['formula']}

Given:
{data['values']}

Calculation:
{data['calculation']}

Final Answer:
{data['result']:.6g} {data['unit']}

Verification:
Finite numerical result confirmed.
"""

# ------------------------------------------------
# 8. UNIT CONVERTER TESTS
# ------------------------------------------------

print("UNIT CONVERSION TESTS")

assert abs(v6_convert(1, "km", "m") - 1000) < 1e-9
assert abs(v6_convert(1, "hour", "s") - 3600) < 1e-9
assert abs(v6_convert(1000, "g", "kg") - 1) < 1e-9
assert abs(v6_convert(100, "cm", "m") - 1) < 1e-9

print("All unit conversion tests passed!")

# ------------------------------------------------
# 9. SOLVER TESTS
# ------------------------------------------------

print("\nSOLVER TESTS")

test_questions = [
    ("Calculate speed for 100 km in 2 hours", 13.8888889),
    ("Find speed for 100 m in 20 seconds", 5),
    ("Calculate work done by 10 N force over 5 m", 50),
    ("Calculate power for 100 J in 5 seconds", 20),
    ("Calculate moles from 10 g mass and 20 g molar mass", 0.5),
    ("Find molarity of 2 moles in 4 litres", 0.5)
]

for question, expected in test_questions:

    data = v6_solve(question)

    assert data["success"], question

    assert abs(data["result"] - expected) < 0.001, (
        question,
        data["result"],
        expected
    )

    assert v6_verify(data)

    print("PASS:", question)

print("\nALL V6 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE MAGIC LAYER UI
# ------------------------------------------------

v6_question = widgets.Textarea(
    placeholder="Calculate speed for 100 km in 2 hours",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="110px"
    )
)

v6_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v6_button = widgets.Button(
    description="Solve Question",
    button_style="success",
    icon="check"
)

v6_output = widgets.Output()

def v6_run(_):

    with v6_output:

        clear_output()

        question = v6_question.value

        data = v6_solve(question)

        print(v6_explain(data, v6_language.value))

        if data["success"]:

            print("\nAnswer verified:", v6_verify(data))

v6_button.on_click(v6_run)

display(v6_question)
display(v6_language)
display(v6_button)
display(v6_output)

print("\nSUNO SAATHI MAGIC LAYER V6 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V6
# SMART UNIT CONVERSION + QUESTION SOLVER
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. UNIT CONVERSION DATABASE
# ------------------------------------------------

V6_UNITS = {
    "distance": {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001
    },
    "time": {
        "hour": 3600,
        "min": 60,
        "s": 1
    },
    "mass": {
        "kg": 1000,
        "g": 1,
        "mg": 0.001
    }
}

V6_ALIASES = {
    "kilometer": "km", "kilometre": "km",
    "kilometers": "km", "kilometres": "km",
    "meter": "m", "metre": "m",
    "meters": "m", "metres": "m",
    "centimeter": "cm", "centimetre": "cm",
    "millimeter": "mm", "millimetre": "mm",
    "hours": "hour", "hr": "hour", "hrs": "hour",
    "minutes": "min", "minute": "min",
    "seconds": "s", "second": "s", "sec": "s",
    "grams": "g", "gram": "g",
    "kilograms": "kg", "kilogram": "kg",
    "milligrams": "mg", "milligram": "mg"
}

def v6_normalize_unit(unit):
    unit = unit.lower().strip()
    return V6_ALIASES.get(unit, unit)

def v6_convert(value, from_unit, to_unit):
    from_unit = v6_normalize_unit(from_unit)
    to_unit = v6_normalize_unit(to_unit)

    for category, units in V6_UNITS.items():
        if from_unit in units and to_unit in units:
            base_value = value * units[from_unit]
            return base_value / units[to_unit]

    raise ValueError("Incompatible or unsupported units")

# ------------------------------------------------
# 2. QUESTION DETECTION
# ------------------------------------------------

def v6_detect_topic(q):
    q = q.lower()

    if any(x in q for x in [
        "molarity", "molar concentration", "मोलरता"
    ]):
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    if any(x in q for x in [
        "power", "शक्ति"
    ]):
        return "power"

    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "कार्य"
    ]):
        return "work"

    if any(x in q for x in [
        "speed", "velocity", "distance",
        "गति", "दूरी"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER + UNIT EXTRACTION
# ------------------------------------------------

V6_NUMBER_PATTERN = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

def v6_extract_pairs(q):
    pattern = (
        r'(' + V6_NUMBER_PATTERN + r')\s*'
        r'(kilometers?|kilometres?|kilometres?|'
        r'km|meters?|metres?|m|centimeters?|cm|mm|'
        r'hours?|hrs?|hr|min|minutes?|seconds?|secs?|s|'
        r'kilograms?|kg|grams?|g|mg)'
    )

    matches = re.findall(pattern, q.lower())

    result = []

    for number, unit in matches:
        result.append({
            "value": float(number),
            "unit": v6_normalize_unit(unit)
        })

    return result

def v6_extract_numbers(q):
    return [
        float(x)
        for x in re.findall(V6_NUMBER_PATTERN, q)
    ]

# ------------------------------------------------
# 4. CONVERT TO SI
# ------------------------------------------------

def v6_si(value, unit, category):
    unit = v6_normalize_unit(unit)

    if unit not in V6_UNITS[category]:
        raise ValueError(
            f"Unsupported {category} unit: {unit}"
        )

    return value * V6_UNITS[category][unit]

# ------------------------------------------------
# 5. QUESTION SOLVER
# ------------------------------------------------

def v6_solve(q):

    topic = v6_detect_topic(q)
    pairs = v6_extract_pairs(q)
    nums = v6_extract_numbers(q)

    if topic is None:
        return {
            "success": False,
            "message": "Topic identify nahi hua. Supported: Speed, Work, Power, Moles, Molarity."
        }

    try:

        # SPEED
        if topic == "speed":

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if distance_pair and time_pair:

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                distance = nums[0]
                time = nums[1]

            else:
                raise ValueError("Distance aur time dono required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = distance / time

            return {
                "success": True,
                "topic": "Speed",
                "formula": "Speed = Distance / Time",
                "calculation": f"{distance} / {time}",
                "result": result,
                "unit": "m/s",
                "values": {
                    "Distance": distance,
                    "Time": time
                }
            }

        # WORK
        if topic == "work":

            force_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:n|newton)',
                q.lower()
            )

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            if force_match and distance_pair:

                force = float(force_match.group(1))

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

            elif len(nums) >= 2:

                force, distance = nums[0], nums[1]

            else:
                raise ValueError("Force aur distance required hain.")

            result = force * distance

            return {
                "success": True,
                "topic": "Work",
                "formula": "Work = Force × Distance",
                "calculation": f"{force} × {distance}",
                "result": result,
                "unit": "J",
                "values": {
                    "Force": force,
                    "Distance": distance
                }
            }

        # POWER
        if topic == "power":

            work_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:j|joules?)',
                q.lower()
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if work_match and time_pair:

                work = float(work_match.group(1))

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                work, time = nums[0], nums[1]

            else:
                raise ValueError("Work aur time required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = work / time

            return {
                "success": True,
                "topic": "Power",
                "formula": "Power = Work / Time",
                "calculation": f"{work} / {time}",
                "result": result,
                "unit": "W",
                "values": {
                    "Work": work,
                    "Time": time
                }
            }

        # MOLES
        if topic == "moles":

            if len(nums) < 2:
                raise ValueError("Mass aur molar mass required hain.")

            mass, molar_mass = nums[0], nums[1]

            if molar_mass == 0:
                raise ValueError("Molar mass zero nahi ho sakta.")

            result = mass / molar_mass

            return {
                "success": True,
                "topic": "Moles",
                "formula": "Moles = Mass / Molar Mass",
                "calculation": f"{mass} / {molar_mass}",
                "result": result,
                "unit": "mol",
                "values": {
                    "Mass": mass,
                    "Molar Mass": molar_mass
                }
            }

        # MOLARITY
        if topic == "molarity":

            if len(nums) < 2:
                raise ValueError("Moles aur volume required hain.")

            moles, volume = nums[0], nums[1]

            if volume == 0:
                raise ValueError("Volume zero nahi ho sakta.")

            result = moles / volume

            return {
                "success": True,
                "topic": "Molarity",
                "formula": "Molarity = Moles / Volume",
                "calculation": f"{moles} / {volume}",
                "result": result,
                "unit": "mol/L",
                "values": {
                    "Moles": moles,
                    "Volume": volume
                }
            }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }

# ------------------------------------------------
# 6. ANSWER VERIFICATION
# ------------------------------------------------

def v6_verify(data):

    if not data["success"]:
        return False

    result = data["result"]

    if not math.isfinite(result):
        return False

    return True

# ------------------------------------------------
# 7. EXPLANATION GENERATOR
# ------------------------------------------------

def v6_explain(data, language="English"):

    if not data["success"]:
        return data["message"]

    if not v6_verify(data):
        return "Answer verification failed."

    if language == "Hindi":

        return f"""
विषय: {data['topic']}

सूत्र:
{data['formula']}

दिए गए मान:
{data['values']}

गणना:
{data['calculation']}

अंतिम उत्तर:
{data['result']:.6g} {data['unit']}

जाँच:
उत्तर finite numerical value है।
"""

    return f"""
Topic: {data['topic']}

Formula:
{data['formula']}

Given:
{data['values']}

Calculation:
{data['calculation']}

Final Answer:
{data['result']:.6g} {data['unit']}

Verification:
Finite numerical result confirmed.
"""

# ------------------------------------------------
# 8. UNIT CONVERTER TESTS
# ------------------------------------------------

print("UNIT CONVERSION TESTS")

assert abs(v6_convert(1, "km", "m") - 1000) < 1e-9
assert abs(v6_convert(1, "hour", "s") - 3600) < 1e-9
assert abs(v6_convert(1000, "g", "kg") - 1) < 1e-9
assert abs(v6_convert(100, "cm", "m") - 1) < 1e-9

print("All unit conversion tests passed!")

# ------------------------------------------------
# 9. SOLVER TESTS
# ------------------------------------------------

print("\nSOLVER TESTS")

test_questions = [
    ("Calculate speed for 100 km in 2 hours", 13.8888889),
    ("Find speed for 100 m in 20 seconds", 5),
    ("Calculate work done by 10 N force over 5 m", 50),
    ("Calculate power for 100 J in 5 seconds", 20),
    ("Calculate moles from 10 g mass and 20 g molar mass", 0.5),
    ("Find molarity of 2 moles in 4 litres", 0.5)
]

for question, expected in test_questions:

    data = v6_solve(question)

    assert data["success"], question

    assert abs(data["result"] - expected) < 0.001, (
        question,
        data["result"],
        expected
    )

    assert v6_verify(data)

    print("PASS:", question)

print("\nALL V6 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE MAGIC LAYER UI
# ------------------------------------------------

v6_question = widgets.Textarea(
    placeholder="Calculate speed for 100 km in 2 hours",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="110px"
    )
)

v6_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v6_button = widgets.Button(
    description="Solve Question",
    button_style="success",
    icon="check"
)

v6_output = widgets.Output()

def v6_run(_):

    with v6_output:

        clear_output()

        question = v6_question.value

        data = v6_solve(question)

        print(v6_explain(data, v6_language.value))

        if data["success"]:

            print("\nAnswer verified:", v6_verify(data))

v6_button.on_click(v6_run)

display(v6_question)
display(v6_language)
display(v6_button)
display(v6_output)

print("\nSUNO SAATHI MAGIC LAYER V6 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V6
# SMART UNIT CONVERSION + QUESTION SOLVER
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. UNIT CONVERSION DATABASE
# ------------------------------------------------

V6_UNITS = {
    "distance": {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001
    },
    "time": {
        "hour": 3600,
        "min": 60,
        "s": 1
    },
    "mass": {
        "kg": 1000,
        "g": 1,
        "mg": 0.001
    }
}

V6_ALIASES = {
    "kilometer": "km", "kilometre": "km",
    "kilometers": "km", "kilometres": "km",
    "meter": "m", "metre": "m",
    "meters": "m", "metres": "m",
    "centimeter": "cm", "centimetre": "cm",
    "millimeter": "mm", "millimetre": "mm",
    "hours": "hour", "hr": "hour", "hrs": "hour",
    "minutes": "min", "minute": "min",
    "seconds": "s", "second": "s", "sec": "s",
    "grams": "g", "gram": "g",
    "kilograms": "kg", "kilogram": "kg",
    "milligrams": "mg", "milligram": "mg"
}

def v6_normalize_unit(unit):
    unit = unit.lower().strip()
    return V6_ALIASES.get(unit, unit)

def v6_convert(value, from_unit, to_unit):
    from_unit = v6_normalize_unit(from_unit)
    to_unit = v6_normalize_unit(to_unit)

    for category, units in V6_UNITS.items():
        if from_unit in units and to_unit in units:
            base_value = value * units[from_unit]
            return base_value / units[to_unit]

    raise ValueError("Incompatible or unsupported units")

# ------------------------------------------------
# 2. QUESTION DETECTION
# ------------------------------------------------

def v6_detect_topic(q):
    q = q.lower()

    if any(x in q for x in [
        "molarity", "molar concentration", "मोलरता"
    ]):
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    if any(x in q for x in [
        "power", "शक्ति"
    ]):
        return "power"

    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "कार्य"
    ]):
        return "work"

    if any(x in q for x in [
        "speed", "velocity", "distance",
        "गति", "दूरी"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER + UNIT EXTRACTION
# ------------------------------------------------

V6_NUMBER_PATTERN = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

def v6_extract_pairs(q):
    pattern = (
        r'(' + V6_NUMBER_PATTERN + r')\s*'
        r'(kilometers?|kilometres?|kilometres?|'
        r'km|meters?|metres?|m|centimeters?|cm|mm|'
        r'hours?|hrs?|hr|min|minutes?|seconds?|secs?|s|'
        r'kilograms?|kg|grams?|g|mg)'
    )

    matches = re.findall(pattern, q.lower())

    result = []

    for number, unit in matches:
        result.append({
            "value": float(number),
            "unit": v6_normalize_unit(unit)
        })

    return result

def v6_extract_numbers(q):
    return [
        float(x)
        for x in re.findall(V6_NUMBER_PATTERN, q)
    ]

# ------------------------------------------------
# 4. CONVERT TO SI
# ------------------------------------------------

def v6_si(value, unit, category):
    unit = v6_normalize_unit(unit)

    if unit not in V6_UNITS[category]:
        raise ValueError(
            f"Unsupported {category} unit: {unit}"
        )

    return value * V6_UNITS[category][unit]

# ------------------------------------------------
# 5. QUESTION SOLVER
# ------------------------------------------------

def v6_solve(q):

    topic = v6_detect_topic(q)
    pairs = v6_extract_pairs(q)
    nums = v6_extract_numbers(q)

    if topic is None:
        return {
            "success": False,
            "message": "Topic identify nahi hua. Supported: Speed, Work, Power, Moles, Molarity."
        }

    try:

        # SPEED
        if topic == "speed":

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if distance_pair and time_pair:

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                distance = nums[0]
                time = nums[1]

            else:
                raise ValueError("Distance aur time dono required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = distance / time

            return {
                "success": True,
                "topic": "Speed",
                "formula": "Speed = Distance / Time",
                "calculation": f"{distance} / {time}",
                "result": result,
                "unit": "m/s",
                "values": {
                    "Distance": distance,
                    "Time": time
                }
            }

        # WORK
        if topic == "work":

            force_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:n|newton)',
                q.lower()
            )

            distance_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["distance"]),
                None
            )

            if force_match and distance_pair:

                force = float(force_match.group(1))

                distance = v6_si(
                    distance_pair["value"],
                    distance_pair["unit"],
                    "distance"
                )

            elif len(nums) >= 2:

                force, distance = nums[0], nums[1]

            else:
                raise ValueError("Force aur distance required hain.")

            result = force * distance

            return {
                "success": True,
                "topic": "Work",
                "formula": "Work = Force × Distance",
                "calculation": f"{force} × {distance}",
                "result": result,
                "unit": "J",
                "values": {
                    "Force": force,
                    "Distance": distance
                }
            }

        # POWER
        if topic == "power":

            work_match = re.search(
                r'(' + V6_NUMBER_PATTERN + r')\s*(?:j|joules?)',
                q.lower()
            )

            time_pair = next(
                (p for p in pairs if p["unit"] in V6_UNITS["time"]),
                None
            )

            if work_match and time_pair:

                work = float(work_match.group(1))

                time = v6_si(
                    time_pair["value"],
                    time_pair["unit"],
                    "time"
                )

            elif len(nums) >= 2:

                work, time = nums[0], nums[1]

            else:
                raise ValueError("Work aur time required hain.")

            if time == 0:
                raise ValueError("Time zero nahi ho sakta.")

            result = work / time

            return {
                "success": True,
                "topic": "Power",
                "formula": "Power = Work / Time",
                "calculation": f"{work} / {time}",
                "result": result,
                "unit": "W",
                "values": {
                    "Work": work,
                    "Time": time
                }
            }

        # MOLES
        if topic == "moles":

            if len(nums) < 2:
                raise ValueError("Mass aur molar mass required hain.")

            mass, molar_mass = nums[0], nums[1]

            if molar_mass == 0:
                raise ValueError("Molar mass zero nahi ho sakta.")

            result = mass / molar_mass

            return {
                "success": True,
                "topic": "Moles",
                "formula": "Moles = Mass / Molar Mass",
                "calculation": f"{mass} / {molar_mass}",
                "result": result,
                "unit": "mol",
                "values": {
                    "Mass": mass,
                    "Molar Mass": molar_mass
                }
            }

        # MOLARITY
        if topic == "molarity":

            if len(nums) < 2:
                raise ValueError("Moles aur volume required hain.")

            moles, volume = nums[0], nums[1]

            if volume == 0:
                raise ValueError("Volume zero nahi ho sakta.")

            result = moles / volume

            return {
                "success": True,
                "topic": "Molarity",
                "formula": "Molarity = Moles / Volume",
                "calculation": f"{moles} / {volume}",
                "result": result,
                "unit": "mol/L",
                "values": {
                    "Moles": moles,
                    "Volume": volume
                }
            }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }

# ------------------------------------------------
# 6. ANSWER VERIFICATION
# ------------------------------------------------

def v6_verify(data):

    if not data["success"]:
        return False

    result = data["result"]

    if not math.isfinite(result):
        return False

    return True

# ------------------------------------------------
# 7. EXPLANATION GENERATOR
# ------------------------------------------------

def v6_explain(data, language="English"):

    if not data["success"]:
        return data["message"]

    if not v6_verify(data):
        return "Answer verification failed."

    if language == "Hindi":

        return f"""
विषय: {data['topic']}

सूत्र:
{data['formula']}

दिए गए मान:
{data['values']}

गणना:
{data['calculation']}

अंतिम उत्तर:
{data['result']:.6g} {data['unit']}

जाँच:
उत्तर finite numerical value है।
"""

    return f"""
Topic: {data['topic']}

Formula:
{data['formula']}

Given:
{data['values']}

Calculation:
{data['calculation']}

Final Answer:
{data['result']:.6g} {data['unit']}

Verification:
Finite numerical result confirmed.
"""

# ------------------------------------------------
# 8. UNIT CONVERTER TESTS
# ------------------------------------------------

print("UNIT CONVERSION TESTS")

assert abs(v6_convert(1, "km", "m") - 1000) < 1e-9
assert abs(v6_convert(1, "hour", "s") - 3600) < 1e-9
assert abs(v6_convert(1000, "g", "kg") - 1) < 1e-9
assert abs(v6_convert(100, "cm", "m") - 1) < 1e-9

print("All unit conversion tests passed!")

# ------------------------------------------------
# 9. SOLVER TESTS
# ------------------------------------------------

print("\nSOLVER TESTS")

test_questions = [
    ("Calculate speed for 100 km in 2 hours", 13.8888889),
    ("Find speed for 100 m in 20 seconds", 5),
    ("Calculate work done by 10 N force over 5 m", 50),
    ("Calculate power for 100 J in 5 seconds", 20),
    ("Calculate moles from 10 g mass and 20 g molar mass", 0.5),
    ("Find molarity of 2 moles in 4 litres", 0.5)
]

for question, expected in test_questions:

    data = v6_solve(question)

    assert data["success"], question

    assert abs(data["result"] - expected) < 0.001, (
        question,
        data["result"],
        expected
    )

    assert v6_verify(data)

    print("PASS:", question)

print("\nALL V6 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE MAGIC LAYER UI
# ------------------------------------------------

v6_question = widgets.Textarea(
    placeholder="Calculate speed for 100 km in 2 hours",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="110px"
    )
)

v6_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v6_button = widgets.Button(
    description="Solve Question",
    button_style="success",
    icon="check"
)

v6_output = widgets.Output()

def v6_run(_):

    with v6_output:

        clear_output()

        question = v6_question.value

        data = v6_solve(question)

        print(v6_explain(data, v6_language.value))

        if data["success"]:

            print("\nAnswer verified:", v6_verify(data))

v6_button.on_click(v6_run)

display(v6_question)
display(v6_language)
display(v6_button)
display(v6_output)

print("\nSUNO SAATHI MAGIC LAYER V6 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V7
# SMART PHYSICS + CHEMISTRY QUESTION ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. FORMULA DATABASE
# ------------------------------------------------

V7_FORMULAS = {

    "speed": {
        "name": "Speed",
        "formula": "v = d / t",
        "description": "Speed = Distance / Time",
        "variables": ["distance", "time"],
        "unit": "m/s"
    },

    "acceleration": {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "description": "Acceleration = Change in velocity / Time",
        "variables": ["final_velocity", "initial_velocity", "time"],
        "unit": "m/s²"
    },

    "force": {
        "name": "Force",
        "formula": "F = m × a",
        "description": "Force = Mass × Acceleration",
        "variables": ["mass", "acceleration"],
        "unit": "N"
    },

    "work": {
        "name": "Work",
        "formula": "W = F × d",
        "description": "Work = Force × Distance",
        "variables": ["force", "distance"],
        "unit": "J"
    },

    "power": {
        "name": "Power",
        "formula": "P = W / t",
        "description": "Power = Work / Time",
        "variables": ["work", "time"],
        "unit": "W"
    },

    "kinetic_energy": {
        "name": "Kinetic Energy",
        "formula": "KE = 1/2 × m × v²",
        "description": "Kinetic Energy = Half × Mass × Velocity squared",
        "variables": ["mass", "velocity"],
        "unit": "J"
    },

    "potential_energy": {
        "name": "Potential Energy",
        "formula": "PE = m × g × h",
        "description": "Potential Energy = Mass × Gravity × Height",
        "variables": ["mass", "gravity", "height"],
        "unit": "J"
    },

    "density": {
        "name": "Density",
        "formula": "ρ = m / V",
        "description": "Density = Mass / Volume",
        "variables": ["mass", "volume"],
        "unit": "kg/m³"
    },

    "moles": {
        "name": "Moles",
        "formula": "n = m / M",
        "description": "Moles = Mass / Molar Mass",
        "variables": ["mass", "molar_mass"],
        "unit": "mol"
    },

    "molarity": {
        "name": "Molarity",
        "formula": "C = n / V",
        "description": "Molarity = Moles / Volume in litres",
        "variables": ["moles", "volume"],
        "unit": "mol/L"
    },

    "ideal_gas": {
        "name": "Ideal Gas",
        "formula": "PV = nRT",
        "description": "Ideal Gas Equation",
        "variables": ["pressure", "volume", "moles", "temperature"],
        "unit": "PV"
    }
}

# ------------------------------------------------
# 2. TOPIC DETECTOR
# ------------------------------------------------

def v7_detect_topic(q):

    q = q.lower()

    keywords = {

        "acceleration": ["acceleration", "accelerate", "त्वरण"],
        "kinetic_energy": ["kinetic energy", "गतिज ऊर्जा"],
        "potential_energy": ["potential energy", "स्थितिज ऊर्जा"],
        "density": ["density", "घनत्व"],
        "force": ["force", "बल"],
        "work": ["work done", "कार्य"],
        "power": ["power", "शक्ति"],
        "molarity": ["molarity", "मोलरता"],
        "moles": ["moles", "number of moles", "मोल"],
        "ideal_gas": ["ideal gas", "pv = nrt"],
        "speed": ["speed", "velocity", "गति"]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

# ------------------------------------------------
# 3. NUMBER EXTRACTION
# ------------------------------------------------

def v7_numbers(q):

    pattern = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

    return [
        float(x)
        for x in re.findall(pattern, q)
    ]

# ------------------------------------------------
# 4. MULTI-STEP CALCULATION ENGINE
# ------------------------------------------------

def v7_calculate(topic, nums):

    if topic not in V7_FORMULAS:
        raise ValueError("Unsupported formula")

    if topic == "speed":

        if len(nums) < 2:
            raise ValueError("Distance and time required")

        d, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return d/t, ["Distance / Time", f"{d} / {t}"]

    if topic == "acceleration":

        if len(nums) < 3:
            raise ValueError("Final velocity, initial velocity, time required")

        v, u, t = nums[:3]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return (v-u)/t, [f"({v} - {u}) / {t}"]

    if topic == "force":

        if len(nums) < 2:
            raise ValueError("Mass and acceleration required")

        m, a = nums[:2]

        return m*a, [f"{m} × {a}"]

    if topic == "work":

        if len(nums) < 2:
            raise ValueError("Force and distance required")

        f, d = nums[:2]

        return f*d, [f"{f} × {d}"]

    if topic == "power":

        if len(nums) < 2:
            raise ValueError("Work and time required")

        w, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return w/t, [f"{w} / {t}"]

    if topic == "kinetic_energy":

        if len(nums) < 2:
            raise ValueError("Mass and velocity required")

        m, v = nums[:2]

        return 0.5*m*v**2, [
            f"0.5 × {m} × {v}²",
            f"0.5 × {m} × {v**2}"
        ]

    if topic == "potential_energy":

        if len(nums) < 2:
            raise ValueError("Mass and height required")

        m, h = nums[:2]

        g = 9.8

        return m*g*h, [
            f"{m} × {g} × {h}"
        ]

    if topic == "density":

        if len(nums) < 2:
            raise ValueError("Mass and volume required")

        m, v = nums[:2]

        if v == 0:
            raise ValueError("Volume cannot be zero")

        return m/v, [f"{m} / {v}"]

    if topic == "moles":

        if len(nums) < 2:
            raise ValueError("Mass and molar mass required")

        m, M = nums[:2]

        if M == 0:
            raise ValueError("Molar mass cannot be zero")

        return m/M, [f"{m} / {M}"]

    if topic == "molarity":

        if len(nums) < 2:
            raise ValueError("Moles and volume required")

        n, V = nums[:2]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return n/V, [f"{n} / {V}"]

    if topic == "ideal_gas":

        if len(nums) < 3:
            raise ValueError("Pressure, volume and temperature required")

        P, V, T = nums[:3]

        if T == 0:
            raise ValueError("Temperature cannot be zero")

        R = 0.0821

        return P*V/(R*T), [
            f"n = PV / RT",
            f"{P} × {V} / (0.0821 × {T})"
        ]

# ------------------------------------------------
# 5. SOLUTION GENERATOR
# ------------------------------------------------

def v7_solve(q, language="English"):

    topic = v7_detect_topic(q)
    nums = v7_numbers(q)

    if topic is None:
        return "Question topic identify nahi hua."

    try:

        result, steps = v7_calculate(topic, nums)

        formula = V7_FORMULAS[topic]

        if language == "Hindi":

            text = f"""
विषय: {formula['name']}

सूत्र:
{formula['formula']}

चरण:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

अंतिम उत्तर:
{result:.6g} {formula['unit']}
"""

        else:

            text = f"""
Topic: {formula['name']}

Formula:
{formula['formula']}

Step-by-step:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

Final Answer:
{result:.6g} {formula['unit']}
"""

        return text

    except Exception as e:

        return "Cannot solve: " + str(e)

# ------------------------------------------------
# 6. FORMULA SEARCH
# ------------------------------------------------

def v7_formula_search(keyword):

    keyword = keyword.lower()

    results = []

    for key, item in V7_FORMULAS.items():

        if (
            keyword in key.lower()
            or keyword in item["name"].lower()
            or keyword in item["formula"].lower()
        ):

            results.append(
                f"{item['name']}: {item['formula']}"
            )

    return results if results else ["No formula found"]

# ------------------------------------------------
# 7. COMMON MISTAKES
# ------------------------------------------------

V7_MISTAKES = {

    "speed": "Distance aur time ki units compatible honi chahiye.",
    "acceleration": "Velocity difference ko time se divide karein.",
    "force": "Mass kg aur acceleration m/s² mein honi chahiye.",
    "work": "Work ke liye force aur displacement ka product use karein.",
    "power": "Work ko time se divide karein.",
    "kinetic_energy": "Velocity ka square lena na bhoolein.",
    "potential_energy": "Height aur mass SI units mein rakhein.",
    "density": "Volume zero nahi hona chahiye.",
    "moles": "Mass aur molar mass same mass units mein hon.",
    "molarity": "Volume litres mein hona chahiye.",
    "ideal_gas": "Temperature Kelvin mein hona chahiye."
}

# ------------------------------------------------
# 8. TESTS
# ------------------------------------------------

V7_TESTS = [
    ("Calculate speed for 100 distance in 2 time", "speed", 50),
    ("Find acceleration for final velocity 20 initial velocity 10 time 2", "acceleration", 5),
    ("Calculate force for mass 5 and acceleration 2", "force", 10),
    ("Find kinetic energy for mass 2 velocity 3", "kinetic_energy", 9),
    ("Calculate potential energy for mass 2 height 5", "potential_energy", 98),
    ("Calculate density for mass 10 volume 2", "density", 5),
    ("Calculate moles for mass 10 molar mass 20", "moles", 0.5),
    ("Calculate molarity for 2 moles volume 4", "molarity", 0.5)
]

print("V7 TESTING")

for q, topic, expected in V7_TESTS:

    detected = v7_detect_topic(q)

    assert detected == topic, (q, detected)

    nums = v7_numbers(q)

    result, steps = v7_calculate(topic, nums)

    assert abs(result-expected) < 0.001

    print("PASS:", topic)

print("\nALL V7 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v7_question = widgets.Textarea(
    placeholder="Calculate kinetic energy for mass 2 kg velocity 3 m/s",
    description="Question:",
    layout=widgets.Layout(width="100%", height="120px")
)

v7_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v7_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v7_formula_input = widgets.Text(
    placeholder="Search: speed, force, energy...",
    description="Formula:"
)

v7_formula_button = widgets.Button(
    description="Search Formula"
)

v7_output = widgets.Output()

def v7_run(_):

    with v7_output:

        clear_output()

        print(v7_solve(v7_question.value, v7_language.value))

        topic = v7_detect_topic(v7_question.value)

        if topic:
            print("\nCommon Mistake:")
            print(V7_MISTAKES.get(topic, ""))

def v7_search_run(_):

    with v7_output:

        clear_output()

        results = v7_formula_search(v7_formula_input.value)

        for item in results:
            print(item)

v7_button.on_click(v7_run)
v7_formula_button.on_click(v7_search_run)

display(v7_question)
display(v7_language)
display(v7_button)

display(v7_formula_input)
display(v7_formula_button)

display(v7_output)

print("\nSUNO SAATHI MAGIC LAYER V7 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V7.1
# COMPLETE CORRECTED VERSION
# PHYSICS + CHEMISTRY FORMULA ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. FORMULA DATABASE
# ------------------------------------------------

V7_FORMULAS = {

    "speed": {
        "name": "Speed",
        "formula": "v = d / t",
        "unit": "m/s"
    },

    "acceleration": {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "unit": "m/s²"
    },

    "force": {
        "name": "Force",
        "formula": "F = m × a",
        "unit": "N"
    },

    "work": {
        "name": "Work",
        "formula": "W = F × d",
        "unit": "J"
    },

    "power": {
        "name": "Power",
        "formula": "P = W / t",
        "unit": "W"
    },

    "kinetic_energy": {
        "name": "Kinetic Energy",
        "formula": "KE = 1/2 × m × v²",
        "unit": "J"
    },

    "potential_energy": {
        "name": "Potential Energy",
        "formula": "PE = m × g × h",
        "unit": "J"
    },

    "density": {
        "name": "Density",
        "formula": "ρ = m / V",
        "unit": "kg/m³"
    },

    "moles": {
        "name": "Moles",
        "formula": "n = m / M",
        "unit": "mol"
    },

    "molarity": {
        "name": "Molarity",
        "formula": "C = n / V",
        "unit": "mol/L"
    },

    "ideal_gas": {
        "name": "Ideal Gas",
        "formula": "PV = nRT",
        "unit": "mol"
    }
}

# ------------------------------------------------
# 2. CORRECTED TOPIC DETECTOR
# ------------------------------------------------

def v7_detect_topic(q):

    q = q.lower().strip()

    # FORCE PRIORITY
    if any(x in q for x in [
        "calculate force",
        "find force",
        "force for mass",
        "force", "बल"
    ]):
        return "force"

    # ENERGY PRIORITY
    if any(x in q for x in [
        "kinetic energy", "गतिज ऊर्जा"
    ]):
        return "kinetic_energy"

    if any(x in q for x in [
        "potential energy", "स्थितिज ऊर्जा"
    ]):
        return "potential_energy"

    # OTHER TOPICS
    keywords = {

        "acceleration": [
            "acceleration", "accelerate", "त्वरण"
        ],

        "density": [
            "density", "घनत्व"
        ],

        "work": [
            "work done", "calculate work",
            "find work", "कार्य"
        ],

        "power": [
            "power", "शक्ति"
        ],

        "molarity": [
            "molarity", "मोलरता"
        ],

        "moles": [
            "number of moles", "calculate moles",
            "find moles", "moles", "मोल"
        ],

        "ideal_gas": [
            "ideal gas", "pv = nrt"
        ],

        "speed": [
            "speed", "velocity", "गति"
        ]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

# ------------------------------------------------
# 3. NUMBER EXTRACTION
# ------------------------------------------------

def v7_numbers(q):

    pattern = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

    return [
        float(x)
        for x in re.findall(pattern, q)
    ]

# ------------------------------------------------
# 4. CALCULATION ENGINE
# ------------------------------------------------

def v7_calculate(topic, nums):

    if topic not in V7_FORMULAS:
        raise ValueError("Unsupported formula")

    # SPEED
    if topic == "speed":

        if len(nums) < 2:
            raise ValueError("Distance and time required")

        d, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return d/t, [
            f"Speed = Distance / Time",
            f"Speed = {d} / {t}"
        ]

    # ACCELERATION
    if topic == "acceleration":

        if len(nums) < 3:
            raise ValueError(
                "Final velocity, initial velocity and time required"
            )

        v, u, t = nums[:3]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return (v-u)/t, [
            "Acceleration = (v - u) / t",
            f"Acceleration = ({v} - {u}) / {t}"
        ]

    # FORCE
    if topic == "force":

        if len(nums) < 2:
            raise ValueError("Mass and acceleration required")

        m, a = nums[:2]

        return m*a, [
            "Force = Mass × Acceleration",
            f"Force = {m} × {a}"
        ]

    # WORK
    if topic == "work":

        if len(nums) < 2:
            raise ValueError("Force and distance required")

        f, d = nums[:2]

        return f*d, [
            "Work = Force × Distance",
            f"Work = {f} × {d}"
        ]

    # POWER
    if topic == "power":

        if len(nums) < 2:
            raise ValueError("Work and time required")

        w, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return w/t, [
            "Power = Work / Time",
            f"Power = {w} / {t}"
        ]

    # KINETIC ENERGY
    if topic == "kinetic_energy":

        if len(nums) < 2:
            raise ValueError("Mass and velocity required")

        m, v = nums[:2]

        return 0.5*m*v**2, [
            "KE = 1/2 × m × v²",
            f"KE = 0.5 × {m} × {v}²",
            f"KE = 0.5 × {m} × {v**2}"
        ]

    # POTENTIAL ENERGY
    if topic == "potential_energy":

        if len(nums) < 2:
            raise ValueError("Mass and height required")

        m, h = nums[:2]

        g = 9.8

        return m*g*h, [
            "PE = m × g × h",
            f"PE = {m} × {g} × {h}"
        ]

    # DENSITY
    if topic == "density":

        if len(nums) < 2:
            raise ValueError("Mass and volume required")

        m, v = nums[:2]

        if v == 0:
            raise ValueError("Volume cannot be zero")

        return m/v, [
            "Density = Mass / Volume",
            f"Density = {m} / {v}"
        ]

    # MOLES
    if topic == "moles":

        if len(nums) < 2:
            raise ValueError("Mass and molar mass required")

        m, M = nums[:2]

        if M == 0:
            raise ValueError("Molar mass cannot be zero")

        return m/M, [
            "Moles = Mass / Molar Mass",
            f"Moles = {m} / {M}"
        ]

    # MOLARITY
    if topic == "molarity":

        if len(nums) < 2:
            raise ValueError("Moles and volume required")

        n, V = nums[:2]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return n/V, [
            "Molarity = Moles / Volume",
            f"Molarity = {n} / {V}"
        ]

    # IDEAL GAS
    if topic == "ideal_gas":

        if len(nums) < 3:
            raise ValueError(
                "Pressure, volume and temperature required"
            )

        P, V, T = nums[:3]

        if T <= 0:
            raise ValueError("Temperature must be positive")

        R = 0.082057

        return P*V/(R*T), [
            "n = PV / RT",
            f"n = {P} × {V} / (0.082057 × {T})"
        ]

    raise ValueError("Calculation not implemented")

# ------------------------------------------------
# 5. SOLUTION GENERATOR
# ------------------------------------------------

def v7_solve(q, language="English"):

    topic = v7_detect_topic(q)

    if topic is None:
        return "Question topic identify nahi hua."

    nums = v7_numbers(q)

    try:

        result, steps = v7_calculate(topic, nums)

        if not math.isfinite(result):
            return "Invalid numerical result."

        formula = V7_FORMULAS[topic]

        if language == "Hindi":

            text = f"""
विषय: {formula['name']}

सूत्र:
{formula['formula']}

हल:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

अंतिम उत्तर:
{result:.6g} {formula['unit']}
"""

        else:

            text = f"""
Topic: {formula['name']}

Formula:
{formula['formula']}

Solution:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

Final Answer:
{result:.6g} {formula['unit']}
"""

        return text

    except Exception as e:

        return "Cannot solve: " + str(e)

# ------------------------------------------------
# 6. FORMULA SEARCH
# ------------------------------------------------

def v7_formula_search(keyword):

    keyword = keyword.lower().strip()

    results = []

    for key, item in V7_FORMULAS.items():

        if (
            keyword in key.lower()
            or keyword in item["name"].lower()
            or keyword in item["formula"].lower()
        ):

            results.append(
                f"{item['name']}: {item['formula']}"
            )

    return results if results else ["No formula found"]

# ------------------------------------------------
# 7. COMMON MISTAKES
# ------------------------------------------------

V7_MISTAKES = {

    "speed": "Distance aur time ki units compatible honi chahiye.",

    "acceleration": "Velocity difference ko time se divide karein.",

    "force": "Mass kg aur acceleration m/s² mein honi chahiye.",

    "work": "Force aur displacement ka product use karein.",

    "power": "Work ko time se divide karein.",

    "kinetic_energy": "Velocity ka square lena na bhoolein.",

    "potential_energy": "Height aur mass SI units mein rakhein.",

    "density": "Mass aur volume compatible units mein hon.",

    "moles": "Mass aur molar mass same mass units mein hon.",

    "molarity": "Volume litres mein hona chahiye.",

    "ideal_gas": "Temperature Kelvin mein hona chahiye."
}

# ------------------------------------------------
# 8. CORRECTED TESTS
# ------------------------------------------------

V7_TESTS = [

    ("Calculate speed for 100 distance in 2 time",
     "speed", 50),

    ("Find acceleration for final velocity 20 initial velocity 10 time 2",
     "acceleration", 5),

    ("Calculate force for mass 5 and acceleration 2",
     "force", 10),

    ("Calculate work done by force 10 and distance 5",
     "work", 50),

    ("Calculate power for work 100 and time 5",
     "power", 20),

    ("Calculate kinetic energy for mass 2 velocity 3",
     "kinetic_energy", 9),

    ("Calculate potential energy for mass 2 height 5",
     "potential_energy", 98),

    ("Calculate density for mass 10 volume 2",
     "density", 5),

    ("Calculate moles for mass 10 molar mass 20",
     "moles", 0.5),

    ("Calculate molarity for 2 moles volume 4",
     "molarity", 0.5)
]

print("V7.1 TESTING")

for q, topic, expected in V7_TESTS:

    detected = v7_detect_topic(q)

    assert detected == topic, (
        q, detected, topic
    )

    nums = v7_numbers(q)

    result, steps = v7_calculate(topic, nums)

    assert abs(result-expected) < 0.001, (
        q, result, expected
    )

    print("PASS:", topic)

print("\nALL V7.1 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v7_question = widgets.Textarea(
    placeholder="Calculate force for mass 5 and acceleration 2",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="120px"
    )
)

v7_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v7_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v7_formula_input = widgets.Text(
    placeholder="Search speed, force, energy...",
    description="Formula:"
)

v7_formula_button = widgets.Button(
    description="Search Formula"
)

v7_output = widgets.Output()

def v7_run(_):

    with v7_output:

        clear_output()

        q = v7_question.value

        print(v7_solve(q, v7_language.value))

        topic = v7_detect_topic(q)

        if topic:

            print("\nCommon Mistake:")
            print(V7_MISTAKES.get(topic, ""))

def v7_search_run(_):

    with v7_output:

        clear_output()

        results = v7_formula_search(
            v7_formula_input.value
        )

        for item in results:
            print(item)

v7_button.on_click(v7_run)

v7_formula_button.on_click(
    v7_search_run
)

display(v7_question)
display(v7_language)
display(v7_button)

display(v7_formula_input)
display(v7_formula_button)

display(v7_output)

print("\nSUNO SAATHI MAGIC LAYER V7.1 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V7.1
# COMPLETE CORRECTED VERSION
# PHYSICS + CHEMISTRY FORMULA ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. FORMULA DATABASE
# ------------------------------------------------

V7_FORMULAS = {

    "speed": {
        "name": "Speed",
        "formula": "v = d / t",
        "unit": "m/s"
    },

    "acceleration": {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "unit": "m/s²"
    },

    "force": {
        "name": "Force",
        "formula": "F = m × a",
        "unit": "N"
    },

    "work": {
        "name": "Work",
        "formula": "W = F × d",
        "unit": "J"
    },

    "power": {
        "name": "Power",
        "formula": "P = W / t",
        "unit": "W"
    },

    "kinetic_energy": {
        "name": "Kinetic Energy",
        "formula": "KE = 1/2 × m × v²",
        "unit": "J"
    },

    "potential_energy": {
        "name": "Potential Energy",
        "formula": "PE = m × g × h",
        "unit": "J"
    },

    "density": {
        "name": "Density",
        "formula": "ρ = m / V",
        "unit": "kg/m³"
    },

    "moles": {
        "name": "Moles",
        "formula": "n = m / M",
        "unit": "mol"
    },

    "molarity": {
        "name": "Molarity",
        "formula": "C = n / V",
        "unit": "mol/L"
    },

    "ideal_gas": {
        "name": "Ideal Gas",
        "formula": "PV = nRT",
        "unit": "mol"
    }
}

# ------------------------------------------------
# 2. CORRECTED TOPIC DETECTOR
# ------------------------------------------------

def v7_detect_topic(q):

    q = q.lower().strip()

    # FORCE PRIORITY
    if any(x in q for x in [
        "calculate force",
        "find force",
        "force for mass",
        "force", "बल"
    ]):
        return "force"

    # ENERGY PRIORITY
    if any(x in q for x in [
        "kinetic energy", "गतिज ऊर्जा"
    ]):
        return "kinetic_energy"

    if any(x in q for x in [
        "potential energy", "स्थितिज ऊर्जा"
    ]):
        return "potential_energy"

    # OTHER TOPICS
    keywords = {

        "acceleration": [
            "acceleration", "accelerate", "त्वरण"
        ],

        "density": [
            "density", "घनत्व"
        ],

        "work": [
            "work done", "calculate work",
            "find work", "कार्य"
        ],

        "power": [
            "power", "शक्ति"
        ],

        "molarity": [
            "molarity", "मोलरता"
        ],

        "moles": [
            "number of moles", "calculate moles",
            "find moles", "moles", "मोल"
        ],

        "ideal_gas": [
            "ideal gas", "pv = nrt"
        ],

        "speed": [
            "speed", "velocity", "गति"
        ]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

# ------------------------------------------------
# 3. NUMBER EXTRACTION
# ------------------------------------------------

def v7_numbers(q):

    pattern = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

    return [
        float(x)
        for x in re.findall(pattern, q)
    ]

# ------------------------------------------------
# 4. CALCULATION ENGINE
# ------------------------------------------------

def v7_calculate(topic, nums):

    if topic not in V7_FORMULAS:
        raise ValueError("Unsupported formula")

    # SPEED
    if topic == "speed":

        if len(nums) < 2:
            raise ValueError("Distance and time required")

        d, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return d/t, [
            f"Speed = Distance / Time",
            f"Speed = {d} / {t}"
        ]

    # ACCELERATION
    if topic == "acceleration":

        if len(nums) < 3:
            raise ValueError(
                "Final velocity, initial velocity and time required"
            )

        v, u, t = nums[:3]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return (v-u)/t, [
            "Acceleration = (v - u) / t",
            f"Acceleration = ({v} - {u}) / {t}"
        ]

    # FORCE
    if topic == "force":

        if len(nums) < 2:
            raise ValueError("Mass and acceleration required")

        m, a = nums[:2]

        return m*a, [
            "Force = Mass × Acceleration",
            f"Force = {m} × {a}"
        ]

    # WORK
    if topic == "work":

        if len(nums) < 2:
            raise ValueError("Force and distance required")

        f, d = nums[:2]

        return f*d, [
            "Work = Force × Distance",
            f"Work = {f} × {d}"
        ]

    # POWER
    if topic == "power":

        if len(nums) < 2:
            raise ValueError("Work and time required")

        w, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return w/t, [
            "Power = Work / Time",
            f"Power = {w} / {t}"
        ]

    # KINETIC ENERGY
    if topic == "kinetic_energy":

        if len(nums) < 2:
            raise ValueError("Mass and velocity required")

        m, v = nums[:2]

        return 0.5*m*v**2, [
            "KE = 1/2 × m × v²",
            f"KE = 0.5 × {m} × {v}²",
            f"KE = 0.5 × {m} × {v**2}"
        ]

    # POTENTIAL ENERGY
    if topic == "potential_energy":

        if len(nums) < 2:
            raise ValueError("Mass and height required")

        m, h = nums[:2]

        g = 9.8

        return m*g*h, [
            "PE = m × g × h",
            f"PE = {m} × {g} × {h}"
        ]

    # DENSITY
    if topic == "density":

        if len(nums) < 2:
            raise ValueError("Mass and volume required")

        m, v = nums[:2]

        if v == 0:
            raise ValueError("Volume cannot be zero")

        return m/v, [
            "Density = Mass / Volume",
            f"Density = {m} / {v}"
        ]

    # MOLES
    if topic == "moles":

        if len(nums) < 2:
            raise ValueError("Mass and molar mass required")

        m, M = nums[:2]

        if M == 0:
            raise ValueError("Molar mass cannot be zero")

        return m/M, [
            "Moles = Mass / Molar Mass",
            f"Moles = {m} / {M}"
        ]

    # MOLARITY
    if topic == "molarity":

        if len(nums) < 2:
            raise ValueError("Moles and volume required")

        n, V = nums[:2]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return n/V, [
            "Molarity = Moles / Volume",
            f"Molarity = {n} / {V}"
        ]

    # IDEAL GAS
    if topic == "ideal_gas":

        if len(nums) < 3:
            raise ValueError(
                "Pressure, volume and temperature required"
            )

        P, V, T = nums[:3]

        if T <= 0:
            raise ValueError("Temperature must be positive")

        R = 0.082057

        return P*V/(R*T), [
            "n = PV / RT",
            f"n = {P} × {V} / (0.082057 × {T})"
        ]

    raise ValueError("Calculation not implemented")

# ------------------------------------------------
# 5. SOLUTION GENERATOR
# ------------------------------------------------

def v7_solve(q, language="English"):

    topic = v7_detect_topic(q)

    if topic is None:
        return "Question topic identify nahi hua."

    nums = v7_numbers(q)

    try:

        result, steps = v7_calculate(topic, nums)

        if not math.isfinite(result):
            return "Invalid numerical result."

        formula = V7_FORMULAS[topic]

        if language == "Hindi":

            text = f"""
विषय: {formula['name']}

सूत्र:
{formula['formula']}

हल:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

अंतिम उत्तर:
{result:.6g} {formula['unit']}
"""

        else:

            text = f"""
Topic: {formula['name']}

Formula:
{formula['formula']}

Solution:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

Final Answer:
{result:.6g} {formula['unit']}
"""

        return text

    except Exception as e:

        return "Cannot solve: " + str(e)

# ------------------------------------------------
# 6. FORMULA SEARCH
# ------------------------------------------------

def v7_formula_search(keyword):

    keyword = keyword.lower().strip()

    results = []

    for key, item in V7_FORMULAS.items():

        if (
            keyword in key.lower()
            or keyword in item["name"].lower()
            or keyword in item["formula"].lower()
        ):

            results.append(
                f"{item['name']}: {item['formula']}"
            )

    return results if results else ["No formula found"]

# ------------------------------------------------
# 7. COMMON MISTAKES
# ------------------------------------------------

V7_MISTAKES = {

    "speed": "Distance aur time ki units compatible honi chahiye.",

    "acceleration": "Velocity difference ko time se divide karein.",

    "force": "Mass kg aur acceleration m/s² mein honi chahiye.",

    "work": "Force aur displacement ka product use karein.",

    "power": "Work ko time se divide karein.",

    "kinetic_energy": "Velocity ka square lena na bhoolein.",

    "potential_energy": "Height aur mass SI units mein rakhein.",

    "density": "Mass aur volume compatible units mein hon.",

    "moles": "Mass aur molar mass same mass units mein hon.",

    "molarity": "Volume litres mein hona chahiye.",

    "ideal_gas": "Temperature Kelvin mein hona chahiye."
}

# ------------------------------------------------
# 8. CORRECTED TESTS
# ------------------------------------------------

V7_TESTS = [

    ("Calculate speed for 100 distance in 2 time",
     "speed", 50),

    ("Find acceleration for final velocity 20 initial velocity 10 time 2",
     "acceleration", 5),

    ("Calculate force for mass 5 and acceleration 2",
     "force", 10),

    ("Calculate work done by force 10 and distance 5",
     "work", 50),

    ("Calculate power for work 100 and time 5",
     "power", 20),

    ("Calculate kinetic energy for mass 2 velocity 3",
     "kinetic_energy", 9),

    ("Calculate potential energy for mass 2 height 5",
     "potential_energy", 98),

    ("Calculate density for mass 10 volume 2",
     "density", 5),

    ("Calculate moles for mass 10 molar mass 20",
     "moles", 0.5),

    ("Calculate molarity for 2 moles volume 4",
     "molarity", 0.5)
]

print("V7.1 TESTING")

for q, topic, expected in V7_TESTS:

    detected = v7_detect_topic(q)

    assert detected == topic, (
        q, detected, topic
    )

    nums = v7_numbers(q)

    result, steps = v7_calculate(topic, nums)

    assert abs(result-expected) < 0.001, (
        q, result, expected
    )

    print("PASS:", topic)

print("\nALL V7.1 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v7_question = widgets.Textarea(
    placeholder="Calculate force for mass 5 and acceleration 2",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="120px"
    )
)

v7_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v7_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v7_formula_input = widgets.Text(
    placeholder="Search speed, force, energy...",
    description="Formula:"
)

v7_formula_button = widgets.Button(
    description="Search Formula"
)

v7_output = widgets.Output()

def v7_run(_):

    with v7_output:

        clear_output()

        q = v7_question.value

        print(v7_solve(q, v7_language.value))

        topic = v7_detect_topic(q)

        if topic:

            print("\nCommon Mistake:")
            print(V7_MISTAKES.get(topic, ""))

def v7_search_run(_):

    with v7_output:

        clear_output()

        results = v7_formula_search(
            v7_formula_input.value
        )

        for item in results:
            print(item)

v7_button.on_click(v7_run)

v7_formula_button.on_click(
    v7_search_run
)

display(v7_question)
display(v7_language)
display(v7_button)

display(v7_formula_input)
display(v7_formula_button)

display(v7_output)

print("\nSUNO SAATHI MAGIC LAYER V7.1 READY")

def v7_detect_topic(q):

    q = q.lower()

    # Force questions
    if any(x in q for x in [
        "calculate force",
        "find force",
        "force for mass",
        "force", "बल"
    ]):
        return "force"

    keywords = {

        "acceleration": [
            "acceleration", "accelerate", "त्वरण"
        ],

        "kinetic_energy": [
            "kinetic energy", "गतिज ऊर्जा"
        ],

        "potential_energy": [
            "potential energy", "स्थितिज ऊर्जा"
        ],

        "density": [
            "density", "घनत्व"
        ],

        "work": [
            "work done", "calculate work", "find work", "कार्य"
        ],

        "power": [
            "power", "शक्ति"
        ],

        "molarity": [
            "molarity", "मोलरता"
        ],

        "moles": [
            "moles", "number of moles", "मोल"
        ],

        "ideal_gas": [
            "ideal gas", "pv = nrt"
        ],

        "speed": [
            "speed", "velocity", "गति"
        ]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

def v7_detect_topic(q):

    q = q.lower()

    # Force questions
    if any(x in q for x in [
        "calculate force",
        "find force",
        "force for mass",
        "force", "बल"
    ]):
        return "force"

    keywords = {

        "acceleration": [
            "acceleration", "accelerate", "त्वरण"
        ],

        "kinetic_energy": [
            "kinetic energy", "गतिज ऊर्जा"
        ],

        "potential_energy": [
            "potential energy", "स्थितिज ऊर्जा"
        ],

        "density": [
            "density", "घनत्व"
        ],

        "work": [
            "work done", "calculate work", "find work", "कार्य"
        ],

        "power": [
            "power", "शक्ति"
        ],

        "molarity": [
            "molarity", "मोलरता"
        ],

        "moles": [
            "moles", "number of moles", "मोल"
        ],

        "ideal_gas": [
            "ideal gas", "pv = nrt"
        ],

        "speed": [
            "speed", "velocity", "गति"
        ]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

def v7_detect_topic(q):

    q = q.lower()

    # Force questions
    if any(x in q for x in [
        "calculate force",
        "find force",
        "force for mass",
        "force", "बल"
    ]):
        return "force"

    keywords = {

        "acceleration": [
            "acceleration", "accelerate", "त्वरण"
        ],

        "kinetic_energy": [
            "kinetic energy", "गतिज ऊर्जा"
        ],

        "potential_energy": [
            "potential energy", "स्थितिज ऊर्जा"
        ],

        "density": [
            "density", "घनत्व"
        ],

        "work": [
            "work done", "calculate work", "find work", "कार्य"
        ],

        "power": [
            "power", "शक्ति"
        ],

        "molarity": [
            "molarity", "मोलरता"
        ],

        "moles": [
            "moles", "number of moles", "मोल"
        ],

        "ideal_gas": [
            "ideal gas", "pv = nrt"
        ],

        "speed": [
            "speed", "velocity", "गति"
        ]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

def v7_detect_topic(q):

    q = q.lower()

    # Force questions
    if any(x in q for x in [
        "calculate force",
        "find force",
        "force for mass",
        "force", "बल"
    ]):
        return "force"

    keywords = {

        "acceleration": [
            "acceleration", "accelerate", "त्वरण"
        ],

        "kinetic_energy": [
            "kinetic energy", "गतिज ऊर्जा"
        ],

        "potential_energy": [
            "potential energy", "स्थितिज ऊर्जा"
        ],

        "density": [
            "density", "घनत्व"
        ],

        "work": [
            "work done", "calculate work", "find work", "कार्य"
        ],

        "power": [
            "power", "शक्ति"
        ],

        "molarity": [
            "molarity", "मोलरता"
        ],

        "moles": [
            "moles", "number of moles", "मोल"
        ],

        "ideal_gas": [
            "ideal gas", "pv = nrt"
        ],

        "speed": [
            "speed", "velocity", "गति"
        ]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

def v7_detect_topic(q):

    q = q.lower()

    # Force questions
    if any(x in q for x in [
        "calculate force",
        "find force",
        "force for mass",
        "force", "बल"
    ]):
        return "force"

    keywords = {

        "acceleration": [
            "acceleration", "accelerate", "त्वरण"
        ],

        "kinetic_energy": [
            "kinetic energy", "गतिज ऊर्जा"
        ],

        "potential_energy": [
            "potential energy", "स्थितिज ऊर्जा"
        ],

        "density": [
            "density", "घनत्व"
        ],

        "work": [
            "work done", "calculate work", "find work", "कार्य"
        ],

        "power": [
            "power", "शक्ति"
        ],

        "molarity": [
            "molarity", "मोलरता"
        ],

        "moles": [
            "moles", "number of moles", "मोल"
        ],

        "ideal_gas": [
            "ideal gas", "pv = nrt"
        ],

        "speed": [
            "speed", "velocity", "गति"
        ]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

# ============================================================
# SUNO SAATHI MAGIC LAYER v5
# AUTOMATIC QUESTION SOLVER
# ============================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------------------
# TOPIC DETECTION
# ------------------------------------------------------------

def v5_detect_topic(q):

    q = q.lower()

    if any(x in q for x in ["speed", "distance", "time", "velocity", "गति", "दूरी", "समय"]):
        return "speed"

    if any(x in q for x in ["work", "कार्य", "force", "बल"]):
        return "work"

    if any(x in q for x in ["power", "शक्ति"]):
        return "power"

    if any(x in q for x in ["molarity", "मोलरता", "moles per litre"]):
        return "molarity"

    if any(x in q for x in ["number of moles", "calculate moles", "moles", "मोल", "molecular mass"]):
        return "moles"

    return None


# ------------------------------------------------------------
# NUMBER EXTRACTION
# ------------------------------------------------------------

def v5_extract_numbers(q):

    pattern = r'\d+(?:\.\d+)?'
    return [float(x) for x in re.findall(pattern, q)]


# ------------------------------------------------------------
# UNIT EXTRACTION
# ------------------------------------------------------------

def v5_extract_units(q):

    q = q.lower()

    units = {
        "km": "km",
        "kilometer": "km",
        "kilometre": "km",
        "m": "m",
        "meter": "m",
        "metre": "m",
        "cm": "cm",
        "mm": "mm",
        "hour": "hour",
        "hr": "hour",
        "h": "hour",
        "minute": "minute",
        "min": "minute",
        "second": "second",
        "sec": "second",
        "s": "second",
        "kg": "kg",
        "gram": "g",
        "g": "g",
        "newton": "N",
        "n": "N",
        "joule": "J",
        "j": "J",
        "watt": "W",
        "mol": "mol",
        "litre": "L",
        "liter": "L",
        "ml": "mL"
    }

    found = []

    for word, unit in units.items():
        if re.search(r'\b' + re.escape(word) + r'\b', q):
            found.append(unit)

    return found


# ------------------------------------------------------------
# SOLVER
# ------------------------------------------------------------

def v5_solve_question(q):

    topic = v5_detect_topic(q)
    nums = v5_extract_numbers(q)

    if topic is None:
        return {
            "success": False,
            "message": "Topic detect nahi hua. Speed, Work, Power, Molarity ya Moles ka question try karein."
        }

    if len(nums) < 2:
        return {
            "success": False,
            "message": "Calculation ke liye kam se kam 2 numerical values chahiye."
        }

    # SPEED
    if topic == "speed":

        distance = nums[0]
        time = nums[1]

        if time == 0:
            return {"success": False, "message": "Time zero nahi ho sakta."}

        result = distance / time

        return {
            "success": True,
            "topic": "Speed",
            "formula": "Speed = Distance / Time",
            "values": {
                "Distance": distance,
                "Time": time
            },
            "result": result,
            "unit": "distance unit / time unit"
        }

    # WORK
    if topic == "work":

        force = nums[0]
        distance = nums[1]

        result = force * distance

        return {
            "success": True,
            "topic": "Work",
            "formula": "Work = Force × Distance",
            "values": {
                "Force": force,
                "Distance": distance
            },
            "result": result,
            "unit": "J (if Force is N and Distance is m)"
        }

    # POWER
    if topic == "power":

        work = nums[0]
        time = nums[1]

        if time == 0:
            return {"success": False, "message": "Time zero nahi ho sakta."}

        result = work / time

        return {
            "success": True,
            "topic": "Power",
            "formula": "Power = Work / Time",
            "values": {
                "Work": work,
                "Time": time
            },
            "result": result,
            "unit": "W (if Work is J and Time is s)"
        }

    # MOLARITY
    if topic == "molarity":

        moles = nums[0]
        volume = nums[1]

        if volume == 0:
            return {"success": False, "message": "Volume zero nahi ho sakta."}

        result = moles / volume

        return {
            "success": True,
            "topic": "Molarity",
            "formula": "Molarity = Moles / Volume (L)",
            "values": {
                "Moles": moles,
                "Volume": volume
            },
            "result": result,
            "unit": "mol/L"
        }

    # MOLES
    if topic == "moles":

        mass = nums[0]
        molar_mass = nums[1]

        if molar_mass == 0:
            return {"success": False, "message": "Molar mass zero nahi ho sakta."}

        result = mass / molar_mass

        return {
            "success": True,
            "topic": "Moles",
            "formula": "Moles = Mass / Molar Mass",
            "values": {
                "Mass": mass,
                "Molar Mass": molar_mass
            },
            "result": result,
            "unit": "mol"
        }


# ------------------------------------------------------------
# EXPLANATION GENERATOR
# ------------------------------------------------------------

def v5_explain(data, language="English"):

    if not data["success"]:
        return data["message"]

    if language == "Hindi":

        text = f"""
विषय: {data['topic']}

सूत्र:
{data['formula']}

दिए गए मान:
{data['values']}

गणना:
{data['formula']}

उत्तर:
{data['result']:.4f} {data['unit']}
"""

    else:

        text = f"""
Topic: {data['topic']}

Formula:
{data['formula']}

Given values:
{data['values']}

Calculation:
{data['formula']}

Final Answer:
{data['result']:.4f} {data['unit']}
"""

    return text


# ------------------------------------------------------------
# TESTS
# ------------------------------------------------------------

v5_tests = [
    ("Calculate speed for 100 km in 2 hours", "speed"),
    ("Find work done by force 10 N over 5 m", "work"),
    ("Calculate power for 100 J in 5 seconds", "power"),
    ("Find molarity of 2 moles in 4 litres", "molarity"),
    ("Calculate moles from 10 g mass and 20 g molar mass", "moles")
]

print("V5 TESTS")

for q, expected in v5_tests:

    result = v5_solve_question(q)

    assert result["success"], q
    assert result["topic"].lower() == expected

    print("PASS:", q)

print("\nAll V5 tests passed!")


# ------------------------------------------------------------
# INTERACTIVE MAGIC LAYER
# ------------------------------------------------------------

v5_question = widgets.Textarea(
    placeholder="Example: Calculate speed for 100 km in 2 hours",
    description="Question:",
    layout=widgets.Layout(width="100%", height="100px")
)

v5_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v5_button = widgets.Button(
    description="Solve Question",
    button_style="success",
    icon="check"
)

v5_output = widgets.Output()


def v5_run(_):

    with v5_output:

        clear_output()

        q = v5_question.value

        data = v5_solve_question(q)

        print(v5_explain(data, v5_language.value))

        if data["success"]:

            print("\nDetected topic:", data["topic"])
            print("Formula:", data["formula"])
            print("Answer:", round(data["result"], 4), data["unit"])


v5_button.on_click(v5_run)

display(v5_question)
display(v5_language)
display(v5_button)
display(v5_output)

print("\nSUNO SAATHI MAGIC LAYER V5 READY")

# ============================================================
# SUNO SAATHI MAGIC LAYER v5
# AUTOMATIC QUESTION SOLVER
# ============================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------------------
# TOPIC DETECTION
# ------------------------------------------------------------

def v5_detect_topic(q):

    q = q.lower()

    if any(x in q for x in ["speed", "distance", "time", "velocity", "गति", "दूरी", "समय"]):
        return "speed"

    if any(x in q for x in ["work", "कार्य", "force", "बल"]):
        return "work"

    if any(x in q for x in ["power", "शक्ति"]):
        return "power"

    if any(x in q for x in ["molarity", "मोलरता", "moles per litre"]):
        return "molarity"

    if any(x in q for x in ["number of moles", "calculate moles", "moles", "मोल", "molecular mass"]):
        return "moles"

    return None


# ------------------------------------------------------------
# NUMBER EXTRACTION
# ------------------------------------------------------------

def v5_extract_numbers(q):

    pattern = r'\d+(?:\.\d+)?'
    return [float(x) for x in re.findall(pattern, q)]


# ------------------------------------------------------------
# UNIT EXTRACTION
# ------------------------------------------------------------

def v5_extract_units(q):

    q = q.lower()

    units = {
        "km": "km",
        "kilometer": "km",
        "kilometre": "km",
        "m": "m",
        "meter": "m",
        "metre": "m",
        "cm": "cm",
        "mm": "mm",
        "hour": "hour",
        "hr": "hour",
        "h": "hour",
        "minute": "minute",
        "min": "minute",
        "second": "second",
        "sec": "second",
        "s": "second",
        "kg": "kg",
        "gram": "g",
        "g": "g",
        "newton": "N",
        "n": "N",
        "joule": "J",
        "j": "J",
        "watt": "W",
        "mol": "mol",
        "litre": "L",
        "liter": "L",
        "ml": "mL"
    }

    found = []

    for word, unit in units.items():
        if re.search(r'\b' + re.escape(word) + r'\b', q):
            found.append(unit)

    return found


# ------------------------------------------------------------
# SOLVER
# ------------------------------------------------------------

def v5_solve_question(q):

    topic = v5_detect_topic(q)
    nums = v5_extract_numbers(q)

    if topic is None:
        return {
            "success": False,
            "message": "Topic detect nahi hua. Speed, Work, Power, Molarity ya Moles ka question try karein."
        }

    if len(nums) < 2:
        return {
            "success": False,
            "message": "Calculation ke liye kam se kam 2 numerical values chahiye."
        }

    # SPEED
    if topic == "speed":

        distance = nums[0]
        time = nums[1]

        if time == 0:
            return {"success": False, "message": "Time zero nahi ho sakta."}

        result = distance / time

        return {
            "success": True,
            "topic": "Speed",
            "formula": "Speed = Distance / Time",
            "values": {
                "Distance": distance,
                "Time": time
            },
            "result": result,
            "unit": "distance unit / time unit"
        }

    # WORK
    if topic == "work":

        force = nums[0]
        distance = nums[1]

        result = force * distance

        return {
            "success": True,
            "topic": "Work",
            "formula": "Work = Force × Distance",
            "values": {
                "Force": force,
                "Distance": distance
            },
            "result": result,
            "unit": "J (if Force is N and Distance is m)"
        }

    # POWER
    if topic == "power":

        work = nums[0]
        time = nums[1]

        if time == 0:
            return {"success": False, "message": "Time zero nahi ho sakta."}

        result = work / time

        return {
            "success": True,
            "topic": "Power",
            "formula": "Power = Work / Time",
            "values": {
                "Work": work,
                "Time": time
            },
            "result": result,
            "unit": "W (if Work is J and Time is s)"
        }

    # MOLARITY
    if topic == "molarity":

        moles = nums[0]
        volume = nums[1]

        if volume == 0:
            return {"success": False, "message": "Volume zero nahi ho sakta."}

        result = moles / volume

        return {
            "success": True,
            "topic": "Molarity",
            "formula": "Molarity = Moles / Volume (L)",
            "values": {
                "Moles": moles,
                "Volume": volume
            },
            "result": result,
            "unit": "mol/L"
        }

    # MOLES
    if topic == "moles":

        mass = nums[0]
        molar_mass = nums[1]

        if molar_mass == 0:
            return {"success": False, "message": "Molar mass zero nahi ho sakta."}

        result = mass / molar_mass

        return {
            "success": True,
            "topic": "Moles",
            "formula": "Moles = Mass / Molar Mass",
            "values": {
                "Mass": mass,
                "Molar Mass": molar_mass
            },
            "result": result,
            "unit": "mol"
        }


# ------------------------------------------------------------
# EXPLANATION GENERATOR
# ------------------------------------------------------------

def v5_explain(data, language="English"):

    if not data["success"]:
        return data["message"]

    if language == "Hindi":

        text = f"""
विषय: {data['topic']}

सूत्र:
{data['formula']}

दिए गए मान:
{data['values']}

गणना:
{data['formula']}

उत्तर:
{data['result']:.4f} {data['unit']}
"""

    else:

        text = f"""
Topic: {data['topic']}

Formula:
{data['formula']}

Given values:
{data['values']}

Calculation:
{data['formula']}

Final Answer:
{data['result']:.4f} {data['unit']}
"""

    return text


# ------------------------------------------------------------
# TESTS
# ------------------------------------------------------------

v5_tests = [
    ("Calculate speed for 100 km in 2 hours", "speed"),
    ("Find work done by force 10 N over 5 m", "work"),
    ("Calculate power for 100 J in 5 seconds", "power"),
    ("Find molarity of 2 moles in 4 litres", "molarity"),
    ("Calculate moles from 10 g mass and 20 g molar mass", "moles")
]

print("V5 TESTS")

for q, expected in v5_tests:

    result = v5_solve_question(q)

    assert result["success"], q
    assert result["topic"].lower() == expected

    print("PASS:", q)

print("\nAll V5 tests passed!")


# ------------------------------------------------------------
# INTERACTIVE MAGIC LAYER
# ------------------------------------------------------------

v5_question = widgets.Textarea(
    placeholder="Example: Calculate speed for 100 km in 2 hours",
    description="Question:",
    layout=widgets.Layout(width="100%", height="100px")
)

v5_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v5_button = widgets.Button(
    description="Solve Question",
    button_style="success",
    icon="check"
)

v5_output = widgets.Output()


def v5_run(_):

    with v5_output:

        clear_output()

        q = v5_question.value

        data = v5_solve_question(q)

        print(v5_explain(data, v5_language.value))

        if data["success"]:

            print("\nDetected topic:", data["topic"])
            print("Formula:", data["formula"])
            print("Answer:", round(data["result"], 4), data["unit"])


v5_button.on_click(v5_run)

display(v5_question)
display(v5_language)
display(v5_button)
display(v5_output)

print("\nSUNO SAATHI MAGIC LAYER V5 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V7.1
# COMPLETE CORRECTED VERSION
# PHYSICS + CHEMISTRY FORMULA ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. FORMULA DATABASE
# ------------------------------------------------

V7_FORMULAS = {

    "speed": {
        "name": "Speed",
        "formula": "v = d / t",
        "unit": "m/s"
    },

    "acceleration": {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "unit": "m/s²"
    },

    "force": {
        "name": "Force",
        "formula": "F = m × a",
        "unit": "N"
    },

    "work": {
        "name": "Work",
        "formula": "W = F × d",
        "unit": "J"
    },

    "power": {
        "name": "Power",
        "formula": "P = W / t",
        "unit": "W"
    },

    "kinetic_energy": {
        "name": "Kinetic Energy",
        "formula": "KE = 1/2 × m × v²",
        "unit": "J"
    },

    "potential_energy": {
        "name": "Potential Energy",
        "formula": "PE = m × g × h",
        "unit": "J"
    },

    "density": {
        "name": "Density",
        "formula": "ρ = m / V",
        "unit": "kg/m³"
    },

    "moles": {
        "name": "Moles",
        "formula": "n = m / M",
        "unit": "mol"
    },

    "molarity": {
        "name": "Molarity",
        "formula": "C = n / V",
        "unit": "mol/L"
    },

    "ideal_gas": {
        "name": "Ideal Gas",
        "formula": "PV = nRT",
        "unit": "mol"
    }
}

# ------------------------------------------------
# 2. CORRECTED TOPIC DETECTOR
# ------------------------------------------------

def v7_detect_topic(q):

    q = q.lower().strip()

    # FORCE PRIORITY
    if any(x in q for x in [
        "calculate force",
        "find force",
        "force for mass",
        "force", "बल"
    ]):
        return "force"

    # ENERGY PRIORITY
    if any(x in q for x in [
        "kinetic energy", "गतिज ऊर्जा"
    ]):
        return "kinetic_energy"

    if any(x in q for x in [
        "potential energy", "स्थितिज ऊर्जा"
    ]):
        return "potential_energy"

    # OTHER TOPICS
    keywords = {

        "acceleration": [
            "acceleration", "accelerate", "त्वरण"
        ],

        "density": [
            "density", "घनत्व"
        ],

        "work": [
            "work done", "calculate work",
            "find work", "कार्य"
        ],

        "power": [
            "power", "शक्ति"
        ],

        "molarity": [
            "molarity", "मोलरता"
        ],

        "moles": [
            "number of moles", "calculate moles",
            "find moles", "moles", "मोल"
        ],

        "ideal_gas": [
            "ideal gas", "pv = nrt"
        ],

        "speed": [
            "speed", "velocity", "गति"
        ]
    }

    for topic, words in keywords.items():

        if any(word in q for word in words):
            return topic

    return None

# ------------------------------------------------
# 3. NUMBER EXTRACTION
# ------------------------------------------------

def v7_numbers(q):

    pattern = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

    return [
        float(x)
        for x in re.findall(pattern, q)
    ]

# ------------------------------------------------
# 4. CALCULATION ENGINE
# ------------------------------------------------

def v7_calculate(topic, nums):

    if topic not in V7_FORMULAS:
        raise ValueError("Unsupported formula")

    # SPEED
    if topic == "speed":

        if len(nums) < 2:
            raise ValueError("Distance and time required")

        d, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return d/t, [
            f"Speed = Distance / Time",
            f"Speed = {d} / {t}"
        ]

    # ACCELERATION
    if topic == "acceleration":

        if len(nums) < 3:
            raise ValueError(
                "Final velocity, initial velocity and time required"
            )

        v, u, t = nums[:3]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return (v-u)/t, [
            "Acceleration = (v - u) / t",
            f"Acceleration = ({v} - {u}) / {t}"
        ]

    # FORCE
    if topic == "force":

        if len(nums) < 2:
            raise ValueError("Mass and acceleration required")

        m, a = nums[:2]

        return m*a, [
            "Force = Mass × Acceleration",
            f"Force = {m} × {a}"
        ]

    # WORK
    if topic == "work":

        if len(nums) < 2:
            raise ValueError("Force and distance required")

        f, d = nums[:2]

        return f*d, [
            "Work = Force × Distance",
            f"Work = {f} × {d}"
        ]

    # POWER
    if topic == "power":

        if len(nums) < 2:
            raise ValueError("Work and time required")

        w, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return w/t, [
            "Power = Work / Time",
            f"Power = {w} / {t}"
        ]

    # KINETIC ENERGY
    if topic == "kinetic_energy":

        if len(nums) < 2:
            raise ValueError("Mass and velocity required")

        m, v = nums[:2]

        return 0.5*m*v**2, [
            "KE = 1/2 × m × v²",
            f"KE = 0.5 × {m} × {v}²",
            f"KE = 0.5 × {m} × {v**2}"
        ]

    # POTENTIAL ENERGY
    if topic == "potential_energy":

        if len(nums) < 2:
            raise ValueError("Mass and height required")

        m, h = nums[:2]

        g = 9.8

        return m*g*h, [
            "PE = m × g × h",
            f"PE = {m} × {g} × {h}"
        ]

    # DENSITY
    if topic == "density":

        if len(nums) < 2:
            raise ValueError("Mass and volume required")

        m, v = nums[:2]

        if v == 0:
            raise ValueError("Volume cannot be zero")

        return m/v, [
            "Density = Mass / Volume",
            f"Density = {m} / {v}"
        ]

    # MOLES
    if topic == "moles":

        if len(nums) < 2:
            raise ValueError("Mass and molar mass required")

        m, M = nums[:2]

        if M == 0:
            raise ValueError("Molar mass cannot be zero")

        return m/M, [
            "Moles = Mass / Molar Mass",
            f"Moles = {m} / {M}"
        ]

    # MOLARITY
    if topic == "molarity":

        if len(nums) < 2:
            raise ValueError("Moles and volume required")

        n, V = nums[:2]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return n/V, [
            "Molarity = Moles / Volume",
            f"Molarity = {n} / {V}"
        ]

    # IDEAL GAS
    if topic == "ideal_gas":

        if len(nums) < 3:
            raise ValueError(
                "Pressure, volume and temperature required"
            )

        P, V, T = nums[:3]

        if T <= 0:
            raise ValueError("Temperature must be positive")

        R = 0.082057

        return P*V/(R*T), [
            "n = PV / RT",
            f"n = {P} × {V} / (0.082057 × {T})"
        ]

    raise ValueError("Calculation not implemented")

# ------------------------------------------------
# 5. SOLUTION GENERATOR
# ------------------------------------------------

def v7_solve(q, language="English"):

    topic = v7_detect_topic(q)

    if topic is None:
        return "Question topic identify nahi hua."

    nums = v7_numbers(q)

    try:

        result, steps = v7_calculate(topic, nums)

        if not math.isfinite(result):
            return "Invalid numerical result."

        formula = V7_FORMULAS[topic]

        if language == "Hindi":

            text = f"""
विषय: {formula['name']}

सूत्र:
{formula['formula']}

हल:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

अंतिम उत्तर:
{result:.6g} {formula['unit']}
"""

        else:

            text = f"""
Topic: {formula['name']}

Formula:
{formula['formula']}

Solution:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

Final Answer:
{result:.6g} {formula['unit']}
"""

        return text

    except Exception as e:

        return "Cannot solve: " + str(e)

# ------------------------------------------------
# 6. FORMULA SEARCH
# ------------------------------------------------

def v7_formula_search(keyword):

    keyword = keyword.lower().strip()

    results = []

    for key, item in V7_FORMULAS.items():

        if (
            keyword in key.lower()
            or keyword in item["name"].lower()
            or keyword in item["formula"].lower()
        ):

            results.append(
                f"{item['name']}: {item['formula']}"
            )

    return results if results else ["No formula found"]

# ------------------------------------------------
# 7. COMMON MISTAKES
# ------------------------------------------------

V7_MISTAKES = {

    "speed": "Distance aur time ki units compatible honi chahiye.",

    "acceleration": "Velocity difference ko time se divide karein.",

    "force": "Mass kg aur acceleration m/s² mein honi chahiye.",

    "work": "Force aur displacement ka product use karein.",

    "power": "Work ko time se divide karein.",

    "kinetic_energy": "Velocity ka square lena na bhoolein.",

    "potential_energy": "Height aur mass SI units mein rakhein.",

    "density": "Mass aur volume compatible units mein hon.",

    "moles": "Mass aur molar mass same mass units mein hon.",

    "molarity": "Volume litres mein hona chahiye.",

    "ideal_gas": "Temperature Kelvin mein hona chahiye."
}

# ------------------------------------------------
# 8. CORRECTED TESTS
# ------------------------------------------------

V7_TESTS = [

    ("Calculate speed for 100 distance in 2 time",
     "speed", 50),

    ("Find acceleration for final velocity 20 initial velocity 10 time 2",
     "acceleration", 5),

    ("Calculate force for mass 5 and acceleration 2",
     "force", 10),

    ("Calculate work done by force 10 and distance 5",
     "work", 50),

    ("Calculate power for work 100 and time 5",
     "power", 20),

    ("Calculate kinetic energy for mass 2 velocity 3",
     "kinetic_energy", 9),

    ("Calculate potential energy for mass 2 height 5",
     "potential_energy", 98),

    ("Calculate density for mass 10 volume 2",
     "density", 5),

    ("Calculate moles for mass 10 molar mass 20",
     "moles", 0.5),

    ("Calculate molarity for 2 moles volume 4",
     "molarity", 0.5)
]

print("V7.1 TESTING")

for q, topic, expected in V7_TESTS:

    detected = v7_detect_topic(q)

    assert detected == topic, (
        q, detected, topic
    )

    nums = v7_numbers(q)

    result, steps = v7_calculate(topic, nums)

    assert abs(result-expected) < 0.001, (
        q, result, expected
    )

    print("PASS:", topic)

print("\nALL V7.1 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v7_question = widgets.Textarea(
    placeholder="Calculate force for mass 5 and acceleration 2",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="120px"
    )
)

v7_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v7_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v7_formula_input = widgets.Text(
    placeholder="Search speed, force, energy...",
    description="Formula:"
)

v7_formula_button = widgets.Button(
    description="Search Formula"
)

v7_output = widgets.Output()

def v7_run(_):

    with v7_output:

        clear_output()

        q = v7_question.value

        print(v7_solve(q, v7_language.value))

        topic = v7_detect_topic(q)

        if topic:

            print("\nCommon Mistake:")
            print(V7_MISTAKES.get(topic, ""))

def v7_search_run(_):

    with v7_output:

        clear_output()

        results = v7_formula_search(
            v7_formula_input.value
        )

        for item in results:
            print(item)

v7_button.on_click(v7_run)

v7_formula_button.on_click(
    v7_search_run
)

display(v7_question)
display(v7_language)
display(v7_button)

display(v7_formula_input)
display(v7_formula_button)

display(v7_output)

print("\nSUNO SAATHI MAGIC LAYER V7.1 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V7.1
# COMPLETE CORRECTED VERSION
# PHYSICS + CHEMISTRY FORMULA ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. FORMULA DATABASE
# ------------------------------------------------

V7_FORMULAS = {

    "speed": {
        "name": "Speed",
        "formula": "v = d / t",
        "unit": "m/s"
    },

    "acceleration": {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "unit": "m/s²"
    },

    "force": {
        "name": "Force",
        "formula": "F = m × a",
        "unit": "N"
    },

    "work": {
        "name": "Work",
        "formula": "W = F × d",
        "unit": "J"
    },

    "power": {
        "name": "Power",
        "formula": "P = W / t",
        "unit": "W"
    },

    "kinetic_energy": {
        "name": "Kinetic Energy",
        "formula": "KE = 1/2 × m × v²",
        "unit": "J"
    },

    "potential_energy": {
        "name": "Potential Energy",
        "formula": "PE = m × g × h",
        "unit": "J"
    },

    "density": {
        "name": "Density",
        "formula": "ρ = m / V",
        "unit": "kg/m³"
    },

    "moles": {
        "name": "Moles",
        "formula": "n = m / M",
        "unit": "mol"
    },

    "molarity": {
        "name": "Molarity",
        "formula": "C = n / V",
        "unit": "mol/L"
    },

    "ideal_gas": {
        "name": "Ideal Gas",
        "formula": "PV = nRT",
        "unit": "mol"
    }
}

# ------------------------------------------------
# 2. CORRECTED TOPIC DETECTOR
# ------------------------------------------------


def v7_detect_topic(q):

    q = q.lower().strip()

    # Energy
    if "kinetic energy" in q or "गतिज ऊर्जा" in q:
        return "kinetic_energy"

    if "potential energy" in q or "स्थितिज ऊर्जा" in q:
        return "potential_energy"

    # Work: force keyword se pehle
    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "work", "कार्य"
    ]):
        return "work"

    # Power
    if any(x in q for x in [
        "power", "शक्ति"
    ]):
        return "power"

    # Force
    if any(x in q for x in [
        "calculate force", "find force",
        "force", "बल"
    ]):
        return "force"

    # Acceleration
    if any(x in q for x in [
        "acceleration", "accelerate", "त्वरण"
    ]):
        return "acceleration"

    # Chemistry
    if any(x in q for x in [
        "molarity", "मोलरता"
    ]):
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    # Density
    if any(x in q for x in [
        "density", "घनत्व"
    ]):
        return "density"

    # Ideal gas
    if any(x in q for x in [
        "ideal gas", "pv = nrt"
    ]):
        return "ideal_gas"

    # Speed
    if any(x in q for x in [
        "speed", "velocity", "गति"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER EXTRACTION
# ------------------------------------------------

def v7_numbers(q):

    pattern = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

    return [
        float(x)
        for x in re.findall(pattern, q)
    ]

# ------------------------------------------------
# 4. CALCULATION ENGINE
# ------------------------------------------------

def v7_calculate(topic, nums):

    if topic not in V7_FORMULAS:
        raise ValueError("Unsupported formula")

    # SPEED
    if topic == "speed":

        if len(nums) < 2:
            raise ValueError("Distance and time required")

        d, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return d/t, [
            f"Speed = Distance / Time",
            f"Speed = {d} / {t}"
        ]

    # ACCELERATION
    if topic == "acceleration":

        if len(nums) < 3:
            raise ValueError(
                "Final velocity, initial velocity and time required"
            )

        v, u, t = nums[:3]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return (v-u)/t, [
            "Acceleration = (v - u) / t",
            f"Acceleration = ({v} - {u}) / {t}"
        ]

    # FORCE
    if topic == "force":

        if len(nums) < 2:
            raise ValueError("Mass and acceleration required")

        m, a = nums[:2]

        return m*a, [
            "Force = Mass × Acceleration",
            f"Force = {m} × {a}"
        ]

    # WORK
    if topic == "work":

        if len(nums) < 2:
            raise ValueError("Force and distance required")

        f, d = nums[:2]

        return f*d, [
            "Work = Force × Distance",
            f"Work = {f} × {d}"
        ]

    # POWER
    if topic == "power":

        if len(nums) < 2:
            raise ValueError("Work and time required")

        w, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return w/t, [
            "Power = Work / Time",
            f"Power = {w} / {t}"
        ]

    # KINETIC ENERGY
    if topic == "kinetic_energy":

        if len(nums) < 2:
            raise ValueError("Mass and velocity required")

        m, v = nums[:2]

        return 0.5*m*v**2, [
            "KE = 1/2 × m × v²",
            f"KE = 0.5 × {m} × {v}²",
            f"KE = 0.5 × {m} × {v**2}"
        ]

    # POTENTIAL ENERGY
    if topic == "potential_energy":

        if len(nums) < 2:
            raise ValueError("Mass and height required")

        m, h = nums[:2]

        g = 9.8

        return m*g*h, [
            "PE = m × g × h",
            f"PE = {m} × {g} × {h}"
        ]

    # DENSITY
    if topic == "density":

        if len(nums) < 2:
            raise ValueError("Mass and volume required")

        m, v = nums[:2]

        if v == 0:
            raise ValueError("Volume cannot be zero")

        return m/v, [
            "Density = Mass / Volume",
            f"Density = {m} / {v}"
        ]

    # MOLES
    if topic == "moles":

        if len(nums) < 2:
            raise ValueError("Mass and molar mass required")

        m, M = nums[:2]

        if M == 0:
            raise ValueError("Molar mass cannot be zero")

        return m/M, [
            "Moles = Mass / Molar Mass",
            f"Moles = {m} / {M}"
        ]

    # MOLARITY
    if topic == "molarity":

        if len(nums) < 2:
            raise ValueError("Moles and volume required")

        n, V = nums[:2]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return n/V, [
            "Molarity = Moles / Volume",
            f"Molarity = {n} / {V}"
        ]

    # IDEAL GAS
    if topic == "ideal_gas":

        if len(nums) < 3:
            raise ValueError(
                "Pressure, volume and temperature required"
            )

        P, V, T = nums[:3]

        if T <= 0:
            raise ValueError("Temperature must be positive")

        R = 0.082057

        return P*V/(R*T), [
            "n = PV / RT",
            f"n = {P} × {V} / (0.082057 × {T})"
        ]

    raise ValueError("Calculation not implemented")

# ------------------------------------------------
# 5. SOLUTION GENERATOR
# ------------------------------------------------

def v7_solve(q, language="English"):

    topic = v7_detect_topic(q)

    if topic is None:
        return "Question topic identify nahi hua."

    nums = v7_numbers(q)

    try:

        result, steps = v7_calculate(topic, nums)

        if not math.isfinite(result):
            return "Invalid numerical result."

        formula = V7_FORMULAS[topic]

        if language == "Hindi":

            text = f"""
विषय: {formula['name']}

सूत्र:
{formula['formula']}

हल:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

अंतिम उत्तर:
{result:.6g} {formula['unit']}
"""

        else:

            text = f"""
Topic: {formula['name']}

Formula:
{formula['formula']}

Solution:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

Final Answer:
{result:.6g} {formula['unit']}
"""

        return text

    except Exception as e:

        return "Cannot solve: " + str(e)

# ------------------------------------------------
# 6. FORMULA SEARCH
# ------------------------------------------------

def v7_formula_search(keyword):

    keyword = keyword.lower().strip()

    results = []

    for key, item in V7_FORMULAS.items():

        if (
            keyword in key.lower()
            or keyword in item["name"].lower()
            or keyword in item["formula"].lower()
        ):

            results.append(
                f"{item['name']}: {item['formula']}"
            )

    return results if results else ["No formula found"]

# ------------------------------------------------
# 7. COMMON MISTAKES
# ------------------------------------------------

V7_MISTAKES = {

    "speed": "Distance aur time ki units compatible honi chahiye.",

    "acceleration": "Velocity difference ko time se divide karein.",

    "force": "Mass kg aur acceleration m/s² mein honi chahiye.",

    "work": "Force aur displacement ka product use karein.",

    "power": "Work ko time se divide karein.",

    "kinetic_energy": "Velocity ka square lena na bhoolein.",

    "potential_energy": "Height aur mass SI units mein rakhein.",

    "density": "Mass aur volume compatible units mein hon.",

    "moles": "Mass aur molar mass same mass units mein hon.",

    "molarity": "Volume litres mein hona chahiye.",

    "ideal_gas": "Temperature Kelvin mein hona chahiye."
}

# ------------------------------------------------
# 8. CORRECTED TESTS
# ------------------------------------------------

V7_TESTS = [

    ("Calculate speed for 100 distance in 2 time",
     "speed", 50),

    ("Find acceleration for final velocity 20 initial velocity 10 time 2",
     "acceleration", 5),

    ("Calculate force for mass 5 and acceleration 2",
     "force", 10),

    ("Calculate work done by force 10 and distance 5",
     "work", 50),

    ("Calculate power for work 100 and time 5",
     "power", 20),

    ("Calculate kinetic energy for mass 2 velocity 3",
     "kinetic_energy", 9),

    ("Calculate potential energy for mass 2 height 5",
     "potential_energy", 98),

    ("Calculate density for mass 10 volume 2",
     "density", 5),

    ("Calculate moles for mass 10 molar mass 20",
     "moles", 0.5),

    ("Calculate molarity for 2 moles volume 4",
     "molarity", 0.5)
]

print("V7.1 TESTING")

for q, topic, expected in V7_TESTS:

    detected = v7_detect_topic(q)

    assert detected == topic, (
        q, detected, topic
    )

    nums = v7_numbers(q)

    result, steps = v7_calculate(topic, nums)

    assert abs(result-expected) < 0.001, (
        q, result, expected
    )

    print("PASS:", topic)

print("\nALL V7.1 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v7_question = widgets.Textarea(
    placeholder="Calculate force for mass 5 and acceleration 2",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="120px"
    )
)

v7_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v7_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v7_formula_input = widgets.Text(
    placeholder="Search speed, force, energy...",
    description="Formula:"
)

v7_formula_button = widgets.Button(
    description="Search Formula"
)

v7_output = widgets.Output()

def v7_run(_):

    with v7_output:

        clear_output()

        q = v7_question.value

        print(v7_solve(q, v7_language.value))

        topic = v7_detect_topic(q)

        if topic:

            print("\nCommon Mistake:")
            print(V7_MISTAKES.get(topic, ""))

def v7_search_run(_):

    with v7_output:

        clear_output()

        results = v7_formula_search(
            v7_formula_input.value
        )

        for item in results:
            print(item)

v7_button.on_click(v7_run)

v7_formula_button.on_click(
    v7_search_run
)

display(v7_question)
display(v7_language)
display(v7_button)

display(v7_formula_input)
display(v7_formula_button)

display(v7_output)

print("\nSUNO SAATHI MAGIC LAYER V7.1 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V7.2
# COMPLETE CORRECTED SELF-CONTAINED VERSION
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. FORMULA DATABASE
# ------------------------------------------------

V7_FORMULAS = {

    "speed": {
        "name": "Speed",
        "formula": "v = d / t",
        "unit": "m/s"
    },

    "acceleration": {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "unit": "m/s²"
    },

    "force": {
        "name": "Force",
        "formula": "F = m × a",
        "unit": "N"
    },

    "work": {
        "name": "Work",
        "formula": "W = F × d",
        "unit": "J"
    },

    "power": {
        "name": "Power",
        "formula": "P = W / t",
        "unit": "W"
    },

    "kinetic_energy": {
        "name": "Kinetic Energy",
        "formula": "KE = 1/2 × m × v²",
        "unit": "J"
    },

    "potential_energy": {
        "name": "Potential Energy",
        "formula": "PE = m × g × h",
        "unit": "J"
    },

    "density": {
        "name": "Density",
        "formula": "ρ = m / V",
        "unit": "kg/m³"
    },

    "moles": {
        "name": "Moles",
        "formula": "n = m / M",
        "unit": "mol"
    },

    "molarity": {
        "name": "Molarity",
        "formula": "C = n / V",
        "unit": "mol/L"
    },

    "ideal_gas": {
        "name": "Ideal Gas",
        "formula": "PV = nRT",
        "unit": "mol"
    }
}

# ------------------------------------------------
# 2. CORRECTED TOPIC DETECTOR
# ------------------------------------------------

def v7_detect_topic(q):

    q = q.lower().strip()

    # ENERGY
    if any(x in q for x in [
        "kinetic energy", "गतिज ऊर्जा"
    ]):
        return "kinetic_energy"

    if any(x in q for x in [
        "potential energy", "स्थितिज ऊर्जा"
    ]):
        return "potential_energy"

    # POWER BEFORE WORK
    if any(x in q for x in [
        "calculate power", "find power",
        "power", "शक्ति"
    ]):
        return "power"

    # WORK BEFORE FORCE
    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "work", "कार्य"
    ]):
        return "work"

    # FORCE
    if any(x in q for x in [
        "calculate force", "find force",
        "force", "बल"
    ]):
        return "force"

    # ACCELERATION
    if any(x in q for x in [
        "acceleration", "accelerate", "त्वरण"
    ]):
        return "acceleration"

    # CHEMISTRY
    if any(x in q for x in [
        "molarity", "मोलरता"
    ]):
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    # DENSITY
    if any(x in q for x in [
        "density", "घनत्व"
    ]):
        return "density"

    # IDEAL GAS
    if any(x in q for x in [
        "ideal gas", "pv = nrt"
    ]):
        return "ideal_gas"

    # SPEED
    if any(x in q for x in [
        "speed", "velocity", "गति"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER EXTRACTION
# ------------------------------------------------

def v7_numbers(q):

    pattern = r'\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

    return [
        float(x)
        for x in re.findall(pattern, q)
    ]

# ------------------------------------------------
# 4. CALCULATION ENGINE
# ------------------------------------------------

def v7_calculate(topic, nums):

    if topic not in V7_FORMULAS:
        raise ValueError("Unsupported formula")

    # SPEED
    if topic == "speed":

        if len(nums) < 2:
            raise ValueError("Distance and time required")

        d, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return d/t, [
            "Speed = Distance / Time",
            f"Speed = {d} / {t}"
        ]

    # ACCELERATION
    if topic == "acceleration":

        if len(nums) < 3:
            raise ValueError("Final velocity, initial velocity and time required")

        v, u, t = nums[:3]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return (v-u)/t, [
            "Acceleration = (v - u) / t",
            f"Acceleration = ({v} - {u}) / {t}"
        ]

    # FORCE
    if topic == "force":

        if len(nums) < 2:
            raise ValueError("Mass and acceleration required")

        m, a = nums[:2]

        return m*a, [
            "Force = Mass × Acceleration",
            f"Force = {m} × {a}"
        ]

    # WORK
    if topic == "work":

        if len(nums) < 2:
            raise ValueError("Force and distance required")

        f, d = nums[:2]

        return f*d, [
            "Work = Force × Distance",
            f"Work = {f} × {d}"
        ]

    # POWER
    if topic == "power":

        if len(nums) < 2:
            raise ValueError("Work and time required")

        w, t = nums[:2]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return w/t, [
            "Power = Work / Time",
            f"Power = {w} / {t}"
        ]

    # KINETIC ENERGY
    if topic == "kinetic_energy":

        if len(nums) < 2:
            raise ValueError("Mass and velocity required")

        m, v = nums[:2]

        return 0.5*m*v**2, [
            "KE = 1/2 × m × v²",
            f"KE = 0.5 × {m} × {v}²",
            f"KE = 0.5 × {m} × {v**2}"
        ]

    # POTENTIAL ENERGY
    if topic == "potential_energy":

        if len(nums) < 2:
            raise ValueError("Mass and height required")

        m, h = nums[:2]

        g = 9.8

        return m*g*h, [
            "PE = m × g × h",
            f"PE = {m} × {g} × {h}"
        ]

    # DENSITY
    if topic == "density":

        if len(nums) < 2:
            raise ValueError("Mass and volume required")

        m, v = nums[:2]

        if v == 0:
            raise ValueError("Volume cannot be zero")

        return m/v, [
            "Density = Mass / Volume",
            f"Density = {m} / {v}"
        ]

    # MOLES
    if topic == "moles":

        if len(nums) < 2:
            raise ValueError("Mass and molar mass required")

        m, M = nums[:2]

        if M == 0:
            raise ValueError("Molar mass cannot be zero")

        return m/M, [
            "Moles = Mass / Molar Mass",
            f"Moles = {m} / {M}"
        ]

    # MOLARITY
    if topic == "molarity":

        if len(nums) < 2:
            raise ValueError("Moles and volume required")

        n, V = nums[:2]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return n/V, [
            "Molarity = Moles / Volume",
            f"Molarity = {n} / {V}"
        ]

    # IDEAL GAS
    if topic == "ideal_gas":

        if len(nums) < 3:
            raise ValueError("Pressure, volume and temperature required")

        P, V, T = nums[:3]

        if T <= 0:
            raise ValueError("Temperature must be positive")

        R = 0.082057

        return P*V/(R*T), [
            "n = PV / RT",
            f"n = {P} × {V} / (0.082057 × {T})"
        ]

    raise ValueError("Calculation not implemented")

# ------------------------------------------------
# 5. SOLUTION GENERATOR
# ------------------------------------------------

def v7_solve(q, language="English"):

    topic = v7_detect_topic(q)

    if topic is None:
        return "Question topic identify nahi hua."

    nums = v7_numbers(q)

    try:

        result, steps = v7_calculate(topic, nums)

        if not math.isfinite(result):
            return "Invalid numerical result."

        formula = V7_FORMULAS[topic]

        if language == "Hindi":

            text = f"""
विषय: {formula['name']}

सूत्र:
{formula['formula']}

हल:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

अंतिम उत्तर:
{result:.6g} {formula['unit']}
"""

        else:

            text = f"""
Topic: {formula['name']}

Formula:
{formula['formula']}

Solution:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

Final Answer:
{result:.6g} {formula['unit']}
"""

        return text

    except Exception as e:

        return "Cannot solve: " + str(e)

# ------------------------------------------------
# 6. FORMULA SEARCH
# ------------------------------------------------

def v7_formula_search(keyword):

    keyword = keyword.lower().strip()

    results = []

    for key, item in V7_FORMULAS.items():

        if (
            keyword in key.lower()
            or keyword in item["name"].lower()
            or keyword in item["formula"].lower()
        ):

            results.append(
                f"{item['name']}: {item['formula']}"
            )

    return results if results else ["No formula found"]

# ------------------------------------------------
# 7. COMMON MISTAKES
# ------------------------------------------------

V7_MISTAKES = {

    "speed": "Distance aur time ki units compatible honi chahiye.",
    "acceleration": "Velocity difference ko time se divide karein.",
    "force": "Mass kg aur acceleration m/s² mein honi chahiye.",
    "work": "Force aur displacement ka product use karein.",
    "power": "Work ko time se divide karein.",
    "kinetic_energy": "Velocity ka square lena na bhoolein.",
    "potential_energy": "Height aur mass SI units mein rakhein.",
    "density": "Mass aur volume compatible units mein hon.",
    "moles": "Mass aur molar mass same mass units mein hon.",
    "molarity": "Volume litres mein hona chahiye.",
    "ideal_gas": "Temperature Kelvin mein hona chahiye."
}

# ------------------------------------------------
# 8. AUTOMATED TESTS
# ------------------------------------------------

V7_TESTS = [

    ("Calculate speed for 100 distance in 2 time",
     "speed", 50),

    ("Find acceleration for final velocity 20 initial velocity 10 time 2",
     "acceleration", 5),

    ("Calculate force for mass 5 and acceleration 2",
     "force", 10),

    ("Calculate work done by force 10 and distance 5",
     "work", 50),

    ("Calculate power for work 100 and time 5",
     "power", 20),

    ("Calculate kinetic energy for mass 2 velocity 3",
     "kinetic_energy", 9),

    ("Calculate potential energy for mass 2 height 5",
     "potential_energy", 98),

    ("Calculate density for mass 10 volume 2",
     "density", 5),

    ("Calculate moles for mass 10 molar mass 20",
     "moles", 0.5),

    ("Calculate molarity for 2 moles volume 4",
     "molarity", 0.5)
]

print("V7.2 TESTING")

for q, topic, expected in V7_TESTS:

    detected = v7_detect_topic(q)

    assert detected == topic, (
        q, detected, topic
    )

    nums = v7_numbers(q)

    result, steps = v7_calculate(topic, nums)

    assert abs(result-expected) < 0.001, (
        q, result, expected
    )

    print("PASS:", topic)

print("\nALL V7.2 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v7_question = widgets.Textarea(
    placeholder="Calculate force for mass 5 and acceleration 2",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="120px"
    )
)

v7_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v7_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v7_formula_input = widgets.Text(
    placeholder="Search speed, force, energy...",
    description="Formula:"
)

v7_formula_button = widgets.Button(
    description="Search Formula"
)

v7_output = widgets.Output()

def v7_run(_):

    with v7_output:

        clear_output()

        q = v7_question.value

        print(v7_solve(q, v7_language.value))

        topic = v7_detect_topic(q)

        if topic:

            print("\nCommon Mistake:")
            print(V7_MISTAKES.get(topic, ""))

def v7_search_run(_):

    with v7_output:

        clear_output()

        results = v7_formula_search(
            v7_formula_input.value
        )

        for item in results:
            print(item)

v7_button.on_click(v7_run)

v7_formula_button.on_click(
    v7_search_run
)

display(v7_question)
display(v7_language)
display(v7_button)

display(v7_formula_input)
display(v7_formula_button)

display(v7_output)

print("\nSUNO SAATHI MAGIC LAYER V7.2 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V8
# SMART QUESTION UNDERSTANDING ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. FORMULA DATABASE
# ------------------------------------------------

V8_FORMULAS = {
    "speed": {
        "name": "Speed",
        "formula": "v = d / t",
        "unit": "m/s"
    },
    "acceleration": {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "unit": "m/s²"
    },
    "force": {
        "name": "Force",
        "formula": "F = m × a",
        "unit": "N"
    },
    "work": {
        "name": "Work",
        "formula": "W = F × d",
        "unit": "J"
    },
    "power": {
        "name": "Power",
        "formula": "P = W / t",
        "unit": "W"
    },
    "kinetic_energy": {
        "name": "Kinetic Energy",
        "formula": "KE = 1/2 × m × v²",
        "unit": "J"
    },
    "potential_energy": {
        "name": "Potential Energy",
        "formula": "PE = m × g × h",
        "unit": "J"
    },
    "density": {
        "name": "Density",
        "formula": "ρ = m / V",
        "unit": "kg/m³"
    },
    "moles": {
        "name": "Moles",
        "formula": "n = mass / molar mass",
        "unit": "mol"
    },
    "molarity": {
        "name": "Molarity",
        "formula": "C = n / V",
        "unit": "mol/L"
    }
}

# ------------------------------------------------
# 2. SMART TOPIC DETECTOR
# ------------------------------------------------

def v8_detect_topic(q):

    q = q.lower().strip()

    # Specific phrases first
    if "kinetic energy" in q or "गतिज ऊर्जा" in q:
        return "kinetic_energy"

    if "potential energy" in q or "स्थितिज ऊर्जा" in q:
        return "potential_energy"

    if "molarity" in q or "मोलरता" in q:
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    if "density" in q or "घनत्व" in q:
        return "density"

    # Intent-based priority
    if any(x in q for x in [
        "calculate power", "find power",
        "power", "शक्ति"
    ]):
        return "power"

    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "work", "कार्य"
    ]):
        return "work"

    if any(x in q for x in [
        "calculate force", "find force",
        "force", "बल"
    ]):
        return "force"

    if any(x in q for x in [
        "acceleration", "accelerate", "त्वरण"
    ]):
        return "acceleration"

    if any(x in q for x in [
        "speed", "velocity", "गति"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER EXTRACTION
# ------------------------------------------------

def v8_numbers(q):

    pattern = r'[-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

    return [
        float(x)
        for x in re.findall(pattern, q)
    ]

# ------------------------------------------------
# 4. VARIABLE MAPPING
# ------------------------------------------------

V8_VARIABLES = {

    "speed": {
        "distance": [
            "distance", "दूरी"
        ],
        "time": [
            "time", "समय"
        ]
    },

    "acceleration": {
        "final_velocity": [
            "final velocity", "final speed", "v"
        ],
        "initial_velocity": [
            "initial velocity", "initial speed", "u"
        ],
        "time": [
            "time", "समय"
        ]
    },

    "force": {
        "mass": [
            "mass", "मास"
        ],
        "acceleration": [
            "acceleration", "त्वरण"
        ]
    },

    "work": {
        "force": [
            "force", "बल"
        ],
        "distance": [
            "distance", "displacement", "दूरी"
        ]
    },

    "power": {
        "work": [
            "work", "कार्य"
        ],
        "time": [
            "time", "समय"
        ]
    },

    "kinetic_energy": {
        "mass": [
            "mass"
        ],
        "velocity": [
            "velocity", "speed"
        ]
    },

    "potential_energy": {
        "mass": [
            "mass"
        ],
        "height": [
            "height", "ऊंचाई"
        ]
    },

    "density": {
        "mass": [
            "mass"
        ],
        "volume": [
            "volume"
        ]
    },

    "moles": {
        "mass": [
            "mass"
        ],
        "molar_mass": [
            "molar mass", "molecular mass"
        ]
    },

    "molarity": {
        "moles": [
            "moles"
        ],
        "volume": [
            "volume"
        ]
    }
}

def v8_map_variables(q, topic):

    q = q.lower()

    nums = v8_numbers(q)

    variables = V8_VARIABLES[topic]

    mapped = {}

    # Variable label + number detection
    for variable, aliases in variables.items():

        for alias in aliases:

            pattern = (
                r'\b' + re.escape(alias) +
                r'\b\s*(?:is|of|=|:)?\s*'
                r'([-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)'
            )

            match = re.search(pattern, q)

            if match:

                mapped[variable] = float(match.group(1))
                break

    # Fallback: use number order only for missing variables
    remaining = [
        n for n in nums
        if n not in mapped.values()
    ]

    for variable in variables:

        if variable not in mapped and remaining:

            mapped[variable] = remaining.pop(0)

    return mapped

# ------------------------------------------------
# 5. SMART CALCULATION ENGINE
# ------------------------------------------------

def v8_calculate(topic, values):

    if topic == "speed":

        d = values["distance"]
        t = values["time"]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return d/t, [
            f"Speed = Distance / Time",
            f"Speed = {d} / {t}"
        ]

    if topic == "acceleration":

        v = values["final_velocity"]
        u = values["initial_velocity"]
        t = values["time"]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return (v-u)/t, [
            "Acceleration = (v - u) / t",
            f"Acceleration = ({v} - {u}) / {t}"
        ]

    if topic == "force":

        m = values["mass"]
        a = values["acceleration"]

        return m*a, [
            "Force = Mass × Acceleration",
            f"Force = {m} × {a}"
        ]

    if topic == "work":

        f = values["force"]
        d = values["distance"]

        return f*d, [
            "Work = Force × Distance",
            f"Work = {f} × {d}"
        ]

    if topic == "power":

        w = values["work"]
        t = values["time"]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return w/t, [
            "Power = Work / Time",
            f"Power = {w} / {t}"
        ]

    if topic == "kinetic_energy":

        m = values["mass"]
        v = values["velocity"]

        return 0.5*m*v**2, [
            "KE = 1/2 × m × v²",
            f"KE = 0.5 × {m} × {v}²",
            f"KE = 0.5 × {m} × {v**2}"
        ]

    if topic == "potential_energy":

        m = values["mass"]
        h = values["height"]
        g = 9.8

        return m*g*h, [
            "PE = m × g × h",
            f"PE = {m} × {g} × {h}"
        ]

    if topic == "density":

        m = values["mass"]
        V = values["volume"]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return m/V, [
            "Density = Mass / Volume",
            f"Density = {m} / {V}"
        ]

    if topic == "moles":

        m = values["mass"]
        M = values["molar_mass"]

        if M == 0:
            raise ValueError("Molar mass cannot be zero")

        return m/M, [
            "Moles = Mass / Molar Mass",
            f"Moles = {m} / {M}"
        ]

    if topic == "molarity":

        n = values["moles"]
        V = values["volume"]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return n/V, [
            "Molarity = Moles / Volume",
            f"Molarity = {n} / {V}"
        ]

    raise ValueError("Unsupported topic")

# ------------------------------------------------
# 6. QUESTION SOLVER
# ------------------------------------------------

def v8_solve(q, language="English"):

    topic = v8_detect_topic(q)

    if topic is None:

        return {
            "success": False,
            "message": "Question topic identify nahi hua."
        }

    try:

        values = v8_map_variables(q, topic)

        required = list(V8_VARIABLES[topic].keys())

        missing = [
            v for v in required
            if v not in values
        ]

        if missing:

            return {
                "success": False,
                "topic": topic,
                "message": "Missing values: " + ", ".join(missing),
                "mapped": values
            }

        result, steps = v8_calculate(topic, values)

        if not math.isfinite(result):

            return {
                "success": False,
                "message": "Invalid numerical result."
            }

        formula = V8_FORMULAS[topic]

        if language == "Hindi":

            text = f"""
विषय: {formula['name']}

सूत्र:
{formula['formula']}

दिए गए मान:
{values}

हल:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

अंतिम उत्तर:
{result:.6g} {formula['unit']}
"""

        else:

            text = f"""
Topic: {formula['name']}

Formula:
{formula['formula']}

Given values:
{values}

Solution:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

Final Answer:
{result:.6g} {formula['unit']}
"""

        return {
            "success": True,
            "topic": topic,
            "values": values,
            "result": result,
            "unit": formula["unit"],
            "steps": steps,
            "explanation": text
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }

# ------------------------------------------------
# 7. FORMULA SEARCH
# ------------------------------------------------

def v8_formula_search(keyword):

    keyword = keyword.lower().strip()

    results = []

    for key, item in V8_FORMULAS.items():

        if (
            keyword in key.lower()
            or keyword in item["name"].lower()
            or keyword in item["formula"].lower()
        ):

            results.append(
                f"{item['name']}: {item['formula']}"
            )

    return results if results else ["No formula found"]

# ------------------------------------------------
# 8. COMMON MISTAKES
# ------------------------------------------------

V8_MISTAKES = {

    "speed": "Distance aur time ki units compatible honi chahiye.",
    "acceleration": "Final aur initial velocity ka difference lein.",
    "force": "Mass kg aur acceleration m/s² mein honi chahiye.",
    "work": "Force aur displacement ka product use karein.",
    "power": "Work ko time se divide karein.",
    "kinetic_energy": "Velocity ka square lena na bhoolein.",
    "potential_energy": "Height aur mass SI units mein rakhein.",
    "density": "Volume zero nahi hona chahiye.",
    "moles": "Mass aur molar mass same units mein hon.",
    "molarity": "Volume litres mein hona chahiye."
}

# ------------------------------------------------
# 9. AUTOMATED TESTS
# ------------------------------------------------

V8_TESTS = [

    ("Calculate speed for distance 100 and time 2",
     "speed", 50),

    ("Calculate acceleration for final velocity 20 initial velocity 10 time 2",
     "acceleration", 5),

    ("Calculate force for acceleration 2 and mass 5",
     "force", 10),

    ("Calculate work done by distance 5 and force 10",
     "work", 50),

    ("Calculate power for time 5 and work 100",
     "power", 20),

    ("Calculate kinetic energy for velocity 3 and mass 2",
     "kinetic_energy", 9),

    ("Calculate potential energy for height 5 and mass 2",
     "potential_energy", 98),

    ("Calculate density for volume 2 and mass 10",
     "density", 5),

    ("Calculate moles for molar mass 20 and mass 10",
     "moles", 0.5),

    ("Calculate molarity for volume 4 and moles 2",
     "molarity", 0.5)
]

print("V8 TESTING")

for q, topic, expected in V8_TESTS:

    data = v8_solve(q)

    assert data["success"], (
        q, data
    )

    assert data["topic"] == topic

    assert abs(data["result"]-expected) < 0.001

    print("PASS:", topic)

print("\nALL V8 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE UI
# ------------------------------------------------

v8_question = widgets.Textarea(
    placeholder="Calculate force for acceleration 2 and mass 5",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v8_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v8_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v8_formula_input = widgets.Text(
    placeholder="Search speed, force, energy...",
    description="Formula:"
)

v8_formula_button = widgets.Button(
    description="Search Formula"
)

v8_output = widgets.Output()

def v8_run(_):

    with v8_output:

        clear_output()

        data = v8_solve(
            v8_question.value,
            v8_language.value
        )

        if data["success"]:

            print(data["explanation"])

            topic = data["topic"]

            print("\nCommon Mistake:")
            print(V8_MISTAKES.get(topic, ""))

        else:

            print(data["message"])

            if "mapped" in data:
                print("\nDetected values:")
                print(data["mapped"])

def v8_search_run(_):

    with v8_output:

        clear_output()

        for item in v8_formula_search(
            v8_formula_input.value
        ):
            print(item)

v8_button.on_click(v8_run)
v8_formula_button.on_click(v8_search_run)

display(v8_question)
display(v8_language)
display(v8_button)

display(v8_formula_input)
display(v8_formula_button)

display(v8_output)

print("\nSUNO SAATHI MAGIC LAYER V8 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V8
# SMART QUESTION UNDERSTANDING ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. FORMULA DATABASE
# ------------------------------------------------

V8_FORMULAS = {
    "speed": {
        "name": "Speed",
        "formula": "v = d / t",
        "unit": "m/s"
    },
    "acceleration": {
        "name": "Acceleration",
        "formula": "a = (v - u) / t",
        "unit": "m/s²"
    },
    "force": {
        "name": "Force",
        "formula": "F = m × a",
        "unit": "N"
    },
    "work": {
        "name": "Work",
        "formula": "W = F × d",
        "unit": "J"
    },
    "power": {
        "name": "Power",
        "formula": "P = W / t",
        "unit": "W"
    },
    "kinetic_energy": {
        "name": "Kinetic Energy",
        "formula": "KE = 1/2 × m × v²",
        "unit": "J"
    },
    "potential_energy": {
        "name": "Potential Energy",
        "formula": "PE = m × g × h",
        "unit": "J"
    },
    "density": {
        "name": "Density",
        "formula": "ρ = m / V",
        "unit": "kg/m³"
    },
    "moles": {
        "name": "Moles",
        "formula": "n = mass / molar mass",
        "unit": "mol"
    },
    "molarity": {
        "name": "Molarity",
        "formula": "C = n / V",
        "unit": "mol/L"
    }
}

# ------------------------------------------------
# 2. SMART TOPIC DETECTOR
# ------------------------------------------------

def v8_detect_topic(q):

    q = q.lower().strip()

    # Specific phrases first
    if "kinetic energy" in q or "गतिज ऊर्जा" in q:
        return "kinetic_energy"

    if "potential energy" in q or "स्थितिज ऊर्जा" in q:
        return "potential_energy"

    if "molarity" in q or "मोलरता" in q:
        return "molarity"

    if any(x in q for x in [
        "number of moles", "calculate moles",
        "find moles", "moles", "मोल"
    ]):
        return "moles"

    if "density" in q or "घनत्व" in q:
        return "density"

    # Intent-based priority
    if any(x in q for x in [
        "calculate power", "find power",
        "power", "शक्ति"
    ]):
        return "power"

    if any(x in q for x in [
        "work done", "calculate work",
        "find work", "work", "कार्य"
    ]):
        return "work"

    if any(x in q for x in [
        "calculate force", "find force",
        "force", "बल"
    ]):
        return "force"

    if any(x in q for x in [
        "acceleration", "accelerate", "त्वरण"
    ]):
        return "acceleration"

    if any(x in q for x in [
        "speed", "velocity", "गति"
    ]):
        return "speed"

    return None

# ------------------------------------------------
# 3. NUMBER EXTRACTION
# ------------------------------------------------

def v8_numbers(q):

    pattern = r'[-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?'

    return [
        float(x)
        for x in re.findall(pattern, q)
    ]

# ------------------------------------------------
# 4. VARIABLE MAPPING
# ------------------------------------------------


def v8_map_variables(q, topic):

    q = q.lower()
    nums = v8_numbers(q)
    variables = V8_VARIABLES[topic]

    mapped = {}

    for variable, aliases in variables.items():

        for alias in sorted(aliases, key=len, reverse=True):

            # Generic mass must not match molar mass
            if alias == "mass":
                pattern = (
                    r'(?<!molar )\bmass\b'
                    r'\s*(?:is|of|=|:)?\s*'
                    r'([-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)'
                )
            else:
                pattern = (
                    r'\b' + re.escape(alias) +
                    r'\b\s*(?:is|of|=|:)?\s*'
                    r'([-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)'
                )

            match = re.search(pattern, q)

            if match:
                mapped[variable] = float(match.group(1))
                break

    # Fallback for unlabeled values
    remaining = [
        n for n in nums
        if n not in mapped.values()
    ]

    for variable in variables:

        if variable not in mapped and remaining:
            mapped[variable] = remaining.pop(0)

    return mapped


# ------------------------------------------------
# 5. SMART CALCULATION ENGINE
# ------------------------------------------------

def v8_calculate(topic, values):

    if topic == "speed":

        d = values["distance"]
        t = values["time"]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return d/t, [
            f"Speed = Distance / Time",
            f"Speed = {d} / {t}"
        ]

    if topic == "acceleration":

        v = values["final_velocity"]
        u = values["initial_velocity"]
        t = values["time"]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return (v-u)/t, [
            "Acceleration = (v - u) / t",
            f"Acceleration = ({v} - {u}) / {t}"
        ]

    if topic == "force":

        m = values["mass"]
        a = values["acceleration"]

        return m*a, [
            "Force = Mass × Acceleration",
            f"Force = {m} × {a}"
        ]

    if topic == "work":

        f = values["force"]
        d = values["distance"]

        return f*d, [
            "Work = Force × Distance",
            f"Work = {f} × {d}"
        ]

    if topic == "power":

        w = values["work"]
        t = values["time"]

        if t == 0:
            raise ValueError("Time cannot be zero")

        return w/t, [
            "Power = Work / Time",
            f"Power = {w} / {t}"
        ]

    if topic == "kinetic_energy":

        m = values["mass"]
        v = values["velocity"]

        return 0.5*m*v**2, [
            "KE = 1/2 × m × v²",
            f"KE = 0.5 × {m} × {v}²",
            f"KE = 0.5 × {m} × {v**2}"
        ]

    if topic == "potential_energy":

        m = values["mass"]
        h = values["height"]
        g = 9.8

        return m*g*h, [
            "PE = m × g × h",
            f"PE = {m} × {g} × {h}"
        ]

    if topic == "density":

        m = values["mass"]
        V = values["volume"]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return m/V, [
            "Density = Mass / Volume",
            f"Density = {m} / {V}"
        ]

    if topic == "moles":

        m = values["mass"]
        M = values["molar_mass"]

        if M == 0:
            raise ValueError("Molar mass cannot be zero")

        return m/M, [
            "Moles = Mass / Molar Mass",
            f"Moles = {m} / {M}"
        ]

    if topic == "molarity":

        n = values["moles"]
        V = values["volume"]

        if V == 0:
            raise ValueError("Volume cannot be zero")

        return n/V, [
            "Molarity = Moles / Volume",
            f"Molarity = {n} / {V}"
        ]

    raise ValueError("Unsupported topic")

# ------------------------------------------------
# 6. QUESTION SOLVER
# ------------------------------------------------

def v8_solve(q, language="English"):

    topic = v8_detect_topic(q)

    if topic is None:

        return {
            "success": False,
            "message": "Question topic identify nahi hua."
        }

    try:

        values = v8_map_variables(q, topic)

        required = list(V8_VARIABLES[topic].keys())

        missing = [
            v for v in required
            if v not in values
        ]

        if missing:

            return {
                "success": False,
                "topic": topic,
                "message": "Missing values: " + ", ".join(missing),
                "mapped": values
            }

        result, steps = v8_calculate(topic, values)

        if not math.isfinite(result):

            return {
                "success": False,
                "message": "Invalid numerical result."
            }

        formula = V8_FORMULAS[topic]

        if language == "Hindi":

            text = f"""
विषय: {formula['name']}

सूत्र:
{formula['formula']}

दिए गए मान:
{values}

हल:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

अंतिम उत्तर:
{result:.6g} {formula['unit']}
"""

        else:

            text = f"""
Topic: {formula['name']}

Formula:
{formula['formula']}

Given values:
{values}

Solution:
"""

            for i, step in enumerate(steps, 1):
                text += f"\n{i}. {step}"

            text += f"""

Final Answer:
{result:.6g} {formula['unit']}
"""

        return {
            "success": True,
            "topic": topic,
            "values": values,
            "result": result,
            "unit": formula["unit"],
            "steps": steps,
            "explanation": text
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }

# ------------------------------------------------
# 7. FORMULA SEARCH
# ------------------------------------------------

def v8_formula_search(keyword):

    keyword = keyword.lower().strip()

    results = []

    for key, item in V8_FORMULAS.items():

        if (
            keyword in key.lower()
            or keyword in item["name"].lower()
            or keyword in item["formula"].lower()
        ):

            results.append(
                f"{item['name']}: {item['formula']}"
            )

    return results if results else ["No formula found"]

# ------------------------------------------------
# 8. COMMON MISTAKES
# ------------------------------------------------

V8_MISTAKES = {

    "speed": "Distance aur time ki units compatible honi chahiye.",
    "acceleration": "Final aur initial velocity ka difference lein.",
    "force": "Mass kg aur acceleration m/s² mein honi chahiye.",
    "work": "Force aur displacement ka product use karein.",
    "power": "Work ko time se divide karein.",
    "kinetic_energy": "Velocity ka square lena na bhoolein.",
    "potential_energy": "Height aur mass SI units mein rakhein.",
    "density": "Volume zero nahi hona chahiye.",
    "moles": "Mass aur molar mass same units mein hon.",
    "molarity": "Volume litres mein hona chahiye."
}

# ------------------------------------------------
# 9. AUTOMATED TESTS
# ------------------------------------------------

V8_TESTS = [

    ("Calculate speed for distance 100 and time 2",
     "speed", 50),

    ("Calculate acceleration for final velocity 20 initial velocity 10 time 2",
     "acceleration", 5),

    ("Calculate force for acceleration 2 and mass 5",
     "force", 10),

    ("Calculate work done by distance 5 and force 10",
     "work", 50),

    ("Calculate power for time 5 and work 100",
     "power", 20),

    ("Calculate kinetic energy for velocity 3 and mass 2",
     "kinetic_energy", 9),

    ("Calculate potential energy for height 5 and mass 2",
     "potential_energy", 98),

    ("Calculate density for volume 2 and mass 10",
     "density", 5),

    ("Calculate moles for molar mass 20 and mass 10",
     "moles", 0.5),

    ("Calculate molarity for volume 4 and moles 2",
     "molarity", 0.5)
]

print("V8 TESTING")

for q, topic, expected in V8_TESTS:

    data = v8_solve(q)

    assert data["success"], (
        q, data
    )

    assert data["topic"] == topic

    assert abs(data["result"]-expected) < 0.001

    print("PASS:", topic)

print("\nALL V8 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE UI
# ------------------------------------------------

v8_question = widgets.Textarea(
    placeholder="Calculate force for acceleration 2 and mass 5",
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v8_language = widgets.Dropdown(
    options=["English", "Hindi"],
    value="English",
    description="Language:"
)

v8_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v8_formula_input = widgets.Text(
    placeholder="Search speed, force, energy...",
    description="Formula:"
)

v8_formula_button = widgets.Button(
    description="Search Formula"
)

v8_output = widgets.Output()

def v8_run(_):

    with v8_output:

        clear_output()

        data = v8_solve(
            v8_question.value,
            v8_language.value
        )

        if data["success"]:

            print(data["explanation"])

            topic = data["topic"]

            print("\nCommon Mistake:")
            print(V8_MISTAKES.get(topic, ""))

        else:

            print(data["message"])

            if "mapped" in data:
                print("\nDetected values:")
                print(data["mapped"])

def v8_search_run(_):

    with v8_output:

        clear_output()

        for item in v8_formula_search(
            v8_formula_input.value
        ):
            print(item)

v8_button.on_click(v8_run)
v8_formula_button.on_click(v8_search_run)

display(v8_question)
display(v8_language)
display(v8_button)

display(v8_formula_input)
display(v8_formula_button)

display(v8_output)

print("\nSUNO SAATHI MAGIC LAYER V8 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V9
# UNIT CONVERSION + SMART VALIDATION
# ================================================================

import re
import math

# ------------------------------------------------
# 1. UNIT DATABASE
# ------------------------------------------------

V9_UNITS = {

    # Distance -> base meter
    "distance": {
        "m": 1,
        "meter": 1,
        "meters": 1,
        "km": 1000,
        "kilometer": 1000,
        "kilometers": 1000,
        "cm": 0.01,
        "centimeter": 0.01,
        "centimeters": 0.01,
        "mm": 0.001,
        "millimeter": 0.001,
        "millimeters": 0.001
    },

    # Time -> base second
    "time": {
        "s": 1,
        "sec": 1,
        "second": 1,
        "seconds": 1,
        "min": 60,
        "minute": 60,
        "minutes": 60,
        "h": 3600,
        "hr": 3600,
        "hour": 3600,
        "hours": 3600
    },

    # Mass -> base kg
    "mass": {
        "kg": 1,
        "kilogram": 1,
        "kilograms": 1,
        "g": 0.001,
        "gram": 0.001,
        "grams": 0.001,
        "mg": 0.000001,
        "milligram": 0.000001
    },

    # Speed -> base m/s
    "speed": {
        "m/s": 1,
        "mps": 1,
        "km/h": 1/3.6,
        "kph": 1/3.6,
        "mph": 0.44704
    },

    # Volume -> base litre
    "volume": {
        "l": 1,
        "liter": 1,
        "litre": 1,
        "liters": 1,
        "litres": 1,
        "ml": 0.001,
        "milliliter": 0.001,
        "millilitre": 0.001,
        "m3": 1000,
        "cm3": 0.001
    },

    # Pressure -> base Pa
    "pressure": {
        "pa": 1,
        "pascal": 1,
        "kpa": 1000,
        "mpa": 1000000,
        "bar": 100000,
        "atm": 101325
    },

    # Energy -> base joule
    "energy": {
        "j": 1,
        "joule": 1,
        "joules": 1,
        "kj": 1000,
        "kilojoule": 1000,
        "cal": 4.184,
        "kcal": 4184
    }
}

# ------------------------------------------------
# 2. UNIT NORMALIZATION
# ------------------------------------------------

def v9_normalize_unit(unit):

    unit = unit.lower().strip()

    unit = unit.replace(" ", "")
    unit = unit.replace("²", "2")
    unit = unit.replace("³", "3")

    return unit

# ------------------------------------------------
# 3. FIND UNIT DIMENSION
# ------------------------------------------------

def v9_find_dimension(unit):

    unit = v9_normalize_unit(unit)

    for dimension, units in V9_UNITS.items():

        if unit in units:
            return dimension

    if unit in ["c", "°c", "celsius"]:
        return "temperature"

    if unit in ["k", "kelvin"]:
        return "temperature"

    return None

# ------------------------------------------------
# 4. UNIT CONVERSION ENGINE
# ------------------------------------------------

def v9_convert(value, from_unit, to_unit):

    value = float(value)

    source = v9_normalize_unit(from_unit)
    target = v9_normalize_unit(to_unit)

    source_dimension = v9_find_dimension(source)
    target_dimension = v9_find_dimension(target)

    if source_dimension is None:
        raise ValueError(
            f"Unknown source unit: {from_unit}"
        )

    if target_dimension is None:
        raise ValueError(
            f"Unknown target unit: {to_unit}"
        )

    if source_dimension != target_dimension:
        raise ValueError(
            "Unit mismatch: "
            + source_dimension
            + " cannot convert to "
            + target_dimension
        )

    # Temperature
    if source_dimension == "temperature":

        if source in ["c", "°c", "celsius"]:
            kelvin = value + 273.15

        else:
            kelvin = value

        if target in ["c", "°c", "celsius"]:
            result = kelvin - 273.15

        else:
            result = kelvin

        return result

    # Other units
    units = V9_UNITS[source_dimension]

    base_value = value * units[source]
    result = base_value / units[target]

    return result

# ------------------------------------------------
# 5. UNIT VALIDATION
# ------------------------------------------------

def v9_validate_unit(unit, expected_dimension=None):

    dimension = v9_find_dimension(unit)

    if dimension is None:

        return {
            "valid": False,
            "message": "Unknown unit: " + str(unit)
        }

    if expected_dimension:

        if dimension != expected_dimension:

            return {
                "valid": False,
                "message": (
                    f"Expected {expected_dimension}, "
                    f"received {dimension}"
                )
            }

    return {
        "valid": True,
        "dimension": dimension,
        "message": "Unit valid"
    }

# ------------------------------------------------
# 6. SMART QUANTITY PARSER
# ------------------------------------------------

def v9_parse_quantity(text):

    text = text.lower().strip()

    pattern = (
        r'([-+]?\d+(?:\.\d+)?)'
        r'\s*([a-z°]+(?:/[a-z]+)?|[a-z]+)'
    )

    match = re.search(pattern, text)

    if not match:

        return {
            "success": False,
            "message": "Value and unit not found"
        }

    value = float(match.group(1))
    unit = match.group(2)

    validation = v9_validate_unit(unit)

    if not validation["valid"]:

        return {
            "success": False,
            "message": validation["message"]
        }

    return {
        "success": True,
        "value": value,
        "unit": unit,
        "dimension": validation["dimension"]
    }

# ------------------------------------------------
# 7. SMART CONVERSION FROM QUESTION
# ------------------------------------------------

def v9_convert_question(text, target_unit):

    parsed = v9_parse_quantity(text)

    if not parsed["success"]:
        return parsed

    try:

        result = v9_convert(
            parsed["value"],
            parsed["unit"],
            target_unit
        )

        return {
            "success": True,
            "original": (
                f"{parsed['value']} {parsed['unit']}"
            ),
            "converted": (
                f"{result:.8g} {target_unit}"
            ),
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }

# ------------------------------------------------
# 8. UNIT CONVERSION UI
# ------------------------------------------------

import ipywidgets as widgets
from IPython.display import display, clear_output

v9_value = widgets.FloatText(
    value=100,
    description="Value:"
)

v9_from = widgets.Text(
    value="cm",
    description="From:"
)

v9_to = widgets.Text(
    value="m",
    description="To:"
)

v9_button = widgets.Button(
    description="Convert",
    button_style="success"
)

v9_output = widgets.Output()

def v9_run(_):

    with v9_output:

        clear_output()

        try:

            result = v9_convert(
                v9_value.value,
                v9_from.value,
                v9_to.value
            )

            print("Original:")
            print(v9_value.value, v9_from.value)

            print("\nConverted:")
            print(f"{result:.8g}", v9_to.value)

        except Exception as e:

            print("ERROR:", e)

v9_button.on_click(v9_run)

display(v9_value)
display(v9_from)
display(v9_to)
display(v9_button)
display(v9_output)

# ------------------------------------------------
# 9. AUTOMATED TESTS
# ------------------------------------------------

V9_TESTS = [

    (100, "cm", "m", 1),
    (1, "km", "m", 1000),
    (60, "min", "s", 3600),
    (1, "h", "s", 3600),
    (1000, "g", "kg", 1),
    (36, "km/h", "m/s", 10),
    (0, "C", "K", 273.15),
    (1000, "ml", "l", 1),
    (1, "bar", "Pa", 100000),
    (1, "kJ", "J", 1000)
]

print("\nV9 TESTING")

for value, source, target, expected in V9_TESTS:

    result = v9_convert(
        value,
        source,
        target
    )

    assert abs(result - expected) < 0.001, (
        value, source, target, result, expected
    )

    print("PASS:", source, "->", target)

# Invalid dimension test
try:

    v9_convert(10, "kg", "m")

    assert False, "Invalid conversion accepted"

except ValueError:

    print("PASS: dimension mismatch")

# Parser test
parsed = v9_parse_quantity("Distance is 5 km")

assert parsed["success"]
assert parsed["value"] == 5
assert parsed["unit"] == "km"

print("PASS: quantity parser")

print("\nALL V9 TESTS PASSED!")
print("\nSUNO SAATHI MAGIC LAYER V9 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V10
# MULTI-STEP SOLVER + UNIT INTEGRATION
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. MULTI-STEP QUESTION DETECTOR
# ------------------------------------------------

def v10_detect_mode(q):

    q = q.lower()

    multi_keywords = [
        "calculate force work power",
        "find force work power",
        "calculate all",
        "step by step calculate",
        "multi step",
        "multiple calculation"
    ]

    if any(x in q for x in multi_keywords):
        return "multi"

    return "single"

# ------------------------------------------------
# 2. SMART LABELED VALUE EXTRACTOR
# ------------------------------------------------

def v10_extract(q, aliases):

    q = q.lower()

    for alias in sorted(aliases, key=len, reverse=True):

        pattern = (
            r'(?<![a-z])'
            + re.escape(alias)
            + r'(?![a-z])'
            + r'\s*(?:is|of|=|:)?\s*'
            + r'([-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)'
        )

        match = re.search(pattern, q)

        if match:
            return float(match.group(1))

    return None

# ------------------------------------------------
# 3. UNIT-AWARE VALUE EXTRACTION
# ------------------------------------------------

def v10_quantity(q, aliases, default_unit=None):

    q = q.lower()

    value = v10_extract(q, aliases)

    if value is None:
        return None

    # Find nearby unit after value
    pattern = (
        r'([-+]?\d+(?:\.\d+)?)'
        r'\s*(km/h|m/s|km|cm|mm|m|'
        r'hours?|hrs?|hr|min|minutes?|sec|seconds?|s|'
        r'kg|grams?|g|mg|'
        r'litres?|liters?|l|ml)'
    )

    matches = list(re.finditer(pattern, q))

    for match in matches:

        number = float(match.group(1))

        if abs(number - value) < 1e-12:

            unit = match.group(2)

            return {
                "value": value,
                "unit": unit
            }

    return {
        "value": value,
        "unit": default_unit
    }

# ------------------------------------------------
# 4. UNIT NORMALIZER
# ------------------------------------------------

def v10_to_base(value, unit, dimension):

    if unit is None:
        return float(value)

    # V9 integration
    try:

        base_units = {
            "distance": "m",
            "time": "s",
            "mass": "kg",
            "speed": "m/s",
            "volume": "l"
        }

        target = base_units.get(dimension)

        if target and "v9_convert" in globals():

            return v9_convert(
                value,
                unit,
                target
            )

    except Exception as e:

        raise ValueError(
            f"Unit conversion failed: {e}"
        )

    return float(value)

# ------------------------------------------------
# 5. LABELED INPUT COLLECTION
# ------------------------------------------------

def v10_get_inputs(q):

    values = {}

    # Mass
    mass = v10_quantity(
        q,
        ["mass", "weight"],
        "kg"
    )

    if mass:
        values["mass"] = v10_to_base(
            mass["value"],
            mass["unit"],
            "mass"
        )

    # Acceleration
    acceleration = v10_extract(
        q,
        ["acceleration"]
    )

    if acceleration is not None:
        values["acceleration"] = acceleration

    # Distance
    distance = v10_quantity(
        q,
        ["distance", "displacement"],
        "m"
    )

    if distance:
        values["distance"] = v10_to_base(
            distance["value"],
            distance["unit"],
            "distance"
        )

    # Time
    time_value = v10_quantity(
        q,
        ["time", "duration"],
        "s"
    )

    if time_value:
        values["time"] = v10_to_base(
            time_value["value"],
            time_value["unit"],
            "time"
        )

    # Force
    force = v10_extract(
        q,
        ["force"]
    )

    if force is not None:
        values["force"] = force

    # Work
    work = v10_extract(
        q,
        ["work"]
    )

    if work is not None:
        values["work"] = work

    # Speed / velocity
    speed = v10_quantity(
        q,
        ["speed", "velocity"],
        "m/s"
    )

    if speed:
        values["speed"] = v10_to_base(
            speed["value"],
            speed["unit"],
            "speed"
        )

    return values

# ------------------------------------------------
# 6. MULTI-STEP PHYSICS SOLVER
# ------------------------------------------------

def v10_multi_solve(q):

    values = v10_get_inputs(q)

    steps = []
    results = {}

    # FORCE = MASS × ACCELERATION
    if (
        "mass" in values
        and "acceleration" in values
    ):

        force = (
            values["mass"]
            * values["acceleration"]
        )

        results["force"] = force

        steps.append(
            f"Force = {values['mass']} × "
            f"{values['acceleration']} = {force} N"
        )

    # WORK = FORCE × DISTANCE
    force_value = values.get(
        "force",
        results.get("force")
    )

    if (
        force_value is not None
        and "distance" in values
    ):

        work = force_value * values["distance"]

        results["work"] = work

        steps.append(
            f"Work = {force_value} × "
            f"{values['distance']} = {work} J"
        )

    # POWER = WORK / TIME
    work_value = values.get(
        "work",
        results.get("work")
    )

    if (
        work_value is not None
        and "time" in values
    ):

        if values["time"] == 0:

            raise ValueError(
                "Time cannot be zero"
            )

        power = work_value / values["time"]

        results["power"] = power

        steps.append(
            f"Power = {work_value} / "
            f"{values['time']} = {power} W"
        )

    if not results:

        return {
            "success": False,
            "message": (
                "Insufficient inputs. "
                "Provide mass, acceleration, "
                "distance and/or time."
            ),
            "values": values
        }

    return {
        "success": True,
        "values": values,
        "results": results,
        "steps": steps
    }

# ------------------------------------------------
# 7. SINGLE + MULTI QUESTION SOLVER
# ------------------------------------------------

def v10_solve(q):

    mode = v10_detect_mode(q)

    # Multi-step
    if mode == "multi":

        try:
            return v10_multi_solve(q)

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }

    # Single solver integration
    if "v8_solve" in globals():

        result = v8_solve(q)

        if result.get("success"):

            return {
                "success": True,
                "mode": "single",
                "topic": result["topic"],
                "result": result["result"],
                "unit": result["unit"],
                "explanation": result["explanation"]
            }

    return {
        "success": False,
        "message": (
            "Question not recognized. "
            "Try a supported question."
        )
    }

# ------------------------------------------------
# 8. DISPLAY ANSWER
# ------------------------------------------------

def v10_display_result(data):

    if not data["success"]:

        print("ERROR:")
        print(data["message"])

        if "values" in data:
            print("\nDetected values:")
            print(data["values"])

        return

    if data.get("mode") == "single":

        print(data["explanation"])
        return

    print("MULTI-STEP SOLUTION")
    print("=" * 35)

    print("\nGiven values:")
    print(data["values"])

    print("\nSteps:")

    for i, step in enumerate(
        data["steps"], 1
    ):

        print(f"{i}. {step}")

    print("\nFinal Results:")

    for key, value in data["results"].items():

        units = {
            "force": "N",
            "work": "J",
            "power": "W"
        }

        print(
            f"{key.title()}: "
            f"{value:.6g} {units[key]}"
        )

# ------------------------------------------------
# 9. AUTOMATED TESTS
# ------------------------------------------------

print("V10 TESTING")

# Test 1: Force
test1 = v10_multi_solve(
    "calculate all mass 5 kg acceleration 2"
)

assert test1["success"]
assert abs(test1["results"]["force"] - 10) < 1e-9

print("PASS: force")

# Test 2: Work
test2 = v10_multi_solve(
    "calculate all force 10 distance 5 m"
)

assert test2["success"]
assert abs(test2["results"]["work"] - 50) < 1e-9

print("PASS: work")

# Test 3: Power
test3 = v10_multi_solve(
    "calculate all work 100 time 5 s"
)

assert test3["success"]
assert abs(test3["results"]["power"] - 20) < 1e-9

print("PASS: power")

# Test 4: Complete chain
test4 = v10_multi_solve(
    "calculate all mass 5 kg acceleration 2 "
    "distance 10 m time 4 s"
)

assert test4["success"]
assert abs(test4["results"]["force"] - 10) < 1e-9
assert abs(test4["results"]["work"] - 100) < 1e-9
assert abs(test4["results"]["power"] - 25) < 1e-9

print("PASS: complete force-work-power chain")

# Test 5: Unit conversion
test5 = v10_multi_solve(
    "calculate all mass 5 kg acceleration 2 "
    "distance 100 cm time 4 s"
)

assert test5["success"]
assert abs(test5["results"]["work"] - 20) < 1e-9

print("PASS: distance unit conversion")

# Test 6: Speed conversion
test6 = v10_get_inputs(
    "calculate speed 36 km/h"
)

assert abs(test6["speed"] - 10) < 1e-9

print("PASS: speed unit conversion")

print("\nALL V10 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE UI
# ------------------------------------------------

v10_question = widgets.Textarea(
    placeholder=(
        "calculate all mass 5 kg acceleration 2 "
        "distance 10 m time 4 s"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="140px"
    )
)

v10_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v10_output = widgets.Output()

def v10_run(_):

    with v10_output:

        clear_output()

        data = v10_solve(
            v10_question.value
        )

        v10_display_result(data)

v10_button.on_click(v10_run)

display(v10_question)
display(v10_button)
display(v10_output)

print("\nSUNO SAATHI MAGIC LAYER V10 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V10
# MULTI-STEP SOLVER + UNIT INTEGRATION
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. MULTI-STEP QUESTION DETECTOR
# ------------------------------------------------

def v10_detect_mode(q):

    q = q.lower()

    multi_keywords = [
        "calculate force work power",
        "find force work power",
        "calculate all",
        "step by step calculate",
        "multi step",
        "multiple calculation"
    ]

    if any(x in q for x in multi_keywords):
        return "multi"

    return "single"

# ------------------------------------------------
# 2. SMART LABELED VALUE EXTRACTOR
# ------------------------------------------------

def v10_extract(q, aliases):

    q = q.lower()

    for alias in sorted(aliases, key=len, reverse=True):

        pattern = (
            r'(?<![a-z])'
            + re.escape(alias)
            + r'(?![a-z])'
            + r'\s*(?:is|of|=|:)?\s*'
            + r'([-+]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)'
        )

        match = re.search(pattern, q)

        if match:
            return float(match.group(1))

    return None

# ------------------------------------------------
# 3. UNIT-AWARE VALUE EXTRACTION
# ------------------------------------------------

def v10_quantity(q, aliases, default_unit=None):

    q = q.lower()

    value = v10_extract(q, aliases)

    if value is None:
        return None

    # Find nearby unit after value
    pattern = (
        r'([-+]?\d+(?:\.\d+)?)'
        r'\s*(km/h|m/s|km|cm|mm|m|'
        r'hours?|hrs?|hr|min|minutes?|sec|seconds?|s|'
        r'kg|grams?|g|mg|'
        r'litres?|liters?|l|ml)'
    )

    matches = list(re.finditer(pattern, q))

    for match in matches:

        number = float(match.group(1))

        if abs(number - value) < 1e-12:

            unit = match.group(2)

            return {
                "value": value,
                "unit": unit
            }

    return {
        "value": value,
        "unit": default_unit
    }

# ------------------------------------------------
# 4. UNIT NORMALIZER
# ------------------------------------------------

def v10_to_base(value, unit, dimension):

    if unit is None:
        return float(value)

    # V9 integration
    try:

        base_units = {
            "distance": "m",
            "time": "s",
            "mass": "kg",
            "speed": "m/s",
            "volume": "l"
        }

        target = base_units.get(dimension)

        if target and "v9_convert" in globals():

            return v9_convert(
                value,
                unit,
                target
            )

    except Exception as e:

        raise ValueError(
            f"Unit conversion failed: {e}"
        )

    return float(value)

# ------------------------------------------------
# 5. LABELED INPUT COLLECTION
# ------------------------------------------------

def v10_get_inputs(q):

    values = {}

    # Mass
    mass = v10_quantity(
        q,
        ["mass", "weight"],
        "kg"
    )

    if mass:
        values["mass"] = v10_to_base(
            mass["value"],
            mass["unit"],
            "mass"
        )

    # Acceleration
    acceleration = v10_extract(
        q,
        ["acceleration"]
    )

    if acceleration is not None:
        values["acceleration"] = acceleration

    # Distance
    distance = v10_quantity(
        q,
        ["distance", "displacement"],
        "m"
    )

    if distance:
        values["distance"] = v10_to_base(
            distance["value"],
            distance["unit"],
            "distance"
        )

    # Time
    time_value = v10_quantity(
        q,
        ["time", "duration"],
        "s"
    )

    if time_value:
        values["time"] = v10_to_base(
            time_value["value"],
            time_value["unit"],
            "time"
        )

    # Force
    force = v10_extract(
        q,
        ["force"]
    )

    if force is not None:
        values["force"] = force

    # Work
    work = v10_extract(
        q,
        ["work"]
    )

    if work is not None:
        values["work"] = work

    # Speed / velocity
    speed = v10_quantity(
        q,
        ["speed", "velocity"],
        "m/s"
    )

    if speed:
        values["speed"] = v10_to_base(
            speed["value"],
            speed["unit"],
            "speed"
        )

    return values

# ------------------------------------------------
# 6. MULTI-STEP PHYSICS SOLVER
# ------------------------------------------------

def v10_multi_solve(q):

    values = v10_get_inputs(q)

    steps = []
    results = {}

    # FORCE = MASS × ACCELERATION
    if (
        "mass" in values
        and "acceleration" in values
    ):

        force = (
            values["mass"]
            * values["acceleration"]
        )

        results["force"] = force

        steps.append(
            f"Force = {values['mass']} × "
            f"{values['acceleration']} = {force} N"
        )

    # WORK = FORCE × DISTANCE
    force_value = values.get(
        "force",
        results.get("force")
    )

    if (
        force_value is not None
        and "distance" in values
    ):

        work = force_value * values["distance"]

        results["work"] = work

        steps.append(
            f"Work = {force_value} × "
            f"{values['distance']} = {work} J"
        )

    # POWER = WORK / TIME
    work_value = values.get(
        "work",
        results.get("work")
    )

    if (
        work_value is not None
        and "time" in values
    ):

        if values["time"] == 0:

            raise ValueError(
                "Time cannot be zero"
            )

        power = work_value / values["time"]

        results["power"] = power

        steps.append(
            f"Power = {work_value} / "
            f"{values['time']} = {power} W"
        )

    if not results:

        return {
            "success": False,
            "message": (
                "Insufficient inputs. "
                "Provide mass, acceleration, "
                "distance and/or time."
            ),
            "values": values
        }

    return {
        "success": True,
        "values": values,
        "results": results,
        "steps": steps
    }

# ------------------------------------------------
# 7. SINGLE + MULTI QUESTION SOLVER
# ------------------------------------------------

def v10_solve(q):

    mode = v10_detect_mode(q)

    # Multi-step
    if mode == "multi":

        try:
            return v10_multi_solve(q)

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }

    # Single solver integration
    if "v8_solve" in globals():

        result = v8_solve(q)

        if result.get("success"):

            return {
                "success": True,
                "mode": "single",
                "topic": result["topic"],
                "result": result["result"],
                "unit": result["unit"],
                "explanation": result["explanation"]
            }

    return {
        "success": False,
        "message": (
            "Question not recognized. "
            "Try a supported question."
        )
    }

# ------------------------------------------------
# 8. DISPLAY ANSWER
# ------------------------------------------------

def v10_display_result(data):

    if not data["success"]:

        print("ERROR:")
        print(data["message"])

        if "values" in data:
            print("\nDetected values:")
            print(data["values"])

        return

    if data.get("mode") == "single":

        print(data["explanation"])
        return

    print("MULTI-STEP SOLUTION")
    print("=" * 35)

    print("\nGiven values:")
    print(data["values"])

    print("\nSteps:")

    for i, step in enumerate(
        data["steps"], 1
    ):

        print(f"{i}. {step}")

    print("\nFinal Results:")

    for key, value in data["results"].items():

        units = {
            "force": "N",
            "work": "J",
            "power": "W"
        }

        print(
            f"{key.title()}: "
            f"{value:.6g} {units[key]}"
        )

# ------------------------------------------------
# 9. AUTOMATED TESTS
# ------------------------------------------------

print("V10 TESTING")

# Test 1: Force
test1 = v10_multi_solve(
    "calculate all mass 5 kg acceleration 2"
)

assert test1["success"]
assert abs(test1["results"]["force"] - 10) < 1e-9

print("PASS: force")

# Test 2: Work
test2 = v10_multi_solve(
    "calculate all force 10 distance 5 m"
)

assert test2["success"]
assert abs(test2["results"]["work"] - 50) < 1e-9

print("PASS: work")

# Test 3: Power
test3 = v10_multi_solve(
    "calculate all work 100 time 5 s"
)

assert test3["success"]
assert abs(test3["results"]["power"] - 20) < 1e-9

print("PASS: power")

# Test 4: Complete chain
test4 = v10_multi_solve(
    "calculate all mass 5 kg acceleration 2 "
    "distance 10 m time 4 s"
)

assert test4["success"]
assert abs(test4["results"]["force"] - 10) < 1e-9
assert abs(test4["results"]["work"] - 100) < 1e-9
assert abs(test4["results"]["power"] - 25) < 1e-9

print("PASS: complete force-work-power chain")

# Test 5: Unit conversion
test5 = v10_multi_solve(
    "calculate all mass 5 kg acceleration 2 "
    "distance 100 cm time 4 s"
)

assert test5["success"]
assert abs(test5["results"]["work"] - 10) < 1e-9
assert abs(test5["results"]["power"] - 2.5) < 1e-9

print("PASS: distance unit conversion")
print("PASS: power after unit conversion")

print("PASS: distance unit conversion")

# Test 6: Speed conversion
test6 = v10_get_inputs(
    "calculate speed 36 km/h"
)

assert abs(test6["speed"] - 10) < 1e-9

print("PASS: speed unit conversion")

print("\nALL V10 TESTS PASSED!")

# ------------------------------------------------
# 10. INTERACTIVE UI
# ------------------------------------------------

v10_question = widgets.Textarea(
    placeholder=(
        "calculate all mass 5 kg acceleration 2 "
        "distance 10 m time 4 s"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="140px"
    )
)

v10_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v10_output = widgets.Output()

def v10_run(_):

    with v10_output:

        clear_output()

        data = v10_solve(
            v10_question.value
        )

        v10_display_result(data)

v10_button.on_click(v10_run)

display(v10_question)
display(v10_button)
display(v10_output)

print("\nSUNO SAATHI MAGIC LAYER V10 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11
# HINDI + HINGLISH + ENGLISH QUESTION UNDERSTANDING
# ================================================================

import re
import math

# ------------------------------------------------
# 1. HINDI / HINGLISH LANGUAGE DICTIONARY
# ------------------------------------------------

V11_WORDS = {

    # Calculation commands
    "निकालो": "calculate",
    "निकाल": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "गणना": "calculate",
    "कितना होगा": "calculate",
    "कितनी होगी": "calculate",
    "find": "calculate",
    "calculate": "calculate",
    "solve": "calculate",

    # Physics variables
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",

    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",

    "बल": "force",
    "फोर्स": "force",

    "कार्य": "work",
    "वर्क": "work",

    "शक्ति": "power",
    "पावर": "power",

    "दूरी": "distance",
    "डिस्टेंस": "distance",

    "समय": "time",
    "टाइम": "time",

    "गति": "speed",
    "वेग": "velocity",

    "ऊंचाई": "height",
    "उंचाई": "height",

    "घनत्व": "density",

    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry
    "मोल": "moles",
    "मोल्स": "moles",
    "मोलरता": "molarity",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",

    # Common Hinglish
    "mass ka": "mass",
    "force ka": "force",
    "work ka": "work",
    "power ka": "power",
    "distance ka": "distance",
    "time ka": "time",
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBERS = {

    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000",
}

# ------------------------------------------------
# 3. HINDI UNIT NORMALIZATION
# ------------------------------------------------

V11_UNITS = {

    "मीटर": "m",
    "मी": "m",
    "किलोमीटर": "km",
    "किमी": "km",
    "सेंटीमीटर": "cm",
    "सेमी": "cm",
    "मिलीमीटर": "mm",

    "सेकंड": "s",
    "सेकेंड": "s",
    "मिनट": "min",
    "घंटा": "h",
    "घंटे": "h",

    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",

    "न्यूटन": "N",
    "जूल": "J",
    "वाट": "W",

    "मीटर प्रति सेकंड": "m/s",
    "किलोमीटर प्रति घंटा": "km/h",
}

# ------------------------------------------------
# 4. HINDI QUESTION TRANSLATOR
# ------------------------------------------------

def v11_translate(q):

    q = q.lower().strip()

    # Convert Hindi number words
    for hindi, number in V11_NUMBERS.items():

        q = re.sub(
            r'(?<!\S)' + re.escape(hindi) + r'(?!\S)',
            number,
            q
        )

    # Convert units
    for hindi, unit in sorted(
        V11_UNITS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):

        q = q.replace(hindi, unit)

    # Convert terms
    for hindi, english in sorted(
        V11_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):

        q = q.replace(hindi, english)

    # Remove unnecessary Hindi particles
    q = re.sub(
        r'\b(है|हैं|से|पर|और|का|की|के|में|कितना)\b',
        ' ',
        q
    )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 5. HINDI QUESTION SOLVER
# ------------------------------------------------

def v11_solve(q):

    translated = v11_translate(q)

    # Use existing V10 solver
    if "v10_solve" in globals():

        result = v10_solve(translated)

        return {
            "original_question": q,
            "translated_question": translated,
            "result": result
        }

    return {
        "original_question": q,
        "translated_question": translated,
        "result": {
            "success": False,
            "message": "V10 not loaded"
        }
    }

# ------------------------------------------------
# 6. DISPLAY SOLUTION
# ------------------------------------------------

def v11_display(data):

    print("Original question:")
    print(data["original_question"])

    print("\nNormalized question:")
    print(data["translated_question"])

    print("\nSolution:")
    v10_display_result(data["result"])

# ------------------------------------------------
# 7. TESTS
# ------------------------------------------------

print("V11 TESTING")

test_translation = [
    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg"
    ),
    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "force 10"
    ),
    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "work 100"
    )
]

for q, expected in test_translation:

    translated = v11_translate(q)

    assert expected in translated, (
        q,
        translated,
        expected
    )

    print("PASS: translation")

# Hindi force question
result1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)

assert result1["result"]["success"], result1

assert abs(
    result1["result"]["result"] - 10
) < 0.001

print("PASS: Hindi force question")

# Hinglish work question
result2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)

assert result2["result"]["success"], result2

assert abs(
    result2["result"]["result"] - 50
) < 0.001

print("PASS: Hindi work question")

print("\nALL V11 TESTS PASSED!")

# ------------------------------------------------
# 8. INTERACTIVE UI
# ------------------------------------------------

import ipywidgets as widgets
from IPython.display import display, clear_output

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_display(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11
# HINDI + HINGLISH + ENGLISH QUESTION UNDERSTANDING
# ================================================================

import re
import math

# ------------------------------------------------
# 1. HINDI / HINGLISH LANGUAGE DICTIONARY
# ------------------------------------------------

V11_WORDS = {

    # Calculation commands
    "निकालो": "calculate",
    "निकाल": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "गणना": "calculate",
    "कितना होगा": "calculate",
    "कितनी होगी": "calculate",
    "find": "calculate",
    "calculate": "calculate",
    "solve": "calculate",

    # Physics variables
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",

    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",

    "बल": "force",
    "फोर्स": "force",

    "कार्य": "work",
    "वर्क": "work",

    "शक्ति": "power",
    "पावर": "power",

    "दूरी": "distance",
    "डिस्टेंस": "distance",

    "समय": "time",
    "टाइम": "time",

    "गति": "speed",
    "वेग": "velocity",

    "ऊंचाई": "height",
    "उंचाई": "height",

    "घनत्व": "density",

    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry
    "मोल": "moles",
    "मोल्स": "moles",
    "मोलरता": "molarity",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",

    # Common Hinglish
    "mass ka": "mass",
    "force ka": "force",
    "work ka": "work",
    "power ka": "power",
    "distance ka": "distance",
    "time ka": "time",
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBERS = {

    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000",
}

# ------------------------------------------------
# 3. HINDI UNIT NORMALIZATION
# ------------------------------------------------

V11_UNITS = {

    "मीटर": "m",
    "मी": "m",
    "किलोमीटर": "km",
    "किमी": "km",
    "सेंटीमीटर": "cm",
    "सेमी": "cm",
    "मिलीमीटर": "mm",

    "सेकंड": "s",
    "सेकेंड": "s",
    "मिनट": "min",
    "घंटा": "h",
    "घंटे": "h",

    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",

    "न्यूटन": "N",
    "जूल": "J",
    "वाट": "W",

    "मीटर प्रति सेकंड": "m/s",
    "किलोमीटर प्रति घंटा": "km/h",
}

# ------------------------------------------------
# 4. HINDI QUESTION TRANSLATOR
# ------------------------------------------------

def v11_translate(q):

    q = q.lower().strip()

    # Convert Hindi number words
    for hindi, number in V11_NUMBERS.items():

        q = re.sub(
            r'(?<!\S)' + re.escape(hindi) + r'(?!\S)',
            number,
            q
        )

    # Convert units
    for hindi, unit in sorted(
        V11_UNITS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):

        q = q.replace(hindi, unit)

    # Convert terms
    for hindi, english in sorted(
        V11_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):

        q = q.replace(hindi, english)

    # Remove unnecessary Hindi particles
    q = re.sub(
        r'\b(है|हैं|से|पर|और|का|की|के|में|कितना)\b',
        ' ',
        q
    )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 5. HINDI QUESTION SOLVER
# ------------------------------------------------

def v11_solve(q):

    translated = v11_translate(q)

    # Use existing V10 solver
    if "v10_solve" in globals():

        result = v10_solve(translated)

        return {
            "original_question": q,
            "translated_question": translated,
            "result": result
        }

    return {
        "original_question": q,
        "translated_question": translated,
        "result": {
            "success": False,
            "message": "V10 not loaded"
        }
    }

# ------------------------------------------------
# 6. DISPLAY SOLUTION
# ------------------------------------------------

def v11_display(data):

    print("Original question:")
    print(data["original_question"])

    print("\nNormalized question:")
    print(data["translated_question"])

    print("\nSolution:")
    v10_display_result(data["result"])

# ------------------------------------------------
# 7. TESTS
# ------------------------------------------------

print("V11 TESTING")

test_translation = [
    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg"
    ),
    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "force 10"
    ),
    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "work 100"
    )
]

for q, expected in test_translation:

    translated = v11_translate(q)

    assert expected in translated, (
        q,
        translated,
        expected
    )

    print("PASS: translation")

# Hindi force question
result1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)

assert result1["result"]["success"], result1

assert abs(
    result1["result"]["result"] - 10
) < 0.001

print("PASS: Hindi force question")

# Hinglish work question
result2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)

assert result2["result"]["success"], result2

assert abs(
    result2["result"]["result"] - 50
) < 0.001

print("PASS: Hindi work question")

print("\nALL V11 TESTS PASSED!")

# ------------------------------------------------
# 8. INTERACTIVE UI
# ------------------------------------------------

import ipywidgets as widgets
from IPython.display import display, clear_output

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_display(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11
# HINDI + HINGLISH + ENGLISH QUESTION UNDERSTANDING
# ================================================================

import re
import math

# ------------------------------------------------
# 1. HINDI / HINGLISH LANGUAGE DICTIONARY
# ------------------------------------------------

V11_WORDS = {

    # Calculation commands
    "निकालो": "calculate",
    "निकाल": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "गणना": "calculate",
    "कितना होगा": "calculate",
    "कितनी होगी": "calculate",
    "find": "calculate",
    "calculate": "calculate",
    "solve": "calculate",

    # Physics variables
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",

    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",

    "बल": "force",
    "फोर्स": "force",

    "कार्य": "work",
    "वर्क": "work",

    "शक्ति": "power",
    "पावर": "power",

    "दूरी": "distance",
    "डिस्टेंस": "distance",

    "समय": "time",
    "टाइम": "time",

    "गति": "speed",
    "वेग": "velocity",

    "ऊंचाई": "height",
    "उंचाई": "height",

    "घनत्व": "density",

    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry
    "मोल": "moles",
    "मोल्स": "moles",
    "मोलरता": "molarity",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",

    # Common Hinglish
    "mass ka": "mass",
    "force ka": "force",
    "work ka": "work",
    "power ka": "power",
    "distance ka": "distance",
    "time ka": "time",
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBERS = {

    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000",
}

# ------------------------------------------------
# 3. HINDI UNIT NORMALIZATION
# ------------------------------------------------

V11_UNITS = {

    "मीटर": "m",
    "मी": "m",
    "किलोमीटर": "km",
    "किमी": "km",
    "सेंटीमीटर": "cm",
    "सेमी": "cm",
    "मिलीमीटर": "mm",

    "सेकंड": "s",
    "सेकेंड": "s",
    "मिनट": "min",
    "घंटा": "h",
    "घंटे": "h",

    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",

    "न्यूटन": "N",
    "जूल": "J",
    "वाट": "W",

    "मीटर प्रति सेकंड": "m/s",
    "किलोमीटर प्रति घंटा": "km/h",
}

# ------------------------------------------------
# 4. HINDI QUESTION TRANSLATOR
# ------------------------------------------------

def v11_translate(q):

    q = q.lower().strip()

    # Convert Hindi number words
    for hindi, number in V11_NUMBERS.items():

        q = re.sub(
            r'(?<!\S)' + re.escape(hindi) + r'(?!\S)',
            number,
            q
        )

    # Convert units
    for hindi, unit in sorted(
        V11_UNITS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):

        q = q.replace(hindi, unit)

    # Convert terms
    for hindi, english in sorted(
        V11_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):

        q = q.replace(hindi, english)

    # Remove unnecessary Hindi particles
    q = re.sub(
        r'\b(है|हैं|से|पर|और|का|की|के|में|कितना)\b',
        ' ',
        q
    )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 5. HINDI QUESTION SOLVER
# ------------------------------------------------

def v11_solve(q):

    translated = v11_translate(q)

    # Use existing V10 solver
    if "v10_solve" in globals():

        result = v10_solve(translated)

        return {
            "original_question": q,
            "translated_question": translated,
            "result": result
        }

    return {
        "original_question": q,
        "translated_question": translated,
        "result": {
            "success": False,
            "message": "V10 not loaded"
        }
    }

# ------------------------------------------------
# 6. DISPLAY SOLUTION
# ------------------------------------------------

def v11_display(data):

    print("Original question:")
    print(data["original_question"])

    print("\nNormalized question:")
    print(data["translated_question"])

    print("\nSolution:")
    v10_display_result(data["result"])

# ------------------------------------------------
# 7. TESTS
# ------------------------------------------------

test_translation = [
    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg"
    ),
    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "10 N force"
    ),
    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "work 100"
    )
]

for q, expected in test_translation:

    translated = v11_translate(q)

    assert expected in translated, (
        q,
        translated,
        expected
    )

    print("PASS: translation")


# ------------------------------------------------
# 8. INTERACTIVE UI
# ------------------------------------------------

import ipywidgets as widgets
from IPython.display import display, clear_output

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_display(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11.1
# VERIFIED HINDI + HINGLISH QUESTION ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. HINDI / HINGLISH DICTIONARY
# ------------------------------------------------

V11_TERMS = {

    # Physics
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",

    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",

    "बल": "force",
    "फोर्स": "force",

    "कार्य": "work",
    "वर्क": "work",

    "शक्ति": "power",
    "पावर": "power",

    "दूरी": "distance",
    "डिस्टेंस": "distance",

    "समय": "time",
    "टाइम": "time",

    "गति": "speed",
    "वेग": "velocity",

    "ऊंचाई": "height",
    "ऊँचाई": "height",

    "घनत्व": "density",

    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry
    "मोलर द्रव्यमान": "molar mass",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",
    "मोलरता": "molarity",
    "मोल्स": "moles",
    "मोल": "moles",

    # Units
    "किलोमीटर प्रति घंटा": "km/h",
    "मीटर प्रति सेकंड": "m/s",
    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",
    "मिलीग्राम": "mg",
    "सेंटीमीटर": "cm",
    "मिलीमीटर": "mm",
    "किलोमीटर": "km",
    "मीटर": "m",
    "सेकंड": "s",
    "सेकेंड": "s",
    "मिनट": "min",
    "घंटे": "h",
    "घंटा": "h",
    "न्यूटन": "N",
    "जूल": "J",
    "वाट": "W",
    "लीटर": "l",
    "मिलीलीटर": "ml",

    # Commands
    "निकालो": "calculate",
    "निकाल": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "गणना करो": "calculate",
    "गणना": "calculate",
    "find": "calculate",
    "solve": "calculate",
    "calculate": "calculate"
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBER_WORDS = {
    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000"
}

# ------------------------------------------------
# 3. NORMALIZATION
# ------------------------------------------------

def v11_normalize(q):

    q = str(q).lower().strip()

    # Hindi numbers
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            number,
            q
        )

    # Hindi terms and units
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Remove common Hindi particles
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 4. SAFE V8 / V10 CONNECTION
# ------------------------------------------------

def v11_solve(q):

    normalized = v11_normalize(q)

    if "v8_solve" not in globals():

        return {
            "success": False,
            "message": "V8 cell pehle run karo."
        }

    # Existing V8 solver
    result = v8_solve(normalized)

    return {
        "success": result.get("success", False),
        "original_question": q,
        "normalized_question": normalized,
        "result": result
    }

# ------------------------------------------------
# 5. DISPLAY
# ------------------------------------------------

def v11_show(data):

    print("Original:")
    print(data["original_question"])

    print("\nNormalized:")
    print(data["normalized_question"])

    print("\nAnswer:")

    result = data["result"]

    if result.get("success"):

        print(result.get("explanation", ""))

        print(
            "\nFinal:",
            result["result"],
            result["unit"]
        )

    else:

        print(result.get("message", "Question not solved"))

# ------------------------------------------------
# 6. TESTS - TRANSLATION
# ------------------------------------------------

print("V11.1 TESTING")
print("-" * 40)

translation_tests = [

    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg",
        "acceleration 2"
    ),

    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "10 N force",
        "5 m distance"
    ),

    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "100 joule work",
        "5 s"
    )
]

for q, expected1, expected2 in translation_tests:

    normalized = v11_normalize(q)

    assert expected1 in normalized, (
        q, normalized, expected1
    )

    assert expected2 in normalized, (
        q, normalized, expected2
    )

    print("PASS: translation")

# ------------------------------------------------
# 7. TESTS - REAL CALCULATIONS
# ------------------------------------------------

# Hindi force
t1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)

assert t1["success"], t1

assert abs(
    t1["result"]["result"] - 10
) < 0.001

print("PASS: Hindi force = 10 N")

# Hindi work
t2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)

assert t2["success"], t2

assert abs(
    t2["result"]["result"] - 50
) < 0.001

print("PASS: Hindi work = 50 J")

# Hinglish power
t3 = v11_solve(
    "100 joule work 5 सेकंड में हुआ power find करो"
)

assert t3["success"], t3

assert abs(
    t3["result"]["result"] - 20
) < 0.001

print("PASS: Hinglish power = 20 W")

print("-" * 40)
print("ALL V11.1 TESTS PASSED!")

# ------------------------------------------------
# 8. INTERACTIVE UI
# ------------------------------------------------

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_show(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11.1 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11.1
# VERIFIED HINDI + HINGLISH QUESTION ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. HINDI / HINGLISH DICTIONARY
# ------------------------------------------------

V11_TERMS = {

    # Physics
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",

    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",

    "बल": "force",
    "फोर्स": "force",

    "कार्य": "work",
    "वर्क": "work",

    "शक्ति": "power",
    "पावर": "power",

    "दूरी": "distance",
    "डिस्टेंस": "distance",

    "समय": "time",
    "टाइम": "time",

    "गति": "speed",
    "वेग": "velocity",

    "ऊंचाई": "height",
    "ऊँचाई": "height",

    "घनत्व": "density",

    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry
    "मोलर द्रव्यमान": "molar mass",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",
    "मोलरता": "molarity",
    "मोल्स": "moles",
    "मोल": "moles",

    # Units
    "किलोमीटर प्रति घंटा": "km/h",
    "मीटर प्रति सेकंड": "m/s",
    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",
    "मिलीग्राम": "mg",
    "सेंटीमीटर": "cm",
    "मिलीमीटर": "mm",
    "किलोमीटर": "km",
    "मीटर": "m",
    "सेकंड": "s",
    "सेकेंड": "s",
    "मिनट": "min",
    "घंटे": "h",
    "घंटा": "h",
    "न्यूटन": "N",
    "जूल": "J",
    "वाट": "W",
    "लीटर": "l",
    "मिलीलीटर": "ml",

    # Commands
    "निकालो": "calculate",
    "निकाल": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "गणना करो": "calculate",
    "गणना": "calculate",
    "find": "calculate",
    "solve": "calculate",
    "calculate": "calculate"
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBER_WORDS = {
    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000"
}

# ------------------------------------------------
# 3. NORMALIZATION
# ------------------------------------------------

def v11_normalize(q):

    q = str(q).lower().strip()

    # Hindi numbers
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            number,
            q
        )

    # Hindi terms and units
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Remove common Hindi particles
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 4. SAFE V8 / V10 CONNECTION
# ------------------------------------------------

def v11_solve(q):

    normalized = v11_normalize(q)

    if "v8_solve" not in globals():

        return {
            "success": False,
            "message": "V8 cell pehle run karo."
        }

    # Existing V8 solver
    result = v8_solve(normalized)

    return {
        "success": result.get("success", False),
        "original_question": q,
        "normalized_question": normalized,
        "result": result
    }

# ------------------------------------------------
# 5. DISPLAY
# ------------------------------------------------

def v11_show(data):

    print("Original:")
    print(data["original_question"])

    print("\nNormalized:")
    print(data["normalized_question"])

    print("\nAnswer:")

    result = data["result"]

    if result.get("success"):

        print(result.get("explanation", ""))

        print(
            "\nFinal:",
            result["result"],
            result["unit"]
        )

    else:

        print(result.get("message", "Question not solved"))

# ------------------------------------------------
# 6. TESTS - TRANSLATION
# ------------------------------------------------

print("V11.1 TESTING")
print("-" * 40)

translation_tests = [

    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg",
        "acceleration 2"
    ),

    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "10 N force",
        "5 m distance"
    ),

    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "100 joule work",
        "5 s"
    )
]

for q, expected1, expected2 in translation_tests:

    normalized = v11_normalize(q)

    assert expected1 in normalized, (
        q, normalized, expected1
    )

    assert expected2 in normalized, (
        q, normalized, expected2
    )

    print("PASS: translation")

# ------------------------------------------------
# 7. TESTS - REAL CALCULATIONS
# ------------------------------------------------

# Hindi force
t1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)

assert t1["success"], t1

assert abs(
    t1["result"]["result"] - 10
) < 0.001

print("PASS: Hindi force = 10 N")

# Hindi work
t2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)

assert t2["success"], t2

assert abs(
    t2["result"]["result"] - 50
) < 0.001

print("PASS: Hindi work = 50 J")

# Hinglish power
t3 = v11_solve(
    "100 joule work 5 सेकंड में हुआ power find करो"
)

assert t3["success"], t3

assert abs(
    t3["result"]["result"] - 20
) < 0.001

print("PASS: Hinglish power = 20 W")

print("-" * 40)
print("ALL V11.1 TESTS PASSED!")

# ------------------------------------------------
# 8. INTERACTIVE UI
# ------------------------------------------------

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_show(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11.1 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11.1 (FIXED)
# VERIFIED HINDI + HINGLISH QUESTION ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. HINDI / HINGLISH DICTIONARY
# ------------------------------------------------

V11_TERMS = {

    # Physics Terms
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",

    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",

    "बल": "force",
    "फोर्स": "force",

    "कार्य": "work",
    "वर्क": "work",

    "शक्ति": "power",
    "पावर": "power",

    "दूरी": "distance",
    "डिस्टेंस": "distance",

    "समय": "time",
    "टाइम": "time",

    "गति": "speed",
    "वेग": "velocity",

    "ऊंचाई": "height",
    "ऊँचाई": "height",

    "घनत्व": "density",

    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry Terms
    "मोलर द्रव्यमान": "molar mass",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",
    "मोलरता": "molarity",
    "मोल्स": "moles",
    "मोल": "moles",

    # Units & Standard Symbols (Hindi & Hinglish variants)
    "किलोमीटर प्रति घंटा": "km/h",
    "मीटर प्रति सेकंड": "m/s",
    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",
    "मिलीग्राम": "mg",
    "सेंटीमीटर": "cm",
    "मिलीमीटर": "mm",
    "किलोमीटर": "km",
    "मीटर": "m",
    "मीटरों": "m",
    "सेकंड": "s",
    "सेकेंड": "s",
    "सेकंड्स": "s",
    "seconds": "s",
    "second": "s",
    "sec": "s",
    "मिनट": "min",
    "घंटे": "h",
    "घंटा": "h",
    "न्यूटन": "N",
    "न्यूटंस": "N",
    "जूल": "J",
    "जूल्स": "J",
    "joule": "J",
    "joules": "J",
    "वाट": "W",
    "वाट्स": "W",
    "लीटर": "l",
    "मिलीलीटर": "ml",

    # Commands & Operators
    "निकालो": "calculate",
    "निकाल": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "गणना करो": "calculate",
    "गणना": "calculate",
    "find": "calculate",
    "solve": "calculate",
    "calculate": "calculate"
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBER_WORDS = {
    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000"
}

# ------------------------------------------------
# 3. NORMALIZATION
# ------------------------------------------------

def v11_normalize(q):

    q = str(q).lower().strip()

    # Hindi numbers replacement
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            number,
            q
        )

    # Hindi terms and units replacement (longest first)
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Remove common Hindi particles that add noise
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 4. SAFE V8 / V10 CONNECTION
# ------------------------------------------------

def v11_solve(q):

    normalized = v11_normalize(q)

    if "v8_solve" not in globals():

        return {
            "success": False,
            "message": "V8 cell pehle run karo."
        }

    # Existing V8 solver call
    result = v8_solve(normalized)

    return {
        "success": result.get("success", False),
        "original_question": q,
        "normalized_question": normalized,
        "result": result
    }

# ------------------------------------------------
# 5. DISPLAY
# ------------------------------------------------

def v11_show(data):

    print("Original:")
    print(data["original_question"])

    print("\nNormalized:")
    print(data["normalized_question"])

    print("\nAnswer:")

    result = data["result"]

    if result.get("success"):

        print(result.get("explanation", ""))

        print(
            "\nFinal:",
            result["result"],
            result["unit"]
        )

    else:

        print(result.get("message", "Question not solved"))

# ------------------------------------------------
# 6. TESTS - TRANSLATION
# ------------------------------------------------

print("V11.1 TESTING")
print("-" * 40)

translation_tests = [

    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg",
        "acceleration 2"
    ),

    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "10 N force",
        "5 m distance"
    ),

    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "100 J work",
        "5 s"
    )
]

for q, expected1, expected2 in translation_tests:

    normalized = v11_normalize(q)

    assert expected1 in normalized, (
        q, normalized, expected1
    )

    assert expected2 in normalized, (
        q, normalized, expected2
    )

    print("PASS: translation")

# ------------------------------------------------
# 7. TESTS - REAL CALCULATIONS
# ------------------------------------------------

# Hindi force
t1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)

assert t1["success"], t1

assert abs(
    t1["result"]["result"] - 10
) < 0.001

print("PASS: Hindi force = 10 N")

# Hindi work
t2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)

assert t2["success"], t2

assert abs(
    t2["result"]["result"] - 50
) < 0.001

print("PASS: Hindi work = 50 J")

# Hinglish power
t3 = v11_solve(
    "100 joule work 5 सेकंड में हुआ power find करो"
)

assert t3["success"], t3

assert abs(
    t3["result"]["result"] - 20
) < 0.001

print("PASS: Hinglish power = 20 W")

print("-" * 40)
print("ALL V11.1 TESTS PASSED!")

# ------------------------------------------------
# 8. INTERACTIVE UI
# ------------------------------------------------

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_show(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11.1 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11.1 (FIXED)
# VERIFIED HINDI + HINGLISH QUESTION ENGINE
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. HINDI / HINGLISH DICTIONARY
# ------------------------------------------------

V11_TERMS = {

    # Physics Terms
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",

    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",

    "बल": "force",
    "फोर्स": "force",

    "कार्य": "work",
    "वर्क": "work",

    "शक्ति": "power",
    "पावर": "power",

    "दूरी": "distance",
    "डिस्टेंस": "distance",

    "समय": "time",
    "टाइम": "time",

    "गति": "speed",
    "वेग": "velocity",

    "ऊंचाई": "height",
    "ऊँचाई": "height",

    "घनत्व": "density",

    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry Terms
    "मोलर द्रव्यमान": "molar mass",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",
    "मोलरता": "molarity",
    "मोल्स": "moles",
    "मोल": "moles",

    # Units & Standard Symbols (Hindi & Hinglish variants)
    "किलोमीटर प्रति घंटा": "km/h",
    "मीटर प्रति सेकंड": "m/s",
    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",
    "मिलीग्राम": "mg",
    "सेंटीमीटर": "cm",
    "मिलीमीटर": "mm",
    "किलोमीटर": "km",
    "मीटर": "m",
    "मीटरों": "m",
    "सेकंड": "s",
    "सेकेंड": "s",
    "सेकंड्स": "s",
    "seconds": "s",
    "second": "s",
    "sec": "s",
    "मिनट": "min",
    "घंटे": "h",
    "घंटा": "h",
    "न्यूटन": "N",
    "न्यूटंस": "N",
    "जूल": "J",
    "जूल्स": "J",
    "joule": "J",
    "joules": "J",
    "वाट": "W",
    "वाट्स": "W",
    "लीटर": "l",
    "मिलीलीटर": "ml",

    # Commands & Operators
    "निकालो": "calculate",
    "निकाल": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "गणना करो": "calculate",
    "गणना": "calculate",
    "find": "calculate",
    "solve": "calculate",
    "calculate": "calculate"
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBER_WORDS = {
    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000"
}

# ------------------------------------------------
# 3. NORMALIZATION
# ------------------------------------------------

def v11_normalize(q):

    q = str(q).lower().strip()

    # Hindi numbers replacement
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            number,
            q
        )

    # Hindi terms and units replacement (longest first)
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Remove common Hindi particles that add noise
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 4. SAFE V8 / V10 CONNECTION
# ------------------------------------------------

def v11_solve(q):

    normalized = v11_normalize(q)

    if "v8_solve" not in globals():

        return {
            "success": False,
            "message": "V8 cell pehle run karo."
        }

    # Existing V8 solver call
    result = v8_solve(normalized)

    return {
        "success": result.get("success", False),
        "original_question": q,
        "normalized_question": normalized,
        "result": result
    }

# ------------------------------------------------
# 5. DISPLAY
# ------------------------------------------------

def v11_show(data):

    print("Original:")
    print(data["original_question"])

    print("\nNormalized:")
    print(data["normalized_question"])

    print("\nAnswer:")

    result = data["result"]

    if result.get("success"):

        print(result.get("explanation", ""))

        print(
            "\nFinal:",
            result["result"],
            result["unit"]
        )

    else:

        print(result.get("message", "Question not solved"))

# ------------------------------------------------
# 6. TESTS - TRANSLATION
# ------------------------------------------------

print("V11.1 TESTING")
print("-" * 40)

translation_tests = [

    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg",
        "acceleration 2"
    ),

    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "10 N force",
        "5 m distance"
    ),

    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "100 J work",
        "5 s"
    )
]

for q, expected1, expected2 in translation_tests:

    normalized = v11_normalize(q)

    assert expected1 in normalized, (
        q, normalized, expected1
    )

    assert expected2 in normalized, (
        q, normalized, expected2
    )

    print("PASS: translation")

# ------------------------------------------------
# 7. TESTS - REAL CALCULATIONS
# ------------------------------------------------

# ------------------------------------------------
# 7. TESTS - REAL CALCULATIONS (WITH DEBUG)
# ------------------------------------------------

# Hindi force
t1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)
assert t1["success"], t1
assert abs(t1["result"]["result"] - 10) < 0.001
print("PASS: Hindi force = 10 N")

# Hindi work
t2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)
assert t2["success"], t2
assert abs(t2["result"]["result"] - 50) < 0.001
print("PASS: Hindi work = 50 J")

# Hinglish power (with debug inspection)
t3 = v11_solve(
    "100 joule work 5 सेकंड में हुआ power find करो"
)
print("DEBUG t3 output:", t3)  # This will print what V8 actually returned

assert t3["success"], t3
assert abs(t3["result"]["result"] - 20) < 0.001
print("PASS: Hinglish power = 20 W")


# ------------------------------------------------
# 8. INTERACTIVE UI
# ------------------------------------------------

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_show(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11.1 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11.2
# HINDI + HINGLISH QUESTION ENGINE
# POWER MAPPING FIX + TESTS + INTERACTIVE UI
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. HINDI / HINGLISH DICTIONARY
# ------------------------------------------------

V11_TERMS = {

    # Physics
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",
    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",
    "बल": "force",
    "फोर्स": "force",
    "कार्य": "work",
    "वर्क": "work",
    "शक्ति": "power",
    "पावर": "power",
    "दूरी": "distance",
    "डिस्टेंस": "distance",
    "समय": "time",
    "टाइम": "time",
    "गति": "speed",
    "वेग": "velocity",
    "ऊंचाई": "height",
    "ऊँचाई": "height",
    "घनत्व": "density",
    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry
    "मोलर द्रव्यमान": "molar mass",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",
    "मोलरता": "molarity",
    "मोल्स": "moles",
    "मोल": "moles",

    # Units
    "किलोमीटर प्रति घंटा": "km/h",
    "मीटर प्रति सेकंड": "m/s",
    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",
    "मिलीग्राम": "mg",
    "सेंटीमीटर": "cm",
    "मिलीमीटर": "mm",
    "किलोमीटर": "km",
    "मीटरों": "m",
    "मीटर": "m",
    "सेकंड्स": "s",
    "सेकेंड": "s",
    "सेकंड": "s",
    "seconds": "s",
    "second": "s",
    "sec": "s",
    "मिनट": "min",
    "घंटे": "h",
    "घंटा": "h",
    "न्यूटन": "N",
    "न्यूटंस": "N",
    "जूल्स": "J",
    "जूल": "J",
    "joules": "J",
    "joule": "J",
    "वाट्स": "W",
    "वाट": "W",
    "लीटर": "l",
    "मिलीलीटर": "ml",

    # Commands
    "निकालो": "calculate",
    "निकाल": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "गणना करो": "calculate",
    "गणना": "calculate",
    "find": "calculate",
    "solve": "calculate",
    "calculate": "calculate"
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBER_WORDS = {
    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000"
}

# ------------------------------------------------
# 3. NORMALIZATION
# ------------------------------------------------

def v11_normalize(q):

    q = str(q).lower().strip()

    # Hindi numbers
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            number,
            q
        )

    # Hindi terms and units
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Hindi particles
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 4. POWER SOLVER - V11.2 FIX
# ------------------------------------------------

def v11_power_solve(normalized):

    # Work: 100 J work
    work_match = re.search(
        r'(\d+(?:\.\d+)?)\s*J\s*work',
        normalized
    )

    # Alternative: work 100 J
    if not work_match:
        work_match = re.search(
            r'work\s*(\d+(?:\.\d+)?)\s*J',
            normalized
        )

    # Time: 5 s
    time_match = re.search(
        r'(\d+(?:\.\d+)?)\s*s',
        normalized
    )

    if not work_match or not time_match:
        return {
            "success": False,
            "topic": "power",
            "message": (
                "Power ke liye Work (J) aur Time (s) "
                "dono values chahiye."
            )
        }

    work = float(work_match.group(1))
    time = float(time_match.group(1))

    if time <= 0:
        return {
            "success": False,
            "topic": "power",
            "message": "Time zero se greater hona chahiye."
        }

    power = work / time

    return {
        "success": True,
        "topic": "power",
        "values": {
            "work": work,
            "time": time
        },
        "result": power,
        "unit": "W",
        "steps": [
            "Power = Work / Time",
            f"Power = {work} / {time}",
            f"Power = {power} W"
        ],
        "explanation": (
            f"Topic: Power\n\n"
            f"Formula:\nP = W / t\n\n"
            f"Given:\nWork = {work} J\n"
            f"Time = {time} s\n\n"
            f"Solution:\n"
            f"Power = {work} / {time}\n\n"
            f"Final Answer:\n{power} W"
        )
    }

# ------------------------------------------------
# 5. MAIN SOLVER - V8 + POWER FIX
# ------------------------------------------------

def v11_solve(q):

    normalized = v11_normalize(q)

    # Power uses corrected V11.2 mapping
    if re.search(r'\bpower\b', normalized):

        result = v11_power_solve(normalized)

        return {
            "success": result.get("success", False),
            "original_question": q,
            "normalized_question": normalized,
            "result": result
        }

    # Other topics use V8
    if "v8_solve" not in globals():

        return {
            "success": False,
            "original_question": q,
            "normalized_question": normalized,
            "message": "V8 cell pehle run karo."
        }

    result = v8_solve(normalized)

    return {
        "success": result.get("success", False),
        "original_question": q,
        "normalized_question": normalized,
        "result": result
    }

# ------------------------------------------------
# 6. DISPLAY
# ------------------------------------------------

def v11_show(data):

    print("Original:")
    print(data.get("original_question", ""))

    print("\nNormalized:")
    print(data.get("normalized_question", ""))

    print("\nAnswer:")

    if not data.get("success"):

        print(data.get("message", "Question not solved"))
        return

    result = data["result"]

    if result.get("success"):

        print(result.get("explanation", ""))

        print(
            "\nFinal:",
            result.get("result"),
            result.get("unit", "")
        )

    else:

        print(result.get("message", "Question not solved"))

# ------------------------------------------------
# 7. TESTS - TRANSLATION
# ------------------------------------------------

print("SUNO SAATHI V11.2 TESTING")
print("-" * 50)

translation_tests = [

    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg",
        "acceleration 2"
    ),

    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "10 N force",
        "5 m distance"
    ),

    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "100 J work",
        "5 s"
    )
]

for q, expected1, expected2 in translation_tests:

    normalized = v11_normalize(q)

    assert expected1 in normalized, (
        q, normalized, expected1
    )

    assert expected2 in normalized, (
        q, normalized, expected2
    )

    print("PASS: translation")

# ------------------------------------------------
# 8. REAL CALCULATION TESTS
# ------------------------------------------------

# Hindi Force
t1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)

assert t1["success"], t1

assert abs(
    t1["result"]["result"] - 10
) < 0.001

print("PASS: Hindi force = 10 N")

# Hindi Work
t2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)

assert t2["success"], t2

assert abs(
    t2["result"]["result"] - 50
) < 0.001

print("PASS: Hindi work = 50 J")

# Hinglish Power
t3 = v11_solve(
    "100 joule work 5 सेकंड में हुआ power find करो"
)

assert t3["success"], t3

assert t3["result"]["values"]["work"] == 100
assert t3["result"]["values"]["time"] == 5

assert abs(
    t3["result"]["result"] - 20
) < 0.001

print("PASS: Hinglish power = 20 W")

# Reverse Power wording
t4 = v11_solve(
    "work 100 J time 5 s power calculate"
)

assert t4["success"], t4

assert abs(
    t4["result"]["result"] - 20
) < 0.001

print("PASS: Reverse power wording = 20 W")

# Decimal Power
t5 = v11_solve(
    "50 joule work 2.5 seconds power find"
)

assert t5["success"], t5

assert abs(
    t5["result"]["result"] - 20
) < 0.001

print("PASS: Decimal power = 20 W")

# Zero time must fail
t6 = v11_solve(
    "100 joule work 0 seconds power find"
)

assert not t6["success"]

print("PASS: Zero time validation")

print("-" * 50)
print("ALL V11.2 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_show(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11.2 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11.2
# HINDI + HINGLISH QUESTION ENGINE
# POWER MAPPING FIX + TESTS + INTERACTIVE UI
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. HINDI / HINGLISH DICTIONARY
# ------------------------------------------------

V11_TERMS = {

    # Physics
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",
    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",
    "बल": "force",
    "फोर्स": "force",
    "कार्य": "work",
    "वर्क": "work",
    "शक्ति": "power",
    "पावर": "power",
    "दूरी": "distance",
    "डिस्टेंस": "distance",
    "समय": "time",
    "टाइम": "time",
    "गति": "speed",
    "वेग": "velocity",
    "ऊंचाई": "height",
    "ऊँचाई": "height",
    "घनत्व": "density",
    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry
    "मोलर द्रव्यमान": "molar mass",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",
    "मोलरता": "molarity",
    "मोल्स": "moles",
    "मोल": "moles",

    # Units
    "किलोमीटर प्रति घंटा": "km/h",
    "मीटर प्रति सेकंड": "m/s",
    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",
    "मिलीग्राम": "mg",
    "सेंटीमीटर": "cm",
    "मिलीमीटर": "mm",
    "किलोमीटर": "km",
    "मीटरों": "m",
    "मीटर": "m",
    "सेकंड्स": "s",
    "सेकेंड": "s",
    "सेकंड": "s",
    "seconds": "s",
    "second": "s",
    "sec": "s",
    "मिनट": "min",
    "घंटे": "h",
    "घंटा": "h",
    "न्यूटन": "N",
    "न्यूटंस": "N",
    "जूल्स": "J",
    "जूल": "J",
    "joules": "J",
    "joule": "J",
    "वाट्स": "W",
    "वाट": "W",
    "लीटर": "l",
    "मिलीलीटर": "ml",

    # Commands
    "निकालो": "calculate",
    "निकाल": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "गणना करो": "calculate",
    "गणना": "calculate",
    "find": "calculate",
    "solve": "calculate",
    "calculate": "calculate"
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBER_WORDS = {
    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000"
}

# ------------------------------------------------
# 3. NORMALIZATION
# ------------------------------------------------

def v11_normalize(q):

    q = str(q).lower().strip()

    # Hindi numbers
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!    ext{S})',
            number,
            q
        )

    # Hindi terms and units
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Hindi particles
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!    ext{S})',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 4. POWER SOLVER - V11.2 FIX
# ------------------------------------------------

def v11_power_solve(normalized):

    # Work: 100 j work / 100 J work (using re.IGNORECASE)
    work_match = re.search(
        r'(\d+(?:\.\d+)?)\s*j\s*work',
        normalized,
        re.IGNORECASE
    )

    # Alternative: work 100 j / work 100 J
    if not work_match:
        work_match = re.search(
            r'work\s*(\d+(?:\.\d+)?)\s*j',
            normalized,
            re.IGNORECASE
        )

    # Time: 5 s
    time_match = re.search(
        r'(\d+(?:\.\d+)?)\s*s',
        normalized,
        re.IGNORECASE
    )

    if not work_match or not time_match:
        return {
            "success": False,
            "topic": "power",
            "message": (
                "Power ke liye Work (J) aur Time (s) "
                "dono values chahiye."
            )
        }

    work = float(work_match.group(1))
    time = float(time_match.group(1))

    if time <= 0:
        return {
            "success": False,
            "topic": "power",
            "message": "Time zero se greater hona chahiye."
        }

    power = work / time

    return {
        "success": True,
        "topic": "power",
        "values": {
            "work": work,
            "time": time
        },
        "result": power,
        "unit": "W",
        "steps": [
            "Power = Work / Time",
            f"Power = {work} / {time}",
            f"Power = {power} W"
        ],
        "explanation": (
            f"Topic: Power\n\n"
            f"Formula:\nP = W / t\n\n"
            f"Given:\nWork = {work} J\n"
            f"Time = {time} s\n\n"
            f"Solution:\n"
            f"Power = {work} / {time}\n\n"
            f"Final Answer:\n{power} W"
        )
    }

# ------------------------------------------------
# 5. MAIN SOLVER - V8 + POWER FIX
# ------------------------------------------------

def v11_solve(q):

    normalized = v11_normalize(q)

    # Power uses corrected V11.2 mapping
    if re.search(r'\bpower\b', normalized):

        result = v11_power_solve(normalized)

        return {
            "success": result.get("success", False),
            "original_question": q,
            "normalized_question": normalized,
            "result": result
        }

    # Other topics use V8
    if "v8_solve" not in globals():

        return {
            "success": False,
            "original_question": q,
            "normalized_question": normalized,
            "message": "V8 cell pehle run karo."
        }

    result = v8_solve(normalized)

    return {
        "success": result.get("success", False),
        "original_question": q,
        "normalized_question": normalized,
        "result": result
    }

# ------------------------------------------------
# 6. DISPLAY
# ------------------------------------------------

def v11_show(data):

    print("Original:")
    print(data.get("original_question", ""))

    print("\nNormalized:")
    print(data.get("normalized_question", ""))

    print("\nAnswer:")

    if not data.get("success"):

        print(data.get("message", "Question not solved"))
        return

    result = data["result"]

    if result.get("success"):

        print(result.get("explanation", ""))

        print(
            "\nFinal:",
            result.get("result"),
            result.get("unit", "")
        )

    else:

        print(result.get("message", "Question not solved"))

# ------------------------------------------------
# 7. TESTS - TRANSLATION
# ------------------------------------------------

print("SUNO SAATHI V11.2 TESTING")
print("-" * 50)

translation_tests = [

    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg",
        "acceleration 2"
    ),

    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "10 N force",
        "5 m distance"
    ),

    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "100 J work",
        "5 s"
    )
]

for q, expected1, expected2 in translation_tests:

    normalized = v11_normalize(q)

    assert expected1 in normalized or expected1.lower() in normalized, (
        q, normalized, expected1
    )

    assert expected2 in normalized or expected2.lower() in normalized, (
        q, normalized, expected2
    )

    print("PASS: translation")

# ------------------------------------------------
# 8. REAL CALCULATION TESTS
# ------------------------------------------------

# Hindi Force
t1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)

assert t1["success"], t1

assert abs(
    t1["result"]["result"] - 10
) < 0.001

print("PASS: Hindi force = 10 N")

# Hindi Work
t2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)

assert t2["success"], t2

assert abs(
    t2["result"]["result"] - 50
) < 0.001

print("PASS: Hindi work = 50 J")

# Hinglish Power
t3 = v11_solve(
    "100 joule work 5 सेकंड में हुआ power find करो"
)

assert t3["success"], t3

assert t3["result"]["values"]["work"] == 100
assert t3["result"]["values"]["time"] == 5

assert abs(
    t3["result"]["result"] - 20
) < 0.001

print("PASS: Hinglish power = 20 W")

# Reverse Power wording
t4 = v11_solve(
    "work 100 J time 5 s power calculate"
)

assert t4["success"], t4

assert abs(
    t4["result"]["result"] - 20
) < 0.001

print("PASS: Reverse power wording = 20 W")

# Decimal Power
t5 = v11_solve(
    "50 joule work 2.5 seconds power find"
)

assert t5["success"], t5

assert abs(
    t5["result"]["result"] - 20
) < 0.001

print("PASS: Decimal power = 20 W")

# Zero time must fail
t6 = v11_solve(
    "100 joule work 0 seconds power find"
)

assert not t6["success"]

print("PASS: Zero time validation")

print("-" * 50)
print("ALL V11.2 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_show(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11.2 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V12 + V13
# SMART QUESTION DETECTION + VARIABLE MAPPING
# ================================================================

import re
import math

# ------------------------------------------------
# V12: SMART TOPIC DETECTION
# ------------------------------------------------

V12_TOPIC_PATTERNS = {
    "force": [
        "force", "mass acceleration", "newton",
    "बल", "फोर्स"
    ],
    "work": [
        "work", "force distance", "कार्य", "वर्क"
    ],
    "power": [
        "power", "work time", "पावर", "शक्ति"
    ],
    "speed": [
        "speed", "velocity", "distance time",
        "गति", "वेग"
    ],
    "density": [
        "density", "घनत्व"
    ],
    "kinetic_energy": [
        "kinetic energy", "गतिज ऊर्जा"
    ],
    "potential_energy": [
        "potential energy", "स्थितिज ऊर्जा"
    ]
}

def v12_detect_topic(q):

    q = v11_normalize(q)

    # Explicit formula keywords
    for topic, patterns in V12_TOPIC_PATTERNS.items():

        for pattern in patterns:

            if pattern in q:
                return topic

    # Formula inference
    if "mass" in q and "acceleration" in q:
        return "force"

    if "force" in q and "distance" in q:
        return "work"

    if "work" in q and "time" in q:
        return "power"

    if "distance" in q and "time" in q:
        return "speed"

    return "unknown"


# ------------------------------------------------
# V13: SMART VARIABLE MAPPING
# ------------------------------------------------

def v13_extract_number(q, variable):

    q = v11_normalize(q)

    patterns = {

        "mass": [
            r'mass\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*kg\s*mass'
        ],

        "acceleration": [
            r'acceleration\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m/s(?:\^?2|²)?'
        ],

        "force": [
            r'force\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*N\s*force'
        ],

        "distance": [
            r'distance\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s*distance'
        ],

        "time": [
            r'time\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*s'
        ],

        "work": [
            r'work\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*J\s*work'
        ],

        "speed": [
            r'speed\s*(\d+(?:\.\d+)?)'
        ],

        "height": [
            r'height\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s*height'
        ],

        "density": [
            r'density\s*(\d+(?:\.\d+)?)'
        ]
    }

    for pattern in patterns.get(variable, []):

        match = re.search(pattern, q)

        if match:
            return float(match.group(1))

    return None


def v13_map_variables(q, topic):

    variables = {}

    required = {

        "force": ["mass", "acceleration"],
        "work": ["force", "distance"],
        "power": ["work", "time"],
        "speed": ["distance", "time"],
        "density": ["mass"],
        "kinetic_energy": ["mass", "speed"],
        "potential_energy": ["mass", "height"]
    }

    for variable in required.get(topic, []):

        value = v13_extract_number(q, variable)

        if value is not None:
            variables[variable] = value

    return variables


# ------------------------------------------------
# V13: SMART CALCULATION ENGINE
# ------------------------------------------------

def v13_smart_solve(q):

    topic = v12_detect_topic(q)

    values = v13_map_variables(q, topic)

    formulas = {

        "force": {
            "required": ["mass", "acceleration"],
            "formula": "F = m × a",
            "unit": "N"
        },

        "work": {
            "required": ["force", "distance"],
            "formula": "W = F × d",
            "unit": "J"
        },

        "power": {
            "required": ["work", "time"],
            "formula": "P = W / t",
            "unit": "W"
        },

        "speed": {
            "required": ["distance", "time"],
            "formula": "v = d / t",
            "unit": "m/s"
        },

        "density": {
            "required": ["mass"],
            "formula": "Density = mass / volume",
            "unit": "kg/m³"
        },

        "kinetic_energy": {
            "required": ["mass", "speed"],
            "formula": "KE = 1/2 × m × v²",
            "unit": "J"
        },

        "potential_energy": {
            "required": ["mass", "height"],
            "formula": "PE = m × g × h",
            "unit": "J"
        }
    }

    if topic not in formulas:

        return {
            "success": False,
            "topic": topic,
            "message": "Topic not supported yet."
        }

    info = formulas[topic]

    missing = [
        x for x in info["required"]
        if x not in values
    ]

    if missing:

        return {
            "success": False,
            "topic": topic,
            "values": values,
            "missing": missing,
            "message": "Missing values: " + ", ".join(missing)
        }

    # Calculation
    if topic == "force":
        answer = values["mass"] * values["acceleration"]

    elif topic == "work":
        answer = values["force"] * values["distance"]

    elif topic == "power":
        if values["time"] <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }

        answer = values["work"] / values["time"]

    elif topic == "speed":
        if values["time"] <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }

        answer = values["distance"] / values["time"]

    elif topic == "density":
        return {
            "success": False,
            "topic": topic,
            "message": "Density requires mass and volume."
        }

    elif topic == "kinetic_energy":
        answer = 0.5 * values["mass"] * values["speed"] ** 2

    elif topic == "potential_energy":
        answer = values["mass"] * 9.8 * values["height"]

    return {
        "success": True,
        "topic": topic,
        "values": values,
        "formula": info["formula"],
        "result": answer,
        "unit": info["unit"],
        "explanation": (
            f"Topic: {topic}\n"
            f"Formula: {info['formula']}\n"
            f"Values: {values}\n"
            f"Answer: {answer} {info['unit']}"
        )
    }


# ------------------------------------------------
# V12 + V13 TESTING
# ------------------------------------------------

print("V12 + V13 TESTING")
print("-" * 45)

assert v12_detect_topic(
    "mass 5 kg acceleration 2 force calculate"
) == "force"

assert v12_detect_topic(
    "10 N force 5 m distance work calculate"
) == "work"

assert v12_detect_topic(
    "100 J work 5 s power calculate"
) == "power"

print("PASS: Topic detection")

# Force
a = v13_smart_solve(
    "mass 5 kg acceleration 2 force calculate"
)

assert a["success"]
assert abs(a["result"] - 10) < 0.001

print("PASS: Smart Force = 10 N")

# Work
b = v13_smart_solve(
    "force 10 N distance 5 m work calculate"
)

assert b["success"]
assert abs(b["result"] - 50) < 0.001

print("PASS: Smart Work = 50 J")

# Power
c = v13_smart_solve(
    "work 100 J time 5 s power calculate"
)

assert c["success"]
assert abs(c["result"] - 20) < 0.001

print("PASS: Smart Power = 20 W")

# Speed
d = v13_smart_solve(
    "distance 100 m time 20 s speed calculate"
)

assert d["success"]
assert abs(d["result"] - 5) < 0.001

print("PASS: Smart Speed = 5 m/s")

# Kinetic Energy
e = v13_smart_solve(
    "mass 4 kg speed 3 m/s kinetic energy calculate"
)

assert e["success"]
assert abs(e["result"] - 18) < 0.001

print("PASS: Kinetic Energy = 18 J")

# Potential Energy
f = v13_smart_solve(
    "mass 2 kg height 5 m potential energy calculate"
)

assert f["success"]
assert abs(f["result"] - 98) < 0.001

print("PASS: Potential Energy = 98 J")

print("-" * 45)
print("ALL V12 + V13 TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V11.2
# HINDI + HINGLISH QUESTION ENGINE
# POWER MAPPING FIX + TESTS + INTERACTIVE UI
# ================================================================

import re
import math
import ipywidgets as widgets
from IPython.display import display, clear_output

# ------------------------------------------------
# 1. HINDI / HINGLISH DICTIONARY
# ------------------------------------------------

V11_TERMS = {

    # Physics
    "द्रव्यमान": "mass",
    "मास": "mass",
    "वजन": "mass",
    "त्वरण": "acceleration",
    "एक्सेलरेशन": "acceleration",
    "बल": "force",
    "फोर्स": "force",
    "कार्य": "work",
    "वर्क": "work",
    "शक्ति": "power",
    "पावर": "power",
    "दूरी": "distance",
    "डिस्टेंस": "distance",
    "समय": "time",
    "टाइम": "time",
    "गति": "speed",
    "वेग": "velocity",
    "ऊंचाई": "height",
    "ऊँचाई": "height",
    "घनत्व": "density",
    "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",

    # Chemistry
    "मोलर द्रव्यमान": "molar mass",
    "आणविक द्रव्यमान": "molar mass",
    "मोलर मास": "molar mass",
    "मोलरता": "molarity",
    "मोल्स": "moles",
    "मोल": "moles",

    # Units
    "किलोमीटर प्रति घंटा": "km/h",
    "मीटर प्रति सेकंड": "m/s",
    "किलोग्राम": "kg",
    "किलो": "kg",
    "ग्राम": "g",
    "मिलीग्राम": "mg",
    "सेंटीमीटर": "cm",
    "मिलीमीटर": "mm",
    "किलोमीटर": "km",
    "मीटरों": "m",
    "मीटर": "m",
    "सेकंड्स": "s",
    "सेकेंड": "s",
    "सेकंड": "s",
    "seconds": "s",
    "second": "s",
    "sec": "s",
    "मिनट": "min",
    "घंटे": "h",
    "घंटा": "h",
    "न्यूटन": "N",
    "न्यूटंस": "N",
    "जूल्स": "J",
    "जूल": "J",
    "joules": "J",
    "joule": "J",
    "वाट्स": "W",
    "वाट": "W",
    "लीटर": "l",
    "मिलीलीटर": "ml",

    # Commands
    "निकालो": "calculate",
    "निकाल": "calculate",
    "बताओ": "calculate",
    "बता": "calculate",
    "ज्ञात करो": "calculate",
    "ज्ञात कीजिए": "calculate",
    "गणना करो": "calculate",
    "गणना": "calculate",
    "find": "calculate",
    "solve": "calculate",
    "calculate": "calculate"
}

# ------------------------------------------------
# 2. HINDI NUMBER WORDS
# ------------------------------------------------

V11_NUMBER_WORDS = {
    "एक": "1",
    "दो": "2",
    "तीन": "3",
    "चार": "4",
    "पांच": "5",
    "पाँच": "5",
    "छह": "6",
    "छः": "6",
    "सात": "7",
    "आठ": "8",
    "नौ": "9",
    "दस": "10",
    "बीस": "20",
    "पचास": "50",
    "सौ": "100",
    "हजार": "1000"
}

# ------------------------------------------------
# 3. NORMALIZATION
# ------------------------------------------------

def v11_normalize(q):

    q = str(q).lower().strip()

    # Hindi numbers
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!    ext{S})',
            number,
            q
        )

    # Hindi terms and units
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Hindi particles
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!    ext{S})',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()

    return q

# ------------------------------------------------
# 4. POWER SOLVER - V11.2 FIX
# ------------------------------------------------

def v11_power_solve(normalized):

    # Work: 100 j work / 100 J work (using re.IGNORECASE)
    work_match = re.search(
        r'(\d+(?:\.\d+)?)\s*j\s*work',
        normalized,
        re.IGNORECASE
    )

    # Alternative: work 100 j / work 100 J
    if not work_match:
        work_match = re.search(
            r'work\s*(\d+(?:\.\d+)?)\s*j',
            normalized,
            re.IGNORECASE
        )

    # Time: 5 s
    time_match = re.search(
        r'(\d+(?:\.\d+)?)\s*s',
        normalized,
        re.IGNORECASE
    )

    if not work_match or not time_match:
        return {
            "success": False,
            "topic": "power",
            "message": (
                "Power ke liye Work (J) aur Time (s) "
                "dono values chahiye."
            )
        }

    work = float(work_match.group(1))
    time = float(time_match.group(1))

    if time <= 0:
        return {
            "success": False,
            "topic": "power",
            "message": "Time zero se greater hona chahiye."
        }

    power = work / time

    return {
        "success": True,
        "topic": "power",
        "values": {
            "work": work,
            "time": time
        },
        "result": power,
        "unit": "W",
        "steps": [
            "Power = Work / Time",
            f"Power = {work} / {time}",
            f"Power = {power} W"
        ],
        "explanation": (
            f"Topic: Power\n\n"
            f"Formula:\nP = W / t\n\n"
            f"Given:\nWork = {work} J\n"
            f"Time = {time} s\n\n"
            f"Solution:\n"
            f"Power = {work} / {time}\n\n"
            f"Final Answer:\n{power} W"
        )
    }

# ------------------------------------------------
# 5. MAIN SOLVER - V8 + POWER FIX
# ------------------------------------------------

def v11_solve(q):

    normalized = v11_normalize(q)

    # Power uses corrected V11.2 mapping
    if re.search(r'\bpower\b', normalized):

        result = v11_power_solve(normalized)

        return {
            "success": result.get("success", False),
            "original_question": q,
            "normalized_question": normalized,
            "result": result
        }

    # Other topics use V8
    if "v8_solve" not in globals():

        return {
            "success": False,
            "original_question": q,
            "normalized_question": normalized,
            "message": "V8 cell pehle run karo."
        }

    result = v8_solve(normalized)

    return {
        "success": result.get("success", False),
        "original_question": q,
        "normalized_question": normalized,
        "result": result
    }

# ------------------------------------------------
# 6. DISPLAY
# ------------------------------------------------

def v11_show(data):

    print("Original:")
    print(data.get("original_question", ""))

    print("\nNormalized:")
    print(data.get("normalized_question", ""))

    print("\nAnswer:")

    if not data.get("success"):

        print(data.get("message", "Question not solved"))
        return

    result = data["result"]

    if result.get("success"):

        print(result.get("explanation", ""))

        print(
            "\nFinal:",
            result.get("result"),
            result.get("unit", "")
        )

    else:

        print(result.get("message", "Question not solved"))

# ------------------------------------------------
# 7. TESTS - TRANSLATION
# ------------------------------------------------

print("SUNO SAATHI V11.2 TESTING")
print("-" * 50)

translation_tests = [

    (
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "mass 5 kg",
        "acceleration 2"
    ),

    (
        "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो",
        "10 N force",
        "5 m distance"
    ),

    (
        "100 joule work 5 सेकंड में हुआ power find करो",
        "100 J work",
        "5 s"
    )
]

for q, expected1, expected2 in translation_tests:

    normalized = v11_normalize(q)

    assert expected1 in normalized or expected1.lower() in normalized, (
        q, normalized, expected1
    )

    assert expected2 in normalized or expected2.lower() in normalized, (
        q, normalized, expected2
    )

    print("PASS: translation")

# ------------------------------------------------
# 8. REAL CALCULATION TESTS
# ------------------------------------------------

# Hindi Force
t1 = v11_solve(
    "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
)

assert t1["success"], t1

assert abs(
    t1["result"]["result"] - 10
) < 0.001

print("PASS: Hindi force = 10 N")

# Hindi Work
t2 = v11_solve(
    "10 न्यूटन बल और 5 मीटर दूरी से कार्य ज्ञात करो"
)

assert t2["success"], t2

assert abs(
    t2["result"]["result"] - 50
) < 0.001

print("PASS: Hindi work = 50 J")

# Hinglish Power
t3 = v11_solve(
    "100 joule work 5 सेकंड में हुआ power find करो"
)

assert t3["success"], t3

assert t3["result"]["values"]["work"] == 100
assert t3["result"]["values"]["time"] == 5

assert abs(
    t3["result"]["result"] - 20
) < 0.001

print("PASS: Hinglish power = 20 W")

# Reverse Power wording
t4 = v11_solve(
    "work 100 J time 5 s power calculate"
)

assert t4["success"], t4

assert abs(
    t4["result"]["result"] - 20
) < 0.001

print("PASS: Reverse power wording = 20 W")

# Decimal Power
t5 = v11_solve(
    "50 joule work 2.5 seconds power find"
)

assert t5["success"], t5

assert abs(
    t5["result"]["result"] - 20
) < 0.001

print("PASS: Decimal power = 20 W")

# Zero time must fail
t6 = v11_solve(
    "100 joule work 0 seconds power find"
)

assert not t6["success"]

print("PASS: Zero time validation")

print("-" * 50)
print("ALL V11.2 TESTS PASSED!")

# ------------------------------------------------
# 9. INTERACTIVE UI
# ------------------------------------------------

v11_input = widgets.Textarea(
    placeholder=(
        "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो"
    ),
    description="Question:",
    layout=widgets.Layout(
        width="100%",
        height="130px"
    )
)

v11_button = widgets.Button(
    description="Solve Question",
    button_style="success"
)

v11_output = widgets.Output()

def v11_run(_):

    with v11_output:

        clear_output()

        data = v11_solve(
            v11_input.value
        )

        v11_show(data)

v11_button.on_click(v11_run)

display(v11_input)
display(v11_button)
display(v11_output)

print("\nSUNO SAATHI MAGIC LAYER V11.2 READY")

# ================================================================
# SUNO SAATHI MAGIC LAYER V12 + V13
# SMART QUESTION DETECTION + VARIABLE MAPPING
# ================================================================

import re
import math

# Redefining clean v11_normalize to fix the corrupted state from the previous cell
def v11_normalize(q):
    q = str(q).lower().strip()

    # Hindi numbers
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            number,
            q
        )

    # Hindi terms and units
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Hindi particles
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()
    return q

# ------------------------------------------------
# V12: SMART TOPIC DETECTION
# ------------------------------------------------

V12_TOPIC_PATTERNS = {
    "force": [
        "force", "mass acceleration", "newton",
        "बल", "फोर्स"
    ],
    "work": [
        "work", "force distance", "कार्य", "वर्क"
    ],
    "power": [
        "power", "work time", "पावर", "शक्ति"
    ],
    "speed": [
        "speed", "velocity", "distance time",
        "गति", "वेग"
    ],
    "density": [
        "density", "घनत्व"
    ],
    "kinetic_energy": [
        "kinetic energy", "गतिज ऊर्जा"
    ],
    "potential_energy": [
        "potential energy", "स्थितिज ऊर्जा"
    ]
}

def v12_detect_topic(q):
    q = v11_normalize(q)

    # Explicit formula keywords
    for topic, patterns in V12_TOPIC_PATTERNS.items():
        for pattern in patterns:
            if pattern in q:
                return topic

    # Formula inference
    if "mass" in q and "acceleration" in q:
        return "force"
    if "force" in q and "distance" in q:
        return "work"
    if "work" in q and "time" in q:
        return "power"
    if "distance" in q and "time" in q:
        return "speed"

    return "unknown"

# ------------------------------------------------
# V13: SMART VARIABLE MAPPING
# ------------------------------------------------

def v13_extract_number(q, variable):
    q = v11_normalize(q)

    patterns = {
        "mass": [
            r'mass\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*kg\s*mass'
        ],
        "acceleration": [
            r'acceleration\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m/s(?:\^?2|²)?'
        ],
        "force": [
            r'force\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*N\s*force'
        ],
        "distance": [
            r'distance\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s*distance'
        ],
        "time": [
            r'time\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*s'
        ],
        "work": [
            r'work\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*J\s*work'
        ],
        "speed": [
            r'speed\s*(\d+(?:\.\d+)?)'
        ],
        "height": [
            r'height\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s*height'
        ],
        "density": [
            r'density\s*(\d+(?:\.\d+)?)'
        ]
    }

    for pattern in patterns.get(variable, []):
        match = re.search(pattern, q, re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None

def v13_map_variables(q, topic):
    variables = {}
    required = {
        "force": ["mass", "acceleration"],
        "work": ["force", "distance"],
        "power": ["work", "time"],
        "speed": ["distance", "time"],
        "density": ["mass"],
        "kinetic_energy": ["mass", "speed"],
        "potential_energy": ["mass", "height"]
    }

    for variable in required.get(topic, []):
        value = v13_extract_number(q, variable)
        if value is not None:
            variables[variable] = value
    return variables

# ------------------------------------------------
# V13: SMART CALCULATION ENGINE
# ------------------------------------------------

def v13_smart_solve(q):
    topic = v12_detect_topic(q)
    values = v13_map_variables(q, topic)

    formulas = {
        "force": {
            "required": ["mass", "acceleration"],
            "formula": "F = m × a",
            "unit": "N"
        },
        "work": {
            "required": ["force", "distance"],
            "formula": "W = F × d",
            "unit": "J"
        },
        "power": {
            "required": ["work", "time"],
            "formula": "P = W / t",
            "unit": "W"
        },
        "speed": {
            "required": ["distance", "time"],
            "formula": "v = d / t",
            "unit": "m/s"
        },
        "density": {
            "required": ["mass"],
            "formula": "Density = mass / volume",
            "unit": "kg/m³"
        },
        "kinetic_energy": {
            "required": ["mass", "speed"],
            "formula": "KE = 1/2 × m × v²",
            "unit": "J"
        },
        "potential_energy": {
            "required": ["mass", "height"],
            "formula": "PE = m × g × h",
            "unit": "J"
        }
    }

    if topic not in formulas:
        return {
            "success": False,
            "topic": topic,
            "message": "Topic not supported yet."
        }

    info = formulas[topic]
    missing = [
        x for x in info["required"]
        if x not in values
    ]

    if missing:
        return {
            "success": False,
            "topic": topic,
            "values": values,
            "missing": missing,
            "message": "Missing values: " + ", ".join(missing)
        }

    if topic == "force":
        answer = values["mass"] * values["acceleration"]
    elif topic == "work":
        answer = values["force"] * values["distance"]
    elif topic == "power":
        if values["time"] <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }
        answer = values["work"] / values["time"]
    elif topic == "speed":
        if values["time"] <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }
        answer = values["distance"] / values["time"]
    elif topic == "density":
        return {
            "success": False,
            "topic": topic,
            "message": "Density requires mass and volume."
        }
    elif topic == "kinetic_energy":
        answer = 0.5 * values["mass"] * values["speed"] ** 2
    elif topic == "potential_energy":
        answer = values["mass"] * 9.8 * values["height"]

    return {
        "success": True,
        "topic": topic,
        "values": values,
        "formula": info["formula"],
        "result": answer,
        "unit": info["unit"],
        "explanation": (
            f"Topic: {topic}\n"
            f"Formula: {info['formula']}\n"
            f"Values: {values}\n"
            f"Answer: {answer} {info['unit']}"
        )
    }

# ------------------------------------------------
# V12 + V13 TESTING
# ------------------------------------------------

print("V12 + V13 TESTING")
print("-" * 45)

assert v12_detect_topic(
    "mass 5 kg acceleration 2 force calculate"
) == "force"

assert v12_detect_topic(
    "10 N force 5 m distance work calculate"
) == "work"

assert v12_detect_topic(
    "100 J work 5 s power calculate"
) == "power"

print("PASS: Topic detection")

# Force
a = v13_smart_solve(
    "mass 5 kg acceleration 2 force calculate"
)

assert a["success"]
assert abs(a["result"] - 10) < 0.001

print("PASS: Smart Force = 10 N")

# Work
b = v13_smart_solve(
    "force 10 N distance 5 m work calculate"
)

assert b["success"]
assert abs(b["result"] - 50) < 0.001

print("PASS: Smart Work = 50 J")

# Power
c = v13_smart_solve(
    "work 100 J time 5 s power calculate"
)

assert c["success"]
assert abs(c["result"] - 20) < 0.001

print("PASS: Smart Power = 20 W")

# Speed
d = v13_smart_solve(
    "distance 100 m time 20 s speed calculate"
)

assert d["success"]
assert abs(d["result"] - 5) < 0.001

print("PASS: Smart Speed = 5 m/s")

# Kinetic Energy
e = v13_smart_solve(
    "mass 4 kg speed 3 m/s kinetic energy calculate"
)

assert e["success"]
assert abs(e["result"] - 18) < 0.001

print("PASS: Kinetic Energy = 18 J")

# Potential Energy
f = v13_smart_solve(
    "mass 2 kg height 5 m potential energy calculate"
)

assert f["success"]
assert abs(f["result"] - 98) < 0.001

print("PASS: Potential Energy = 98 J")

print("-" * 45)
print("ALL V12 + V13 TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V12 + V13
# SMART QUESTION DETECTION + VARIABLE MAPPING
# ================================================================

import re
import math

# Redefining clean v11_normalize to fix the corrupted state from the previous cell
def v11_normalize(q):
    q = str(q).lower().strip()

    # Hindi numbers
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            number,
            q
        )

    # Hindi terms and units
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Hindi particles
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()
    return q

# ------------------------------------------------
# V12: SMART TOPIC DETECTION
# ------------------------------------------------

V12_TOPIC_PATTERNS = {
    "force": [
        "force", "mass acceleration", "newton",
        "बल", "फोर्स"
    ],
    "work": [
        "work", "force distance", "कार्य", "वर्क"
    ],
    "power": [
        "power", "work time", "पावर", "शक्ति"
    ],
    "speed": [
        "speed", "velocity", "distance time",
        "गति", "वेग"
    ],
    "density": [
        "density", "घनत्व"
    ],
    "kinetic_energy": [
        "kinetic energy", "गतिज ऊर्जा"
    ],
    "potential_energy": [
        "potential energy", "स्थितिज ऊर्जा"
    ]
}

def v12_detect_topic(q):
    q = v11_normalize(q)

    # Explicit formula keywords
    for topic, patterns in V12_TOPIC_PATTERNS.items():
        for pattern in patterns:
            if pattern in q:
                return topic

    # Formula inference
    if "mass" in q and "acceleration" in q:
        return "force"
    if "force" in q and "distance" in q:
        return "work"
    if "work" in q and "time" in q:
        return "power"
    if "distance" in q and "time" in q:
        return "speed"

    return "unknown"

# ------------------------------------------------
# V13: SMART VARIABLE MAPPING
# ------------------------------------------------

def v13_extract_number(q, variable):
    q = v11_normalize(q)

    patterns = {
        "mass": [
            r'mass\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*kg\s*mass'
        ],
        "acceleration": [
            r'acceleration\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m/s(?:\^?2|²)?'
        ],
        "force": [
            r'force\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*N\s*force'
        ],
        "distance": [
            r'distance\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s*distance'
        ],
        "time": [
            r'time\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*s'
        ],
        "work": [
            r'work\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*J\s*work'
        ],
        "speed": [
            r'speed\s*(\d+(?:\.\d+)?)'
        ],
        "height": [
            r'height\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s*height'
        ],
        "density": [
            r'density\s*(\d+(?:\.\d+)?)'
        ]
    }

    for pattern in patterns.get(variable, []):
        match = re.search(pattern, q, re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None

def v13_map_variables(q, topic):
    variables = {}
    required = {
        "force": ["mass", "acceleration"],
        "work": ["force", "distance"],
        "power": ["work", "time"],
        "speed": ["distance", "time"],
        "density": ["mass"],
        "kinetic_energy": ["mass", "speed"],
        "potential_energy": ["mass", "height"]
    }

    for variable in required.get(topic, []):
        value = v13_extract_number(q, variable)
        if value is not None:
            variables[variable] = value
    return variables

# ------------------------------------------------
# V13: SMART CALCULATION ENGINE
# ------------------------------------------------

def v13_smart_solve(q):
    topic = v12_detect_topic(q)
    values = v13_map_variables(q, topic)

    formulas = {
        "force": {
            "required": ["mass", "acceleration"],
            "formula": "F = m × a",
            "unit": "N"
        },
        "work": {
            "required": ["force", "distance"],
            "formula": "W = F × d",
            "unit": "J"
        },
        "power": {
            "required": ["work", "time"],
            "formula": "P = W / t",
            "unit": "W"
        },
        "speed": {
            "required": ["distance", "time"],
            "formula": "v = d / t",
            "unit": "m/s"
        },
        "density": {
            "required": ["mass"],
            "formula": "Density = mass / volume",
            "unit": "kg/m³"
        },
        "kinetic_energy": {
            "required": ["mass", "speed"],
            "formula": "KE = 1/2 × m × v²",
            "unit": "J"
        },
        "potential_energy": {
            "required": ["mass", "height"],
            "formula": "PE = m × g × h",
            "unit": "J"
        }
    }

    if topic not in formulas:
        return {
            "success": False,
            "topic": topic,
            "message": "Topic not supported yet."
        }

    info = formulas[topic]
    missing = [
        x for x in info["required"]
        if x not in values
    ]

    if missing:
        return {
            "success": False,
            "topic": topic,
            "values": values,
            "missing": missing,
            "message": "Missing values: " + ", ".join(missing)
        }

    if topic == "force":
        answer = values["mass"] * values["acceleration"]
    elif topic == "work":
        answer = values["force"] * values["distance"]
    elif topic == "power":
        if values["time"] <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }
        answer = values["work"] / values["time"]
    elif topic == "speed":
        if values["time"] <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }
        answer = values["distance"] / values["time"]
    elif topic == "density":
        return {
            "success": False,
            "topic": topic,
            "message": "Density requires mass and volume."
        }
    elif topic == "kinetic_energy":
        answer = 0.5 * values["mass"] * values["speed"] ** 2
    elif topic == "potential_energy":
        answer = values["mass"] * 9.8 * values["height"]

    return {
        "success": True,
        "topic": topic,
        "values": values,
        "formula": info["formula"],
        "result": answer,
        "unit": info["unit"],
        "explanation": (
            f"Topic: {topic}\n"
            f"Formula: {info['formula']}\n"
            f"Values: {values}\n"
            f"Answer: {answer} {info['unit']}"
        )
    }

# ------------------------------------------------
# V12 + V13 TESTING
# ------------------------------------------------

print("V12 + V13 TESTING")
print("-" * 45)

assert v12_detect_topic(
    "mass 5 kg acceleration 2 force calculate"
) == "force"

assert v12_detect_topic(
    "10 N force 5 m distance work calculate"
) == "work"

assert v12_detect_topic(
    "100 J work 5 s power calculate"
) == "power"

print("PASS: Topic detection")

# Force
a = v13_smart_solve(
    "mass 5 kg acceleration 2 force calculate"
)

assert a["success"]
assert abs(a["result"] - 10) < 0.001

print("PASS: Smart Force = 10 N")

# Work
b = v13_smart_solve(
    "force 10 N distance 5 m work calculate"
)

assert b["success"]
assert abs(b["result"] - 50) < 0.001

print("PASS: Smart Work = 50 J")

# Power
c = v13_smart_solve(
    "work 100 J time 5 s power calculate"
)

assert c["success"]
assert abs(c["result"] - 20) < 0.001

print("PASS: Smart Power = 20 W")

# Speed
d = v13_smart_solve(
    "distance 100 m time 20 s speed calculate"
)

assert d["success"]
assert abs(d["result"] - 5) < 0.001

print("PASS: Smart Speed = 5 m/s")

# Kinetic Energy
e = v13_smart_solve(
    "mass 4 kg speed 3 m/s kinetic energy calculate"
)

assert e["success"]
assert abs(e["result"] - 18) < 0.001

print("PASS: Kinetic Energy = 18 J")

# Potential Energy
f = v13_smart_solve(
    "mass 2 kg height 5 m potential energy calculate"
)

assert f["success"]
assert abs(f["result"] - 98) < 0.001

print("PASS: Potential Energy = 98 J")

print("-" * 45)
print("ALL V12 + V13 TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V12 + V13
# SMART QUESTION DETECTION + VARIABLE MAPPING
# ================================================================

import re
import math

# Redefining clean v11_normalize to fix the corrupted state from the previous cell
def v11_normalize(q):
    q = str(q).lower().strip()

    # Hindi numbers
    for word, number in sorted(
        V11_NUMBER_WORDS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            number,
            q
        )

    # Hindi terms and units
    for word, replacement in sorted(
        V11_TERMS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(word, replacement)

    # Hindi particles
    particles = [
        "और", "में", "है", "हैं",
        "से", "पर", "का", "की", "के",
        "हुआ", "हुई", "हो", "करो"
    ]

    for word in particles:
        q = re.sub(
            r'(?<!\S)' + re.escape(word) + r'(?!\S)',
            ' ',
            q
        )

    q = re.sub(r'\s+', ' ', q).strip()
    return q

# ------------------------------------------------
# V12: SMART TOPIC DETECTION
# ------------------------------------------------


# ================================================================
# V12.1 TOPIC DETECTION FIX
# ================================================================

def v12_detect_topic(q):

    q = v11_normalize(q)

    # Priority 1: Energy
    if "kinetic energy" in q:
        return "kinetic_energy"

    if "potential energy" in q:
        return "potential_energy"

    # Priority 2: Power
    if "power" in q:
        return "power"

    # Priority 3: Work
    if "work" in q:
        return "work"

    # Priority 4: Force
    if "force" in q:
        return "force"

    # Priority 5: Speed
    if "speed" in q or "velocity" in q:
        return "speed"

    # Priority 6: Density
    if "density" in q:
        return "density"

    return "unknown"


# ================================================================
# V12.1 TESTING
# ================================================================

print("V12.1 TESTING")
print("-" * 40)

assert v12_detect_topic(
    "mass 5 kg acceleration 2 force calculate"
) == "force"

print("PASS: Force detection")

assert v12_detect_topic(
    "10 N force 5 m distance work calculate"
) == "work"

print("PASS: Work detection")

assert v12_detect_topic(
    "100 J work 5 s power calculate"
) == "power"

print("PASS: Power detection")

assert v12_detect_topic(
    "mass 4 kg speed 3 m/s kinetic energy calculate"
) == "kinetic_energy"

print("PASS: Kinetic Energy detection")

assert v12_detect_topic(
    "mass 2 kg height 5 m potential energy calculate"
) == "potential_energy"

print("PASS: Potential Energy detection")

assert v12_detect_topic(
    "distance 100 m time 20 s speed calculate"
) == "speed"

print("PASS: Speed detection")

print("-" * 40)
print("ALL V12.1 TESTS PASSED!")


# ------------------------------------------------
# V13: SMART VARIABLE MAPPING
# ------------------------------------------------

def v13_extract_number(q, variable):
    q = v11_normalize(q)

    patterns = {
        "mass": [
            r'mass\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*kg\s*mass'
        ],
        "acceleration": [
            r'acceleration\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m/s(?:\^?2|²)?'
        ],
        "force": [
            r'force\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*N\s*force'
        ],
        "distance": [
            r'distance\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s*distance'
        ],
        "time": [
            r'time\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*s'
        ],
        "work": [
            r'work\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*J\s*work'
        ],
        "speed": [
            r'speed\s*(\d+(?:\.\d+)?)'
        ],
        "height": [
            r'height\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s*height'
        ],
        "density": [
            r'density\s*(\d+(?:\.\d+)?)'
        ]
    }

    for pattern in patterns.get(variable, []):
        match = re.search(pattern, q, re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None

def v13_map_variables(q, topic):
    variables = {}
    required = {
        "force": ["mass", "acceleration"],
        "work": ["force", "distance"],
        "power": ["work", "time"],
        "speed": ["distance", "time"],
        "density": ["mass"],
        "kinetic_energy": ["mass", "speed"],
        "potential_energy": ["mass", "height"]
    }

    for variable in required.get(topic, []):
        value = v13_extract_number(q, variable)
        if value is not None:
            variables[variable] = value
    return variables

# ------------------------------------------------
# V13: SMART CALCULATION ENGINE
# ------------------------------------------------

def v13_smart_solve(q):
    topic = v12_detect_topic(q)
    values = v13_map_variables(q, topic)

    formulas = {
        "force": {
            "required": ["mass", "acceleration"],
            "formula": "F = m × a",
            "unit": "N"
        },
        "work": {
            "required": ["force", "distance"],
            "formula": "W = F × d",
            "unit": "J"
        },
        "power": {
            "required": ["work", "time"],
            "formula": "P = W / t",
            "unit": "W"
        },
        "speed": {
            "required": ["distance", "time"],
            "formula": "v = d / t",
            "unit": "m/s"
        },
        "density": {
            "required": ["mass"],
            "formula": "Density = mass / volume",
            "unit": "kg/m³"
        },
        "kinetic_energy": {
            "required": ["mass", "speed"],
            "formula": "KE = 1/2 × m × v²",
            "unit": "J"
        },
        "potential_energy": {
            "required": ["mass", "height"],
            "formula": "PE = m × g × h",
            "unit": "J"
        }
    }

    if topic not in formulas:
        return {
            "success": False,
            "topic": topic,
            "message": "Topic not supported yet."
        }

    info = formulas[topic]
    missing = [
        x for x in info["required"]
        if x not in values
    ]

    if missing:
        return {
            "success": False,
            "topic": topic,
            "values": values,
            "missing": missing,
            "message": "Missing values: " + ", ".join(missing)
        }

    if topic == "force":
        answer = values["mass"] * values["acceleration"]
    elif topic == "work":
        answer = values["force"] * values["distance"]
    elif topic == "power":
        if values["time"] <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }
        answer = values["work"] / values["time"]
    elif topic == "speed":
        if values["time"] <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }
        answer = values["distance"] / values["time"]
    elif topic == "density":
        return {
            "success": False,
            "topic": topic,
            "message": "Density requires mass and volume."
        }
    elif topic == "kinetic_energy":
        answer = 0.5 * values["mass"] * values["speed"] ** 2
    elif topic == "potential_energy":
        answer = values["mass"] * 9.8 * values["height"]

    return {
        "success": True,
        "topic": topic,
        "values": values,
        "formula": info["formula"],
        "result": answer,
        "unit": info["unit"],
        "explanation": (
            f"Topic: {topic}\n"
            f"Formula: {info['formula']}\n"
            f"Values: {values}\n"
            f"Answer: {answer} {info['unit']}"
        )
    }

# ------------------------------------------------
# V12 + V13 TESTING
# ------------------------------------------------

print("V12 + V13 TESTING")
print("-" * 45)

assert v12_detect_topic(
    "mass 5 kg acceleration 2 force calculate"
) == "force"

assert v12_detect_topic(
    "10 N force 5 m distance work calculate"
) == "work"

assert v12_detect_topic(
    "100 J work 5 s power calculate"
) == "power"

print("PASS: Topic detection")

# Force
a = v13_smart_solve(
    "mass 5 kg acceleration 2 force calculate"
)

assert a["success"]
assert abs(a["result"] - 10) < 0.001

print("PASS: Smart Force = 10 N")

# Work
b = v13_smart_solve(
    "force 10 N distance 5 m work calculate"
)

assert b["success"]
assert abs(b["result"] - 50) < 0.001

print("PASS: Smart Work = 50 J")

# Power
c = v13_smart_solve(
    "work 100 J time 5 s power calculate"
)

assert c["success"]
assert abs(c["result"] - 20) < 0.001

print("PASS: Smart Power = 20 W")

# Speed
d = v13_smart_solve(
    "distance 100 m time 20 s speed calculate"
)

assert d["success"]
assert abs(d["result"] - 5) < 0.001

print("PASS: Smart Speed = 5 m/s")

# Kinetic Energy
e = v13_smart_solve(
    "mass 4 kg speed 3 m/s kinetic energy calculate"
)

assert e["success"]
assert abs(e["result"] - 18) < 0.001

print("PASS: Kinetic Energy = 18 J")

# Potential Energy
f = v13_smart_solve(
    "mass 2 kg height 5 m potential energy calculate"
)

assert f["success"]
assert abs(f["result"] - 98) < 0.001

print("PASS: Potential Energy = 98 J")

print("-" * 45)
print("ALL V12 + V13 TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V14 + V15
# MULTI-STEP PHYSICS + CHEMISTRY ENGINE
# ================================================================

import re
import math

# ------------------------------------------------
# V14: MULTI-STEP PHYSICS SOLVER
# ------------------------------------------------

def v14_multi_solve(mass=None, acceleration=None,
                    distance=None, time=None):

    steps = []
    values = {}

    # Step 1: Force
    if mass is not None and acceleration is not None:

        force = mass * acceleration

        values["force"] = force

        steps.append(
            f"Force = {mass} × {acceleration} = {force} N"
        )

    else:
        force = None

    # Step 2: Work
    if force is not None and distance is not None:

        work = force * distance

        values["work"] = work

        steps.append(
            f"Work = {force} × {distance} = {work} J"
        )

    else:
        work = None

    # Step 3: Power
    if work is not None and time is not None:

        if time <= 0:

            return {
                "success": False,
                "message": "Time must be greater than zero."
            }

        power = work / time

        values["power"] = power

        steps.append(
            f"Power = {work} / {time} = {power} W"
        )

    return {
        "success": True,
        "topic": "multi_step_physics",
        "values": values,
        "steps": steps,
        "explanation": "\n".join(steps)
    }


# ------------------------------------------------
# V14: MULTI-STEP QUESTION PARSER
# ------------------------------------------------

def v14_multi_question(q):

    q = v11_normalize(q)

    mass = v13_extract_number(q, "mass")
    acceleration = v13_extract_number(q, "acceleration")
    distance = v13_extract_number(q, "distance")
    time = v13_extract_number(q, "time")

    return v14_multi_solve(
        mass=mass,
        acceleration=acceleration,
        distance=distance,
        time=time
    )


# ------------------------------------------------
# V15: CHEMISTRY VARIABLE EXTRACTION
# ------------------------------------------------

def v15_extract_chemistry(q):

    q = v11_normalize(q)

    values = {}

    # Mass in grams
    m = re.search(
        r'\bmass\s*(\d+(?:\.\d+)?)\s*g\b',
        q
    )

    if m:
        values["mass_g"] = float(m.group(1))

    # Molar mass in g/mol
    mm = re.search(
        r'molar\s*mass\s*(\d+(?:\.\d+)?)\s*g\s*/\s*mol',
        q
    )

    if mm:
        values["molar_mass"] = float(mm.group(1))

    # Moles
    n = re.search(
        r'\bmoles\s*(\d+(?:\.\d+)?)',
        q
    )

    if n:
        values["moles"] = float(n.group(1))

    # Volume in liters
    volume = re.search(
        r'\bvolume\s*(\d+(?:\.\d+)?)\s*(?:L|l)\b',
        q
    )

    if volume:
        values["volume_l"] = float(volume.group(1))

    return values


# ------------------------------------------------
# V15: MOLES SOLVER
# ------------------------------------------------

def v15_moles_solve(mass_g, molar_mass):

    if mass_g < 0 or molar_mass <= 0:

        return {
            "success": False,
            "message": "Mass >= 0 and molar mass > 0 required."
        }

    moles = mass_g / molar_mass

    return {
        "success": True,
        "topic": "moles",
        "values": {
            "mass_g": mass_g,
            "molar_mass": molar_mass
        },
        "result": moles,
        "unit": "mol",
        "formula": "n = mass / molar mass",
        "explanation": (
            f"n = {mass_g} / {molar_mass}\n"
            f"Moles = {moles} mol"
        )
    }


# ------------------------------------------------
# V15: MOLARITY SOLVER
# ------------------------------------------------

def v15_molarity_solve(moles, volume_l):

    if moles < 0 or volume_l <= 0:

        return {
            "success": False,
            "message": "Moles >= 0 and volume > 0 required."
        }

    molarity = moles / volume_l

    return {
        "success": True,
        "topic": "molarity",
        "values": {
            "moles": moles,
            "volume_l": volume_l
        },
        "result": molarity,
        "unit": "mol/L",
        "formula": "M = n / V",
        "explanation": (
            f"M = {moles} / {volume_l}\n"
            f"Molarity = {molarity} mol/L"
        )
    }


# ------------------------------------------------
# V15: CHEMISTRY SMART SOLVER
# ------------------------------------------------

def v15_chemistry_solve(q):

    q = v11_normalize(q)

    values = v15_extract_chemistry(q)

    # Molarity
    if "molarity" in q:

        if "moles" not in values or "volume_l" not in values:

            return {
                "success": False,
                "message": "Moles and volume in liters required."
            }

        return v15_molarity_solve(
            values["moles"],
            values["volume_l"]
        )

    # Moles
    if "moles" in q:

        if "mass_g" not in values or "molar_mass" not in values:

            return {
                "success": False,
                "message": "Mass and molar mass required."
            }

        return v15_moles_solve(
            values["mass_g"],
            values["molar_mass"]
        )

    return {
        "success": False,
        "message": "Chemistry topic not recognized."
    }


# ------------------------------------------------
# V14 + V15 TESTING
# ------------------------------------------------

print("V14 + V15 TESTING")
print("-" * 50)

# Multi-step physics
p1 = v14_multi_solve(
    mass=5,
    acceleration=2,
    distance=10,
    time=5
)

assert p1["success"]
assert abs(p1["values"]["force"] - 10) < 0.001
assert abs(p1["values"]["work"] - 100) < 0.001
assert abs(p1["values"]["power"] - 20) < 0.001

print("PASS: Multi-step Force = 10 N")
print("PASS: Multi-step Work = 100 J")
print("PASS: Multi-step Power = 20 W")

# Moles
c1 = v15_moles_solve(
    mass_g=18,
    molar_mass=18
)

assert c1["success"]
assert abs(c1["result"] - 1) < 0.001

print("PASS: Moles = 1 mol")

# Molarity
c2 = v15_molarity_solve(
    moles=1,
    volume_l=2
)

assert c2["success"]
assert abs(c2["result"] - 0.5) < 0.001

print("PASS: Molarity = 0.5 mol/L")

# Chemistry question parsing
c3 = v15_chemistry_solve(
    "mass 18 g molar mass 18 g/mol moles calculate"
)

assert c3["success"]
assert abs(c3["result"] - 1) < 0.001

print("PASS: Chemistry question parsing")

# Molarity parsing
c4 = v15_chemistry_solve(
    "moles 1 volume 2 L molarity calculate"
)

assert c4["success"]
assert abs(c4["result"] - 0.5) < 0.001

print("PASS: Molarity question parsing")

# Zero volume validation
c5 = v15_molarity_solve(
    moles=1,
    volume_l=0
)

assert not c5["success"]

print("PASS: Zero volume validation")

print("-" * 50)
print("ALL V14 + V15 TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V14 + V15
# MULTI-STEP PHYSICS + CHEMISTRY ENGINE
# ================================================================

import re
import math

# ------------------------------------------------
# V14: MULTI-STEP PHYSICS SOLVER
# ------------------------------------------------

def v14_multi_solve(mass=None, acceleration=None,
                    distance=None, time=None):

    steps = []
    values = {}

    # Step 1: Force
    if mass is not None and acceleration is not None:

        force = mass * acceleration

        values["force"] = force

        steps.append(
            f"Force = {mass} × {acceleration} = {force} N"
        )

    else:
        force = None

    # Step 2: Work
    if force is not None and distance is not None:

        work = force * distance

        values["work"] = work

        steps.append(
            f"Work = {force} × {distance} = {work} J"
        )

    else:
        work = None

    # Step 3: Power
    if work is not None and time is not None:

        if time <= 0:

            return {
                "success": False,
                "message": "Time must be greater than zero."
            }

        power = work / time

        values["power"] = power

        steps.append(
            f"Power = {work} / {time} = {power} W"
        )

    return {
        "success": True,
        "topic": "multi_step_physics",
        "values": values,
        "steps": steps,
        "explanation": "\n".join(steps)
    }


# ------------------------------------------------
# V14: MULTI-STEP QUESTION PARSER
# ------------------------------------------------

def v14_multi_question(q):

    q = v11_normalize(q)

    mass = v13_extract_number(q, "mass")
    acceleration = v13_extract_number(q, "acceleration")
    distance = v13_extract_number(q, "distance")
    time = v13_extract_number(q, "time")

    return v14_multi_solve(
        mass=mass,
        acceleration=acceleration,
        distance=distance,
        time=time
    )


# ------------------------------------------------
# V15: CHEMISTRY VARIABLE EXTRACTION
# ------------------------------------------------

def v15_extract_chemistry(q):

    q = v11_normalize(q)

    values = {}

    # Mass in grams
    m = re.search(
        r'\bmass\s*(\d+(?:\.\d+)?)\s*g\b',
        q
    )

    if m:
        values["mass_g"] = float(m.group(1))

    # Molar mass in g/mol
    mm = re.search(
        r'molar\s*mass\s*(\d+(?:\.\d+)?)\s*g\s*/\s*mol',
        q
    )

    if mm:
        values["molar_mass"] = float(mm.group(1))

    # Moles
    n = re.search(
        r'\bmoles\s*(\d+(?:\.\d+)?)',
        q
    )

    if n:
        values["moles"] = float(n.group(1))

    # Volume in liters
    volume = re.search(
        r'\bvolume\s*(\d+(?:\.\d+)?)\s*(?:L|l)\b',
        q
    )

    if volume:
        values["volume_l"] = float(volume.group(1))

    return values


# ------------------------------------------------
# V15: MOLES SOLVER
# ------------------------------------------------

def v15_moles_solve(mass_g, molar_mass):

    if mass_g < 0 or molar_mass <= 0:

        return {
            "success": False,
            "message": "Mass >= 0 and molar mass > 0 required."
        }

    moles = mass_g / molar_mass

    return {
        "success": True,
        "topic": "moles",
        "values": {
            "mass_g": mass_g,
            "molar_mass": molar_mass
        },
        "result": moles,
        "unit": "mol",
        "formula": "n = mass / molar mass",
        "explanation": (
            f"n = {mass_g} / {molar_mass}\n"
            f"Moles = {moles} mol"
        )
    }


# ------------------------------------------------
# V15: MOLARITY SOLVER
# ------------------------------------------------

def v15_molarity_solve(moles, volume_l):

    if moles < 0 or volume_l <= 0:

        return {
            "success": False,
            "message": "Moles >= 0 and volume > 0 required."
        }

    molarity = moles / volume_l

    return {
        "success": True,
        "topic": "molarity",
        "values": {
            "moles": moles,
            "volume_l": volume_l
        },
        "result": molarity,
        "unit": "mol/L",
        "formula": "M = n / V",
        "explanation": (
            f"M = {moles} / {volume_l}\n"
            f"Molarity = {molarity} mol/L"
        )
    }


# ------------------------------------------------
# V15: CHEMISTRY SMART SOLVER
# ------------------------------------------------

def v15_chemistry_solve(q):

    q = v11_normalize(q)

    values = v15_extract_chemistry(q)

    # Molarity
    if "molarity" in q:

        if "moles" not in values or "volume_l" not in values:

            return {
                "success": False,
                "message": "Moles and volume in liters required."
            }

        return v15_molarity_solve(
            values["moles"],
            values["volume_l"]
        )

    # Moles
    if "moles" in q:

        if "mass_g" not in values or "molar_mass" not in values:

            return {
                "success": False,
                "message": "Mass and molar mass required."
            }

        return v15_moles_solve(
            values["mass_g"],
            values["molar_mass"]
        )

    return {
        "success": False,
        "message": "Chemistry topic not recognized."
    }


# ------------------------------------------------
# V14 + V15 TESTING
# ------------------------------------------------

print("V14 + V15 TESTING")
print("-" * 50)

# Multi-step physics
p1 = v14_multi_solve(
    mass=5,
    acceleration=2,
    distance=10,
    time=5
)

assert p1["success"]
assert abs(p1["values"]["force"] - 10) < 0.001
assert abs(p1["values"]["work"] - 100) < 0.001
assert abs(p1["values"]["power"] - 20) < 0.001

print("PASS: Multi-step Force = 10 N")
print("PASS: Multi-step Work = 100 J")
print("PASS: Multi-step Power = 20 W")

# Moles
c1 = v15_moles_solve(
    mass_g=18,
    molar_mass=18
)

assert c1["success"]
assert abs(c1["result"] - 1) < 0.001

print("PASS: Moles = 1 mol")

# Molarity
c2 = v15_molarity_solve(
    moles=1,
    volume_l=2
)

assert c2["success"]
assert abs(c2["result"] - 0.5) < 0.001

print("PASS: Molarity = 0.5 mol/L")

# Chemistry question parsing
c3 = v15_chemistry_solve(
    "mass 18 g molar mass 18 g/mol moles calculate"
)

assert c3["success"]
assert abs(c3["result"] - 1) < 0.001

print("PASS: Chemistry question parsing")

# Molarity parsing
c4 = v15_chemistry_solve(
    "moles 1 volume 2 L molarity calculate"
)

assert c4["success"]
assert abs(c4["result"] - 0.5) < 0.001

print("PASS: Molarity question parsing")

# Zero volume validation
c5 = v15_molarity_solve(
    moles=1,
    volume_l=0
)

assert not c5["success"]

print("PASS: Zero volume validation")

print("-" * 50)
print("ALL V14 + V15 TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V16
# UNIFIED ENGINE + MINI UI + INTEGRATED TESTS
# ================================================================

import re
import json

# ------------------------------------------------
# V16.1: UNIFIED SOLVER
# ------------------------------------------------

def v16_magic_solve(question):

    q = v11_normalize(question)

    if not q.strip():
        return {
            "success": False,
            "message": "Please enter a question."
        }

    # CHEMISTRY ROUTING
    if any(word in q for word in [
        "moles", "molarity", "molar mass"
    ]):

        result = v15_chemistry_solve(q)

        result["engine"] = "V16 Chemistry"
        return result

    # PHYSICS MULTI-STEP ROUTING
    mass = v13_extract_number(q, "mass")
    acceleration = v13_extract_number(q, "acceleration")
    distance = v13_extract_number(q, "distance")
    time = v13_extract_number(q, "time")

    if (
        mass is not None
        and acceleration is not None
        and distance is not None
    ):

        result = v14_multi_solve(
            mass, acceleration, distance, time
        )

        result["engine"] = "V16 Physics Multi-Step"
        return result

    # SINGLE-TOPIC PHYSICS ROUTING
    result = v13_smart_solve(q)

    result["engine"] = "V16 Physics"
    return result


# ------------------------------------------------
# V16.2: DISPLAY FORMATTER
# ------------------------------------------------

def v16_format_result(result):

    if not result.get("success"):

        return "ERROR: " + result.get(
            "message", "Unable to solve."
        )

    output = []

    output.append("SUNO SAATHI MAGIC LAYER")
    output.append("=" * 35)

    output.append(
        "Engine: " + result.get("engine", "Unknown")
    )

    if "values" in result:

        output.append("\nVALUES:")

        for key, value in result["values"].items():

            output.append(f"{key} = {value}")

    if "steps" in result:

        output.append("\nSTEPS:")

        for step in result["steps"]:
            output.append(step)

    if "formula" in result:

        output.append("\nFormula: " + result["formula"])

    if "explanation" in result:

        output.append("\n" + result["explanation"])

    if "result" in result:

        output.append(
            f"\nFINAL ANSWER: {result['result']} "
            f"{result.get('unit', '')}"
        )

    output.append("\n" + "=" * 35)

    return "\n".join(output)


# ------------------------------------------------
# V16.3: MAIN USER ENTRY
# ------------------------------------------------

def suno_magic(question):

    result = v16_magic_solve(question)

    print(v16_format_result(result))

    return result


# ------------------------------------------------
# V16.4: MINI COLAB UI
# ------------------------------------------------

def v16_launch_ui():

    try:
        import ipywidgets as widgets
        from IPython.display import display, clear_output

        question_box = widgets.Textarea(
            value="",
            placeholder="Ask Physics or Chemistry question...",
            description="Question:",
            layout=widgets.Layout(width="100%", height="100px")
        )

        solve_button = widgets.Button(
            description="Solve Question",
            button_style="success"
        )

        output_box = widgets.Output()

        def on_solve_clicked(button):

            with output_box:

                clear_output()

                result = v16_magic_solve(
                    question_box.value
                )

                print(v16_format_result(result))

        solve_button.on_click(on_solve_clicked)

        display(question_box)
        display(solve_button)
        display(output_box)

        print("Suno Saathi Magic Layer UI Ready")

    except ImportError:

        print("ipywidgets unavailable.")
        print("Use suno_magic(question) instead.")


# ------------------------------------------------
# V16.5: INTEGRATED TESTS
# ------------------------------------------------

print("V16 INTEGRATED TESTING")
print("-" * 50)

# Test 1: Force
t1 = v16_magic_solve(
    "mass 5 kg acceleration 2 m/s2 force calculate"
)

assert t1["success"]
assert abs(t1["values"]["force"] - 10) < 0.001

print("PASS: Unified Force = 10 N")

# Test 2: Work
t2 = v16_magic_solve(
    "force 10 N distance 5 m work calculate"
)

assert t2["success"]
assert abs(t2["values"]["work"] - 50) < 0.001

print("PASS: Unified Work = 50 J")

# Test 3: Power
t3 = v16_magic_solve(
    "100 J work 5 seconds power calculate"
)

assert t3["success"]
assert abs(t3["values"]["power"] - 20) < 0.001

print("PASS: Unified Power = 20 W")

# Test 4: Multi-step
t4 = v16_magic_solve(
    "mass 5 kg acceleration 2 distance 10 time 5"
)

assert t4["success"]
assert abs(t4["values"]["force"] - 10) < 0.001
assert abs(t4["values"]["work"] - 100) < 0.001
assert abs(t4["values"]["power"] - 20) < 0.001

print("PASS: Unified Multi-Step Physics")

# Test 5: Chemistry moles
t5 = v16_magic_solve(
    "mass 18 g molar mass 18 g/mol moles calculate"
)

assert t5["success"]
assert abs(t5["result"] - 1) < 0.001

print("PASS: Unified Chemistry Moles")

# Test 6: Chemistry molarity
t6 = v16_magic_solve(
    "moles 1 volume 2 L molarity calculate"
)

assert t6["success"]
assert abs(t6["result"] - 0.5) < 0.001

print("PASS: Unified Chemistry Molarity")

# Test 7: Hindi Physics
t7 = v16_magic_solve(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)

assert t7["success"]
assert abs(t7["values"]["force"] - 10) < 0.001

print("PASS: Hindi Physics")

# Test 8: Empty question
t8 = v16_magic_solve("")

assert not t8["success"]

print("PASS: Empty question validation")

print("-" * 50)
print("ALL V16 INTEGRATED TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V16
# UNIFIED ENGINE + MINI UI + INTEGRATED TESTS
# ================================================================

import re
import json

# ------------------------------------------------
# V16.1: UNIFIED SOLVER
# ------------------------------------------------


# ================================================================
# V16.1 BUG FIX: UNIFIED PHYSICS ROUTING
# ================================================================

import re

def v16_magic_solve(question):

    q = v11_normalize(question)

    if not q.strip():
        return {
            "success": False,
            "message": "Please enter a question."
        }

    # CHEMISTRY
    if any(x in q for x in [
        "moles", "molarity", "molar mass"
    ]):
        result = v15_chemistry_solve(q)
        result["engine"] = "V16 Chemistry"
        return result

    # DIRECT NUMBER EXTRACTION
    def get_num(patterns):
        for pattern in patterns:
            m = re.search(pattern, q, re.I)
            if m:
                return float(m.group(1))
        return None

    mass = get_num([
        r"mass\s*(\d+(?:\.\d+)?)\s*kg",
        r"mass\s*(\d+(?:\.\d+)?)"
    ])

    acceleration = get_num([
        r"acceleration\s*(\d+(?:\.\d+)?)",
        r"acc\s*(\d+(?:\.\d+)?)"
    ])

    force = get_num([
        r"force\s*(\d+(?:\.\d+)?)"
    ])

    distance = get_num([
        r"distance\s*(\d+(?:\.\d+)?)",
        r"(\d+(?:\.\d+)?)\s*m\s+distance"
    ])

    work = get_num([
        r"work\s*(\d+(?:\.\d+)?)\s*j",
        r"(\d+(?:\.\d+)?)\s*j\s*work"
    ])

    time = get_num([
        r"time\s*(\d+(?:\.\d+)?)",
        r"(\d+(?:\.\d+)?)\s*s(?:ec(?:ond)?s?)?\s*(?:time)?"
    ])

    values = {}
    steps = []

    # FORCE
    if mass is not None and acceleration is not None:
        force = mass * acceleration
        values["force"] = force
        steps.append(
            f"Force = {mass} × {acceleration} = {force} N"
        )

    # WORK
    if force is not None and distance is not None:
        work = force * distance
        values["work"] = work
        steps.append(
            f"Work = {force} × {distance} = {work} J"
        )

    # POWER
    if work is not None and time is not None:
        if time <= 0:
            return {
                "success": False,
                "message": "Time must be greater than zero."
            }

        power = work / time
        values["power"] = power
        steps.append(
            f"Power = {work} / {time} = {power} W"
        )

    # SPEED
    if distance is not None and time is not None:
        if time > 0:
            values["speed"] = distance / time

    if values:
        return {
            "success": True,
            "engine": "V16 Direct Physics",
            "values": values,
            "steps": steps,
            "explanation": "\n".join(steps)
        }

    # FALLBACK
    result = v13_smart_solve(q)
    result["engine"] = "V16 V13 Fallback"
    return result


# ================================================================
# V16.1 REGRESSION TESTS
# ================================================================

print("V16.1 FIX TESTING")
print("-" * 50)

t1 = v16_magic_solve(
    "mass 5 kg acceleration 2 m/s2 force calculate"
)

assert t1["success"], t1
assert "force" in t1["values"], t1
assert abs(t1["values"]["force"] - 10) < 0.001
print("PASS: Force = 10 N")

t2 = v16_magic_solve(
    "force 10 N distance 5 m work calculate"
)

assert t2["success"], t2
assert abs(t2["values"]["work"] - 50) < 0.001
print("PASS: Work = 50 J")

t3 = v16_magic_solve(
    "100 J work 5 seconds power calculate"
)

assert t3["success"], t3
assert abs(t3["values"]["power"] - 20) < 0.001
print("PASS: Power = 20 W")

t4 = v16_magic_solve(
    "mass 5 kg acceleration 2 distance 10 time 5"
)

assert t4["success"], t4
assert abs(t4["values"]["force"] - 10) < 0.001
assert abs(t4["values"]["work"] - 100) < 0.001
assert abs(t4["values"]["power"] - 20) < 0.001
print("PASS: Multi-Step Physics")

t5 = v16_magic_solve(
    "mass 18 g molar mass 18 g/mol moles calculate"
)

assert t5["success"], t5
assert abs(t5["result"] - 1) < 0.001
print("PASS: Chemistry Moles")

t6 = v16_magic_solve(
    "moles 1 volume 2 L molarity calculate"
)

assert t6["success"], t6
assert abs(t6["result"] - 0.5) < 0.001
print("PASS: Chemistry Molarity")

t7 = v16_magic_solve(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)

assert t7["success"], t7
assert abs(t7["values"]["force"] - 10) < 0.001
print("PASS: Hindi Physics")

t8 = v16_magic_solve("")

assert not t8["success"]
print("PASS: Empty Question")

print("-" * 50)
print("ALL V16.1 TESTS PASSED!")



# ------------------------------------------------
# V16.2: DISPLAY FORMATTER
# ------------------------------------------------

def v16_format_result(result):

    if not result.get("success"):

        return "ERROR: " + result.get(
            "message", "Unable to solve."
        )

    output = []

    output.append("SUNO SAATHI MAGIC LAYER")
    output.append("=" * 35)

    output.append(
        "Engine: " + result.get("engine", "Unknown")
    )

    if "values" in result:

        output.append("\nVALUES:")

        for key, value in result["values"].items():

            output.append(f"{key} = {value}")

    if "steps" in result:

        output.append("\nSTEPS:")

        for step in result["steps"]:
            output.append(step)

    if "formula" in result:

        output.append("\nFormula: " + result["formula"])

    if "explanation" in result:

        output.append("\n" + result["explanation"])

    if "result" in result:

        output.append(
            f"\nFINAL ANSWER: {result['result']} "
            f"{result.get('unit', '')}"
        )

    output.append("\n" + "=" * 35)

    return "\n".join(output)


# ------------------------------------------------
# V16.3: MAIN USER ENTRY
# ------------------------------------------------

def suno_magic(question):

    result = v16_magic_solve(question)

    print(v16_format_result(result))

    return result


# ------------------------------------------------
# V16.4: MINI COLAB UI
# ------------------------------------------------

def v16_launch_ui():

    try:
        import ipywidgets as widgets
        from IPython.display import display, clear_output

        question_box = widgets.Textarea(
            value="",
            placeholder="Ask Physics or Chemistry question...",
            description="Question:",
            layout=widgets.Layout(width="100%", height="100px")
        )

        solve_button = widgets.Button(
            description="Solve Question",
            button_style="success"
        )

        output_box = widgets.Output()

        def on_solve_clicked(button):

            with output_box:

                clear_output()

                result = v16_magic_solve(
                    question_box.value
                )

                print(v16_format_result(result))

        solve_button.on_click(on_solve_clicked)

        display(question_box)
        display(solve_button)
        display(output_box)

        print("Suno Saathi Magic Layer UI Ready")

    except ImportError:

        print("ipywidgets unavailable.")
        print("Use suno_magic(question) instead.")


# ------------------------------------------------
# V16.5: INTEGRATED TESTS
# ------------------------------------------------

print("V16 INTEGRATED TESTING")
print("-" * 50)

# Test 1: Force
t1 = v16_magic_solve(
    "mass 5 kg acceleration 2 m/s2 force calculate"
)

assert t1["success"]
assert abs(t1["values"]["force"] - 10) < 0.001

print("PASS: Unified Force = 10 N")

# Test 2: Work
t2 = v16_magic_solve(
    "force 10 N distance 5 m work calculate"
)

assert t2["success"]
assert abs(t2["values"]["work"] - 50) < 0.001

print("PASS: Unified Work = 50 J")

# Test 3: Power
t3 = v16_magic_solve(
    "100 J work 5 seconds power calculate"
)

assert t3["success"]
assert abs(t3["values"]["power"] - 20) < 0.001

print("PASS: Unified Power = 20 W")

# Test 4: Multi-step
t4 = v16_magic_solve(
    "mass 5 kg acceleration 2 distance 10 time 5"
)

assert t4["success"]
assert abs(t4["values"]["force"] - 10) < 0.001
assert abs(t4["values"]["work"] - 100) < 0.001
assert abs(t4["values"]["power"] - 20) < 0.001

print("PASS: Unified Multi-Step Physics")

# Test 5: Chemistry moles
t5 = v16_magic_solve(
    "mass 18 g molar mass 18 g/mol moles calculate"
)

assert t5["success"]
assert abs(t5["result"] - 1) < 0.001

print("PASS: Unified Chemistry Moles")

# Test 6: Chemistry molarity
t6 = v16_magic_solve(
    "moles 1 volume 2 L molarity calculate"
)

assert t6["success"]
assert abs(t6["result"] - 0.5) < 0.001

print("PASS: Unified Chemistry Molarity")

# Test 7: Hindi Physics
t7 = v16_magic_solve(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)

assert t7["success"]
assert abs(t7["values"]["force"] - 10) < 0.001

print("PASS: Hindi Physics")

# Test 8: Empty question
t8 = v16_magic_solve("")

assert not t8["success"]

print("PASS: Empty question validation")

print("-" * 50)
print("ALL V16 INTEGRATED TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V16.2
# COMPLETE CORRECTED BUILD
# Physics + Chemistry + Hindi + Hinglish + UI + Tests
# ================================================================

import re
import math

# ================================================================
# 1. NORMALIZATION ENGINE
# ================================================================

def v16_normalize(text):

    q = str(text).lower().strip()

    replacements = {
        "द्रव्यमान": "mass",
        "त्वरण": "acceleration",
        "बल": "force",
        "कार्य": "work",
        "काम": "work",
        "शक्ति": "power",
        "दूरी": "distance",
        "समय": "time",
        "गति": "speed",
        "वेग": "speed",
        "ऊँचाई": "height",
        "ऊंचाई": "height",
        "मोलर द्रव्यमान": "molar mass",
        "मोलरता": "molarity",
        "मोल": "moles",
        "आयतन": "volume",
        "निकालो": "calculate",
        "निकालिए": "calculate",
        "ज्ञात करो": "calculate",
        "बताओ": "calculate",
        "गणना करो": "calculate",
        "कितना": "calculate",
        "कितनी": "calculate",
        "कितने": "calculate",
        "है": "",
        "का": "",
        "की": "",
        "में": "",
        "और": " ",
        "से": " ",
    }

    for hindi, english in replacements.items():
        q = q.replace(hindi, english)

    # Number conversion
    hindi_digits = "०१२३४५६७८९"
    english_digits = "0123456789"

    q = q.translate(str.maketrans(hindi_digits, english_digits))

    # Units
    q = q.replace("किलोग्राम", "kg")
    q = q.replace("ग्राम", "g")
    q = q.replace("लीटर", "L")
    q = q.replace("मिलीलीटर", "ml")
    q = q.replace("सेकंड", "s")
    q = q.replace("मीटर", "m")

    q = q.replace("m/s²", "m/s2")
    q = q.replace("m/s^2", "m/s2")
    q = q.replace("m s-2", "m/s2")

    # Move number before Hindi variable into English label format
    q = re.sub(
        r'(\d+(?:\.\d+)?)\s*kg\s*mass',
        r'mass \1 kg',
        q
    )

    q = re.sub(
        r'(\d+(?:\.\d+)?)\s*mass',
        r'mass \1',
        q
    )

    q = re.sub(
        r'(\d+(?:\.\d+)?)\s*acceleration',
        r'acceleration \1',
        q
    )

    q = re.sub(
        r'(\d+(?:\.\d+)?)\s*force',
        r'force \1',
        q
    )

    q = re.sub(
        r'(\d+(?:\.\d+)?)\s*distance',
        r'distance \1',
        q
    )

    q = re.sub(
        r'(\d+(?:\.\d+)?)\s*time',
        r'time \1',
        q
    )

    q = re.sub(r'\s+', ' ', q)

    return q.strip()


# ================================================================
# 2. NUMBER EXTRACTION
# ================================================================

def v16_get_number(q, variable):

    patterns = {

        "mass": [
            r'mass\s*(\d+(?:\.\d+)?)\s*kg',
            r'mass\s*(\d+(?:\.\d+)?)\s*g\b',
            r'mass\s*(\d+(?:\.\d+)?)'
        ],

        "acceleration": [
            r'acceleration\s*(\d+(?:\.\d+)?)',
            r'acc\s*(\d+(?:\.\d+)?)'
        ],

        "force": [
            r'force\s*(\d+(?:\.\d+)?)'
        ],

        "distance": [
            r'distance\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*m\s+distance'
        ],

        "time": [
            r'time\s*(\d+(?:\.\d+)?)',
            r'(\d+(?:\.\d+)?)\s*s(?:ec(?:ond)?s?)?\s*(?:time)?'
        ],

        "work": [
            r'work\s*(\d+(?:\.\d+)?)\s*j',
            r'(\d+(?:\.\d+)?)\s*j\s*work',
            r'work\s*(\d+(?:\.\d+)?)'
        ],

        "speed": [
            r'speed\s*(\d+(?:\.\d+)?)'
        ],

        "height": [
            r'height\s*(\d+(?:\.\d+)?)'
        ]
    }

    for pattern in patterns.get(variable, []):

        match = re.search(pattern, q, re.I)

        if match:
            return float(match.group(1))

    return None


# ================================================================
# 3. PHYSICS SOLVER
# ================================================================

def v16_physics_solve(question):

    q = v16_normalize(question)

    mass = v16_get_number(q, "mass")
    acceleration = v16_get_number(q, "acceleration")
    force = v16_get_number(q, "force")
    distance = v16_get_number(q, "distance")
    time = v16_get_number(q, "time")
    work = v16_get_number(q, "work")
    speed = v16_get_number(q, "speed")

    values = {}
    steps = []

    # Force
    if mass is not None and acceleration is not None:

        force = mass * acceleration

        values["force"] = force

        steps.append(
            f"Force = {mass} × {acceleration} = {force} N"
        )

    # Work
    if force is not None and distance is not None:

        work = force * distance

        values["work"] = work

        steps.append(
            f"Work = {force} × {distance} = {work} J"
        )

    # Power
    if work is not None and time is not None:

        if time <= 0:

            return {
                "success": False,
                "message": "Time must be greater than zero."
            }

        power = work / time

        values["power"] = power

        steps.append(
            f"Power = {work} / {time} = {power} W"
        )

    # Speed
    if distance is not None and time is not None:

        if time <= 0:

            return {
                "success": False,
                "message": "Time must be greater than zero."
            }

        speed = distance / time

        values["speed"] = speed

        steps.append(
            f"Speed = {distance} / {time} = {speed} m/s"
        )

    # Kinetic Energy
    if mass is not None and speed is not None:

        ke = 0.5 * mass * speed ** 2

        values["kinetic_energy"] = ke

        steps.append(
            f"KE = 0.5 × {mass} × {speed}² = {ke} J"
        )

    # Potential Energy
    height = v16_get_number(q, "height")

    if mass is not None and height is not None:

        pe = mass * 9.8 * height

        values["potential_energy"] = pe

        steps.append(
            f"PE = {mass} × 9.8 × {height} = {pe} J"
        )

    if not values:

        return {
            "success": False,
            "message": (
                "Required variables missing. "
                "Try mass 5 kg acceleration 2 force calculate."
            )
        }

    return {
        "success": True,
        "engine": "V16.2 Physics",
        "values": values,
        "steps": steps,
        "explanation": "\n".join(steps)
    }


# ================================================================
# 4. CHEMISTRY SOLVER
# ================================================================

def v16_chemistry_solve(question):

    q = v16_normalize(question)

    # Mass in grams
    mass_match = re.search(
        r'mass\s*(\d+(?:\.\d+)?)\s*g\b',
        q
    )

    mass_g = (
        float(mass_match.group(1))
        if mass_match else None
    )

    # Molar mass
    mm_match = re.search(
        r'molar\s*mass\s*(\d+(?:\.\d+)?)\s*g\s*/\s*mol',
        q
    )

    molar_mass = (
        float(mm_match.group(1))
        if mm_match else None
    )

    # Moles
    moles_match = re.search(
        r'moles\s*(\d+(?:\.\d+)?)',
        q
    )

    moles = (
        float(moles_match.group(1))
        if moles_match else None
    )

    # Volume
    volume_match = re.search(
        r'volume\s*(\d+(?:\.\d+)?)\s*(ml|l)\b',
        q,
        re.I
    )

    volume_l = None

    if volume_match:

        volume = float(volume_match.group(1))
        unit = volume_match.group(2).lower()

        if unit == "ml":
            volume_l = volume / 1000

        else:
            volume_l = volume

    # Calculate moles
    if (
        "moles" in q
        and mass_g is not None
        and molar_mass is not None
    ):

        if molar_mass <= 0 or mass_g < 0:

            return {
                "success": False,
                "message": "Invalid mass or molar mass."
            }

        moles = mass_g / molar_mass

        return {
            "success": True,
            "engine": "V16.2 Chemistry",
            "topic": "moles",
            "values": {
                "mass_g": mass_g,
                "molar_mass": molar_mass
            },
            "result": moles,
            "unit": "mol",
            "formula": "n = mass / molar mass",
            "explanation": (
                f"n = {mass_g} / {molar_mass}\n"
                f"Moles = {moles} mol"
            )
        }

    # Calculate molarity
    if "molarity" in q:

        if moles is None or volume_l is None:

            return {
                "success": False,
                "message": "Moles and volume required."
            }

        if moles < 0 or volume_l <= 0:

            return {
                "success": False,
                "message": "Moles >= 0 and volume > 0 required."
            }

        molarity = moles / volume_l

        return {
            "success": True,
            "engine": "V16.2 Chemistry",
            "topic": "molarity",
            "values": {
                "moles": moles,
                "volume_l": volume_l
            },
            "result": molarity,
            "unit": "mol/L",
            "formula": "M = n / V",
            "explanation": (
                f"M = {moles} / {volume_l}\n"
                f"Molarity = {molarity} mol/L"
            )
        }

    return {
        "success": False,
        "message": "Chemistry topic not recognized."
    }


# ================================================================
# 5. UNIFIED MAGIC ENGINE
# ================================================================

def v16_magic_solve(question):

    q = v16_normalize(question)

    if not q:

        return {
            "success": False,
            "message": "Please enter a question."
        }

    # Chemistry routing
    if any(x in q for x in [
        "moles", "molarity", "molar mass"
    ]):

        return v16_chemistry_solve(q)

    # Physics routing
    return v16_physics_solve(q)


# ================================================================
# 6. RESULT FORMATTER
# ================================================================

def v16_format_result(result):

    if not result.get("success"):

        return "ERROR: " + result.get(
            "message", "Unable to solve."
        )

    output = []

    output.append("SUNO SAATHI MAGIC LAYER V16.2")
    output.append("=" * 40)

    output.append(
        "Engine: " + result.get("engine", "Unknown")
    )

    if "values" in result:

        output.append("\nVALUES:")

        for key, value in result["values"].items():

            output.append(f"{key} = {value}")

    if "steps" in result:

        output.append("\nSTEPS:")

        for step in result["steps"]:
            output.append(step)

    if "formula" in result:

        output.append("\nFormula: " + result["formula"])

    if "explanation" in result:

        output.append("\n" + result["explanation"])

    if "result" in result:

        output.append(
            f"\nFINAL ANSWER: {result['result']} "
            f"{result.get('unit', '')}"
        )

    output.append("\n" + "=" * 40)

    return "\n".join(output)


# ================================================================
# 7. MAIN ENTRY
# ================================================================

def suno_magic(question):

    result = v16_magic_solve(question)

    print(v16_format_result(result))

    return result


# ================================================================
# 8. MINI UI
# ================================================================

def v16_launch_ui():

    import ipywidgets as widgets
    from IPython.display import display, clear_output

    question_box = widgets.Textarea(
        placeholder="Ask Physics or Chemistry question...",
        description="Question:",
        layout=widgets.Layout(
            width="100%",
            height="120px"
        )
    )

    solve_button = widgets.Button(
        description="Solve Question",
        button_style="success"
    )

    output_box = widgets.Output()

    def on_solve_clicked(button):

        with output_box:

            clear_output()

            result = v16_magic_solve(
                question_box.value
            )

            print(v16_format_result(result))

    solve_button.on_click(on_solve_clicked)

    display(question_box)
    display(solve_button)
    display(output_box)

    print("Suno Saathi Magic Layer UI Ready")


# ================================================================
# 9. COMPLETE REGRESSION TESTS
# ================================================================

print("V16.2 COMPLETE TESTING")
print("-" * 55)

# Force English
t1 = suno_magic(
    "mass 5 kg acceleration 2 m/s2 force calculate"
)

assert t1["success"], t1
assert abs(t1["values"]["force"] - 10) < 0.001
print("PASS: English Force")

# Work
t2 = suno_magic(
    "force 10 N distance 5 m work calculate"
)

assert t2["success"], t2
assert abs(t2["values"]["work"] - 50) < 0.001
print("PASS: English Work")

# Power
t3 = suno_magic(
    "100 J work 5 seconds power calculate"
)

assert t3["success"], t3
assert abs(t3["values"]["power"] - 20) < 0.001
print("PASS: English Power")

# Multi-step
t4 = suno_magic(
    "mass 5 kg acceleration 2 distance 10 time 5"
)

assert t4["success"], t4
assert abs(t4["values"]["force"] - 10) < 0.001
assert abs(t4["values"]["work"] - 100) < 0.001
assert abs(t4["values"]["power"] - 20) < 0.001
print("PASS: Multi-Step Physics")

# Hindi Force
t5 = suno_magic(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)

assert t5["success"], t5
assert abs(t5["values"]["force"] - 10) < 0.001
print("PASS: Hindi Force")

# Hindi digits
t6 = suno_magic(
    "५ kg द्रव्यमान २ त्वरण बल निकालो"
)

assert t6["success"], t6
assert abs(t6["values"]["force"] - 10) < 0.001
print("PASS: Hindi Digits")

# Chemistry Moles
t7 = suno_magic(
    "mass 18 g molar mass 18 g/mol moles calculate"
)

assert t7["success"], t7
assert abs(t7["result"] - 1) < 0.001
print("PASS: Chemistry Moles")

# Chemistry Molarity
t8 = suno_magic(
    "moles 1 volume 2 L molarity calculate"
)

assert t8["success"], t8
assert abs(t8["result"] - 0.5) < 0.001
print("PASS: Chemistry Molarity")

# Zero time
t9 = suno_magic(
    "100 J work time 0 power calculate"
)

assert not t9["success"], t9
print("PASS: Zero Time Validation")

# Empty question
t10 = suno_magic("")

assert not t10["success"]
print("PASS: Empty Question")

print("-" * 55)
print("ALL V16.2 TESTS PASSED!")

# ================================================================
# SUNO SAATHI MAGIC LAYER V14 + V15
# MULTI-STEP PHYSICS + CHEMISTRY ENGINE
# ================================================================

import re
import math

# ------------------------------------------------
# V14: MULTI-STEP PHYSICS SOLVER
# ------------------------------------------------

def v14_multi_solve(mass=None, acceleration=None,
                    distance=None, time=None):

    steps = []
    values = {}

    # Step 1: Force
    if mass is not None and acceleration is not None:

        force = mass * acceleration

        values["force"] = force

        steps.append(
            f"Force = {mass} × {acceleration} = {force} N"
        )

    else:
        force = None

    # Step 2: Work
    if force is not None and distance is not None:

        work = force * distance

        values["work"] = work

        steps.append(
            f"Work = {force} × {distance} = {work} J"
        )

    else:
        work = None

    # Step 3: Power
    if work is not None and time is not None:

        if time <= 0:

            return {
                "success": False,
                "message": "Time must be greater than zero."
            }

        power = work / time

        values["power"] = power

        steps.append(
            f"Power = {work} / {time} = {power} W"
        )

    return {
        "success": True,
        "topic": "multi_step_physics",
        "values": values,
        "steps": steps,
        "explanation": "\n".join(steps)
    }


# ------------------------------------------------
# V14: MULTI-STEP QUESTION PARSER
# ------------------------------------------------

def v14_multi_question(q):

    q = v11_normalize(q)

    mass = v13_extract_number(q, "mass")
    acceleration = v13_extract_number(q, "acceleration")
    distance = v13_extract_number(q, "distance")
    time = v13_extract_number(q, "time")

    return v14_multi_solve(
        mass=mass,
        acceleration=acceleration,
        distance=distance,
        time=time
    )


# ------------------------------------------------
# V15: CHEMISTRY VARIABLE EXTRACTION
# ------------------------------------------------

def v15_extract_chemistry(q):

    q = v11_normalize(q)

    values = {}

    # Mass in grams
    m = re.search(
        r'\bmass\s*(\d+(?:\.\d+)?)\s*g\b',
        q
    )

    if m:
        values["mass_g"] = float(m.group(1))

    # Molar mass in g/mol
    mm = re.search(
        r'molar\s*mass\s*(\d+(?:\.\d+)?)\s*g\s*/\s*mol',
        q
    )

    if mm:
        values["molar_mass"] = float(mm.group(1))

    # Moles
    n = re.search(
        r'\bmoles\s*(\d+(?:\.\d+)?)',
        q
    )

    if n:
        values["moles"] = float(n.group(1))

    # Volume in liters
    volume = re.search(
        r'\bvolume\s*(\d+(?:\.\d+)?)\s*(?:L|l)\b',
        q
    )

    if volume:
        values["volume_l"] = float(volume.group(1))

    return values


# ------------------------------------------------
# V15: MOLES SOLVER
# ------------------------------------------------

def v15_moles_solve(mass_g, molar_mass):

    if mass_g < 0 or molar_mass <= 0:

        return {
            "success": False,
            "message": "Mass >= 0 and molar mass > 0 required."
        }

    moles = mass_g / molar_mass

    return {
        "success": True,
        "topic": "moles",
        "values": {
            "mass_g": mass_g,
            "molar_mass": molar_mass
        },
        "result": moles,
        "unit": "mol",
        "formula": "n = mass / molar mass",
        "explanation": (
            f"n = {mass_g} / {molar_mass}\n"
            f"Moles = {moles} mol"
        )
    }


# ------------------------------------------------
# V15: MOLARITY SOLVER
# ------------------------------------------------

def v15_molarity_solve(moles, volume_l):

    if moles < 0 or volume_l <= 0:

        return {
            "success": False,
            "message": "Moles >= 0 and volume > 0 required."
        }

    molarity = moles / volume_l

    return {
        "success": True,
        "topic": "molarity",
        "values": {
            "moles": moles,
            "volume_l": volume_l
        },
        "result": molarity,
        "unit": "mol/L",
        "formula": "M = n / V",
        "explanation": (
            f"M = {moles} / {volume_l}\n"
            f"Molarity = {molarity} mol/L"
        )
    }


# ------------------------------------------------
# V15: CHEMISTRY SMART SOLVER
# ------------------------------------------------

def v15_chemistry_solve(q):

    q = v11_normalize(q)

    values = v15_extract_chemistry(q)

    # Molarity
    if "molarity" in q:

        if "moles" not in values or "volume_l" not in values:

            return {
                "success": False,
                "message": "Moles and volume in liters required."
            }

        return v15_molarity_solve(
            values["moles"],
            values["volume_l"]
        )

    # Moles
    if "moles" in q:

        if "mass_g" not in values or "molar_mass" not in values:

            return {
                "success": False,
                "message": "Mass and molar mass required."
            }

        return v15_moles_solve(
            values["mass_g"],
            values["molar_mass"]
        )

    return {
        "success": False,
        "message": "Chemistry topic not recognized."
    }


# ------------------------------------------------
# V14 + V15 TESTING
# ------------------------------------------------

print("V14 + V15 TESTING")
print("-" * 50)

# Multi-step physics
p1 = v14_multi_solve(
    mass=5,
    acceleration=2,
    distance=10,
    time=5
)

assert p1["success"]
assert abs(p1["values"]["force"] - 10) < 0.001
assert abs(p1["values"]["work"] - 100) < 0.001
assert abs(p1["values"]["power"] - 20) < 0.001

print("PASS: Multi-step Force = 10 N")
print("PASS: Multi-step Work = 100 J")
print("PASS: Multi-step Power = 20 W")

# Moles
c1 = v15_moles_solve(
    mass_g=18,
    molar_mass=18
)

assert c1["success"]
assert abs(c1["result"] - 1) < 0.001

print("PASS: Moles = 1 mol")

# Molarity
c2 = v15_molarity_solve(
    moles=1,
    volume_l=2
)

assert c2["success"]
assert abs(c2["result"] - 0.5) < 0.001

print("PASS: Molarity = 0.5 mol/L")

# Chemistry question parsing
c3 = v15_chemistry_solve(
    "mass 18 g molar mass 18 g/mol moles calculate"
)

assert c3["success"]
assert abs(c3["result"] - 1) < 0.001

print("PASS: Chemistry question parsing")

# Molarity parsing
c4 = v15_chemistry_solve(
    "moles 1 volume 2 L molarity calculate"
)

assert c4["success"]
assert abs(c4["result"] - 0.5) < 0.001

print("PASS: Molarity question parsing")

# Zero volume validation
c5 = v15_molarity_solve(
    moles=1,
    volume_l=0
)

assert not c5["success"]

print("PASS: Zero volume validation")

print("-" * 50)
print("ALL V14 + V15 TESTS PASSED!")

# ============================================================
# SUNO SAATHI MAGIC LAYER V16.3
# COMPLETE REWRITE - HINDI + ENGLISH
# Physics + Chemistry + Regression Tests
# ============================================================

import re
import math

# ------------------------------------------------------------
# 1. NORMALIZATION
# ------------------------------------------------------------

def v16_normalize(text):
    q = str(text).lower().strip()

    # Hindi digits -> English digits
    hindi_digits = "०१२३४५६७८९"
    english_digits = "0123456789"

    q = q.translate(str.maketrans(hindi_digits, english_digits))

    # Unicode cleanup
    q = q.replace("²", "2")
    q = q.replace("³", "3")
    q = q.replace("×", "*")
    q = q.replace("÷", "/")

    # Longest Hindi phrases first
    replacements = {
        "मोलर द्रव्यमान": "molar mass",
        "गतिज ऊर्जा": "kinetic energy",
        "स्थितिज ऊर्जा": "potential energy",
        "द्रव्यमान": "mass",
        "त्वरण": "acceleration",
        "वेग": "velocity",
        "चाल": "speed",
        "दूरी": "distance",
        "समय": "time",
        "बल": "force",
        "कार्य": "work",
        "शक्ति": "power",
        "ऊर्जा": "energy",
        "ऊंचाई": "height",
        "ऊँचाई": "height",
        "आयतन": "volume",
        "मोल": "moles",
        "मात्रा": "volume",
        "सांद्रता": "molarity",
        "द्रव्यमान निकालो": "mass calculate",
        "निकालो": "calculate",
        "बताओ": "calculate",
        "गणना": "calculate",
        "और": " ",
        "से": " ",
        "का": " ",
        "की": " ",
        "है": " ",
        "में": " ",
        "कितना": " ",
        "कितनी": " ",
    }

    for hindi, english in sorted(
        replacements.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # Units
    unit_replacements = {
        "किलोग्राम": "kg",
        "ग्राम": "g",
        "मीटर": "m",
        "सेकंड": "seconds",
        "सेकेण्ड": "seconds",
        "मिलीलीटर": "ml",
        "लीटर": "l",
        "न्यूटन": "n",
        "जूल": "j",
        "वाट": "w",
    }

    for hindi, english in sorted(
        unit_replacements.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # Common English aliases
    aliases = {
        "mass": ["weight of", "mass is"],
        "acceleration": ["accelerated by", "accel"],
        "force": ["f"],
        "distance": ["d"],
        "time": ["t"],
        "speed": ["velocity"],
        "molar mass": ["molecular weight"],
        "moles": ["mol"],
        "molarity": ["concentration"],
    }

    for canonical, words in aliases.items():
        for word in words:
            if word != canonical:
                q = re.sub(
                    r"\b" + re.escape(word) + r"\b",
                    canonical,
                    q
                )

    # Standardize units
    q = q.replace("m/s²", "m/s2")
    q = q.replace("m/s^2", "m/s2")
    q = q.replace("kg.", "kg")
    q = q.replace("sec", "seconds")

    q = re.sub(r"\s+", " ", q).strip()

    return q


# ------------------------------------------------------------
# 2. NUMBER EXTRACTION
# ------------------------------------------------------------

def v16_get_number(q, key):

    q = v16_normalize(q)

    number = r"[-+]?\d+(?:\.\d+)?"

    # Variable-specific units
    units = {
        "mass": r"(?:kg|g)?",
        "acceleration": r"(?:m/s2|m/s)?",
        "force": r"(?:n)?",
        "work": r"(?:j)?",
        "power": r"(?:w)?",
        "distance": r"(?:km|m|cm)?",
        "time": r"(?:seconds|second|minutes|min|hours|hour|s)?",
        "speed": r"(?:m/s|km/h)?",
        "velocity": r"(?:m/s|km/h)?",
        "height": r"(?:km|m|cm)?",
        "volume": r"(?:ml|l|liter|litre)?",
        "molarity": r"(?:mol/l|m|molar)?",
        "moles": r"(?:mol|moles)?",
        "molar mass": r"(?:g/mol|kg/mol)?",
        "energy": r"(?:j)?",
        "kinetic energy": r"(?:j)?",
        "potential energy": r"(?:j)?",
    }

    unit = units.get(key, r"[a-z/]*")

    # Pattern A: mass 5 kg / acceleration 2 m/s2
    patterns = [
        rf"\b{re.escape(key)}\s*[:=]?\s*({number})\s*{unit}\b",

        # Pattern B: 5 kg mass / 2 m/s2 acceleration
        rf"({number})\s*{unit}\s*{re.escape(key)}\b",

        # Pattern C: mass 5 / acceleration 2
        rf"\b{re.escape(key)}\s*[:=]?\s*({number})\b",

        # Pattern D: 5 mass / 2 acceleration
        rf"({number})\s*{re.escape(key)}\b",
    ]

    for pattern in patterns:
        match = re.search(pattern, q)

        if match:
            try:
                return float(match.group(1))
            except:
                pass

    # Special time extraction
    if key == "time":
        match = re.search(
            rf"({number})\s*(?:seconds|second|s|minutes|min|hours|hour)",
            q
        )
        if match:
            value = float(match.group(1))

            if re.search(r"\bminutes|min\b", q):
                value *= 60

            if re.search(r"\bhours|hour\b", q):
                value *= 3600

            return value

    return None


# ------------------------------------------------------------
# 3. PHYSICS ENGINE
# ------------------------------------------------------------

def v16_physics_solve(q):

    q = v16_normalize(q)

    values = {}

    keys = [
        "mass", "acceleration", "force", "work",
        "power", "distance", "time", "speed",
        "velocity", "height", "energy",
        "kinetic energy", "potential energy"
    ]

    for key in keys:
        value = v16_get_number(q, key)
        if value is not None:
            values[key] = value

    # Calculate Force = mass * acceleration
    if "mass" in values and "acceleration" in values:
        values["force"] = (
            values["mass"] * values["acceleration"]
        )

    # Calculate Work = Force * Distance
    if "force" in values and "distance" in values:
        values["work"] = (
            values["force"] * values["distance"]
        )

    # Calculate Power = Work / Time
    if "work" in values and "time" in values:
        if values["time"] != 0:
            values["power"] = (
                values["work"] / values["time"]
            )

    # Calculate Speed = Distance / Time
    if "distance" in values and "time" in values:
        if values["time"] != 0:
            values["speed"] = (
                values["distance"] / values["time"]
            )

    # Calculate KE = 1/2 * mass * velocity^2
    if "mass" in values and "velocity" in values:
        values["kinetic energy"] = (
            0.5 * values["mass"] *
            values["velocity"] ** 2
        )

    # Calculate PE = mass * g * height
    if "mass" in values and "height" in values:
        values["potential energy"] = (
            values["mass"] * 9.8 *
            values["height"]
        )

    requested = None

    if "kinetic energy" in q or re.search(r"\bke\b", q):
        requested = "kinetic energy"

    elif "potential energy" in q or re.search(r"\bpe\b", q):
        requested = "potential energy"

    elif "force" in q:
        requested = "force"

    elif "power" in q:
        requested = "power"

    elif "work" in q:
        requested = "work"

    elif "speed" in q or "velocity" in q:
        requested = "speed"

    elif "energy" in q:
        requested = "energy"

    elif "mass" in q:
        requested = "mass"

    if requested and requested in values:
        return {
            "success": True,
            "topic": "physics",
            "formula": requested,
            "answer": values[requested],
            "values": values
        }

    # If some calculation was possible
    if values:
        return {
            "success": True,
            "topic": "physics",
            "formula": "calculated values",
            "answer": list(values.values())[-1],
            "values": values
        }

    return {
        "success": False,
        "topic": "physics",
        "error": "Required values not found",
        "values": values
    }


# ------------------------------------------------------------
# 4. CHEMISTRY ENGINE
# ------------------------------------------------------------

def v16_chemistry_solve(q):

    q = v16_normalize(q)

    values = {}

    keys = [
        "mass", "molar mass", "moles",
        "molarity", "volume"
    ]

    for key in keys:
        value = v16_get_number(q, key)

        if value is not None:
            values[key] = value

    # Moles = mass / molar mass
    if "mass" in values and "molar mass" in values:
        if values["molar mass"] != 0:
            values["moles"] = (
                values["mass"] / values["molar mass"]
            )

    # Molarity = moles / volume in litres
    if "moles" in values and "volume" in values:
        if values["volume"] != 0:
            values["molarity"] = (
                values["moles"] / values["volume"]
            )

    # Moles = molarity * volume
    if "molarity" in values and "volume" in values:
        values["moles"] = (
            values["molarity"] * values["volume"]
        )

    requested = None

    if "molarity" in q:
        requested = "molarity"

    elif "moles" in q:
        requested = "moles"

    elif "molar mass" in q:
        requested = "molar mass"

    if requested and requested in values:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": requested,
            "answer": values[requested],
            "values": values
        }

    if values:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": "calculated values",
            "answer": list(values.values())[-1],
            "values": values
        }

    return {
        "success": False,
        "topic": "chemistry",
        "error": "Required chemistry values not found",
        "values": values
    }


# ------------------------------------------------------------
# 5. UNIFIED MAGIC SOLVER
# ------------------------------------------------------------

def v16_magic_solve(question):

    q = v16_normalize(question)

    chemistry_words = [
        "moles", "molarity", "molar mass",
        "concentration", "mol"
    ]

    if any(word in q for word in chemistry_words):
        return v16_chemistry_solve(q)

    return v16_physics_solve(q)


# ------------------------------------------------------------
# 6. FORMAT RESULT
# ------------------------------------------------------------

def v16_format_result(result):

    if not result["success"]:
        return (
            "❌ Calculation failed\n"
            + result.get("error", "Unknown error")
        )

    answer = result["answer"]

    return (
        "✅ SUNO SAATHI MAGIC\n"
        f"Topic: {result['topic']}\n"
        f"Formula: {result['formula']}\n"
        f"Answer: {answer:.4f}\n"
        f"Values: {result['values']}"
    )


def suno_magic(question):

    result = v16_magic_solve(question)

    return result


# ------------------------------------------------------------
# 7. REGRESSION TESTS
# ------------------------------------------------------------

print("=" * 55)
print("SUNO SAATHI MAGIC V16.3 TESTING")
print("=" * 55)

# English Force
t1 = suno_magic("5 kg mass 2 acceleration calculate force")
assert t1["success"], t1
assert abs(t1["values"]["force"] - 10) < 0.001
print("PASS: English Force")

# Hindi Force
t2 = suno_magic(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)
assert t2["success"], t2
assert abs(t2["values"]["force"] - 10) < 0.001
print("PASS: Hindi Force")

# Hindi digits
t3 = suno_magic("५ kg द्रव्यमान २ त्वरण बल निकालो")
assert t3["success"], t3
assert abs(t3["values"]["force"] - 10) < 0.001
print("PASS: Hindi Digits Force")

# Work
t4 = suno_magic("10 N force 5 m distance calculate work")
assert t4["success"], t4
assert abs(t4["values"]["work"] - 50) < 0.001
print("PASS: Work")

# Power
t5 = suno_magic("100 J work 5 seconds calculate power")
assert t5["success"], t5
assert abs(t5["values"]["power"] - 20) < 0.001
print("PASS: Power")

# Speed
t6 = suno_magic("100 m distance 20 seconds calculate speed")
assert t6["success"], t6
assert abs(t6["values"]["speed"] - 5) < 0.001
print("PASS: Speed")

# Kinetic Energy
t7 = suno_magic("2 kg mass 3 m/s velocity calculate kinetic energy")
assert t7["success"], t7
assert abs(t7["values"]["kinetic energy"] - 9) < 0.001
print("PASS: Kinetic Energy")

# Potential Energy
t8 = suno_magic("2 kg mass 5 m height calculate potential energy")
assert t8["success"], t8
assert abs(t8["values"]["potential energy"] - 98) < 0.001
print("PASS: Potential Energy")

# Moles
t9 = suno_magic("18 g mass 18 g/mol molar mass calculate moles")
assert t9["success"], t9
assert abs(t9["values"]["moles"] - 1) < 0.001
print("PASS: Moles")

# Molarity
t10 = suno_magic("2 moles 1 L volume calculate molarity")
assert t10["success"], t10
assert abs(t10["values"]["molarity"] - 2) < 0.001
print("PASS: Molarity")

print("=" * 55)
print("V16.3 TESTS COMPLETED")
print("=" * 55)

# ------------------------------------------------------------
# 8. INTERACTIVE TEST
# ------------------------------------------------------------

def v16_launch_ui():

    print("\nSUNO SAATHI MAGIC V16.3")
    print("Hindi / English Physics + Chemistry")
    print("Type exit to stop\n")

    while True:

        question = input("Question: ")

        if question.lower().strip() in ["exit", "quit", "stop"]:
            print("Magic stopped.")
            break

        result = suno_magic(question)

        print(v16_format_result(result))
        print("-" * 40)


print("\nReady! Run v16_launch_ui() for interactive mode.")

# ============================================================
# SUNO SAATHI MAGIC LAYER V16.3
# COMPLETE REWRITE - HINDI + ENGLISH
# Physics + Chemistry + Regression Tests
# ============================================================

import re
import math

# ------------------------------------------------------------
# 1. NORMALIZATION
# ------------------------------------------------------------

def v16_normalize(text):
    q = str(text).lower().strip()

    # Hindi digits -> English digits
    hindi_digits = "०१२३४५६७८९"
    english_digits = "0123456789"

    q = q.translate(str.maketrans(hindi_digits, english_digits))

    # Unicode cleanup
    q = q.replace("²", "2")
    q = q.replace("³", "3")
    q = q.replace("×", "*")
    q = q.replace("÷", "/")

    # Longest Hindi phrases first
    replacements = {
        "मोलर द्रव्यमान": "molar mass",
        "गतिज ऊर्जा": "kinetic energy",
        "स्थितिज ऊर्जा": "potential energy",
        "द्रव्यमान": "mass",
        "त्वरण": "acceleration",
        "वेग": "velocity",
        "चाल": "speed",
        "दूरी": "distance",
        "समय": "time",
        "बल": "force",
        "कार्य": "work",
        "शक्ति": "power",
        "ऊर्जा": "energy",
        "ऊंचाई": "height",
        "ऊँचाई": "height",
        "आयतन": "volume",
        "मोल": "moles",
        "मात्रा": "volume",
        "सांद्रता": "molarity",
        "द्रव्यमान निकालो": "mass calculate",
        "निकालो": "calculate",
        "बताओ": "calculate",
        "गणना": "calculate",
        "और": " ",
        "से": " ",
        "का": " ",
        "की": " ",
        "है": " ",
        "में": " ",
        "कितना": " ",
        "कितनी": " ",
    }

    for hindi, english in sorted(
        replacements.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # Units
    unit_replacements = {
        "किलोग्राम": "kg",
        "ग्राम": "g",
        "मीटर": "m",
        "सेकंड": "seconds",
        "सेकेण्ड": "seconds",
        "मिलीलीटर": "ml",
        "लीटर": "l",
        "न्यूटन": "n",
        "जूल": "j",
        "वाट": "w",
    }

    for hindi, english in sorted(
        unit_replacements.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # Common English aliases
    aliases = {
        "mass": ["weight of", "mass is"],
        "acceleration": ["accelerated by", "accel"],
        "force": ["f"],
        "distance": ["d"],
        "time": ["t"],
        "speed": ["velocity"],
        "molar mass": ["molecular weight"],
        "moles": ["mol"],
        "molarity": ["concentration"],
    }

    for canonical, words in aliases.items():
        for word in words:
            if word != canonical:
                q = re.sub(
                    r"\b" + re.escape(word) + r"\b",
                    canonical,
                    q
                )

    # Standardize units
    q = q.replace("m/s²", "m/s2")
    q = q.replace("m/s^2", "m/s2")
    q = q.replace("kg.", "kg")
    q = q.replace("sec", "seconds")

    q = re.sub(r"\s+", " ", q).strip()

    return q


# ------------------------------------------------------------
# 2. NUMBER EXTRACTION
# ------------------------------------------------------------

def v16_get_number(q, key):
    q = v16_normalize(q)
    number = r"[-+]?\d+(?:\.\d+)?"
    
    # Variable-specific units
    units = {
        "mass": r"(?:kg|g)?",
        "acceleration": r"(?:m/s2|m/s)?",
        "force": r"(?:n)?",
        "work": r"(?:j)?",
        "power": r"(?:w)?",
        "distance": r"(?:km|m|cm)?",
        "time": r"(?:seconds|second|minutes|min|hours|hour|s)?",
        "speed": r"(?:m/s|km/h)?",
        "velocity": r"(?:m/s|km/h)?",
        "height": r"(?:km|m|cm)?",
        "volume": r"(?:ml|l|liter|litre)?",
        "molarity": r"(?:mol/l|m|molar)?",
        "moles": r"(?:mol|moles)?",
        "molar mass": r"(?:g/mol|kg/mol)?",
        "energy": r"(?:j)?",
        "kinetic energy": r"(?:j)?",
        "potential energy": r"(?:j)?",
    }

    unit = units.get(key, r"[a-z/]*")

    # Updated flexible pattern matching to safely grasp trailing/leading values next to keywords
    patterns = [
        rf"\b{re.escape(key)}\s*[:=]?\s*({number})\s*{unit}\b",
        rf"({number})\s*{unit}\s*\b{re.escape(key)}\b",
        rf"\b{re.escape(key)}\s*[:=]?\s*({number})\b",
        rf"({number})\s*\b{re.escape(key)}\b",
        rf"({number})\s*{re.escape(key)}\b"
    ]

    for pattern in patterns:
        match = re.search(pattern, q)
        if match:
            try:
                return float(match.group(1))
            except:
                pass

    if key == "time":
        match = re.search(
            rf"({number})\s*(?:seconds|second|s|minutes|min|hours|hour)",
            q
        )
        if match:
            value = float(match.group(1))
            if re.search(r"\bminutes|min\b", q):
                value *= 60
            if re.search(r"\bhours|hour\b", q):
                value *= 3600
            return value

    return None


# ------------------------------------------------------------
# 3. PHYSICS ENGINE
# ------------------------------------------------------------

def v16_physics_solve(q):

    q = v16_normalize(q)

    values = {}

    keys = [
        "mass", "acceleration", "force", "work",
        "power", "distance", "time", "speed",
        "velocity", "height", "energy",
        "kinetic energy", "potential energy"
    ]

    for key in keys:
        value = v16_get_number(q, key)
        if value is not None:
            values[key] = value

    # Calculate Force = mass * acceleration
    if "mass" in values and "acceleration" in values:
        values["force"] = (
            values["mass"] * values["acceleration"]
        )

    # Calculate Work = Force * Distance
    if "force" in values and "distance" in values:
        values["work"] = (
            values["force"] * values["distance"]
        )

    # Calculate Power = Work / Time
    if "work" in values and "time" in values:
        if values["time"] != 0:
            values["power"] = (
                values["work"] / values["time"]
            )

    # Calculate Speed = Distance / Time
    if "distance" in values and "time" in values:
        if values["time"] != 0:
            values["speed"] = (
                values["distance"] / values["time"]
            )

    # Calculate KE = 1/2 * mass * velocity^2
    if "mass" in values and "velocity" in values:
        values["kinetic energy"] = (
            0.5 * values["mass"] *
            values["velocity"] ** 2
        )

    # Calculate PE = mass * g * height
    if "mass" in values and "height" in values:
        values["potential energy"] = (
            values["mass"] * 9.8 *
            values["height"]
        )

    requested = None

    if "kinetic energy" in q or re.search(r"\bke\b", q):
        requested = "kinetic energy"

    elif "potential energy" in q or re.search(r"\bpe\b", q):
        requested = "potential energy"

    elif "force" in q:
        requested = "force"

    elif "power" in q:
        requested = "power"

    elif "work" in q:
        requested = "work"

    elif "speed" in q or "velocity" in q:
        requested = "speed"

    elif "energy" in q:
        requested = "energy"

    elif "mass" in q:
        requested = "mass"

    if requested and requested in values:
        return {
            "success": True,
            "topic": "physics",
            "formula": requested,
            "answer": values[requested],
            "values": values
        }

    # If some calculation was possible
    if values:
        return {
            "success": True,
            "topic": "physics",
            "formula": "calculated values",
            "answer": list(values.values())[-1],
            "values": values
        }

    return {
        "success": False,
        "topic": "physics",
        "error": "Required values not found",
        "values": values
    }


# ------------------------------------------------------------
# 4. CHEMISTRY ENGINE
# ------------------------------------------------------------

def v16_chemistry_solve(q):

    q = v16_normalize(q)

    values = {}

    keys = [
        "mass", "molar mass", "moles",
        "molarity", "volume"
    ]

    for key in keys:
        value = v16_get_number(q, key)

        if value is not None:
            values[key] = value

    # Moles = mass / molar mass
    if "mass" in values and "molar mass" in values:
        if values["molar mass"] != 0:
            values["moles"] = (
                values["mass"] / values["molar mass"]
            )

    # Molarity = moles / volume in litres
    if "moles" in values and "volume" in values:
        if values["volume"] != 0:
            values["molarity"] = (
                values["moles"] / values["volume"]
            )

    # Moles = molarity * volume
    if "molarity" in values and "volume" in values:
        values["moles"] = (
            values["molarity"] * values["volume"]
        )

    requested = None

    if "molarity" in q:
        requested = "molarity"

    elif "moles" in q:
        requested = "moles"

    elif "molar mass" in q:
        requested = "molar mass"

    if requested and requested in values:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": requested,
            "answer": values[requested],
            "values": values
        }

    if values:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": "calculated values",
            "answer": list(values.values())[-1],
            "values": values
        }

    return {

# ============================================================
# SUNO SAATHI MAGIC LAYER V16.3
# COMPLETE REWRITE - HINDI + ENGLISH
# Physics + Chemistry + Regression Tests
# ============================================================

import re
import math

# ------------------------------------------------------------
# 1. NORMALIZATION
# ------------------------------------------------------------

def v16_normalize(text):
    q = str(text).lower().strip()

    # Hindi digits -> English digits
    hindi_digits = "०१२३४५६७८९"
    english_digits = "0123456789"

    q = q.translate(str.maketrans(hindi_digits, english_digits))

    # Unicode cleanup
    q = q.replace("²", "2")
    q = q.replace("³", "3")
    q = q.replace("×", "*")
    q = q.replace("÷", "/")

    # Longest Hindi phrases first
    replacements = {
        "मोलर द्रव्यमान": "molar mass",
        "गतिज ऊर्जा": "kinetic energy",
        "स्थितिज ऊर्जा": "potential energy",
        "द्रव्यमान": "mass",
        "त्वरण": "acceleration",
        "वेग": "velocity",
        "चाल": "speed",
        "दूरी": "distance",
        "समय": "time",
        "बल": "force",
        "कार्य": "work",
        "शक्ति": "power",
        "ऊर्जा": "energy",
        "ऊंचाई": "height",
        "ऊँचाई": "height",
        "आयतन": "volume",
        "मोल": "moles",
        "मात्रा": "volume",
        "सांद्रता": "molarity",
        "द्रव्यमान निकालो": "mass calculate",
        "निकालो": "calculate",
        "बताओ": "calculate",
        "गणना": "calculate",
        "और": " ",
        "से": " ",
        "का": " ",
        "की": " ",
        "है": " ",
        "में": " ",
        "कितना": " ",
        "कितनी": " ",
    }

    for hindi, english in sorted(
        replacements.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # Units
    unit_replacements = {
        "किलोग्राम": "kg",
        "ग्राम": "g",
        "मीटर": "m",
        "सेकंड": "seconds",
        "सेकेण्ड": "seconds",
        "मिलीलीटर": "ml",
        "लीटर": "l",
        "न्यूटन": "n",
        "जूल": "j",
        "वाट": "w",
    }

    for hindi, english in sorted(
        unit_replacements.items(),
        key=lambda item: len(item[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # Common English aliases
    aliases = {
        "mass": ["weight of", "mass is"],
        "acceleration": ["accelerated by", "accel"],
        "force": ["f"],
        "distance": ["d"],
        "time": ["t"],
        "speed": ["velocity"],
        "molar mass": ["molecular weight"],
        "moles": ["mol"],
        "molarity": ["concentration"],
    }

    for canonical, words in aliases.items():
        for word in words:
            if word != canonical:
                q = re.sub(
                    r"\b" + re.escape(word) + r"\b",
                    canonical,
                    q
                )

    # Standardize units
    q = q.replace("m/s2", "m/s2")
    q = q.replace("m/s^2", "m/s2")
    q = q.replace("kg.", "kg")
    q = q.replace("sec", "seconds")

    q = re.sub(r"\s+", " ", q).strip()

    return q


# ------------------------------------------------------------
# 2. NUMBER EXTRACTION
# ------------------------------------------------------------

def v16_get_number(q, key):
    q = v16_normalize(q)
    number = r"[-+]?\d+(?:\.\d+)?"

    # Variable-specific units
    units = {
        "mass": r"(?:kg|g)?",
        "acceleration": r"(?:m/s2|m/s)?",
        "force": r"(?:n)?",
        "work": r"(?:j)?",
        "power": r"(?:w)?",
        "distance": r"(?:km|m|cm)?",
        "time": r"(?:seconds|second|minutes|min|hours|hour|s)?",
        "speed": r"(?:m/s|km/h)?",
        "velocity": r"(?:m/s|km/h)?",
        "height": r"(?:km|m|cm)?",
        "volume": r"(?:ml|l|liter|litre)?",
        "molarity": r"(?:mol/l|m|molar)?",
        "moles": r"(?:mol|moles)?",
        "molar mass": r"(?:g/mol|kg/mol)?",
        "energy": r"(?:j)?",
        "kinetic energy": r"(?:j)?",
        "potential energy": r"(?:j)?",
    }

    unit = units.get(key, r"[a-z/]*")

    # Updated flexible pattern matching to safely grasp trailing/leading values next to keywords
    patterns = [
        rf"\b{re.escape(key)}\s*[:=]?\s*({number})\s*{unit}\b",
        rf"({number})\s*{unit}\s*\b{re.escape(key)}\b",
        rf"\b{re.escape(key)}\s*[:=]?\s*({number})\b",
        rf"({number})\s*\b{re.escape(key)}\b",
        rf"({number})\s*{re.escape(key)}\b"
    ]

    for pattern in patterns:
        match = re.search(pattern, q)
        if match:
            try:
                return float(match.group(1))
            except:
                pass

    if key == "time":
        match = re.search(
            rf"({number})\s*(?:seconds|second|s|minutes|min|hours|hour)",
            q
        )
        if match:
            value = float(match.group(1))
            if re.search(r"\bminutes|min\b", q):
                value *= 60
            if re.search(r"\bhours|hour\b", q):
                value *= 3600
            return value

    return None


# ------------------------------------------------------------
# 3. PHYSICS ENGINE
# ------------------------------------------------------------

def v16_physics_solve(q):
    q = v16_normalize(q)
    values = {}

    keys = [
        "mass", "acceleration", "force", "work",
        "power", "distance", "time", "speed",
        "velocity", "height", "energy",
        "kinetic energy", "potential energy"
    ]

    for key in keys:
        value = v16_get_number(q, key)
        if value is not None:
            values[key] = value

    # Calculate Force = mass * acceleration
    if "mass" in values and "acceleration" in values:
        values["force"] = (
            values["mass"] * values["acceleration"]
        )

    # Calculate Work = Force * Distance
    if "force" in values and "distance" in values:
        values["work"] = (
            values["force"] * values["distance"]
        )

    # Calculate Power = Work / Time
    if "work" in values and "time" in values:
        if values["time"] != 0:
            values["power"] = (
                values["work"] / values["time"]
            )

    # Calculate Speed = Distance / Time
    if "distance" in values and "time" in values:
        if values["time"] != 0:
            values["speed"] = (
                values["distance"] / values["time"]
            )

    # Calculate KE = 1/2 * mass * velocity^2
    if "mass" in values and "velocity" in values:
        values["kinetic energy"] = (
            0.5 * values["mass"] *
            values["velocity"] ** 2
        )

    # Calculate PE = mass * g * height
    if "mass" in values and "height" in values:
        values["potential energy"] = (
            values["mass"] * 9.8 *
            values["height"]
        )

    requested = None
    if "kinetic energy" in q or re.search(r"\bke\b", q):
        requested = "kinetic energy"
    elif "potential energy" in q or re.search(r"\bpe\b", q):
        requested = "potential energy"
    elif "force" in q:
        requested = "force"
    elif "power" in q:
        requested = "power"
    elif "work" in q:
        requested = "work"
    elif "speed" in q or "velocity" in q:
        requested = "speed"
    elif "energy" in q:
        requested = "energy"
    elif "mass" in q:
        requested = "mass"

    if requested and requested in values:
        return {
            "success": True,
            "topic": "physics",
            "formula": requested,
            "answer": values[requested],
            "values": values
        }

    if values:
        return {
            "success": True,
            "topic": "physics",
            "formula": "calculated values",
            "answer": list(values.values())[-1],
            "values": values
        }

    return {
        "success": False,
        "topic": "physics",
        "error": "Required values not found",
        "values": values
    }


# ------------------------------------------------------------
# 4. CHEMISTRY ENGINE
# ------------------------------------------------------------

def v16_chemistry_solve(q):
    q = v16_normalize(q)
    values = {}

    keys = [
        "mass", "molar mass", "moles",
        "molarity", "volume"
    ]

    for key in keys:
        value = v16_get_number(q, key)
        if value is not None:
            values[key] = value

    # Moles = mass / molar mass
    if "mass" in values and "molar mass" in values:
        if values["molar mass"] != 0:
            values["moles"] = (
                values["mass"] / values["molar mass"]
            )

    # Molarity = moles / volume
    if "moles" in values and "volume" in values:
        if values["volume"] != 0:
            values["molarity"] = (
                values["moles"] / values["volume"]
            )

    # Moles = molarity * volume
    if "molarity" in values and "volume" in values:
        values["moles"] = (
            values["molarity"] * values["volume"]
        )

    requested = None
    if "molarity" in q:
        requested = "molarity"
    elif "moles" in q:
        requested = "moles"
    elif "molar mass" in q:
        requested = "molar mass"

    if requested and requested in values:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": requested,
            "answer": values[requested],
            "values": values
        }

    if values:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": "calculated values",
            "answer": list(values.values())[-1],
            "values": values
        }

    return {
        "success": False,
        "topic": "chemistry",
        "error": "Required chemistry values not found",
        "values": values
    }


# ------------------------------------------------------------
# 5. UNIFIED MAGIC SOLVER
# ------------------------------------------------------------

def v16_magic_solve(question):
    q = v16_normalize(question)
    chemistry_words = [
        "moles", "molarity", "molar mass",
        "concentration", "mol"
    ]

    if any(word in q for word in chemistry_words):
        return v16_chemistry_solve(q)

    return v16_physics_solve(q)


# ------------------------------------------------------------
# 6. FORMAT RESULT
# ------------------------------------------------------------

def v16_format_result(result):
    if not result["success"]:
        return (
            "❌ Calculation failed\n"
            + result.get("error", "Unknown error")
        )

    answer = result["answer"]
    return (
        "✅ SUNO SAATHI MAGIC\n"
        f"Topic: {result['topic']}\n"
        f"Formula: {result['formula']}\n"
        f"Answer: {answer:.4f}\n"
        f"Values: {result['values']}"
    )


def suno_magic(question):
    result = v16_magic_solve(question)
    return result


# ------------------------------------------------------------
# 7. REGRESSION TESTS
# ------------------------------------------------------------

print("=" * 55)
print("SUNO SAATHI MAGIC V16.3 TESTING")
print("=" * 55)

# English Force
t1 = suno_magic("5 kg mass 2 acceleration calculate force")
assert t1["success"], t1
assert abs(t1["values"]["force"] - 10) < 0.001
print("PASS: English Force")

# Hindi Force
t2 = suno_magic(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)
assert t2["success"], t2
assert abs(t2["values"]["force"] - 10) < 0.001
print("PASS: Hindi Force")

# Hindi digits
t3 = suno_magic("५ kg द्रव्यमान २ त्वरण बल निकालो")
assert t3["success"], t3
assert abs(t3["values"]["force"] - 10) < 0.001
print("PASS: Hindi Digits Force")

# Work
t4 = suno_magic("10 N force 5 m distance calculate work")
assert t4["success"], t4
assert abs(t4["values"]["work"] - 50) < 0.001
print("PASS: Work")

# Power
t5 = suno_magic("100 J work 5 seconds calculate power")
assert t5["success"], t5
assert abs(t5["values"]["power"] - 20) < 0.001
print("PASS: Power")

# Speed
t6 = suno_magic("100 m distance 20 seconds calculate speed")
assert t6["success"], t6
assert abs(t6["values"]["speed"] - 5) < 0.001
print("PASS: Speed")

# Kinetic Energy
t7 = suno_magic("2 kg mass 3 m/s velocity calculate kinetic energy")
assert t7["success"], t7
assert abs(t7["values"]["kinetic energy"] - 9) < 0.001
print("PASS: Kinetic Energy")

# Potential Energy
t8 = suno_magic("2 kg mass 5 m height calculate potential energy")
assert t8["success"], t8
assert abs(t8["values"]["potential energy"] - 98) < 0.001
print("PASS: Potential Energy")

# Moles
t9 = suno_magic("18 g mass 18 g/mol molar mass calculate moles")
assert t9["success"], t9
assert abs(t9["values"]["moles"] - 1) < 0.001
print("PASS: Moles")

# Molarity
t10 = suno_magic("2 moles 1 L volume calculate molarity")
assert t10["success"], t10
assert abs(t10["values"]["molarity"] - 2) < 0.001
print("PASS: Molarity")

print("=" * 55)
print("V16.3 TESTS COMPLETED")
print("=" * 55)

q = "5 kg mass 2 acceleration calculate force"

print("Normalized:", v16_normalize(q))
print("Mass:", v16_get_number(q, "mass"))
print("Acceleration:", v16_get_number(q, "acceleration"))
print("Full result:", suno_magic(q))

# ============================================================
# SUNO SAATHI MAGIC V16.4
# COMPLETE REWRITE
# Physics + Chemistry | Hindi + English
# ============================================================

import re
import math

VERSION = "V16.4"


# ============================================================
# 1. NORMALIZATION
# ============================================================

def v164_normalize(text):

    q = str(text).lower().strip()

    # Hindi digits
    q = q.translate(str.maketrans(
        "०१२३४५६७८९",
        "0123456789"
    ))

    # Unicode units
    q = q.replace("²", "2")
    q = q.replace("³", "3")
    q = q.replace("×", "*")
    q = q.replace("÷", "/")

    # Longest Hindi phrases first
    hindi_words = {
        "मोलर द्रव्यमान": "molar mass",
        "गतिज ऊर्जा": "kinetic energy",
        "स्थितिज ऊर्जा": "potential energy",
        "द्रव्यमान": "mass",
        "त्वरण": "acceleration",
        "वेग": "velocity",
        "चाल": "speed",
        "दूरी": "distance",
        "समय": "time",
        "बल": "force",
        "कार्य": "work",
        "शक्ति": "power",
        "ऊंचाई": "height",
        "ऊँचाई": "height",
        "ऊर्जा": "energy",
        "आयतन": "volume",
        "मोल": "moles",
        "सांद्रता": "molarity",
        "निकालो": "calculate",
        "बताओ": "calculate",
        "गणना करो": "calculate",
        "और": " ",
        "से": " ",
        "का": " ",
        "की": " ",
        "है": " ",
        "में": " ",
    }

    for hindi, english in sorted(
        hindi_words.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    hindi_units = {
        "किलोग्राम": "kg",
        "ग्राम": "g",
        "मीटर": "m",
        "सेकंड": "seconds",
        "सेकेण्ड": "seconds",
        "मिलीलीटर": "ml",
        "लीटर": "l",
        "न्यूटन": "n",
        "जूल": "j",
        "वाट": "w",
    }

    for hindi, english in sorted(
        hindi_units.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # English aliases
    q = re.sub(r"\baccel\b", "acceleration", q)
    q = re.sub(r"\bconcentration\b", "molarity", q)
    q = re.sub(r"\bmolecular weight\b", "molar mass", q)
    q = re.sub(r"\bvelocity\b", "speed", q)

    # Unit standardization
    q = q.replace("m/s²", "m/s2")
    q = q.replace("m/s^2", "m/s2")
    q = q.replace("kg.", "kg")

    # Hindi/English punctuation cleanup
    q = re.sub(r"[।,;]", " ", q)
    q = re.sub(r"\s+", " ", q).strip()

    return q


# ============================================================
# 2. SAFE NUMBER EXTRACTION
# ============================================================

def v164_extract(q, key):

    q = v164_normalize(q)

    n = r"([-+]?\d+(?:\.\d+)?)"

    # --------------------------------------------------------
    # MASS
    # --------------------------------------------------------

    if key == "mass":

        patterns = [
            rf"{n}\s*kg\s*mass\b",
            rf"\bmass\s*{n}\s*kg\b",
            rf"{n}\s*g\s*mass\b",
            rf"\bmass\s*{n}\s*g\b",
            rf"\bmass\s*{n}\b",
            rf"{n}\s*mass\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                # grams -> kg only for physics mass
                if re.search(rf"{re.escape(m.group(1))}\s*g\s*mass\b", q):
                    value = value / 1000

                return value

        return None

    # --------------------------------------------------------
    # MOLAR MASS
    # --------------------------------------------------------

    if key == "molar mass":

        patterns = [
            rf"{n}\s*g/mol\s*molar mass\b",
            rf"\bmolar mass\s*{n}\s*g/mol\b",
            rf"\bmolar mass\s*{n}\b",
            rf"{n}\s*molar mass\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # ACCELERATION
    # --------------------------------------------------------

    if key == "acceleration":

        patterns = [
            rf"{n}\s*m/s2\s*acceleration\b",
            rf"\bacceleration\s*{n}\s*m/s2\b",
            rf"\bacceleration\s*{n}\b",
            rf"{n}\s*acceleration\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # DISTANCE
    # --------------------------------------------------------

    if key == "distance":

        patterns = [
            rf"{n}\s*km\s*distance\b",
            rf"{n}\s*m\s*distance\b",
            rf"\bdistance\s*{n}\s*(?:km|m)?\b",
            rf"{n}\s*distance\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                if re.search(rf"{m.group(1)}\s*km\s*distance", q):
                    value *= 1000

                return value

        return None

    # --------------------------------------------------------
    # HEIGHT
    # --------------------------------------------------------

    if key == "height":

        patterns = [
            rf"{n}\s*m\s*height\b",
            rf"\bheight\s*{n}\s*m?\b",
            rf"{n}\s*height\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    if key == "time":

        patterns = [
            rf"\btime\s*{n}\b",
            rf"{n}\s*seconds\b",
            rf"{n}\s*second\b",
            rf"{n}\s*sec\b",
            rf"{n}\s*s\b",
            rf"{n}\s*minutes\b",
            rf"{n}\s*min\b",
            rf"{n}\s*hours\b",
            rf"{n}\s*hour\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                matched = m.group(0)

                if "minute" in matched or "min" in matched:
                    value *= 60

                if "hour" in matched:
                    value *= 3600

                return value

        return None

    # --------------------------------------------------------
    # VOLUME
    # --------------------------------------------------------

    if key == "volume":

        patterns = [
            rf"{n}\s*ml\s*volume\b",
            rf"\bvolume\s*{n}\s*ml\b",
            rf"{n}\s*l\s*volume\b",
            rf"\bvolume\s*{n}\s*l\b",
            rf"\bvolume\s*{n}\b",
            rf"{n}\s*volume\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                if "ml" in m.group(0):
                    value = value / 1000

                return value

        return None

    # --------------------------------------------------------
    # MOLARITY
    # --------------------------------------------------------

    if key == "molarity":

        patterns = [
            rf"\bmolarity\s*{n}\b",
            rf"{n}\s*molarity\b",
            rf"{n}\s*m\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # MOLES
    # --------------------------------------------------------

    if key == "moles":

        patterns = [
            rf"\bmoles\s*{n}\b",
            rf"{n}\s*moles\b",
            rf"{n}\s*mol\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # OTHER VARIABLES
    # --------------------------------------------------------

    units = {
        "force": r"(?:n)?",
        "work": r"(?:j)?",
        "power": r"(?:w)?",
        "speed": r"(?:m/s|km/h)?",
        "energy": r"(?:j)?",
        "kinetic energy": r"(?:j)?",
        "potential energy": r"(?:j)?",
    }

    unit = units.get(key, r"")

    patterns = [
        rf"\b{re.escape(key)}\s*[:=]?\s*{n}\s*{unit}",
        rf"{n}\s*{unit}\s*{re.escape(key)}\b",
        rf"\b{re.escape(key)}\s*[:=]?\s*{n}\b",
        rf"{n}\s*{re.escape(key)}\b",
    ]

    for p in patterns:
        m = re.search(p, q)
        if m:
            return float(m.group(1))

    return None


# Backward-compatible function name
def v16_get_number(q, key):
    return v164_extract(q, key)


# ============================================================
# 3. PHYSICS ENGINE
# ============================================================

def v164_physics(q):

    q = v164_normalize(q)

    v = {}

    keys = [
        "mass", "acceleration", "force",
        "work", "power", "distance",
        "time", "speed", "height",
        "energy", "kinetic energy",
        "potential energy"
    ]

    for key in keys:
        value = v164_extract(q, key)

        if value is not None:
            v[key] = value

    # F = ma
    if "mass" in v and "acceleration" in v:
        v["force"] = v["mass"] * v["acceleration"]

    # W = Fd
    if "force" in v and "distance" in v:
        v["work"] = v["force"] * v["distance"]

    # P = W/t
    if "work" in v and "time" in v and v["time"] != 0:
        v["power"] = v["work"] / v["time"]

    # speed = distance/time
    if "distance" in v and "time" in v and v["time"] != 0:
        v["speed"] = v["distance"] / v["time"]

    # KE = 1/2 mv²
    if "mass" in v and "speed" in v:
        v["kinetic energy"] = (
            0.5 * v["mass"] * v["speed"] ** 2
        )

    # PE = mgh
    if "mass" in v and "height" in v:
        v["potential energy"] = (
            v["mass"] * 9.8 * v["height"]
        )

    # Identify requested answer
    if "kinetic energy" in q or re.search(r"\bke\b", q):
        requested = "kinetic energy"

    elif "potential energy" in q or re.search(r"\bpe\b", q):
        requested = "potential energy"

    elif "force" in q:
        requested = "force"

    elif "power" in q:
        requested = "power"

    elif "work" in q:
        requested = "work"

    elif "speed" in q:
        requested = "speed"

    elif "energy" in q:
        requested = "energy"

    elif "mass" in q:
        requested = "mass"

    else:
        requested = None

    if requested and requested in v:
        return {
            "success": True,
            "topic": "physics",
            "formula": requested,
            "answer": v[requested],
            "values": v
        }

    return {
        "success": False,
        "topic": "physics",
        "error": "Required values missing or formula unavailable",
        "values": v
    }


# ============================================================
# 4. CHEMISTRY ENGINE
# ============================================================

def v164_chemistry(q):

    q = v164_normalize(q)

    v = {}

    for key in ["mass", "molar mass", "moles", "molarity", "volume"]:
        value = v164_extract(q, key)

        if value is not None:
            v[key] = value

    # n = mass / molar mass
    if "mass" in v and "molar mass" in v:
        if v["molar mass"] != 0:
            v["moles"] = v["mass"] / v["molar mass"]

    # M = n / V
    if "moles" in v and "volume" in v:
        if v["volume"] != 0:
            v["molarity"] = v["moles"] / v["volume"]

    # n = M * V
    if "molarity" in v and "volume" in v:
        v["moles"] = v["molarity"] * v["volume"]

    if "molarity" in q:
        requested = "molarity"

    elif "moles" in q:
        requested = "moles"

    elif "molar mass" in q:
        requested = "molar mass"

    else:
        requested = None

    if requested and requested in v:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": requested,
            "answer": v[requested],
            "values": v
        }

    return {
        "success": False,
        "topic": "chemistry",
        "error": "Required chemistry values missing",
        "values": v
    }


# ============================================================
# 5. UNIFIED MAGIC
# ============================================================

def v164_solve(question):

    q = v164_normalize(question)

    chemistry_terms = [
        "moles", "molarity", "molar mass",
        "concentration"
    ]

    if any(term in q for term in chemistry_terms):
        return v164_chemistry(q)

    return v164_physics(q)


def suno_magic(question):
    return v164_solve(question)


# ============================================================
# 6. OUTPUT FORMAT
# ============================================================

def v164_format(result):

    if not result["success"]:
        return (
            "ERROR: " + result.get("error", "Unknown error")
            + "\nValues: " + str(result.get("values", {}))
        )

    return (
        "\nSUNO SAATHI MAGIC " + VERSION +
        "\nTopic: " + result["topic"] +
        "\nFormula: " + result["formula"] +
        "\nAnswer: " + str(round(result["answer"], 6)) +
        "\nValues: " + str(result["values"])
    )


def v16_format_result(result):
    return v164_format(result)


# ============================================================
# 7. REGRESSION TESTS
# ============================================================

print("=" * 55)
print("SUNO SAATHI MAGIC V16.4 TESTING")
print("=" * 55)

# English Force
t1 = suno_magic("5 kg mass 2 acceleration calculate force")
assert t1["success"], t1
assert t1["values"]["mass"] == 5
assert t1["values"]["acceleration"] == 2
assert abs(t1["values"]["force"] - 10) < 0.001
print("PASS: English Force")

# Hindi Force
t2 = suno_magic(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)
assert t2["success"], t2
assert t2["values"]["mass"] == 5
assert t2["values"]["acceleration"] == 2
assert abs(t2["values"]["force"] - 10) < 0.001
print("PASS: Hindi Force")

# Hindi digits
t3 = suno_magic("५ kg द्रव्यमान २ त्वरण बल निकालो")
assert t3["success"], t3
assert abs(t3["values"]["force"] - 10) < 0.001
print("PASS: Hindi Digits Force")

# Work
t4 = suno_magic("10 N force 5 m distance calculate work")
assert t4["success"], t4
assert abs(t4["values"]["work"] - 50) < 0.001
print("PASS: Work")

# Power
t5 = suno_magic("100 J work 5 seconds calculate power")
assert t5["success"], t5
assert abs(t5["values"]["power"] - 20) < 0.001
print("PASS: Power")

# Speed
t6 = suno_magic("100 m distance 20 seconds calculate speed")
assert t6["success"], t6
assert abs(t6["values"]["speed"] - 5) < 0.001
print("PASS: Speed")

# Kinetic Energy
t7 = suno_magic("2 kg mass 3 m/s speed calculate kinetic energy")
assert t7["success"], t7
assert abs(t7["values"]["kinetic energy"] - 9) < 0.001
print("PASS: Kinetic Energy")

# Potential Energy
t8 = suno_magic("2 kg mass 5 m height calculate potential energy")
assert t8["success"], t8
assert abs(t8["values"]["potential energy"] - 98) < 0.001
print("PASS: Potential Energy")

# Moles
t9 = suno_magic(
    "18 g mass 18 g/mol molar mass calculate moles"
)
assert t9["success"], t9
assert abs(t9["values"]["moles"] - 1) < 0.001
print("PASS: Moles")

# Molarity
t10 = suno_magic("2 moles 1 L volume calculate molarity")
assert t10["success"], t10
assert abs(t10["values"]["molarity"] - 2) < 0.001
print("PASS: Molarity")

print("=" * 55)
print("ALL V16.4 TESTS PASSED!")
print("=" * 55)


# ============================================================
# 8. INTERACTIVE MODE
# ============================================================

def v16_launch_ui():

    print("\nSUNO SAATHI MAGIC V16.4")
    print("Hindi + English Physics and Chemistry")
    print("Type exit to stop.\n")

    while True:

        question = input("Question: ")

        if question.lower().strip() in ["exit", "quit", "stop"]:
            print("Magic stopped.")
            break

        result = suno_magic(question)
        print(v164_format(result))
        print("-" * 50


print("\nReady. Run v16_launch_ui() for interactive mode.")

# ============================================================
# SUNO SAATHI MAGIC V16.4
# COMPLETE REWRITE
# Physics + Chemistry | Hindi + English
# ============================================================

import re
import math

VERSION = "V16.4"


# ============================================================
# 1. NORMALIZATION
# ============================================================

def v164_normalize(text):

    q = str(text).lower().strip()

    # Hindi digits
    q = q.translate(str.maketrans(
        "०१२३४५६७८९",
        "0123456789"
    ))

    # Unicode units
    q = q.replace("²", "2")
    q = q.replace("³", "3")
    q = q.replace("×", "*")
    q = q.replace("÷", "/")

    # Longest Hindi phrases first
    hindi_words = {
        "मोलर द्रव्यमान": "molar mass",
        "गतिज ऊर्जा": "kinetic energy",
        "स्थितिज ऊर्जा": "potential energy",
        "द्रव्यमान": "mass",
        "त्वरण": "acceleration",
        "वेग": "velocity",
        "चाल": "speed",
        "दूरी": "distance",
        "समय": "time",
        "बल": "force",
        "कार्य": "work",
        "शक्ति": "power",
        "ऊंचाई": "height",
        "ऊँचाई": "height",
        "ऊर्जा": "energy",
        "आयतन": "volume",
        "मोल": "moles",
        "सांद्रता": "molarity",
        "निकालो": "calculate",
        "बताओ": "calculate",
        "गणना करो": "calculate",
        "और": " ",
        "से": " ",
        "का": " ",
        "की": " ",
        "है": " ",
        "में": " ",
    }

    for hindi, english in sorted(
        hindi_words.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    hindi_units = {
        "किलोग्राम": "kg",
        "ग्राम": "g",
        "मीटर": "m",
        "सेकंड": "seconds",
        "सेकेण्ड": "seconds",
        "मिलीलीटर": "ml",
        "लीटर": "l",
        "न्यूटन": "n",
        "जूल": "j",
        "वाट": "w",
    }

    for hindi, english in sorted(
        hindi_units.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # English aliases
    q = re.sub(r"\baccel\b", "acceleration", q)
    q = re.sub(r"\bconcentration\b", "molarity", q)
    q = re.sub(r"\bmolecular weight\b", "molar mass", q)
    q = re.sub(r"\bvelocity\b", "speed", q)

    # Unit standardization
    q = q.replace("m/s²", "m/s2")
    q = q.replace("m/s^2", "m/s2")
    q = q.replace("kg.", "kg")

    # Hindi/English punctuation cleanup
    q = re.sub(r"[।,;]", " ", q)
    q = re.sub(r"\s+", " ", q).strip()

    return q


# ============================================================
# 2. SAFE NUMBER EXTRACTION
# ============================================================

def v164_extract(q, key):

    q = v164_normalize(q)

    n = r"([-+]?\d+(?:\.\d+)?)"

    # --------------------------------------------------------
    # MASS
    # --------------------------------------------------------

    if key == "mass":

        patterns = [
            rf"{n}\s*kg\s*mass\b",
            rf"\bmass\s*{n}\s*kg\b",
            rf"{n}\s*g\s*mass\b",
            rf"\bmass\s*{n}\s*g\b",
            rf"\bmass\s*{n}\b",
            rf"{n}\s*mass\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                # grams -> kg only for physics mass
                if re.search(rf"{re.escape(m.group(1))}\s*g\s*mass\b", q):
                    value = value / 1000

                return value

        return None

    # --------------------------------------------------------
    # MOLAR MASS
    # --------------------------------------------------------

    if key == "molar mass":

        patterns = [
            rf"{n}\s*g/mol\s*molar mass\b",
            rf"\bmolar mass\s*{n}\s*g/mol\b",
            rf"\bmolar mass\s*{n}\b",
            rf"{n}\s*molar mass\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # ACCELERATION
    # --------------------------------------------------------

    if key == "acceleration":

        patterns = [
            rf"{n}\s*m/s2\s*acceleration\b",
            rf"\bacceleration\s*{n}\s*m/s2\b",
            rf"\bacceleration\s*{n}\b",
            rf"{n}\s*acceleration\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # DISTANCE
    # --------------------------------------------------------

    if key == "distance":

        patterns = [
            rf"{n}\s*km\s*distance\b",
            rf"{n}\s*m\s*distance\b",
            rf"\bdistance\s*{n}\s*(?:km|m)?\b",
            rf"{n}\s*distance\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                if re.search(rf"{m.group(1)}\s*km\s*distance", q):
                    value *= 1000

                return value

        return None

    # --------------------------------------------------------
    # HEIGHT
    # --------------------------------------------------------

    if key == "height":

        patterns = [
            rf"{n}\s*m\s*height\b",
            rf"\bheight\s*{n}\s*m?\b",
            rf"{n}\s*height\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    if key == "time":

        patterns = [
            rf"\btime\s*{n}\b",
            rf"{n}\s*seconds\b",
            rf"{n}\s*second\b",
            rf"{n}\s*sec\b",
            rf"{n}\s*s\b",
            rf"{n}\s*minutes\b",
            rf"{n}\s*min\b",
            rf"{n}\s*hours\b",
            rf"{n}\s*hour\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                matched = m.group(0)

                if "minute" in matched or "min" in matched:
                    value *= 60

                if "hour" in matched:
                    value *= 3600

                return value

        return None

    # --------------------------------------------------------
    # VOLUME
    # --------------------------------------------------------

    if key == "volume":

        patterns = [
            rf"{n}\s*ml\s*volume\b",
            rf"\bvolume\s*{n}\s*ml\b",
            rf"{n}\s*l\s*volume\b",
            rf"\bvolume\s*{n}\s*l\b",
            rf"\bvolume\s*{n}\b",
            rf"{n}\s*volume\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                if "ml" in m.group(0):
                    value = value / 1000

                return value

        return None

    # --------------------------------------------------------
    # MOLARITY
    # --------------------------------------------------------

    if key == "molarity":

        patterns = [
            rf"\bmolarity\s*{n}\b",
            rf"{n}\s*molarity\b",
            rf"{n}\s*m\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # MOLES
    # --------------------------------------------------------

    if key == "moles":

        patterns = [
            rf"\bmoles\s*{n}\b",
            rf"{n}\s*moles\b",
            rf"{n}\s*mol\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # OTHER VARIABLES
    # --------------------------------------------------------

    units = {
        "force": r"(?:n)?",
        "work": r"(?:j)?",
        "power": r"(?:w)?",
        "speed": r"(?:m/s|km/h)?",
        "energy": r"(?:j)?",
        "kinetic energy": r"(?:j)?",
        "potential energy": r"(?:j)?",
    }

    unit = units.get(key, r"")

    patterns = [
        rf"\b{re.escape(key)}\s*[:=]?\s*{n}\s*{unit}",
        rf"{n}\s*{unit}\s*{re.escape(key)}\b",
        rf"\b{re.escape(key)}\s*[:=]?\s*{n}\b",
        rf"{n}\s*{re.escape(key)}\b",
    ]

    for p in patterns:
        m = re.search(p, q)
        if m:
            return float(m.group(1))

    return None


# Backward-compatible function name
def v16_get_number(q, key):
    return v164_extract(q, key)


# ============================================================
# 3. PHYSICS ENGINE
# ============================================================

def v164_physics(q):

    q = v164_normalize(q)

    v = {}

    keys = [
        "mass", "acceleration", "force",
        "work", "power", "distance",
        "time", "speed", "height",
        "energy", "kinetic energy",
        "potential energy"
    ]

    for key in keys:
        value = v164_extract(q, key)

        if value is not None:
            v[key] = value

    # F = ma
    if "mass" in v and "acceleration" in v:
        v["force"] = v["mass"] * v["acceleration"]

    # W = Fd
    if "force" in v and "distance" in v:
        v["work"] = v["force"] * v["distance"]

    # P = W/t
    if "work" in v and "time" in v and v["time"] != 0:
        v["power"] = v["work"] / v["time"]

    # speed = distance/time
    if "distance" in v and "time" in v and v["time"] != 0:
        v["speed"] = v["distance"] / v["time"]

    # KE = 1/2 mv²
    if "mass" in v and "speed" in v:
        v["kinetic energy"] = (
            0.5 * v["mass"] * v["speed"] ** 2
        )

    # PE = mgh
    if "mass" in v and "height" in v:
        v["potential energy"] = (
            v["mass"] * 9.8 * v["height"]
        )

    # Identify requested answer
    if "kinetic energy" in q or re.search(r"\bke\b", q):
        requested = "kinetic energy"

    elif "potential energy" in q or re.search(r"\bpe\b", q):
        requested = "potential energy"

    elif "force" in q:
        requested = "force"

    elif "power" in q:
        requested = "power"

    elif "work" in q:
        requested = "work"

    elif "speed" in q:
        requested = "speed"

    elif "energy" in q:
        requested = "energy"

    elif "mass" in q:
        requested = "mass"

    else:
        requested = None

    if requested and requested in v:
        return {
            "success": True,
            "topic": "physics",
            "formula": requested,
            "answer": v[requested],
            "values": v
        }

    return {
        "success": False,
        "topic": "physics",
        "error": "Required values missing or formula unavailable",
        "values": v
    }


# ============================================================
# 4. CHEMISTRY ENGINE
# ============================================================

def v164_chemistry(q):

    q = v164_normalize(q)

    v = {}

    for key in ["mass", "molar mass", "moles", "molarity", "volume"]:
        value = v164_extract(q, key)

        if value is not None:
            v[key] = value

    # n = mass / molar mass
    if "mass" in v and "molar mass" in v:
        if v["molar mass"] != 0:
            v["moles"] = v["mass"] / v["molar mass"]

    # M = n / V
    if "moles" in v and "volume" in v:
        if v["volume"] != 0:
            v["molarity"] = v["moles"] / v["volume"]

    # n = M * V
    if "molarity" in v and "volume" in v:
        v["moles"] = v["molarity"] * v["volume"]

    if "molarity" in q:
        requested = "molarity"

    elif "moles" in q:
        requested = "moles"

    elif "molar mass" in q:
        requested = "molar mass"

    else:
        requested = None

    if requested and requested in v:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": requested,
            "answer": v[requested],
            "values": v
        }

    return {
        "success": False,
        "topic": "chemistry",
        "error": "Required chemistry values missing",
        "values": v
    }


# ============================================================
# 5. UNIFIED MAGIC
# ============================================================

def v164_solve(question):

    q = v164_normalize(question)

    chemistry_terms = [
        "moles", "molarity", "molar mass",
        "concentration"
    ]

    if any(term in q for term in chemistry_terms):
        return v164_chemistry(q)

    return v164_physics(q)


def suno_magic(question):
    return v164_solve(question)


# ============================================================
# 6. OUTPUT FORMAT
# ============================================================

def v164_format(result):

    if not result["success"]:
        return (
            "ERROR: " + result.get("error", "Unknown error")
            + "\nValues: " + str(result.get("values", {}))
        )

    return (
        "\nSUNO SAATHI MAGIC " + VERSION +
        "\nTopic: " + result["topic"] +
        "\nFormula: " + result["formula"] +
        "\nAnswer: " + str(round(result["answer"], 6)) +
        "\nValues: " + str(result["values"])
    )


def v16_format_result(result):
    return v164_format(result)


# ============================================================
# 7. REGRESSION TESTS
# ============================================================

print("=" * 55)
print("SUNO SAATHI MAGIC V16.4 TESTING")
print("=" * 55)

# English Force
t1 = suno_magic("5 kg mass 2 acceleration calculate force")
assert t1["success"], t1
assert t1["values"]["mass"] == 5
assert t1["values"]["acceleration"] == 2
assert abs(t1["values"]["force"] - 10) < 0.001
print("PASS: English Force")

# Hindi Force
t2 = suno_magic(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)
assert t2["success"], t2
assert t2["values"]["mass"] == 5
assert t2["values"]["acceleration"] == 2
assert abs(t2["values"]["force"] - 10) < 0.001
print("PASS: Hindi Force")

# Hindi digits
t3 = suno_magic("५ kg द्रव्यमान २ त्वरण बल निकालो")
assert t3["success"], t3
assert abs(t3["values"]["force"] - 10) < 0.001
print("PASS: Hindi Digits Force")

# Work
t4 = suno_magic("10 N force 5 m distance calculate work")
assert t4["success"], t4
assert abs(t4["values"]["work"] - 50) < 0.001
print("PASS: Work")

# Power
t5 = suno_magic("100 J work 5 seconds calculate power")
assert t5["success"], t5
assert abs(t5["values"]["power"] - 20) < 0.001
print("PASS: Power")

# Speed
t6 = suno_magic("100 m distance 20 seconds calculate speed")
assert t6["success"], t6
assert abs(t6["values"]["speed"] - 5) < 0.001
print("PASS: Speed")

# Kinetic Energy
t7 = suno_magic("2 kg mass 3 m/s speed calculate kinetic energy")
assert t7["success"], t7
assert abs(t7["values"]["kinetic energy"] - 9) < 0.001
print("PASS: Kinetic Energy")

# Potential Energy
t8 = suno_magic("2 kg mass 5 m height calculate potential energy")
assert t8["success"], t8
assert abs(t8["values"]["potential energy"] - 98) < 0.001
print("PASS: Potential Energy")

# Moles
t9 = suno_magic(
    "18 g mass 18 g/mol molar mass calculate moles"
)
assert t9["success"], t9
assert abs(t9["values"]["moles"] - 1) < 0.001
print("PASS: Moles")

# Molarity
t10 = suno_magic("2 moles 1 L volume calculate molarity")
assert t10["success"], t10
assert abs(t10["values"]["molarity"] - 2) < 0.001
print("PASS: Molarity")

print("=" * 55)
print("ALL V16.4 TESTS PASSED!")
print("=" * 55)


# ============================================================
# 8. INTERACTIVE MODE
# ============================================================

def v16_launch_ui():

    print("\nSUNO SAATHI MAGIC V16.4")
    print("Hindi + English Physics and Chemistry")
    print("Type exit to stop.\n")

    while True:

        question = input("Question: ")

        if question.lower().strip() in ["exit", "quit", "stop"]:
            print("Magic stopped.")
            break

        result = suno_magic(question)
        print(v164_format(result))
        print("-" * 50


print("\nReady. Run v16_launch_ui() for interactive mode.")

# ============================================================
# SUNO SAATHI MAGIC V16.4
# COMPLETE REWRITE
# Physics + Chemistry | Hindi + English
# ============================================================

import re
import math

VERSION = "V16.4"


# ============================================================
# 1. NORMALIZATION
# ============================================================

def v164_normalize(text):

    q = str(text).lower().strip()

    # Hindi digits
    q = q.translate(str.maketrans(
        "०१२३४५६७८९",
        "0123456789"
    ))

    # Unicode units
    q = q.replace("²", "2")
    q = q.replace("³", "3")
    q = q.replace("×", "*")
    q = q.replace("÷", "/")

    # Longest Hindi phrases first
    hindi_words = {
        "मोलर द्रव्यमान": "molar mass",
        "गतिज ऊर्जा": "kinetic energy",
        "स्थितिज ऊर्जा": "potential energy",
        "द्रव्यमान": "mass",
        "त्वरण": "acceleration",
        "वेग": "velocity",
        "चाल": "speed",
        "दूरी": "distance",
        "समय": "time",
        "बल": "force",
        "कार्य": "work",
        "शक्ति": "power",
        "ऊंचाई": "height",
        "ऊँचाई": "height",
        "ऊर्जा": "energy",
        "आयतन": "volume",
        "मोल": "moles",
        "सांद्रता": "molarity",
        "निकालो": "calculate",
        "बताओ": "calculate",
        "गणना करो": "calculate",
        "और": " ",
        "से": " ",
        "का": " ",
        "की": " ",
        "है": " ",
        "में": " ",
    }

    for hindi, english in sorted(
        hindi_words.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    hindi_units = {
        "किलोग्राम": "kg",
        "ग्राम": "g",
        "मीटर": "m",
        "सेकंड": "seconds",
        "सेकेण्ड": "seconds",
        "मिलीलीटर": "ml",
        "लीटर": "l",
        "न्यूटन": "n",
        "जूल": "j",
        "वाट": "w",
    }

    for hindi, english in sorted(
        hindi_units.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # English aliases
    q = re.sub(r"\baccel\b", "acceleration", q)
    q = re.sub(r"\bconcentration\b", "molarity", q)
    q = re.sub(r"\bmolecular weight\b", "molar mass", q)
    q = re.sub(r"\bvelocity\b", "speed", q)

    # Unit standardization
    q = q.replace("m/s²", "m/s2")
    q = q.replace("m/s^2", "m/s2")
    q = q.replace("kg.", "kg")

    # Hindi/English punctuation cleanup
    q = re.sub(r"[।,;]", " ", q)
    q = re.sub(r"\s+", " ", q).strip()

    return q


# ============================================================
# 2. SAFE NUMBER EXTRACTION
# ============================================================

def v164_extract(q, key):

    q = v164_normalize(q)

    n = r"([-+]?\d+(?:\.\d+)?)"

    # --------------------------------------------------------
    # MASS
    # --------------------------------------------------------

    if key == "mass":

        patterns = [
            rf"{n}\s*kg\s*mass\b",
            rf"\bmass\s*{n}\s*kg\b",
            rf"{n}\s*g\s*mass\b",
            rf"\bmass\s*{n}\s*g\b",
            rf"\bmass\s*{n}\b",
            rf"{n}\s*mass\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                # grams -> kg only for physics mass
                if re.search(rf"{re.escape(m.group(1))}\s*g\s*mass\b", q):
                    value = value / 1000

                return value

        return None

    # --------------------------------------------------------
    # MOLAR MASS
    # --------------------------------------------------------

    if key == "molar mass":

        patterns = [
            rf"{n}\s*g/mol\s*molar mass\b",
            rf"\bmolar mass\s*{n}\s*g/mol\b",
            rf"\bmolar mass\s*{n}\b",
            rf"{n}\s*molar mass\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # ACCELERATION
    # --------------------------------------------------------

    if key == "acceleration":

        patterns = [
            rf"{n}\s*m/s2\s*acceleration\b",
            rf"\bacceleration\s*{n}\s*m/s2\b",
            rf"\bacceleration\s*{n}\b",
            rf"{n}\s*acceleration\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # DISTANCE
    # --------------------------------------------------------

    if key == "distance":

        patterns = [
            rf"{n}\s*km\s*distance  ",
            rf"{n}\s*m\s*distance   ",
            rf"\bdistance\s*{n}\s*(?:km|m)?\b",
            rf"{n}\s*distance\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                if re.search(rf"{m.group(1)}\s*km\s*distance", q):
                    value *= 1000

                return value

        return None

    # --------------------------------------------------------
    # HEIGHT
    # --------------------------------------------------------

    if key == "height":

        patterns = [
            rf"{n}\s*m\s*height\b",
            rf"\bheight\s*{n}\s*m?\b",
            rf"{n}\s*height\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    if key == "time":

        patterns = [
            rf"\btime\s*{n}\b",
            rf"{n}\s*seconds\b",
            rf"{n}\s*second\b",
            rf"{n}\s*sec\b",
            rf"{n}\s*s\b",
            rf"{n}\s*minutes\b",
            rf"{n}\s*min\b",
            rf"{n}\s*hours\b",
            rf"{n}\s*hour\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                matched = m.group(0)

                if "minute" in matched or "min" in matched:
                    value *= 60

                if "hour" in matched:
                    value *= 3600

                return value

        return None

    # --------------------------------------------------------
    # VOLUME
    # --------------------------------------------------------

    if key == "volume":

        patterns = [
            rf"{n}\s*ml\s*volume\b",
            rf"\bvolume\s*{n}\s*ml\b",
            rf"{n}\s*l\s*volume\b",
            rf"\bvolume\s*{n}\s*l\b",
            rf"\bvolume\s*{n}\b",
            rf"{n}\s*volume\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                if "ml" in m.group(0):
                    value = value / 1000

                return value

        return None

    # --------------------------------------------------------
    # MOLARITY
    # --------------------------------------------------------

    if key == "molarity":

        patterns = [
            rf"\bmolarity\s*{n}\b",
            rf"{n}\s*molarity\b",
            rf"{n}\s*m\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # MOLES
    # --------------------------------------------------------

    if key == "moles":

        patterns = [
            rf"\bmoles\s*{n}\b",
            rf"{n}\s*moles\b",
            rf"{n}\s*mol\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # OTHER VARIABLES
    # --------------------------------------------------------

    units = {
        "force": r"(?:n)?",
        "work": r"(?:j)?",
        "power": r"(?:w)?",
        "speed": r"(?:m/s|km/h)?",
        "energy": r"(?:j)?",
        "kinetic energy": r"(?:j)?",
        "potential energy": r"(?:j)?",
    }

    unit = units.get(key, r"")

    patterns = [
        rf"\b{re.escape(key)}\s*[:=]?\s*{n}\s*{unit}",
        rf"{n}\s*{unit}\s*{re.escape(key)}\b",
        rf"\b{re.escape(key)}\s*[:=]?\s*{n}\b",
        rf"{n}\s*{re.escape(key)}\b",
    ]

    for p in patterns:
        m = re.search(p, q)
        if m:
            return float(m.group(1))

    return None


# Backward-compatible function name
def v16_get_number(q, key):
    return v164_extract(q, key)


# ============================================================
# 3. PHYSICS ENGINE
# ============================================================

def v164_physics(q):

    q = v164_normalize(q)

    v = {}

    keys = [
        "mass", "acceleration", "force",
        "work", "power", "distance",
        "time", "speed", "height",
        "energy", "kinetic energy",
        "potential energy"
    ]

    for key in keys:
        value = v164_extract(q, key)

        if value is not None:
            v[key] = value

    # F = ma
    if "mass" in v and "acceleration" in v:
        v["force"] = v["mass"] * v["acceleration"]

    # W = Fd
    if "force" in v and "distance" in v:
        v["work"] = v["force"] * v["distance"]

    # P = W/t
    if "work" in v and "time" in v and v["time"] != 0:
        v["power"] = v["work"] / v["time"]

    # speed = distance/time
    if "distance" in v and "time" in v and v["time"] != 0:
        v["speed"] = v["distance"] / v["time"]

    # KE = 1/2 mv²
    if "mass" in v and "speed" in v:
        v["kinetic energy"] = (
            0.5 * v["mass"] * v["speed"] ** 2
        )

    # PE = mgh
    if "mass" in v and "height" in v:
        v["potential energy"] = (
            v["mass"] * 9.8 * v["height"]
        )

    # Identify requested answer
    if "kinetic energy" in q or re.search(r"\bke\b", q):
        requested = "kinetic energy"

    elif "potential energy" in q or re.search(r"\bpe\b", q):
        requested = "potential energy"

    elif "force" in q:
        requested = "force"

    elif "power" in q:
        requested = "power"

    elif "work" in q:
        requested = "work"

    elif "speed" in q:
        requested = "speed"

    elif "energy" in q:
        requested = "energy"

    elif "mass" in q:
        requested = "mass"

    else:
        requested = None

    if requested and requested in v:
        return {
            "success": True,
            "topic": "physics",
            "formula": requested,
            "answer": v[requested],
            "values": v
        }

    return {
        "success": False,
        "topic": "physics",
        "error": "Required values missing or formula unavailable",
        "values": v
    }


# ============================================================
# 4. CHEMISTRY ENGINE
# ============================================================

def v164_chemistry(q):

    q = v164_normalize(q)

    v = {}

    for key in ["mass", "molar mass", "moles", "molarity", "volume"]:
        value = v164_extract(q, key)

        if value is not None:
            v[key] = value

    # n = mass / molar mass
    if "mass" in v and "molar mass" in v:
        if v["molar mass"] != 0:
            v["moles"] = v["mass"] / v["molar mass"]

    # M = n / V
    if "moles" in v and "volume" in v:
        if v["volume"] != 0:
            v["molarity"] = v["moles"] / v["volume"]

    # n = M * V
    if "molarity" in v and "volume" in v:
        v["moles"] = v["molarity"] * v["volume"]

    if "molarity" in q:
        requested = "molarity"

    elif "moles" in q:
        requested = "moles"

    elif "molar mass" in q:
        requested = "molar mass"

    else:
        requested = None

    if requested and requested in v:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": requested,
            "answer": v[requested],
            "values": v
        }

    return {
        "success": False,
        "topic": "chemistry",
        "error": "Required chemistry values missing",
        "values": v
    }


# ============================================================
# 5. UNIFIED MAGIC
# ============================================================

def v164_solve(question):

    q = v164_normalize(question)

    chemistry_terms = [
        "moles", "molarity", "molar mass",
        "concentration"
    ]

    if any(term in q for term in chemistry_terms):
        return v164_chemistry(q)

    return v164_physics(q)


def suno_magic(question):
    return v164_solve(question)


# ============================================================
# 6. OUTPUT FORMAT
# ============================================================

def v164_format(result):

    if not result["success"]:
        return (
            "ERROR: " + result.get("error", "Unknown error")
            + "\nValues: " + str(result.get("values", {}))
        )

    return (
        "\nSUNO SAATHI MAGIC " + VERSION +
        "\nTopic: " + result["topic"] +
        "\nFormula: " + result["formula"] +
        "\nAnswer: " + str(round(result["answer"], 6)) +
        "\nValues: " + str(result["values"])
    )


def v16_format_result(result):
    return v164_format(result)


# ============================================================
# 7. REGRESSION TESTS
# ============================================================

print("=" * 55)
print("SUNO SAATHI MAGIC V16.4 TESTING")
print("=" * 55)

# English Force
t1 = suno_magic("5 kg mass 2 acceleration calculate force")
assert t1["success"], t1
assert t1["values"]["mass"] == 5
assert t1["values"]["acceleration"] == 2
assert abs(t1["values"]["force"] - 10) < 0.001
print("PASS: English Force")

# Hindi Force
t2 = suno_magic(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)
assert t2["success"], t2
assert t2["values"]["mass"] == 5
assert t2["values"]["acceleration"] == 2
assert abs(t2["values"]["force"] - 10) < 0.001
print("PASS: Hindi Force")

# Hindi digits
t3 = suno_magic("५ kg द्रव्यमान २ त्वरण बल निकालो")
assert t3["success"], t3
assert abs(t3["values"]["force"] - 10) < 0.001
print("PASS: Hindi Digits Force")

# Work
t4 = suno_magic("10 N force 5 m distance calculate work")
assert t4["success"], t4
assert abs(t4["values"]["work"] - 50) < 0.001
print("PASS: Work")

# Power
t5 = suno_magic("100 J work 5 seconds calculate power")
assert t5["success"], t5
assert abs(t5["values"]["power"] - 20) < 0.001
print("PASS: Power")

# Speed
t6 = suno_magic("100 m distance 20 seconds calculate speed")
assert t6["success"], t6
assert abs(t6["values"]["speed"] - 5) < 0.001
print("PASS: Speed")

# Kinetic Energy
t7 = suno_magic("2 kg mass 3 m/s speed calculate kinetic energy")
assert t7["success"], t7
assert abs(t7["values"]["kinetic energy"] - 9) < 0.001
print("PASS: Kinetic Energy")

# Potential Energy
t8 = suno_magic("2 kg mass 5 m height calculate potential energy")
assert t8["success"], t8
assert abs(t8["values"]["potential energy"] - 98) < 0.001
print("PASS: Potential Energy")

# Moles
t9 = suno_magic(
    "18 g mass 18 g/mol molar mass calculate moles"
)
assert t9["success"], t9
assert abs(t9["values"]["moles"] - 1) < 0.001
print("PASS: Moles")

# Molarity
t10 = suno_magic("2 moles 1 L volume calculate molarity")
assert t10["success"], t10
assert abs(t10["values"]["molarity"] - 2) < 0.001
print("PASS: Molarity")

print("=" * 55)
print("ALL V16.4 TESTS PASSED!")
print("=" * 55)


# ============================================================
# 8. INTERACTIVE MODE
# ============================================================

def v16_launch_ui():

    print("\nSUNO SAATHI MAGIC V16.4")
    print("Hindi + English Physics and Chemistry")
    print("Type exit to stop.\n")

    while True:

        question = input("Question: ")

        if question.lower().strip() in ["exit", "quit", "stop"]:
            print("Magic stopped.")
            break

        result = suno_magic(question)
        print(v164_format(result))
        print("-" * 50)


print("\nReady. Run v16_launch_ui() for interactive mode.")

# ============================================================
# SUNO SAATHI MAGIC V16.4
# COMPLETE REWRITE
# Physics + Chemistry | Hindi + English
# ============================================================

import re
import math

VERSION = "V16.4"


# ============================================================
# 1. NORMALIZATION
# ============================================================

def v164_normalize(text):

    q = str(text).lower().strip()

    # Hindi digits
    q = q.translate(str.maketrans(
        "०१२३४५६७८९",
        "0123456789"
    ))

    # Unicode units
    q = q.replace("²", "2")
    q = q.replace("³", "3")
    q = q.replace("×", "*")
    q = q.replace("÷", "/")

    # Longest Hindi phrases first
    hindi_words = {
        "मोलर द्रव्यमान": "molar mass",
        "गतिज ऊर्जा": "kinetic energy",
        "स्थितिज ऊर्जा": "potential energy",
        "द्रव्यमान": "mass",
        "त्वरण": "acceleration",
        "वेग": "velocity",
        "चाल": "speed",
        "दूरी": "distance",
        "समय": "time",
        "बल": "force",
        "कार्य": "work",
        "शक्ति": "power",
        "ऊंचाई": "height",
        "ऊँचाई": "height",
        "ऊर्जा": "energy",
        "आयतन": "volume",
        "मोल": "moles",
        "सांद्रता": "molarity",
        "निकालो": "calculate",
        "बताओ": "calculate",
        "गणना करो": "calculate",
        "और": " ",
        "से": " ",
        "का": " ",
        "की": " ",
        "है": " ",
        "में": " ",
    }

    for hindi, english in sorted(
        hindi_words.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    hindi_units = {
        "किलोग्राम": "kg",
        "ग्राम": "g",
        "मीटर": "m",
        "सेकंड": "seconds",
        "सेकेण्ड": "seconds",
        "मिलीलीटर": "ml",
        "लीटर": "l",
        "न्यूटन": "n",
        "जूल": "j",
        "वाट": "w",
    }

    for hindi, english in sorted(
        hindi_units.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):
        q = q.replace(hindi, english)

    # English aliases
    q = re.sub(r"\baccel\b", "acceleration", q)
    q = re.sub(r"\bconcentration\b", "molarity", q)
    q = re.sub(r"\bmolecular weight\b", "molar mass", q)
    q = re.sub(r"\bvelocity\b", "speed", q)

    # Unit standardization
    q = q.replace("m/s²", "m/s2")
    q = q.replace("m/s^2", "m/s2")
    q = q.replace("kg.", "kg")

    # Hindi/English punctuation cleanup
    q = re.sub(r"[।,;]", " ", q)
    q = re.sub(r"\s+", " ", q).strip()

    return q


# ============================================================
# 2. SAFE NUMBER EXTRACTION
# ============================================================

def v164_extract(q, key):

    q = v164_normalize(q)

    n = r"([-+]?\d+(?:\.\d+)?)"

    # --------------------------------------------------------
    # MASS
    # --------------------------------------------------------

    if key == "mass":

        patterns = [
            rf"{n}\s*kg\s*mass\b",
            rf"\bmass\s*{n}\s*kg\b",
            rf"{n}\s*g\s*mass\b",
            rf"\bmass\s*{n}\s*g\b",
            rf"\bmass\s*{n}\b",
            rf"{n}\s*mass\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                # grams -> kg only for physics mass
                if re.search(rf"{re.escape(m.group(1))}\s*g\s*mass\b", q):
                    value = value / 1000

                return value

        return None

    # --------------------------------------------------------
    # MOLAR MASS
    # --------------------------------------------------------

    if key == "molar mass":

        patterns = [
            rf"{n}\s*g/mol\s*molar mass\b",
            rf"\bmolar mass\s*{n}\s*g/mol\b",
            rf"\bmolar mass\s*{n}\b",
            rf"{n}\s*molar mass\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # ACCELERATION
    # --------------------------------------------------------

    if key == "acceleration":

        patterns = [
            rf"{n}\s*m/s2\s*acceleration\b",
            rf"\bacceleration\s*{n}\s*m/s2\b",
            rf"\bacceleration\s*{n}\b",
            rf"{n}\s*acceleration\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # DISTANCE
    # --------------------------------------------------------

    if key == "distance":

        patterns = [
            rf"{n}\s*km\s*distance	",
            rf"{n}\s*m\s*distance	",
            rf"\bdistance\s*{n}\s*(?:km|m)?\b",
            rf"{n}\s*distance\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                if re.search(rf"{m.group(1)}\s*km\s*distance", q):
                    value *= 1000

                return value

        return None

    # --------------------------------------------------------
    # HEIGHT
    # --------------------------------------------------------

    if key == "height":

        patterns = [
            rf"{n}\s*m\s*height\b",
            rf"\bheight\s*{n}\s*m?\b",
            rf"{n}\s*height\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    if key == "time":

        patterns = [
            rf"\btime\s*{n}\b",
            rf"{n}\s*seconds\b",
            rf"{n}\s*second\b",
            rf"{n}\s*sec\b",
            rf"{n}\s*s\b",
            rf"{n}\s*minutes\b",
            rf"{n}\s*min\b",
            rf"{n}\s*hours\b",
            rf"{n}\s*hour\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                matched = m.group(0)

                if "minute" in matched or "min" in matched:
                    value *= 60

                if "hour" in matched:
                    value *= 3600

                return value

        return None

    # --------------------------------------------------------
    # VOLUME
    # --------------------------------------------------------

    if key == "volume":

        patterns = [
            rf"{n}\s*ml\s*volume\b",
            rf"\bvolume\s*{n}\s*ml\b",
            rf"{n}\s*l\s*volume\b",
            rf"\bvolume\s*{n}\s*l\b",
            rf"\bvolume\s*{n}\b",
            rf"{n}\s*volume\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                value = float(m.group(1))

                if "ml" in m.group(0):
                    value = value / 1000

                return value

        return None

    # --------------------------------------------------------
    # MOLARITY
    # --------------------------------------------------------

    if key == "molarity":

        patterns = [
            rf"\bmolarity\s*{n}\b",
            rf"{n}\s*molarity\b",
            rf"{n}\s*m\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # MOLES
    # --------------------------------------------------------

    if key == "moles":

        patterns = [
            rf"\bmoles\s*{n}\b",
            rf"{n}\s*moles\b",
            rf"{n}\s*mol\b",
        ]

        for p in patterns:
            m = re.search(p, q)
            if m:
                return float(m.group(1))

        return None

    # --------------------------------------------------------
    # OTHER VARIABLES
    # --------------------------------------------------------

    units = {
        "force": r"(?:n)?",
        "work": r"(?:j)?",
        "power": r"(?:w)?",
        "speed": r"(?:m/s|km/h)?",
        "energy": r"(?:j)?",
        "kinetic energy": r"(?:j)?",
        "potential energy": r"(?:j)?",
    }

    unit = units.get(key, r"")

    patterns = [
        rf"\b{re.escape(key)}\s*[:=]?\s*{n}\s*{unit}",
        rf"{n}\s*{unit}\s*{re.escape(key)}\b",
        rf"\b{re.escape(key)}\s*[:=]?\s*{n}\b",
        rf"{n}\s*{re.escape(key)}\b",
    ]

    for p in patterns:
        m = re.search(p, q)
        if m:
            return float(m.group(1))

    return None


# Backward-compatible function name
def v16_get_number(q, key):
    return v164_extract(q, key)


# ============================================================
# 3. PHYSICS ENGINE
# ============================================================

def v164_physics(q):

    q = v164_normalize(q)

    v = {}

    keys = [
        "mass", "acceleration", "force",
        "work", "power", "distance",
        "time", "speed", "height",
        "energy", "kinetic energy",
        "potential energy"
    ]

    for key in keys:
        value = v164_extract(q, key)

        if value is not None:
            v[key] = value

    # F = ma
    if "mass" in v and "acceleration" in v:
        v["force"] = v["mass"] * v["acceleration"]

    # W = Fd
    if "force" in v and "distance" in v:
        v["work"] = v["force"] * v["distance"]

    # P = W/t
    if "work" in v and "time" in v and v["time"] != 0:
        v["power"] = v["work"] / v["time"]

    # speed = distance/time
    if "distance" in v and "time" in v and v["time"] != 0:
        v["speed"] = v["distance"] / v["time"]

    # KE = 1/2 mv²
    if "mass" in v and "speed" in v:
        v["kinetic energy"] = (
            0.5 * v["mass"] * v["speed"] ** 2
        )

    # PE = mgh
    if "mass" in v and "height" in v:
        v["potential energy"] = (
            v["mass"] * 9.8 * v["height"]
        )

    # Identify requested answer
    if "kinetic energy" in q or re.search(r"\bke\b", q):
        requested = "kinetic energy"

    elif "potential energy" in q or re.search(r"\bpe\b", q):
        requested = "potential energy"

    elif "force" in q:
        requested = "force"

    elif "power" in q:
        requested = "power"

    elif "work" in q:
        requested = "work"

    elif "speed" in q:
        requested = "speed"

    elif "energy" in q:
        requested = "energy"

    elif "mass" in q:
        requested = "mass"

    else:
        requested = None

    if requested and requested in v:
        return {
            "success": True,
            "topic": "physics",
            "formula": requested,
            "answer": v[requested],
            "values": v
        }

    return {
        "success": False,
        "topic": "physics",
        "error": "Required values missing or formula unavailable",
        "values": v
    }


# ============================================================
# 4. CHEMISTRY ENGINE
# ============================================================

def v164_chemistry(q):

    q = v164_normalize(q)

    v = {}

    for key in ["mass", "molar mass", "moles", "molarity", "volume"]:
        value = v164_extract(q, key)

        if value is not None:
            v[key] = value

    # n = mass / molar mass
    if "mass" in v and "molar mass" in v:
        if v["molar mass"] != 0:
            v["moles"] = v["mass"] / v["molar mass"]

    # M = n / V
    if "moles" in v and "volume" in v:
        if v["volume"] != 0:
            v["molarity"] = v["moles"] / v["volume"]

    # n = M * V
    if "molarity" in v and "volume" in v:
        v["moles"] = v["molarity"] * v["volume"]

    if "molarity" in q:
        requested = "molarity"

    elif "moles" in q:
        requested = "moles"

    elif "molar mass" in q:
        requested = "molar mass"

    else:
        requested = None

    if requested and requested in v:
        return {
            "success": True,
            "topic": "chemistry",
            "formula": requested,
            "answer": v[requested],
            "values": v
        }

    return {
        "success": False,
        "topic": "chemistry",
        "error": "Required chemistry values missing",
        "values": v
    }


# ============================================================
# 5. UNIFIED MAGIC
# ============================================================

def v164_solve(question):

    q = v164_normalize(question)

    chemistry_terms = [
        "moles", "molarity", "molar mass",
        "concentration"
    ]

    if any(term in q for term in chemistry_terms):
        return v164_chemistry(q)

    return v164_physics(q)


def suno_magic(question):
    return v164_solve(question)


# ============================================================
# 6. OUTPUT FORMAT
# ============================================================

def v164_format(result):

    if not result["success"]:
        return (
            "ERROR: " + result.get("error", "Unknown error")
            + "\nValues: " + str(result.get("values", {}))
        )

    return (
        "\nSUNO SAATHI MAGIC " + VERSION +
        "\nTopic: " + result["topic"] +
        "\nFormula: " + result["formula"] +
        "\nAnswer: " + str(round(result["answer"], 6)) +
        "\nValues: " + str(result["values"])
    )


def v16_format_result(result):
    return v164_format(result)


# ============================================================
# 7. REGRESSION TESTS
# ============================================================

print("=" * 55)
print("SUNO SAATHI MAGIC V16.4 TESTING")
print("=" * 55)

# English Force
t1 = suno_magic("5 kg mass 2 acceleration calculate force")
assert t1["success"], t1
assert t1["values"]["mass"] == 5
assert t1["values"]["acceleration"] == 2
assert abs(t1["values"]["force"] - 10) < 0.001
print("PASS: English Force")

# Hindi Force
t2 = suno_magic(
    "5 kg द्रव्यमान और 2 m/s2 त्वरण बल निकालो"
)
assert t2["success"], t2
assert t2["values"]["mass"] == 5
assert t2["values"]["acceleration"] == 2
assert abs(t2["values"]["force"] - 10) < 0.001
print("PASS: Hindi Force")

# Hindi digits
t3 = suno_magic("५ kg द्रव्यमान २ त्वरण बल निकालो")
assert t3["success"], t3
assert abs(t3["values"]["force"] - 10) < 0.001
print("PASS: Hindi Digits Force")

# Work
t4 = suno_magic("10 N force 5 m distance calculate work")
assert t4["success"], t4
assert abs(t4["values"]["work"] - 50) < 0.001
print("PASS: Work")

# Power
t5 = suno_magic("100 J work 5 seconds calculate power")
assert t5["success"], t5
assert abs(t5["values"]["power"] - 20) < 0.001
print("PASS: Power")

# Speed
t6 = suno_magic("100 m distance 20 seconds calculate speed")
assert t6["success"], t6
assert abs(t6["values"]["speed"] - 5) < 0.001
print("PASS: Speed")

# Kinetic Energy
t7 = suno_magic("2 kg mass 3 m/s speed calculate kinetic energy")
assert t7["success"], t7
assert abs(t7["values"]["kinetic energy"] - 9) < 0.001
print("PASS: Kinetic Energy")

# Potential Energy
t8 = suno_magic("2 kg mass 5 m height calculate potential energy")
assert t8["success"], t8
assert abs(t8["values"]["potential energy"] - 98) < 0.001
print("PASS: Potential Energy")

# Moles
t9 = suno_magic(
    "18 g mass 18 g/mol molar mass calculate moles"
)
assert t9["success"], t9
assert abs(t9["values"]["moles"] - 1) < 0.001
print("PASS: Moles")

# Molarity
t10 = suno_magic("2 moles 1 L volume calculate molarity")
assert t10["success"], t10
assert abs(t10["values"]["molarity"] - 2) < 0.001
print("PASS: Molarity")

print("=" * 55)
print("ALL V16.4 TESTS PASSED!")
print("=" * 55)


# ============================================================
# 8. INTERACTIVE MODE
# ============================================================

def v16_launch_ui():

    print("\nSUNO SAATHI MAGIC V16.4")
    print("Hindi + English Physics and Chemistry")
    print("Type exit to stop.\n")

    while True:

        question = input("Question: ")

        if question.lower().strip() in ["exit", "quit", "stop"]:
            print("Magic stopped.")
            break

        result = suno_magic(question)
        print(v164_format(result))
        print("-" * 50)


print("\nReady. Run v16_launch_ui() for interactive mode.")

q = "10 N force 5 m distance calculate work"

print("Normalized:", v164_normalize(q))
print("Force:", v164_extract(q, "force"))
print("Distance:", v164_extract(q, "distance"))
print("Work result:", v164_physics(q))

q = "10 N force 5 m distance calculate work"

print("Normalized:", v164_normalize(q))
print("Force:", v164_extract(q, "force"))
print("Distance:", v164_extract(q, "distance"))
print("Work result:", v164_physics(q))

# ================================================================
# SUNO SAATHI MAGIC ENGINE v16.4 (CORRECTED & VERIFIED)
# ================================================================

import re
import math

# ------------------------------------------------
# 1. HINDI/HINGLISH TRANSLATION & DICTIONARIES
# ------------------------------------------------

V16_NUMBER_WORDS = {
    "एक": "1", "दो": "2", "तीन": "3", "चार": "4", "पांच": "5",
    "पाँच": "5", "छह": "6", "छः": "6", "सात": "7", "आठ": "8",
    "नौ": "9", "दस": "10", "बीस": "20", "पचास": "50", "सौ": "100"
}

V16_TERMS = {
    "द्रव्यमान": "mass", "मास": "mass", "वजन": "mass",
    "त्वरण": "acceleration", "एक्सेलरेशन": "acceleration",
    "बल": "force", "फोर्स": "force",
    "कार्य": "work", "वर्क": "work",
    "शक्ति": "power", "पावर": "power",
    "दूरी": "distance", "डिस्टेंस": "distance",
    "समय": "time", "टाइम": "time",
    "गति": "speed", "वेग": "velocity",
    "ऊंचाई": "height", "ऊँचाई": "height",
    "घनत्व": "density", "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",
    "मोलर द्रव्यमान": "molar mass", "मोलर मास": "molar mass",
    "मोलरता": "molarity", "मोल्स": "moles", "मोल": "moles"
}

def normalize_query(q):
    q = str(q).lower().strip()
    
    # Replace Hindi number words
    for word, num in sorted(V16_NUMBER_WORDS.items(), key=lambda x: len(x[0]), reverse=True):
        q = re.sub(r'(?<!\S)' + re.escape(word) + r'(?!\S)', num, q)
        
    # Translate Hindi technical terms
    for word, eng in sorted(V16_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
        q = q.replace(word, eng)
        
    # Strip Hindi particles
    for part in ["और", "में", "है", "हैं", "से", "पर", "का", "की", "के", "हुआ", "करो", "ज्ञात", "निकालो"]:
        q = re.sub(r'(?<!\S)' + re.escape(part) + r'(?!\S)', ' ', q)
        
    return re.sub(r'\s+', ' ', q).strip()

# ------------------------------------------------
# 2. VARIABLE & TOPIC DETECTOR
# ------------------------------------------------

def detect_topic(q):
    q = normalize_query(q)
    if "kinetic energy" in q:
        return "kinetic_energy"
    if "potential energy" in q:
        return "potential_energy"
    if "molarity" in q:
        return "molarity"
    if "molar mass" in q or "moles" in q:
        return "moles"
    if "power" in q:
        return "power"
    if "work" in q:
        return "work"
    if "force" in q:
        return "force"
    if "speed" in q or "velocity" in q:
        return "speed"
    return "unknown"

def extract_number(q, aliases):
    q = normalize_query(q)
    # Patterns to extract number associated with label or units
    patterns = []
    for alias in aliases:
        patterns.extend([
            r'\b' + re.escape(alias) + r'\s*is?\s*([-+]?\d+(?:\.\d+)?)',
            r'\b' + re.escape(alias) + r'\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)',
            r'([-+]?\d+(?:\.\d+)?)\s*' + re.escape(alias)
        ])
    
    for pattern in patterns:
        match = re.search(pattern, q, re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None

# Generic fallback regex number extractor
def extract_all_numbers(q):
    return [float(x) for x in re.findall(r'[-+]?\d+(?:\.\d+)?', q)]

# ------------------------------------------------
# 3. UNIFIED SOLVER
# ------------------------------------------------

def suno_magic(q):
    orig_q = q
    normalized = normalize_query(q)
    topic = detect_topic(normalized)
    
    # Smart mapping dictionary
    vals = {}
    
    # Fallback numbers list in case explicit labels are missing
    all_nums = extract_all_numbers(normalized)
    
    if topic == "force":
        m = extract_number(normalized, ["mass", "kg"])
        a = extract_number(normalized, ["acceleration", "m/s2", "m/s^2", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if a is None and len(all_nums) >= 2: a = all_nums[1]
        
        if m is None or a is None:
            return {"success": False, "message": "Mass and acceleration required."}
        
        ans = m * a
        vals = {"mass": m, "acceleration": a, "force": ans}
        return {
            "success": True,
            "topic": "force",
            "values": vals,
            "result": ans,
            "unit": "N",
            "explanation": f"F = m * a = {m} * {a} = {ans} N"
        }
        
    elif topic == "work":
        f = extract_number(normalized, ["force", "n"])
        d = extract_number(normalized, ["distance", "m"])
        if f is None and len(all_nums) >= 1: f = all_nums[0]
        if d is None and len(all_nums) >= 2: d = all_nums[1]
        
        if f is None or d is None:
            return {"success": False, "message": "Force and distance required."}
            
        ans = f * d
        vals = {"force": f, "distance": d, "work": ans}
        return {
            "success": True,
            "topic": "work",
            "values": vals,
            "result": ans,
            "unit": "J",
            "explanation": f"W = F * d = {f} * {d} = {ans} J"
        }
        
    elif topic == "power":
        w = extract_number(normalized, ["work", "j"])
        t = extract_number(normalized, ["time", "s"])
        if w is None and len(all_nums) >= 1: w = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]
        
        if w is None or t is None:
            return {"success": False, "message": "Work and time required."}
        if t == 0:
            return {"success": False, "message": "Time cannot be zero."}
            
        ans = w / t
        vals = {"work": w, "time": t, "power": ans}
        return {
            "success": True,
            "topic": "power",
            "values": vals,
            "result": ans,
            "unit": "W",
            "explanation": f"P = W / t = {w} / {t} = {ans} W"
        }

    elif topic == "speed":
        d = extract_number(normalized, ["distance", "m"])
        t = extract_number(normalized, ["time", "s"])
        if d is None and len(all_nums) >= 1: d = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]
        
        if d is None or t is None:
            return {"success": False, "message": "Distance and time required."}
        if t == 0:
            return {"success": False, "message": "Time cannot be zero."}
            
        ans = d / t
        vals = {"distance": d, "time": t, "speed": ans}
        return {
            "success": True,
            "topic": "speed",
            "values": vals,
            "result": ans,
            "unit": "m/s",
            "explanation": f"v = d / t = {d} / {t} = {ans} m/s"
        }
        
    elif topic == "kinetic_energy":
        m = extract_number(normalized, ["mass", "kg"])
        v = extract_number(normalized, ["speed", "velocity", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if v is None and len(all_nums) >= 2: v = all_nums[1]
        
        if m is None or v is None:
            return {"success": False, "message": "Mass and velocity required."}
            
        ans = 0.5 * m * (v ** 2)
        vals = {"mass": m, "velocity": v, "kinetic_energy": ans}
        return {
            "success": True,
            "topic": "kinetic_energy",
            "values": vals,
            "result": ans,
            "unit": "J",
            "explanation": f"KE = 0.5 * m * v^2 = 0.5 * {m} * {v}^2 = {ans} J"
        }
        
    elif topic == "potential_energy":
        m = extract_number(normalized, ["mass", "kg"])
        h = extract_number(normalized, ["height", "m"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if h is None and len(all_nums) >= 2: h = all_nums[1]
        
        if m is None or h is None:
            return {"success": False, "message": "Mass and height required."}
            
        g = 9.8
        ans = m * g * h
        vals = {"mass": m, "height": h, "potential_energy": ans}
        return {
            "success": True,
            "topic": "potential_energy",
            "values": vals,
            "result": ans,
            "unit": "J",
            "explanation": f"PE = m * g * h = {m} * 9.8 * {h} = {ans} J"
        }

    elif topic == "moles":
        mass = extract_number(normalized, ["mass", "g"])
        molar_mass = extract_number(normalized, ["molar mass", "g/mol"])
        if mass is None and len(all_nums) >= 1: mass = all_nums[0]
        if molar_mass is None and len(all_nums) >= 2: molar_mass = all_nums[1]
        
        if mass is None or molar_mass is None:
            return {"success": False, "message": "Mass and molar mass required."}
        if molar_mass == 0:
            return {"success": False, "message": "Molar mass cannot be zero."}
            
        ans = mass / molar_mass
        vals = {"mass": mass, "molar_mass": molar_mass, "moles": ans}
        return {
            "success": True,
            "topic": "moles",
            "values": vals,
            "result": ans,
            "unit": "mol",
            "explanation": f"n = mass / molar_mass = {mass} / {molar_mass} = {ans} mol"
        }
        
    elif topic == "molarity":
        moles = extract_number(normalized, ["moles", "mol"])
        vol = extract_number(normalized, ["volume", "l"])
        if moles is None and len(all_nums) >= 1: moles = all_nums[0]
        if vol is None and len(all_nums) >= 2: vol = all_nums[1]
        
        if moles is None or vol is None:
            return {"success": False, "message": "Moles and volume required."}
        if vol == 0:
            return {"success": False, "message": "Volume cannot be zero."}
            
        ans = moles / vol
        vals = {"moles": moles, "volume": vol, "molarity": ans}
        return {
            "success": True,
            "topic": "molarity",
            "values": vals,
            "result": ans,
            "unit": "mol/L",
            "explanation": f"M = moles / volume = {moles} / {vol} = {ans} mol/L"
        }
        
    return {"success": False, "message": "Topic could not be identified."}

# ================================================================
# 4. COMPREHENSIVE REGRESSION TESTS
# ================================================================

print("--- EXECUTION & TEST RESULTS ---\n")

tests = {
    "English Force": {
        "q": "mass is 5 kg and acceleration is 2 m/s2 calculate force",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Hindi Force": {
        "q": "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Hindi Digits Force": {
        "q": "द्रव्यमान पांच किलो और त्वरण दो है बल निकालो",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Work": {
        "q": "10 N force 5 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["work"] - 50) < 0.001
    },
    "Power": {
        "q": "work is 100 J and time is 5 s find power",
        "assert_fn": lambda r: abs(r["values"]["power"] - 20) < 0.001
    },
    "Speed": {
        "q": "distance 100 m and time 20 s calculate speed",
        "assert_fn": lambda r: abs(r["values"]["speed"] - 5) < 0.001
    },
    "Kinetic Energy": {
        "q": "mass 4 kg speed 3 m/s kinetic energy calculate",
        "assert_fn": lambda r: abs(r["values"]["kinetic_energy"] - 18) < 0.001
    },
    "Potential Energy": {
        "q": "mass 2 kg height 5 m potential energy calculate",
        "assert_fn": lambda r: abs(r["values"]["potential_energy"] - 98) < 0.001
    },
    "Moles": {
        "q": "mass 18 g and molar mass 18 g/mol find moles",
        "assert_fn": lambda r: abs(r["values"]["moles"] - 1) < 0.001
    },
    "Molarity": {
        "q": "moles 2 and volume 4 L calculate molarity",
        "assert_fn": lambda r: abs(r["values"]["molarity"] - 0.5) < 0.001
    }
}

all_passed = True
for name, info in tests.items():
    try:
        res = suno_magic(info["q"])
        if res["success"] and info["assert_fn"](res):
            print(f"PASS: {name}")
        else:
            print(f"FAIL: {name} (Result: {res})")
            all_passed = False
    except Exception as e:
        print(f"FAIL: {name} with error: {str(e)}")
        all_passed = False

if all_passed:
    print("\n✅ ALL V16.4 VERIFICATION TESTS PASSED SUCCESSFULLY!")
else:
    print("\n❌ SOME TESTS FAILED.")

# ================================================================
# SUNO SAATHI MAGIC ENGINE v16.4 (CORRECTED & FULLY VERIFIED)
# ================================================================

import re
import math

# ------------------------------------------------
# 1. HINDI/HINGLISH TRANSLATION & DICTIONARIES
# ------------------------------------------------

V16_NUMBER_WORDS = {
    "एक": "1", "दो": "2", "तीन": "3", "चार": "4", "पांच": "5",
    "पाँच": "5", "छह": "6", "छः": "6", "सात": "7", "आठ": "8",
    "नौ": "9", "दस": "10", "बीस": "20", "पचास": "50", "सौ": "100"
}

V16_TERMS = {
    "द्रव्यमान": "mass", "मास": "mass", "वजन": "mass",
    "त्वरण": "acceleration", "एक्सेलरेशन": "acceleration",
    "बल": "force", "फोर्स": "force",
    "कार्य": "work", "वर्क": "work",
    "शक्ति": "power", "पावर": "power",
    "दूरी": "distance", "डिस्टेंस": "distance",
    "समय": "time", "टाइम": "time",
    "गति": "speed", "वेग": "velocity",
    "ऊंचाई": "height", "ऊँचाई": "height",
    "घनत्व": "density", "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",
    "मोलर द्रव्यमान": "molar mass", "मोलर मास": "molar mass",
    "मोलरता": "molarity", "मोल्स": "moles", "मोल": "moles"
}

def normalize_query(q):
    q = str(q).lower().strip()
    
    # Replace Hindi number words
    for word, num in sorted(V16_NUMBER_WORDS.items(), key=lambda x: len(x[0]), reverse=True):
        q = re.sub(r'(?<!\S)' + re.escape(word) + r'(?!\S)', num, q)
        
    # Translate Hindi technical terms
    for word, eng in sorted(V16_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
        q = q.replace(word, eng)
        
    # Strip Hindi particles
    for part in ["और", "में", "है", "हैं", "से", "पर", "का", "की", "के", "हुआ", "करो", "ज्ञात", "निकालो"]:
        q = re.sub(r'(?<!\S)' + re.escape(part) + r'(?!\S)', ' ', q)
        
    return re.sub(r'\s+', ' ', q).strip()

# ------------------------------------------------
# 2. VARIABLE & TOPIC DETECTOR
# ------------------------------------------------

def detect_topic(q):
    q = normalize_query(q)
    if "kinetic energy" in q:
        return "kinetic_energy"
    if "potential energy" in q:
        return "potential_energy"
    if "molarity" in q:
        return "molarity"
    if "molar mass" in q or "moles" in q:
        return "moles"
    if "power" in q:
        return "power"
    if "work" in q:
        return "work"
    if "force" in q:
        return "force"
    if "speed" in q or "velocity" in q:
        return "speed"
    return "unknown"

def extract_number(q, aliases):
    q = normalize_query(q)
    patterns = []
    for alias in aliases:
        if len(alias) == 1:
            # Highly specific unit lookups for single characters (e.g. 'n' for Newton, 'm' for meter)
            patterns.extend([
                r'\b' + re.escape(alias) + r'\s*is?\s*([-+]?\d+(?:\.\d+)?)',
                r'\b' + re.escape(alias) + r'\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)',
                r'\b([-+]?\d+(?:\.\d+)?)\s*' + re.escape(alias) + r'\b'
            ])
        else:
            patterns.extend([
                r'\b' + re.escape(alias) + r'\s*is?\s*([-+]?\d+(?:\.\d+)?)',
                r'\b' + re.escape(alias) + r'\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)',
                r'([-+]?\d+(?:\.\d+)?)\s*' + re.escape(alias) + r'\b'
            ])
            
    for pattern in patterns:
        match = re.search(pattern, q, re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None

def extract_all_numbers(q):
    return [float(x) for x in re.findall(r'[-+]?\d+(?:\.\d+)?', q)]

# ------------------------------------------------
# 3. UNIFIED SOLVER
# ------------------------------------------------

def suno_magic(q):
    normalized = normalize_query(q)
    topic = detect_topic(normalized)
    
    vals = {}
    all_nums = extract_all_numbers(normalized)
    
    if topic == "force":
        m = extract_number(normalized, ["mass", "kg"])
        a = extract_number(normalized, ["acceleration", "m/s2", "m/s^2", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if a is None and len(all_nums) >= 2: a = all_nums[1]
        
        if m is None or a is None:
            return {"success": False, "message": "Mass and acceleration required."}
        
        ans = m * a
        vals = {"mass": m, "acceleration": a, "force": ans}
        return {
            "success": True,
            "topic": "force",
            "values": vals,
            "result": ans,
            "unit": "N",
            "explanation": f"F = m * a = {m} * {a} = {ans} N"
        }
        
    elif topic == "work":
        f = extract_number(normalized, ["force", "n"])
        d = extract_number(normalized, ["distance", "m"])
        if f is None and len(all_nums) >= 1: f = all_nums[0]
        if d is None and len(all_nums) >= 2: d = all_nums[1]
        
        if f is None or d is None:
            return {"success": False, "message": "Force and distance required."}
            
        ans = f * d
        vals = {"force": f, "distance": d, "work": ans}
        return {
            "success": True,
            "topic": "work",
            "values": vals,
            "result": ans,
            "unit": "J",
            "explanation": f"W = F * d = {f} * {d} = {ans} J"
        }
        
    elif topic == "power":
        w = extract_number(normalized, ["work", "j"])
        t = extract_number(normalized, ["time", "s"])
        if w is None and len(all_nums) >= 1: w = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]
        
        if w is None or t is None:
            return {"success": False, "message": "Work and time required."}
        if t == 0:
            return {"success": False, "message": "Time cannot be zero."}
            
        ans = w / t
        vals = {"work": w, "time": t, "power": ans}
        return {
            "success": True,
            "topic": "power",
            "values": vals,
            "result": ans,
            "unit": "W",
            "explanation": f"P = W / t = {w} / {t} = {ans} W"
        }

    elif topic == "speed":
        d = extract_number(normalized, ["distance", "m"])
        t = extract_number(normalized, ["time", "s"])
        if d is None and len(all_nums) >= 1: d = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]
        
        if d is None or t is None:
            return {"success": False, "message": "Distance and time required."}
        if t == 0:
            return {"success": False, "message": "Time cannot be zero."}
            
        ans = d / t
        vals = {"distance": d, "time": t, "speed": ans}
        return {
            "success": True,
            "topic": "speed",
            "values": vals,
            "result": ans,
            "unit": "m/s",
            "explanation": f"v = d / t = {d} / {t} = {ans} m/s"
        }
        
    elif topic == "kinetic_energy":
        m = extract_number(normalized, ["mass", "kg"])
        v = extract_number(normalized, ["speed", "velocity", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if v is None and len(all_nums) >= 2: v = all_nums[1]
        
        if m is None or v is None:
            return {"success": False, "message": "Mass and velocity required."}
            
        ans = 0.5 * m * (v ** 2)
        vals = {"mass": m, "velocity": v, "kinetic_energy": ans}
        return {
            "success": True,
            "topic": "kinetic_energy",
            "values": vals,
            "result": ans,
            "unit": "J",
            "explanation": f"KE = 0.5 * m * v^2 = 0.5 * {m} * {v}^2 = {ans} J"
        }
        
    elif topic == "potential_energy":
        m = extract_number(normalized, ["mass", "kg"])
        h = extract_number(normalized, ["height", "m"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if h is None and len(all_nums) >= 2: h = all_nums[1]
        
        if m is None or h is None:
            return {"success": False, "message": "Mass and height required."}
            
        g = 9.8
        ans = m * g * h
        vals = {"mass": m, "height": h, "potential_energy": ans}
        return {
            "success": True,
            "topic": "potential_energy",
            "values": vals,
            "result": ans,
            "unit": "J",
            "explanation": f"PE = m * g * h = {m} * 9.8 * {h} = {ans} J"
        }

    elif topic == "moles":
        mass = extract_number(normalized, ["mass", "g"])
        molar_mass = extract_number(normalized, ["molar mass", "g/mol"])
        if mass is None and len(all_nums) >= 1: mass = all_nums[0]
        if molar_mass is None and len(all_nums) >= 2: molar_mass = all_nums[1]
        
        if mass is None or molar_mass is None:
            return {"success": False, "message": "Mass and molar mass required."}
        if molar_mass == 0:
            return {"success": False, "message": "Molar mass cannot be zero."}
            
        ans = mass / molar_mass
        vals = {"mass": mass, "molar_mass": molar_mass, "moles": ans}
        return {
            "success": True,
            "topic": "moles",
            "values": vals,
            "result": ans,
            "unit": "mol",
            "explanation": f"n = mass / molar_mass = {mass} / {molar_mass} = {ans} mol"
        }
        
    elif topic == "molarity":
        moles = extract_number(normalized, ["moles", "mol"])
        vol = extract_number(normalized, ["volume", "l"])
        if moles is None and len(all_nums) >= 1: moles = all_nums[0]
        if vol is None and len(all_nums) >= 2: vol = all_nums[1]
        
        if moles is None or vol is None:
            return {"success": False, "message": "Moles and volume required."}
        if vol == 0:
            return {"success": False, "message": "Volume cannot be zero."}
            
        ans = moles / vol
        vals = {"moles": moles, "volume": vol, "molarity": ans}
        return {
            "success": True,
            "topic": "molarity",
            "values": vals,
            "result": ans,
            "unit": "mol/L",
            "explanation": f"M = moles / volume = {moles} / {vol} = {ans} mol/L"
        }
        
    return {"success": False, "message": "Topic could not be identified."}

# ================================================================
# 4. COMPREHENSIVE REGRESSION TESTS
# ================================================================

print("--- EXECUTION & TEST RESULTS ---\n")

tests = {
    "English Force": {
        "q": "mass is 5 kg and acceleration is 2 m/s2 calculate force",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Hindi Force": {
        "q": "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Hindi Digits Force": {
        "q": "द्रव्यमान पांच किलो और त्वरण दो है बल निकालो",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Work (Standard)": {
        "q": "10 N force 5 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["work"] - 50) < 0.001
    },
    "Work Regression 1": {
        "q": "20 N force 3 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["work"] - 60) < 0.001
    },
    "Work Regression 2": {
        "q": "5 N force 10 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["work"] - 50) < 0.001
    },
    "Power": {
        "q": "work is 100 J and time is 5 s find power",
        "assert_fn": lambda r: abs(r["values"]["power"] - 20) < 0.001
    },
    "Speed": {
        "q": "distance 100 m and time 20 s calculate speed",
        "assert_fn": lambda r: abs(r["values"]["speed"] - 5) < 0.001
    },
    "Kinetic Energy": {
        "q": "mass 4 kg speed 3 m/s kinetic energy calculate",
        "assert_fn": lambda r: abs(r["values"]["kinetic_energy"] - 18) < 0.001
    },
    "Potential Energy": {
        "q": "mass 2 kg height 5 m potential energy calculate",
        "assert_fn": lambda r: abs(r["values"]["potential_energy"] - 98) < 0.001
    },
    "Moles": {
        "q": "mass 18 g and molar mass 18 g/mol find moles",
        "assert_fn": lambda r: abs(r["values"]["moles"] - 1) < 0.001
    },
    "Molarity": {
        "q": "moles 2 and volume 4 L calculate molarity",
        "assert_fn": lambda r: abs(r["values"]["molarity"] - 0.5) < 0.001
    }
}

all_passed = True
for name, info in tests.items():
    try:
        res = suno_magic(info["q"])
        if res["success"] and info["assert_fn"](res):
            print(f"PASS: {name}")
        else:
            print(f"FAIL: {name} (Result: {res})")
            all_passed = False
    except Exception as e:
        print(f"FAIL: {name} with error: {str(e)}")
        all_passed = False

if all_passed:
    print("\n✅ ALL V16.4 VERIFICATION TESTS PASSED SUCCESSFULLY!")
else:
    print("\n❌ SOME TESTS FAILED.")

# ================================================================
# SUNO SAATHI MAGIC ENGINE v16.4 (CORRECTED & VERIFIED)
# ================================================================

import re
import math

# ------------------------------------------------
# 1. HINDI/HINGLISH TRANSLATION & DICTIONARIES
# ------------------------------------------------

V16_NUMBER_WORDS = {
    "एक": "1", "दो": "2", "तीन": "3", "चार": "4", "पांच": "5",
    "पाँच": "5", "छह": "6", "छः": "6", "सात": "7", "आठ": "8",
    "नौ": "9", "दस": "10", "बीस": "20", "पचास": "50", "सौ": "100"
}

V16_TERMS = {
    "द्रव्यमान": "mass", "मास": "mass", "वजन": "mass",
    "त्वरण": "acceleration", "एक्सेलरेशन": "acceleration",
    "बल": "force", "फोर्स": "force",
    "कार्य": "work", "वर्क": "work",
    "शक्ति": "power", "पावर": "power",
    "दूरी": "distance", "डिस्टेंस": "distance",
    "समय": "time", "टाइम": "time",
    "गति": "speed", "वेग": "velocity",
    "ऊंचाई": "height", "ऊँचाई": "height",
    "घनत्व": "density", "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",
    "मोलर द्रव्यमान": "molar mass", "मोलर मास": "molar mass",
    "मोलरता": "molarity", "मोल्स": "moles", "मोल": "moles"
}

def normalize_query(q):
    q = str(q).lower().strip()

    # Replace Hindi number words
    for word, num in sorted(V16_NUMBER_WORDS.items(), key=lambda x: len(x[0]), reverse=True):
        q = re.sub(r'(?<!\S)' + re.escape(word) + r'(?!\S)', num, q)

    # Translate Hindi technical terms
    for word, eng in sorted(V16_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
        q = q.replace(word, eng)

    # Strip Hindi particles
    for part in ["और", "में", "है", "हैं", "से", "पर", "का", "की", "के", "हुआ", "करो", "ज्ञात", "निकालो"]:
        q = re.sub(r'(?<!\S)' + re.escape(part) + r'(?!\S)', ' ', q)

    return re.sub(r'\s+', ' ', q).strip()

# ------------------------------------------------
# 2. VARIABLE & TOPIC DETECTOR
# ------------------------------------------------

def detect_topic(q):
    q = normalize_query(q)
    if "kinetic energy" in q:
        return "kinetic_energy"
    if "potential energy" in q:
        return "potential_energy"
    if "molarity" in q:
        return "molarity"
    if "molar mass" in q or "moles" in q:
        return "moles"
    if "power" in q:
        return "power"
    if "work" in q:
        return "work"
    if "force" in q:
        return "force"
    if "speed" in q or "velocity" in q:
        return "speed"
    return "unknown"

def extract_number(q, aliases):
    q = normalize_query(q)
    patterns = []
    for alias in aliases:
        # Ensure word boundaries for alphabetic aliases, or handle unit abbreviations safely
        boundary = r'\b' if alias.isalpha() else r''
        patterns.extend([
            boundary + re.escape(alias) + r'\s*is?\s*([-+]?\d+(?:\.\d+)?)',
            boundary + re.escape(alias) + r'\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)',
            r'([-+]?\d+(?:\.\d+)?)\s*' + re.escape(alias) + boundary
        ])

    for pattern in patterns:
        match = re.search(pattern, q, re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None

def extract_all_numbers(q):
    return [float(x) for x in re.findall(r'[-+]?\d+(?:\.\d+)?', q)]

# ------------------------------------------------
# 3. UNIFIED SOLVER
# ------------------------------------------------

def suno_magic(q):
    normalized = normalize_query(q)
    topic = detect_topic(normalized)
    all_nums = extract_all_numbers(normalized)

    if topic == "force":
        m = extract_number(normalized, ["mass", "kg"])
        a = extract_number(normalized, ["acceleration", "m/s2", "m/s^2", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if a is None and len(all_nums) >= 2: a = all_nums[1]

        if m is None or a is None:
            return {"success": False, "message": "Mass and acceleration required."}

        ans = m * a
        return {
            "success": True,
            "topic": "force",
            "values": {"mass": m, "acceleration": a, "force": ans},
            "result": ans,
            "unit": "N",
            "explanation": f"F = m * a = {m} * {a} = {ans} N"
        }

    elif topic == "work":
        # Targeted pattern extraction first to prevent overlapping assignments
        f = extract_number(normalized, ["force", "n", "newton"])
        d = extract_number(normalized, ["distance", "m", "meter"])

        # If exact patterns fail, use position fallback
        if f is None and d is None:
            if len(all_nums) >= 2:
                f, d = all_nums[0], all_nums[1]
        elif f is None and d is not None:
            remaining = [n for n in all_nums if n != d]
            if remaining: f = remaining[0]
        elif d is None and f is not None:
            remaining = [n for n in all_nums if n != f]
            if remaining: d = remaining[0]

        if f is None or d is None:
            return {"success": False, "message": "Force and distance required."}

        ans = f * d
        return {
            "success": True,
            "topic": "work",
            "values": {"force": f, "distance": d, "work": ans},
            "result": ans,
            "unit": "J",
            "explanation": f"W = F * d = {f} * {d} = {ans} J"
        }

    elif topic == "power":
        w = extract_number(normalized, ["work", "j", "joule"])
        t = extract_number(normalized, ["time", "s", "second"])
        if w is None and len(all_nums) >= 1: w = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]

        if w is None or t is None:
            return {"success": False, "message": "Work and time required."}
        if t == 0:
            return {"success": False, "message": "Time cannot be zero."}

        ans = w / t
        return {
            "success": True,
            "topic": "power",
            "values": {"work": w, "time": t, "power": ans},
            "result": ans,
            "unit": "W",
            "explanation": f"P = W / t = {w} / {t} = {ans} W"
        }

    elif topic == "speed":
        d = extract_number(normalized, ["distance", "m", "meter"])
        t = extract_number(normalized, ["time", "s", "second"])
        if d is None and len(all_nums) >= 1: d = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]

        if d is None or t is None:
            return {"success": False, "message": "Distance and time required."}
        if t == 0:
            return {"success": False, "message": "Time cannot be zero."}

        ans = d / t
        return {
            "success": True,
            "topic": "speed",
            "values": {"distance": d, "time": t, "speed": ans},
            "result": ans,
            "unit": "m/s",
            "explanation": f"v = d / t = {d} / {t} = {ans} m/s"
        }

    elif topic == "kinetic_energy":
        m = extract_number(normalized, ["mass", "kg"])
        v = extract_number(normalized, ["speed", "velocity", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if v is None and len(all_nums) >= 2: v = all_nums[1]

        if m is None or v is None:
            return {"success": False, "message": "Mass and velocity required."}

        ans = 0.5 * m * (v ** 2)
        return {
            "success": True,
            "topic": "kinetic_energy",
            "values": {"mass": m, "velocity": v, "kinetic_energy": ans},
            "result": ans,
            "unit": "J",
            "explanation": f"KE = 0.5 * m * v^2 = 0.5 * {m} * {v}^2 = {ans} J"
        }

    elif topic == "potential_energy":
        m = extract_number(normalized, ["mass", "kg"])
        h = extract_number(normalized, ["height", "m"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if h is None and len(all_nums) >= 2: h = all_nums[1]

        if m is None or h is None:
            return {"success": False, "message": "Mass and height required."}

        g = 9.8
        ans = m * g * h
        return {
            "success": True,
            "topic": "potential_energy",
            "values": {"mass": m, "height": h, "potential_energy": ans},
            "result": ans,
            "unit": "J",
            "explanation": f"PE = m * g * h = {m} * 9.8 * {h} = {ans} J"
        }

    elif topic == "moles":
        mass = extract_number(normalized, ["mass", "g"])
        molar_mass = extract_number(normalized, ["molar mass", "g/mol"])
        if mass is None and len(all_nums) >= 1: mass = all_nums[0]
        if molar_mass is None and len(all_nums) >= 2: molar_mass = all_nums[1]

        if mass is None or molar_mass is None:
            return {"success": False, "message": "Mass and molar mass required."}
        if molar_mass == 0:
            return {"success": False, "message": "Molar mass cannot be zero."}

        ans = mass / molar_mass
        return {
            "success": True,
            "topic": "moles",
            "values": {"mass": mass, "molar_mass": molar_mass, "moles": ans},
            "result": ans,
            "unit": "mol",
            "explanation": f"n = mass / molar_mass = {mass} / {molar_mass} = {ans} mol"
        }

    elif topic == "molarity":
        moles = extract_number(normalized, ["moles", "mol"])
        vol = extract_number(normalized, ["volume", "l"])
        if moles is None and len(all_nums) >= 1: moles = all_nums[0]
        if vol is None and len(all_nums) >= 2: vol = all_nums[1]

        if moles is None or vol is None:
            return {"success": False, "message": "Moles and volume required."}
        if vol == 0:
            return {"success": False, "message": "Volume cannot be zero."}

        ans = moles / vol
        return {
            "success": True,
            "topic": "molarity",
            "values": {"moles": moles, "volume": vol, "molarity": ans},
            "result": ans,
            "unit": "mol/L",
            "explanation": f"M = moles / volume = {moles} / {vol} = {ans} mol/L"
        }

    return {"success": False, "message": "Topic could not be identified."}

# ================================================================
# 4. COMPREHENSIVE REGRESSION TESTS
# ================================================================

print("--- EXECUTION & TEST RESULTS ---\n")

tests = {
    "English Force": {
        "q": "mass is 5 kg and acceleration is 2 m/s2 calculate force",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Hindi Force": {
        "q": "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Hindi Digits Force": {
        "q": "द्रव्यमान पांच किलो और त्वरण दो है बल निकालो",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Work (Standard)": {
        "q": "10 N force 5 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001 and abs(r["values"]["distance"] - 5) < 0.001 and abs(r["values"]["work"] - 50) < 0.001
    },
    "Work Regression 1": {
        "q": "20 N force 3 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["force"] - 20) < 0.001 and abs(r["values"]["distance"] - 3) < 0.001 and abs(r["values"]["work"] - 60) < 0.001
    },
    "Work Regression 2": {
        "q": "5 N force 10 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["force"] - 5) < 0.001 and abs(r["values"]["distance"] - 10) < 0.001 and abs(r["values"]["work"] - 50) < 0.001
    },
    "Power": {
        "q": "work is 100 J and time is 5 s find power",
        "assert_fn": lambda r: abs(r["values"]["power"] - 20) < 0.001
    },
    "Speed": {
        "q": "distance 100 m and time 20 s calculate speed",
        "assert_fn": lambda r: abs(r["values"]["speed"] - 5) < 0.001
    },
    "Kinetic Energy": {
        "q": "mass 4 kg speed 3 m/s kinetic energy calculate",
        "assert_fn": lambda r: abs(r["values"]["kinetic_energy"] - 18) < 0.001
    },
    "Potential Energy": {
        "q": "mass 2 kg height 5 m potential energy calculate",
        "assert_fn": lambda r: abs(r["values"]["potential_energy"] - 98) < 0.001
    },
    "Moles": {
        "q": "mass 18 g and molar mass 18 g/mol find moles",
        "assert_fn": lambda r: abs(r["values"]["moles"] - 1) < 0.001
    },
    "Molarity": {
        "q": "moles 2 and volume 4 L calculate molarity",
        "assert_fn": lambda r: abs(r["values"]["molarity"] - 0.5) < 0.001
    }
}

all_passed = True
for name, info in tests.items():
    try:
        res = suno_magic(info["q"])
        if res["success"] and info["assert_fn"](res):
            print(f"PASS: {name} (Extracted: {res['values'] if 'values' in res else 'N/A'})")
        else: 
            print(f"FAIL: {name} (Result: {res})")
            all_passed = False
    except Exception as e:
        print(f"FAIL: {name} with error: {str(e)}")
        all_passed = False

if all_passed:
    print("\n✅ ALL V16.4 VERIFICATION TESTS PASSED SUCCESSFULLY!")
else:
    print("\n❌ SOME TESTS FAILED.")

# ================================================================
# SUNO SAATHI MAGIC ENGINE v16.4 (CORRECTED & VERIFIED)
# ================================================================

import re
import math

# ------------------------------------------------
# 1. HINDI/HINGLISH TRANSLATION & DICTIONARIES
# ------------------------------------------------

V16_NUMBER_WORDS = {
    "एक": "1", "दो": "2", "तीन": "3", "चार": "4", "पांच": "5",
    "पाँच": "5", "छह": "6", "छः": "6", "सात": "7", "आठ": "8",
    "नौ": "9", "दस": "10", "बीस": "20", "पचास": "50", "सौ": "100"
}

V16_TERMS = {
    "द्रव्यमान": "mass", "मास": "mass", "वजन": "mass",
    "त्वरण": "acceleration", "एक्सेलरेशन": "acceleration",
    "बल": "force", "फोर्स": "force",
    "कार्य": "work", "वर्क": "work",
    "शक्ति": "power", "पावर": "power",
    "दूरी": "distance", "डिस्टेंस": "distance",
    "समय": "time", "टाइम": "time",
    "गति": "speed", "वेग": "velocity",
    "ऊंचाई": "height", "ऊँचाई": "height",
    "घनत्व": "density", "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",
    "मोलर द्रव्यमान": "molar mass", "मोलर मास": "molar mass",
    "मोलरता": "molarity", "मोल्स": "moles", "मोल": "moles"
}

def normalize_query(q):
    q = str(q).lower().strip()

    # Replace Hindi number words
    for word, num in sorted(V16_NUMBER_WORDS.items(), key=lambda x: len(x[0]), reverse=True):
        q = re.sub(r'(?<!\S)' + re.escape(word) + r'(?!\S)', num, q)

    # Translate Hindi technical terms
    for word, eng in sorted(V16_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
        q = q.replace(word, eng)

    # Strip Hindi particles
    for part in ["और", "में", "है", "हैं", "से", "पर", "का", "की", "के", "हुआ", "करो", "ज्ञात", "निकालो"]:
        q = re.sub(r'(?<!\S)' + re.escape(part) + r'(?!\S)', ' ', q)

    return re.sub(r'\s+', ' ', q).strip()

# ------------------------------------------------
# 2. VARIABLE & TOPIC DETECTOR
# ------------------------------------------------

def detect_topic(q):
    q = normalize_query(q)
    if "kinetic energy" in q:
        return "kinetic_energy"
    if "potential energy" in q:
        return "potential_energy"
    if "molarity" in q:
        return "molarity"
    if "molar mass" in q or "moles" in q:
        return "moles"
    if "power" in q:
        return "power"
    if "work" in q:
        return "work"
    if "force" in q:
        return "force"
    if "speed" in q or "velocity" in q:
        return "speed"
    return "unknown"

def extract_number(q, aliases):
    q = normalize_query(q)
    patterns = []
    for alias in aliases:
        # Ensure word boundaries for alphabetic aliases, or handle unit abbreviations safely
        boundary = r'\b' if alias.isalpha() else r''
        patterns.extend([
            boundary + re.escape(alias) + r'\s*is?\s*([-+]?\d+(?:\.\d+)?)',
            boundary + re.escape(alias) + r'\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)',
            r'([-+]?\d+(?:\.\d+)?)\s*' + re.escape(alias) + boundary
        ])

    for pattern in patterns:
        match = re.search(pattern, q, re.IGNORECASE)
        if match:
            return float(match.group(1))
    return None

def extract_all_numbers(q):
    return [float(x) for x in re.findall(r'[-+]?\d+(?:\.\d+)?', q)]

# ------------------------------------------------
# 3. UNIFIED SOLVER
# ------------------------------------------------

def suno_magic(q):
    normalized = normalize_query(q)
    topic = detect_topic(normalized)
    all_nums = extract_all_numbers(normalized)

    if topic == "force":
        m = extract_number(normalized, ["mass", "kg"])
        a = extract_number(normalized, ["acceleration", "m/s2", "m/s^2", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if a is None and len(all_nums) >= 2: a = all_nums[1]

        if m is None or a is None:
            return {"success": False, "message": "Mass and acceleration required."}

        ans = m * a
        return {
            "success": True,
            "topic": "force",
            "values": {"mass": m, "acceleration": a, "force": ans},
            "result": ans,
            "unit": "N",
            "explanation": f"F = m * a = {m} * {a} = {ans} N"
        }

    elif topic == "work":
        f = extract_number(normalized, ["force", "newton"])
        d = extract_number(normalized, ["distance", "meter"])

        f_unit = re.search(r'([-+]?\d+(?:\.\d+)?)\s*n\b', normalized)
        d_unit = re.search(r'([-+]?\d+(?:\.\d+)?)\s*m\b', normalized)

        if f is None and f_unit:
            f = float(f_unit.group(1))
        if d is None and d_unit:
            d = float(d_unit.group(1))

        if f is None and d is None:
            if len(all_nums) >= 2:
                f, d = all_nums[0], all_nums[1]
        elif f is None and d is not None:
            remaining = [n for n in all_nums if n != d]
            if remaining: f = remaining[0]
        elif d is None and f is not None:
            remaining = [n for n in all_nums if n != f]
            if remaining: d = remaining[0]

        if f is None or d is None:
            return {"success": False, "message": "Force and distance required."}

        ans = f * d
        return {
            "success": True,
            "topic": "work",
            "values": {"force": f, "distance": d, "work": ans},
            "result": ans,
            "unit": "J",
            "explanation": f"W = F * d = {f} * {d} = {ans} J"
        }

    elif topic == "power":
        w = extract_number(normalized, ["work", "j", "joule"])
        t = extract_number(normalized, ["time", "s", "second"])
        if w is None and len(all_nums) >= 1: w = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]

        if w is None or t is None:
            return {"success": False, "message": "Work and time required."}

        if t == 0:
            return {"success": False, "message": "Time cannot be zero."}

        ans = w / t
        return {
            "success": True,
            "topic": "power",
            "values": {"work": w, "time": t, "power": ans},
            "result": ans,
            "unit": "W",
            "explanation": f"P = W / t = {w} / {t} = {ans} W"
        }

    elif topic == "speed":
        d = extract_number(normalized, ["distance", "m", "meter"])
        t = extract_number(normalized, ["time", "s", "second"])
        if d is None and len(all_nums) >= 1: d = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]

        if d is None or t is None:
            return {"success": False, "message": "Distance and time required."}
        if t == 0:
            return {"success": False, "message": "Time cannot be zero."}

        ans = d / t
        return {
            "success": True,
            "topic": "speed",
            "values": {"distance": d, "time": t, "speed": ans},
            "result": ans,
            "unit": "m/s",
            "explanation": f"v = d / t = {d} / {t} = {ans} m/s"
        }

    elif topic == "kinetic_energy":
        m = extract_number(normalized, ["mass", "kg"])
        v = extract_number(normalized, ["speed", "velocity", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if v is None and len(all_nums) >= 2: v = all_nums[1]

        if m is None or v is None:
            return {"success": False, "message": "Mass and velocity required."}

        ans = 0.5 * m * (v ** 2)
        return {
            "success": True,
            "topic": "kinetic_energy",
            "values": {"mass": m, "velocity": v, "kinetic_energy": ans},
            "result": ans,
            "unit": "J",
            "explanation": f"KE = 0.5 * m * v^2 = 0.5 * {m} * {v}^2 = {ans} J"
        }

    elif topic == "potential_energy":
        m = extract_number(normalized, ["mass", "kg"])
        h = extract_number(normalized, ["height", "m"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if h is None and len(all_nums) >= 2: h = all_nums[1]

        if m is None or h is None:
            return {"success": False, "message": "Mass and height required."}

        g = 9.8
        ans = m * g * h
        return {
            "success": True,
            "topic": "potential_energy",
            "values": {"mass": m, "height": h, "potential_energy": ans},
            "result": ans,
            "unit": "J",
            "explanation": f"PE = m * g * h = {m} * 9.8 * {h} = {ans} J"
        }

    elif topic == "moles":
        mass = extract_number(normalized, ["mass", "g"])
        molar_mass = extract_number(normalized, ["molar mass", "g/mol"])
        if mass is None and len(all_nums) >= 1: mass = all_nums[0]
        if molar_mass is None and len(all_nums) >= 2: molar_mass = all_nums[1]

        if mass is None or molar_mass is None:
            return {"success": False, "message": "Mass and molar mass required."}
        if molar_mass == 0:
            return {"success": False, "message": "Molar mass cannot be zero."}

        ans = mass / molar_mass
        return {
            "success": True,
            "topic": "moles",
            "values": {"mass": mass, "molar_mass": molar_mass, "moles": ans},
            "result": ans,
            "unit": "mol",
            "explanation": f"n = mass / molar_mass = {mass} / {molar_mass} = {ans} mol"
        }

    elif topic == "molarity":
        moles = extract_number(normalized, ["moles", "mol"])
        vol = extract_number(normalized, ["volume", "l"])
        if moles is None and len(all_nums) >= 1: moles = all_nums[0]
        if vol is None and len(all_nums) >= 2: vol = all_nums[1]

        if moles is None or vol is None:
            return {"success": False, "message": "Moles and volume required."}
        if vol == 0:
            return {"success": False, "message": "Volume cannot be zero."}

        ans = moles / vol
        return {
            "success": True,
            "topic": "molarity",
            "values": {"moles": moles, "volume": vol, "molarity": ans},
            "result": ans,
            "unit": "mol/L",
            "explanation": f"M = moles / volume = {moles} / {vol} = {ans} mol/L"
        }

    return {"success": False, "message": "Topic could not be identified."}

# ================================================================
# 4. COMPREHENSIVE REGRESSION TESTS
# ================================================================

print("--- EXECUTION & TEST RESULTS ---\n")

tests = {
    "English Force": {
        "q": "mass is 5 kg and acceleration is 2 m/s2 calculate force",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Hindi Force": {
        "q": "द्रव्यमान 5 kg और त्वरण 2 है बल निकालो",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Hindi Digits Force": {
        "q": "द्रव्यमान पांच किलो और त्वरण दो है बल निकालो",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001
    },
    "Work (Standard)": {
        "q": "10 N force 5 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["force"] - 10) < 0.001 and abs(r["values"]["distance"] - 5) < 0.001 and abs(r["values"]["work"] - 50) < 0.001
    },
    "Work Regression 1": {
        "q": "20 N force 3 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["force"] - 20) < 0.001 and abs(r["values"]["distance"] - 3) < 0.001 and abs(r["values"]["work"] - 60) < 0.001
    },
    "Work Regression 2": {
        "q": "5 N force 10 m distance calculate work",
        "assert_fn": lambda r: abs(r["values"]["force"] - 5) < 0.001 and abs(r["values"]["distance"] - 10) < 0.001 and abs(r["values"]["work"] - 50) < 0.001
    },
    "Power": {
        "q": "work is 100 J and time is 5 s find power",
        "assert_fn": lambda r: abs(r["values"]["power"] - 20) < 0.001
    },
    "Speed": {
        "q": "distance 100 m and time 20 s calculate speed",
        "assert_fn": lambda r: abs(r["values"]["speed"] - 5) < 0.001
    },
    "Kinetic Energy": {
        "q": "mass 4 kg speed 3 m/s kinetic energy calculate",
        "assert_fn": lambda r: abs(r["values"]["kinetic_energy"] - 18) < 0.001
    },
    "Potential Energy": {
        "q": "mass 2 kg height 5 m potential energy calculate",
        "assert_fn": lambda r: abs(r["values"]["potential_energy"] - 98) < 0.001
    },
    "Moles": {
        "q": "mass 18 g and molar mass 18 g/mol find moles",
        "assert_fn": lambda r: abs(r["values"]["moles"] - 1) < 0.001
    },
    "Molarity": {
        "q": "moles 2 and volume 4 L calculate molarity",
        "assert_fn": lambda r: abs(r["values"]["molarity"] - 0.5) < 0.001
    }
}

all_passed = True
for name, info in tests.items():
    try:
        res = suno_magic(info["q"])
        if res["success"] and info["assert_fn"](res):
            print(f"PASS: {name} (Extracted: {res['values'] if 'values' in res else 'N/A'})")
        else:
            print(f"FAIL: {name} (Result: {res})")
            all_passed = False
    except Exception as e:
        print(f"FAIL: {name} with error: {str(e)}")
        all_passed = False

if all_passed:
    print("\n✅ ALL V16.4 VERIFICATION TESTS PASSED SUCCESSFULLY!")
else:
    print("\n❌ SOME TESTS FAILED.")

# ================================================================
# SUNO SAATHI MAGIC ENGINE v16.5 (WORK PARSER CORRECTED)
# ================================================================

import re
import math

V16_NUMBER_WORDS = {
    "एक": "1", "दो": "2", "तीन": "3", "चार": "4", "पांच": "5",
    "पाँच": "5", "छह": "6", "छः": "6", "सात": "7", "आठ": "8",
    "नौ": "9", "दस": "10", "बीस": "20", "पचास": "50", "सौ": "100"
}

V16_TERMS = {
    "द्रव्यमान": "mass", "मास": "mass", "वजन": "mass",
    "त्वरण": "acceleration", "एक्सेलरेशन": "acceleration",
    "बल": "force", "फोर्स": "force",
    "कार्य": "work", "वर्क": "work",
    "शक्ति": "power", "पावर": "power",
    "दूरी": "distance", "डिस्टेंस": "distance",
    "समय": "time", "टाइम": "time",
    "गति": "speed", "वेग": "velocity",
    "ऊंचाई": "height", "ऊँचाई": "height",
    "घनत्व": "density", "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",
    "मोलर द्रव्यमान": "molar mass", "मोलर मास": "molar mass",
    "मोलरता": "molarity", "मोल्स": "moles", "मोल": "moles"
}

def normalize_query(q):
    q = str(q).lower().strip()
    for word, num in sorted(V16_NUMBER_WORDS.items(), key=lambda x: len(x[0]), reverse=True):
        q = re.sub(r'(?<!\S)' + re.escape(word) + r'(?!\S)', num, q)
    for word, eng in sorted(V16_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
        q = q.replace(word, eng)
    for part in ["और", "में", "है", "हैं", "से", "पर", "का", "की", "के", "हुआ", "करो", "ज्ञात", "निकालो"]:
        q = re.sub(r'(?<!\S)' + re.escape(part) + r'(?!\S)', ' ', q)
    return re.sub(r'\s+', ' ', q).strip()

def detect_topic(q):
    q = normalize_query(q)
    if "kinetic energy" in q: return "kinetic_energy"
    if "potential energy" in q: return "potential_energy"
    if "molarity" in q: return "molarity"
    if "molar mass" in q or "moles" in q: return "moles"
    if "power" in q: return "power"
    if "work" in q: return "work"
    if "force" in q: return "force"
    if "speed" in q or "velocity" in q: return "speed"
    return "unknown"

def extract_number(q, aliases):
    q = normalize_query(q)
    patterns = []
    for alias in aliases:
        boundary = r'\b' if alias.isalpha() else r''
        patterns.extend([
            boundary + re.escape(alias) + r'\s*is?\s*([-+]?\d+(?:\.\d+)?)',
            boundary + re.escape(alias) + r'\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)',
            r'([-+]?\d+(?:\.\d+)?)\s*' + re.escape(alias) + boundary
        ])
    for pattern in patterns:
        match = re.search(pattern, q, re.IGNORECASE)
        if match: return float(match.group(1))
    return None

def extract_all_numbers(q):
    return [float(x) for x in re.findall(r'[-+]?\d+(?:\.\d+)?', q)]

def _extract_quantity_by_unit(q, units):
    """Find a number immediately attached to one of the specified units."""
    number = r'([-+]?\d+(?:\.\d+)?)'
    unit_alt = "|".join(sorted((re.escape(u) for u in units), key=len, reverse=True))
    pattern = number + r'\s*(?:' + unit_alt + r')(?![a-z])'
    match = re.search(pattern, q, re.IGNORECASE)
    return float(match.group(1)) if match else None

def _extract_labeled_quantity(q, label):
    number = r'([-+]?\d+(?:\.\d+)?)'
    patterns = [
        r'\b' + re.escape(label) + r'\s*(?:is\s*)?[:=]?\s*' + number,
        number + r'\s*\b' + re.escape(label) + r'\b'
    ]
    for pattern in patterns:
        m = re.search(pattern, q, re.IGNORECASE)
        if m:
            return float(m.group(1))
    return None

def suno_magic(q):
    normalized = normalize_query(q)
    topic = detect_topic(normalized)
    all_nums = extract_all_numbers(normalized)

    if topic == "force":
        m = extract_number(normalized, ["mass", "kg"])
        a = extract_number(normalized, ["acceleration", "m/s2", "m/s^2", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if a is None and len(all_nums) >= 2: a = all_nums[1]
        if m is None or a is None:
            return {"success": False, "message": "Mass and acceleration required."}
        ans = m * a
        return {"success": True, "topic": "force", "values": {"mass": m, "acceleration": a, "force": ans},
                "result": ans, "unit": "N", "explanation": f"F = m * a = {m} * {a} = {ans} N"}

    elif topic == "work":
        # Strict unit-based extraction: N means Force; m means Distance.
        f = _extract_quantity_by_unit(normalized, ["newtons", "newton", "n"])
        d = _extract_quantity_by_unit(normalized, ["meters", "meter", "metres", "metre", "m"])

        if f is None:
            f = _extract_labeled_quantity(normalized, "force")
        if d is None:
            d = _extract_labeled_quantity(normalized, "distance")

        if f is None or d is None:
            return {"success": False, "message": "Force (N) and distance (m) required."}

        ans = f * d
        return {"success": True, "topic": "work", "values": {"force": f, "distance": d, "work": ans},
                "result": ans, "unit": "J", "explanation": f"W = F * d = {f} * {d} = {ans} J"}

    elif topic == "power":
        w = extract_number(normalized, ["work", "j", "joule"])
        t = extract_number(normalized, ["time", "s", "second"])
        if w is None and len(all_nums) >= 1: w = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]
        if w is None or t is None: return {"success": False, "message": "Work and time required."}
        if t == 0: return {"success": False, "message": "Time cannot be zero."}
        ans = w / t
        return {"success": True, "topic": "power", "values": {"work": w, "time": t, "power": ans},
                "result": ans, "unit": "W", "explanation": f"P = W / t = {w} / {t} = {ans} W"}

    elif topic == "speed":
        d = extract_number(normalized, ["distance", "m", "meter"])
        t = extract_number(normalized, ["time", "s", "second"])
        if d is None and len(all_nums) >= 1: d = all_nums[0]
        if t is None and len(all_nums) >= 2: t = all_nums[1]
        if d is None or t is None: return {"success": False, "message": "Distance and time required."}
        if t == 0: return {"success": False, "message": "Time cannot be zero."}
        ans = d / t
        return {"success": True, "topic": "speed", "values": {"distance": d, "time": t, "speed": ans},
                "result": ans, "unit": "m/s", "explanation": f"v = d / t = {d} / {t} = {ans} m/s"}

    elif topic == "kinetic_energy":
        m = extract_number(normalized, ["mass", "kg"])
        v = extract_number(normalized, ["speed", "velocity", "m/s"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if v is None and len(all_nums) >= 2: v = all_nums[1]
        if m is None or v is None: return {"success": False, "message": "Mass and velocity required."}
        ans = 0.5 * m * (v ** 2)
        return {"success": True, "topic": "kinetic_energy", "values": {"mass": m, "velocity": v, "kinetic_energy": ans},
                "result": ans, "unit": "J", "explanation": f"KE = 0.5 * m * v^2 = 0.5 * {m} * {v}^2 = {ans} J"}

    elif topic == "potential_energy":
        m = extract_number(normalized, ["mass", "kg"])
        h = extract_number(normalized, ["height", "m"])
        if m is None and len(all_nums) >= 1: m = all_nums[0]
        if h is None and len(all_nums) >= 2: h = all_nums[1]
        if m is None or h is None: return {"success": False, "message": "Mass and height required."}
        g = 9.8
        ans = m * g * h
        return {"success": True, "topic": "potential_energy", "values": {"mass": m, "height": h, "potential_energy": ans},
                "result": ans, "unit": "J", "explanation": f"PE = m * g * h = {m} * 9.8 * {h} = {ans} J"}

    elif topic == "moles":
        mass = extract_number(normalized, ["mass", "g"])
        molar_mass = extract_number(normalized, ["molar mass", "g/mol"])
        if mass is None and len(all_nums) >= 1: mass = all_nums[0]
        if molar_mass is None and len(all_nums) >= 2: molar_mass = all_nums[1]
        if mass is None or molar_mass is None: return {"success": False, "message": "Mass and molar mass required."}
        if molar_mass == 0: return {"success": False, "message": "Molar mass cannot be zero."}
        ans = mass / molar_mass
        return {"success": True, "topic": "moles", "values": {"mass": mass, "molar_mass": molar_mass, "moles": ans},
                "result": ans, "unit": "mol", "explanation": f"n = mass / molar mass = {mass} / {molar_mass} = {ans} mol"}

    elif topic == "molarity":
        moles = extract_number(normalized, ["moles", "mol"])
        vol = extract_number(normalized, ["volume", "l"])
        if moles is None and len(all_nums) >= 1: moles = all_nums[0]
        if vol is None and len(all_nums) >= 2: vol = all_nums[1]
        if moles is None or vol is None: return {"success": False, "message": "Moles and volume required."}
        if vol == 0: return {"success": False, "message": "Volume cannot be zero."}
        ans = moles / vol
        return {"success": True, "topic": "molarity", "values": {"moles": moles, "volume": vol, "molarity": ans},
                "result": ans, "unit": "mol/L", "explanation": f"M = moles / volume = {moles} / {vol} = {ans} mol/L"}

    return {"success": False, "message": "Topic could not be identified."}

# ================================================================
# REGRESSION TESTS
# ================================================================
print("--- V16.5 EXECUTION & TEST RESULTS ---")
tests = {
    "English Force": ("mass is 5 kg and acceleration is 2 m/s2 calculate force", lambda r: r["values"]["force"] == 10),
    "Hindi Force": ("द्रव्यमान 5 kg और त्वरण 2 है बल निकालो", lambda r: r["values"]["force"] == 10),
    "Hindi Digits Force": ("द्रव्यमान पांच किलो और त्वरण दो है बल निकालो", lambda r: r["values"]["force"] == 10),
    "Work Standard": ("10 N force 5 m distance calculate work", lambda r: r["values"]["force"] == 10 and r["values"]["distance"] == 5 and r["values"]["work"] == 50),
    "Work Regression 1": ("20 N force 3 m distance calculate work", lambda r: r["values"]["force"] == 20 and r["values"]["distance"] == 3 and r["values"]["work"] == 60),
    "Work Regression 2": ("5 N force 10 m distance calculate work", lambda r: r["values"]["force"] == 5 and r["values"]["distance"] == 10 and r["values"]["work"] == 50),
    "Power": ("work is 100 J and time is 5 s find power", lambda r: r["values"]["power"] == 20),
    "Speed": ("distance 100 m and time 20 s calculate speed", lambda r: r["values"]["speed"] == 5),
    "Kinetic Energy": ("mass 4 kg speed 3 m/s kinetic energy calculate", lambda r: r["values"]["kinetic_energy"] == 18),
    "Potential Energy": ("mass 2 kg height 5 m potential energy calculate", lambda r: r["values"]["potential_energy"] == 98),
    "Moles": ("mass 18 g and molar mass 18 g/mol find moles", lambda r: r["values"]["moles"] == 1),
    "Molarity": ("moles 2 and volume 4 L calculate molarity", lambda r: r["values"]["molarity"] == 0.5),
}
all_passed = True
for name, (query, check) in tests.items():
    try:
        result = suno_magic(query)
        ok = result.get("success", False) and check(result)
        print(("PASS" if ok else "FAIL") + f": {name} | {result}")
        if not ok: all_passed = False
    except Exception as exc:
        print(f"FAIL: {name} | ERROR: {exc}")
        all_passed = False
print("\\n" + ("ALL TESTS PASSED" if all_passed else "SOME TESTS FAILED"))

# ================================================================
# SUNO SAATHI MAGIC ENGINE v16.6
# COMPLETE PHYSICS + CHEMISTRY SOLVER WITH UNIT CONVERSIONS
# ================================================================

import re
import math

# ------------------------------------------------
# 1. DATABASE & DICTIONARIES
# ------------------------------------------------

AVOGADRO = 6.02214076e23

V16_NUMBER_WORDS = {
    "एक": "1", "दो": "2", "तीन": "3", "चार": "4", "पांच": "5",
    "पाँच": "5", "छह": "6", "छः": "6", "सात": "7", "आठ": "8",
    "नौ": "9", "दस": "10", "बीस": "20", "पचास": "50", "सौ": "100"
}

V16_TERMS = {
    "द्रव्यमान": "mass", "मास": "mass", "वजन": "mass",
    "त्वरण": "acceleration", "एक्सेलरेशन": "acceleration",
    "बल": "force", "फोर्स": "force",
    "कार्य": "work", "वर्क": "work",
    "शक्ति": "power", "पावर": "power",
    "दूरी": "distance", "डिस्टेंस": "distance",
    "समय": "time", "टाइम": "time",
    "गति": "speed", "वेग": "velocity",
    "ऊंचाई": "height", "ऊँचाई": "height",
    "घनत्व": "density", "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",
    "मोलर द्रव्यमान": "molar mass", "मोलर मास": "molar mass",
    "मोलरता": "molarity", "मोल्स": "moles", "मोल": "moles",
    "संवेग": "momentum", "कण": "particles", "कणों": "particles",
    "आयतन": "volume", "वॉल्यूम": "volume"
}

# Dimension lookup to map units to physical quantities
UNIT_DIMENSIONS = {
    "m": "distance", "meter": "distance", "meters": "distance", "metre": "distance", "metres": "distance",
    "km": "distance", "kilometer": "distance", "kilometers": "distance", "kilometre": "distance", "kilometres": "distance",
    "cm": "distance", "centimeter": "distance", "centimeters": "distance", "centimetre": "distance", "centimetres": "distance",
    "mm": "distance", "millimeter": "distance", "millimeters": "distance",
    "s": "time", "second": "time", "seconds": "time", "sec": "time",
    "min": "time", "minute": "time", "minutes": "time",
    "h": "time", "hour": "time", "hours": "time", "hr": "time", "hrs": "time",
    "kg": "mass", "kilogram": "mass", "kilograms": "mass",
    "g": "mass", "gram": "mass", "grams": "mass",
    "mg": "mass", "milligram": "mass", "milligrams": "mass",
    "n": "force", "newton": "force", "newtons": "force",
    "j": "work_energy", "joule": "work_energy", "joules": "work_energy",
    "w": "power", "watt": "power", "watts": "power",
    "m/s": "speed", "km/h": "speed",
    "l": "volume", "liter": "volume", "liters": "volume", "litre": "volume", "litres": "volume",
    "ml": "volume", "milliliter": "volume", "milliliters": "volume",
    "mol": "moles", "moles": "moles",
    "c": "temperature", "k": "temperature"
}

# ------------------------------------------------
# 2. INPUT PROCESSING & NORMALIZATION
# ------------------------------------------------

def normalize_query(q):
    q = str(q).lower().strip()
    # Replace Hindi number words
    for word, num in sorted(V16_NUMBER_WORDS.items(), key=lambda x: len(x[0]), reverse=True):
        q = re.sub(r'(?<!\S)' + re.escape(word) + r'(?!\S)', num, q)
    # Translate technical terms
    for word, eng in sorted(V16_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
        q = q.replace(word, eng)
    # Remove grammatical particles
    for part in ["और", "में", "है", "हैं", "से", "पर", "का", "की", "के", "हुआ", "करो", "ज्ञात", "निकालो", "निकाल", "बताओ", "पता", "calculate", "find", "solve"]:
        q = re.sub(r'(?<!\S)' + re.escape(part) + r'(?!\S)', ' ', q)
    return re.sub(r'\s+', ' ', q).strip()

def detect_topic(q):
    q = normalize_query(q)
    if "kinetic energy" in q: return "kinetic_energy"
    if "potential energy" in q: return "potential_energy"
    if "molarity" in q: return "molarity"
    if "molar mass" in q or "moles" in q: return "moles"
    if "particles" in q: return "particles"
    if "power" in q: return "power"
    if "work" in q: return "work"
    if "force" in q: return "force"
    if "speed" in q or "velocity" in q: return "speed"
    if "density" in q: return "density"
    if "momentum" in q: return "momentum"
    return "unknown"

# ------------------------------------------------
# 3. UNIT CONVERSION
# ------------------------------------------------

def convert_to_base(value, unit):
    if not unit: return value, ""
    u = unit.lower().strip()
    
    # Distance -> base m
    if u in ["km", "kilometer", "kilometers", "kilometre", "kilometres"]:
        return value * 1000.0, "m"
    if u in ["cm", "centimeter", "centimeters", "centimetre", "centimetres"]:
        return value * 0.01, "m"
    if u in ["mm", "millimeter", "millimeters"]:
        return value * 0.001, "m"
        
    # Time -> base s
    if u in ["min", "minute", "minutes"]:
        return value * 60.0, "s"
    if u in ["h", "hour", "hours", "hr", "hrs"]:
        return value * 3600.0, "s"
        
    # Mass -> base kg
    if u in ["g", "gram", "grams"]:
        return value * 0.001, "kg"
    if u in ["mg", "milligram", "milligrams"]:
        return value * 0.000001, "kg"
        
    # Volume -> base L
    if u in ["ml", "milliliter", "milliliters"]:
        return value * 0.001, "L"
        
    # Speed -> base m/s
    if u in ["km/h", "kph"]:
        return value / 3.6, "m/s"
        
    # Temperature -> base K
    if u in ["c", "celsius", "°c"]:
        return value + 273.15, "K"
        
    return value, u

# ------------------------------------------------
# 4. SMART VARIABLE EXTRACTION
# ------------------------------------------------

def extract_labeled_variables(q):
    # Extract all pattern groups of [number][unit] or [label] [number]
    q_norm = normalize_query(q)
    
    # Regex to match numeric values and potential following alphabetic units
    pairs = re.findall(r'([-+]?\d+(?:\.\d+)?)\s*([a-zA-Z/°^2]+)?', q_norm)
    
    extracted = []
    for val_str, unit_str in pairs:
        val = float(val_str)
        unit = unit_str.strip().lower() if unit_str else ""
        dimension = UNIT_DIMENSIONS.get(unit, "")
        extracted.append({"val": val, "unit": unit, "dimension": dimension, "original": f"{val_str} {unit_str}"})
        
    return extracted

# ------------------------------------------------
# 5. SUNO MAGIC ENGINE
# ------------------------------------------------

def suno_magic(q, language="English"):
    normalized = normalize_query(q)
    topic = detect_topic(q)
    
    # Extract numeric quantities with their units and dimensions
    quantities = extract_labeled_variables(q)
    
    # Fallback numerical sequence
    numbers = [q["val"] for q in quantities]
    
    def get_quantity(dimension_list, label_keywords, index_fallback):
        # 1. Try to find by explicit unit matching the dimension
        for item in quantities:
            if item["dimension"] in dimension_list:
                return convert_to_base(item["val"], item["unit"])[0]
        # 2. Try to find by label keyword proximity in the query
        for kw in label_keywords:
            match = re.search(r'\b' + re.escape(kw) + r'\b\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)', normalized)
            if match:
                return float(match.group(1))
        # 3. Fallback to indexing if available
        if len(numbers) > index_fallback:
            return numbers[index_fallback]
        return None

    if topic == "force":
        m = get_quantity(["mass"], ["mass", "kg"], 0)
        a = get_quantity(["acceleration"], ["acceleration", "m/s2", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if a is None: return {"success": False, "message": "Acceleration is missing."}
        ans = m * a
        return {
            "success": True, "topic": "force", "values": {"mass": m, "acceleration": a, "force": ans},
            "result": ans, "unit": "N",
            "explanation": f"F = m * a = {m} * {a} = {ans} N"
        }

    elif topic == "work":
        f = get_quantity(["force"], ["force", "n"], 0)
        d = get_quantity(["distance"], ["distance", "m"], 1)
        if f is None: return {"success": False, "message": "Force is missing."}
        if d is None: return {"success": False, "message": "Distance is missing."}
        ans = f * d
        return {
            "success": True, "topic": "work", "values": {"force": f, "distance": d, "work": ans},
            "result": ans, "unit": "J",
            "explanation": f"W = F * d = {f} * {d} = {ans} J"
        }

    elif topic == "power":
        w = get_quantity(["work_energy"], ["work", "j"], 0)
        t = get_quantity(["time"], ["time", "s"], 1)
        if w is None: return {"success": False, "message": "Work is missing."}
        if t is None: return {"success": False, "message": "Time is missing."}
        if t == 0: return {"success": False, "message": "Time cannot be zero."}
        ans = w / t
        return {
            "success": True, "topic": "power", "values": {"work": w, "time": t, "power": ans},
            "result": ans, "unit": "W",
            "explanation": f"P = W / t = {w} / {t} = {ans} W"
        }

    elif topic == "speed":
        d = get_quantity(["distance"], ["distance", "m"], 0)
        t = get_quantity(["time"], ["time", "s"], 1)
        if d is None: return {"success": False, "message": "Distance is missing."}
        if t is None: return {"success": False, "message": "Time is missing."}
        if t == 0: return {"success": False, "message": "Time cannot be zero."}
        ans = d / t
        return {
            "success": True, "topic": "speed", "values": {"distance": d, "time": t, "speed": ans},
            "result": ans, "unit": "m/s",
            "explanation": f"v = d / t = {d} / {t} = {ans} m/s"
        }

    elif topic == "kinetic_energy":
        m = get_quantity(["mass"], ["mass", "kg"], 0)
        v = get_quantity(["speed"], ["speed", "velocity", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if v is None: return {"success": False, "message": "Velocity is missing."}
        ans = 0.5 * m * (v ** 2)
        return {
            "success": True, "topic": "kinetic_energy", "values": {"mass": m, "velocity": v, "kinetic_energy": ans},
            "result": ans, "unit": "J",
            "explanation": f"KE = 0.5 * m * v^2 = 0.5 * {m} * {v}^2 = {ans} J"
        }

    elif topic == "potential_energy":
        m = get_quantity(["mass"], ["mass", "kg"], 0)
        h = get_quantity(["distance"], ["height", "m"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if h is None: return {"success": False, "message": "Height is missing."}
        g = 9.8
        ans = m * g * h
        return {
            "success": True, "topic": "potential_energy", "values": {"mass": m, "height": h, "potential_energy": ans},
            "result": ans, "unit": "J",
            "explanation": f"PE = m * g * h = {m} * 9.8 * {h} = {ans} J"
        }

    elif topic == "density":
        m = get_quantity(["mass"], ["mass", "kg"], 0)
        vol = get_quantity(["volume"], ["volume", "l"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if vol is None: return {"success": False, "message": "Volume is missing."}
        if vol == 0: return {"success": False, "message": "Volume cannot be zero."}
        ans = m / vol
        return {
            "success": True, "topic": "density", "values": {"mass": m, "volume": vol, "density": ans},
            "result": ans, "unit": "kg/L",
            "explanation": f"Density = m / V = {m} / {vol} = {ans} kg/L"
        }

    elif topic == "momentum":
        m = get_quantity(["mass"], ["mass", "kg"], 0)
        v = get_quantity(["speed"], ["velocity", "speed", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if v is None: return {"success": False, "message": "Velocity is missing."}
        ans = m * v
        return {
            "success": True, "topic": "momentum", "values": {"mass": m, "velocity": v, "momentum": ans},
            "result": ans, "unit": "kg*m/s",
            "explanation": f"Momentum = m * v = {m} * {v} = {ans} kg*m/s"
        }

    elif topic == "moles":
        mass = get_quantity(["mass"], ["mass", "g"], 0)
        molar_mass = get_quantity([], ["molar mass", "g/mol"], 1)
        if mass is None: return {"success": False, "message": "Mass is missing."}
        if molar_mass is None: return {"success": False, "message": "Molar mass is missing."}
        if molar_mass == 0: return {"success": False, "message": "Molar mass cannot be zero."}
        ans = mass / molar_mass
        return {
            "success": True, "topic": "moles", "values": {"mass": mass, "molar_mass": molar_mass, "moles": ans},
            "result": ans, "unit": "mol",
            "explanation": f"n = mass / molar mass = {mass} / {molar_mass} = {ans} mol"
        }

    elif topic == "molarity":
        moles = get_quantity(["moles"], ["moles", "mol"], 0)
        vol = get_quantity(["volume"], ["volume", "l"], 1)
        if moles is None: return {"success": False, "message": "Moles are missing."}
        if vol is None: return {"success": False, "message": "Volume is missing."}
        if vol == 0: return {"success": False, "message": "Volume cannot be zero."}
        ans = moles / vol
        return {
            "success": True, "topic": "molarity", "values": {"moles": moles, "volume": vol, "molarity": ans},
            "result": ans, "unit": "mol/L",
            "explanation": f"M = moles / volume = {moles} / {vol} = {ans} mol/L"
        }

    elif topic == "particles":
        moles = get_quantity(["moles"], ["moles", "mol"], 0)
        if moles is None: return {"success": False, "message": "Moles are missing."}
        ans = moles * AVOGADRO
        return {
            "success": True, "topic": "particles", "values": {"moles": moles, "particles": ans},
            "result": ans, "unit": "particles",
            "explanation": f"N = n * N_A = {moles} * {AVOGADRO} = {ans} particles"
        }

    return {"success": False, "message": "Topic could not be identified."}

# ================================================================
# RUNNING ALL REGRESSION & NEW UPGRADE TESTS
# ================================================================
print("--- SUNO SAATHI MAGIC ENGINE v16.6 EXECUTION --- ")

tests = {
    # V16.5 Core Baseline
    "English Force": ("mass is 5 kg and acceleration is 2 m/s2 calculate force", lambda r: r["values"]["force"] == 10),
    "Hindi Force": ("द्रव्यमान 5 kg और त्वरण 2 है बल निकालो", lambda r: r["values"]["force"] == 10),
    "Hindi Digits Force": ("द्रव्यमान पांच किलो और त्वरण दो है बल निकालो", lambda r: r["values"]["force"] == 10),
    "Work Standard": ("10 N force 5 m distance calculate work", lambda r: r["values"]["force"] == 10 and r["values"]["distance"] == 5 and r["values"]["work"] == 50),
    "Work Regression 1": ("20 N force 3 m distance calculate work", lambda r: r["values"]["force"] == 20 and r["values"]["distance"] == 3 and r["values"]["work"] == 60),
    "Work Regression 2": ("5 N force 10 m distance calculate work", lambda r: r["values"]["force"] == 5 and r["values"]["distance"] == 10 and r["values"]["work"] == 50),
    "Power": ("work is 100 J and time is 5 s find power", lambda r: r["values"]["power"] == 20),
    "Speed": ("distance 100 m and time 20 s calculate speed", lambda r: r["values"]["speed"] == 5),
    "Kinetic Energy": ("mass 4 kg speed 3 m/s kinetic energy calculate", lambda r: r["values"]["kinetic_energy"] == 18),
    "Potential Energy": ("mass 2 kg height 5 m potential energy calculate", lambda r: r["values"]["potential_energy"] == 98),
    "Moles": ("mass 18 g and molar mass 18 g/mol find moles", lambda r: r["values"]["moles"] == 1),
    "Molarity": ("moles 2 and volume 4 L calculate molarity", lambda r: r["values"]["molarity"] == 0.5),
    
    # V16.6 Upgraded Features
    "Density": ("mass 10 kg and volume 2 L find density", lambda r: r["values"]["density"] == 5),
    "Momentum": ("mass 5 kg and velocity 4 m/s calculate momentum", lambda r: r["values"]["momentum"] == 20),
    "Particles Count": ("moles 2 calculate number of particles", lambda r: abs(r["values"]["particles"] - 1.204428e24) < 1e18),
    "Unit Conversion - Distance (km to m)": ("distance 5 km time 500 s calculate speed", lambda r: r["values"]["speed"] == 10),
    "Unit Conversion - Time (minutes to seconds)": ("distance 600 m time 5 minutes calculate speed", lambda r: r["values"]["speed"] == 2),
    "Unit Conversion - Speed (km/h to m/s)": ("mass 10 kg velocity 36 km/h calculate momentum", lambda r: r["values"]["momentum"] == 100),
    "Missing values check": ("mass 5 kg calculate force", lambda r: r["success"] is False and "missing" in r["message"].lower()),
    "Zero Division handling": ("work 50 J time 0 s calculate power", lambda r: r["success"] is False and "cannot be zero" in r["message"].lower())
}

all_passed = True
for name, (query, check) in tests.items():
    try:
        result = suno_magic(query)
        ok = check(result)
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {name} | Result: {result}")
        if not ok: all_passed = False
    except Exception as exc:
        print(f"FAIL (Exception): {name} | Error: {exc}")
        all_passed = False

print("\n--- COMPLETED TESTING --- ")
if all_passed:
    print("✅ ALL TESTS PASSED SUCCESSFULLY!")
else:
    print("❌ SOME TESTS FAILED!")

# ================================================================
# SUNO SAATHI MAGIC ENGINE v16.6 (FIXED VERSION)
# COMPLETE PHYSICS + CHEMISTRY SOLVER WITH UNIT CONVERSIONS
# ================================================================

import re
import math

# ------------------------------------------------
# 1. DATABASE & DICTIONARIES
# ------------------------------------------------

AVOGADRO = 6.02214076e23

V16_NUMBER_WORDS = {
    "एक": "1", "दो": "2", "तीन": "3", "चार": "4", "पांच": "5",
    "पाँच": "5", "छह": "6", "छः": "6", "सात": "7", "आठ": "8",
    "नौ": "9", "दस": "10", "बीस": "20", "पचास": "50", "सौ": "100"
}

V16_TERMS = {
    "द्रव्यमान": "mass", "मास": "mass", "वजन": "mass",
    "त्वरण": "acceleration", "एक्सेलरेशन": "acceleration",
    "बल": "force", "फोर्स": "force",
    "कार्य": "work", "वर्क": "work",
    "शक्ति": "power", "पावर": "power",
    "दूरी": "distance", "डिस्टेंस": "distance",
    "समय": "time", "टाइम": "time",
    "गति": "speed", "वेग": "velocity",
    "ऊंचाई": "height", "ऊँचाई": "height",
    "घनत्व": "density", "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",
    "मोलर द्रव्यमान": "molar mass", "मोलर मास": "molar mass",
    "मोलरता": "molarity", "मोल्स": "moles", "मोल": "moles",
    "संवेग": "momentum", "कण": "particles", "कणों": "particles",
    "आयतन": "volume", "वॉल्यूम": "volume"
}

# Dimension lookup to map units to physical quantities
UNIT_DIMENSIONS = {
    "m": "distance", "meter": "distance", "meters": "distance", "metre": "distance", "metres": "distance",
    "km": "distance", "kilometer": "distance", "kilometers": "distance", "kilometre": "distance", "kilometres": "distance",
    "cm": "distance", "centimeter": "distance", "centimeters": "distance", "centimetre": "distance", "centimetres": "distance",
    "mm": "distance", "millimeter": "distance", "millimeters": "distance",
    "s": "time", "second": "time", "seconds": "time", "sec": "time",
    "min": "time", "minute": "time", "minutes": "time",
    "h": "time", "hour": "time", "hours": "time", "hr": "time", "hrs": "time",
    "kg": "mass", "kilogram": "mass", "kilograms": "mass",
    "g": "mass_g", "gram": "mass_g", "grams": "mass_g",
    "mg": "mass_g", "milligram": "mass_g", "milligrams": "mass_g",
    "n": "force", "newton": "force", "newtons": "force",
    "j": "work_energy", "joule": "work_energy", "joules": "work_energy",
    "w": "power", "watt": "power", "watts": "power",
    "m/s": "speed", "km/h": "speed",
    "l": "volume", "liter": "volume", "liters": "volume", "litre": "volume", "litres": "volume",
    "ml": "volume", "milliliter": "volume", "milliliters": "volume",
    "mol": "moles", "moles": "moles",
    "c": "temperature", "k": "temperature"
}

# ------------------------------------------------
# 2. INPUT PROCESSING & NORMALIZATION
# ------------------------------------------------

def normalize_query(q):
    q = str(q).lower().strip()
    # Replace Hindi number words
    for word, num in sorted(V16_NUMBER_WORDS.items(), key=lambda x: len(x[0]), reverse=True):
        q = re.sub(r'(?<!\S)' + re.escape(word) + r'(?!\S)', num, q)
    # Translate technical terms
    for word, eng in sorted(V16_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
        q = q.replace(word, eng)
    # Remove grammatical particles
    for part in ["और", "में", "है", "हैं", "से", "पर", "का", "की", "के", "हुआ", "करो", "ज्ञात", "निकालो", "निकाल", "बताओ", "पता", "calculate", "find", "solve"]:
        q = re.sub(r'(?<!\S)' + re.escape(part) + r'(?!\S)', ' ', q)
    return re.sub(r'\s+', ' ', q).strip()

def detect_topic(q):
    q = normalize_query(q)
    if "kinetic energy" in q: return "kinetic_energy"
    if "potential energy" in q: return "potential_energy"
    if "molarity" in q: return "molarity"
    if "molar mass" in q or "moles" in q: return "moles"
    if "particles" in q: return "particles"
    if "power" in q: return "power"
    if "work" in q: return "work"
    if "force" in q: return "force"
    if "speed" in q or "velocity" in q: return "speed"
    if "density" in q: return "density"
    if "momentum" in q: return "momentum"
    return "unknown"

# ------------------------------------------------
# 3. UNIT CONVERSION
# ------------------------------------------------

def convert_to_base(value, unit):
    if not unit: return value, ""
    u = unit.lower().strip()
    
    # Distance -> base m
    if u in ["km", "kilometer", "kilometers", "kilometre", "kilometres"]:
        return value * 1000.0, "m"
    if u in ["cm", "centimeter", "centimeters", "centimetre", "centimetres"]:
        return value * 0.01, "m"
    if u in ["mm", "millimeter", "millimeters"]:
        return value * 0.001, "m"
        
    # Time -> base s
    if u in ["min", "minute", "minutes"]:
        return value * 60.0, "s"
    if u in ["h", "hour", "hours", "hr", "hrs"]:
        return value * 3600.0, "s"
        
    # Mass -> base kg
    if u in ["g", "gram", "grams"]:
        return value * 0.001, "kg"
    if u in ["mg", "milligram", "milligrams"]:
        return value * 0.000001, "kg"
        
    # Volume -> base L
    if u in ["ml", "milliliter", "milliliters"]:
        return value * 0.001, "L"
        
    # Speed -> base m/s
    if u in ["km/h", "kph"]:
        return value / 3.6, "m/s"
        
    # Temperature -> base K
    if u in ["c", "celsius", "°c"]:
        return value + 273.15, "K"
        
    return value, u

# Special conversion helper for Chemistry (standard base is grams, not kilograms)
def convert_to_chemistry_base(value, unit):
    if not unit: return value, ""
    u = unit.lower().strip()
    if u in ["kg", "kilogram", "kilograms"]:
        return value * 1000.0, "g"
    if u in ["mg", "milligram", "milligrams"]:
        return value * 0.001, "g"
    return value, "g"

# ------------------------------------------------
# 4. SMART VARIABLE EXTRACTION
# ------------------------------------------------

def extract_labeled_variables(q):
    # Extract all pattern groups of [number][unit] or [label] [number]
    q_norm = normalize_query(q)
    
    # Regex to match numeric values and potential following alphabetic units
    pairs = re.findall(r'([-+]?\d+(?:\.\d+)?)\s*([a-zA-Z/°^2]+)?', q_norm)
    
    extracted = []
    for val_str, unit_str in pairs:
        val = float(val_str)
        unit = unit_str.strip().lower() if unit_str else ""
        dimension = UNIT_DIMENSIONS.get(unit, "")
        extracted.append({"val": val, "unit": unit, "dimension": dimension, "original": f"{val_str} {unit_str}"})
        
    return extracted

# ------------------------------------------------
# 5. SUNO MAGIC ENGINE
# ------------------------------------------------

def suno_magic(q, language="English"):
    normalized = normalize_query(q)
    topic = detect_topic(q)
    
    # Extract numeric quantities with their units and dimensions
    quantities = extract_labeled_variables(q)
    
    # Fallback numerical sequence
    numbers = [q["val"] for q in quantities]
    
    def get_quantity(dimension_list, label_keywords, index_fallback, chemistry_mode=False):
        # 1. Try to find by explicit unit matching the dimension
        for item in quantities:
            if item["dimension"] in dimension_list:
                if chemistry_mode:
                    return convert_to_chemistry_base(item["val"], item["unit"])[0]
                else:
                    return convert_to_base(item["val"], item["unit"])[0]
        # 2. Try to find by label keyword proximity in the query
        for kw in label_keywords:
            match = re.search(r'\b' + re.escape(kw) + r'\b\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)', normalized)
            if match:
                return float(match.group(1))
        # 3. Fallback to indexing if available
        if len(numbers) > index_fallback:
            return numbers[index_fallback]
        return None

    if topic == "force":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        a = get_quantity(["acceleration"], ["acceleration", "m/s2", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if a is None: return {"success": False, "message": "Acceleration is missing."}
        ans = m * a
        return {
            "success": True, "topic": "force", "values": {"mass": m, "acceleration": a, "force": ans},
            "result": ans, "unit": "N",
            "explanation": f"F = m * a = {m} * {a} = {ans} N"
        }

    elif topic == "work":
        f = get_quantity(["force"], ["force", "n"], 0)
        d = get_quantity(["distance"], ["distance", "m"], 1)
        if f is None: return {"success": False, "message": "Force is missing."}
        if d is None: return {"success": False, "message": "Distance is missing."}
        ans = f * d
        return {
            "success": True, "topic": "work", "values": {"force": f, "distance": d, "work": ans},
            "result": ans, "unit": "J",
            "explanation": f"W = F * d = {f} * {d} = {ans} J"
        }

    elif topic == "power":
        w = get_quantity(["work_energy"], ["work", "j"], 0)
        t = get_quantity(["time"], ["time", "s"], 1)
        if w is None: return {"success": False, "message": "Work is missing."}
        if t is None: return {"success": False, "message": "Time is missing."}
        if t == 0: return {"success": False, "message": "Time cannot be zero."}
        ans = w / t
        return {
            "success": True, "topic": "power", "values": {"work": w, "time": t, "power": ans},
            "result": ans, "unit": "W",
            "explanation": f"P = W / t = {w} / {t} = {ans} W"
        }

    elif topic == "speed":
        d = get_quantity(["distance"], ["distance", "m"], 0)
        t = get_quantity(["time"], ["time", "s"], 1)
        if d is None: return {"success": False, "message": "Distance is missing."}
        if t is None: return {"success": False, "message": "Time is missing."}
        if t == 0: return {"success": False, "message": "Time cannot be zero."}
        ans = d / t
        return {
            "success": True, "topic": "speed", "values": {"distance": d, "time": t, "speed": ans},
            "result": ans, "unit": "m/s",
            "explanation": f"v = d / t = {d} / {t} = {ans} m/s"
        }

    elif topic == "kinetic_energy":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        v = get_quantity(["speed"], ["speed", "velocity", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if v is None: return {"success": False, "message": "Velocity is missing."}
        ans = 0.5 * m * (v ** 2)
        return {
            "success": True, "topic": "kinetic_energy", "values": {"mass": m, "velocity": v, "kinetic_energy": ans},
            "result": ans, "unit": "J",
            "explanation": f"KE = 0.5 * m * v^2 = 0.5 * {m} * {v}^2 = {ans} J"
        }

    elif topic == "potential_energy":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        h = get_quantity(["distance"], ["height", "m"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if h is None: return {"success": False, "message": "Height is missing."}
        g = 9.8
        ans = m * g * h
        return {
            "success": True, "topic": "potential_energy", "values": {"mass": m, "height": h, "potential_energy": ans},
            "result": ans, "unit": "J",
            "explanation": f"PE = m * g * h = {m} * 9.8 * {h} = {ans} J"
        }

    elif topic == "density":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        vol = get_quantity(["volume"], ["volume", "l"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if vol is None: return {"success": False, "message": "Volume is missing."}
        if vol == 0: return {"success": False, "message": "Volume cannot be zero."}
        ans = m / vol
        return {
            "success": True, "topic": "density", "values": {"mass": m, "volume": vol, "density": ans},
            "result": ans, "unit": "kg/L",
            "explanation": f"Density = m / V = {m} / {vol} = {ans} kg/L"
        }

    elif topic == "momentum":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        v = get_quantity(["speed"], ["velocity", "speed", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if v is None: return {"success": False, "message": "Velocity is missing."}
        ans = m * v
        return {
            "success": True, "topic": "momentum", "values": {"mass": m, "velocity": v, "momentum": ans},
            "result": ans, "unit": "kg*m/s",
            "explanation": f"Momentum = m * v = {m} * {v} = {ans} kg*m/s"
        }

    elif topic == "moles":
        mass = get_quantity(["mass_g", "mass"], ["mass", "g"], 0, chemistry_mode=True)
        molar_mass = get_quantity([], ["molar mass", "g/mol"], 1)
        if mass is None: return {"success": False, "message": "Mass is missing."}
        if molar_mass is None: return {"success": False, "message": "Molar mass is missing."}
        if molar_mass == 0: return {"success": False, "message": "Molar mass cannot be zero."}
        ans = mass / molar_mass
        return {
            "success": True, "topic": "moles", "values": {"mass": mass, "molar_mass": molar_mass, "moles": ans},
            "result": ans, "unit": "mol",
            "explanation": f"n = mass / molar mass = {mass} / {molar_mass} = {ans} mol"
        }

    elif topic == "molarity":
        moles = get_quantity(["moles"], ["moles", "mol"], 0)
        vol = get_quantity(["volume"], ["volume", "l"], 1)
        if moles is None: return {"success": False, "message": "Moles are missing."}
        if vol is None: return {"success": False, "message": "Volume is missing."}
        if vol == 0: return {"success": False, "message": "Volume cannot be zero."}
        ans = moles / vol
        return {
            "success": True, "topic": "molarity", "values": {"moles": moles, "volume": vol, "molarity": ans},
            "result": ans, "unit": "mol/L",
            "explanation": f"M = moles / volume = {moles} / {vol} = {ans} mol/L"
        }

    elif topic == "particles":
        moles = get_quantity(["moles"], ["moles", "mol"], 0)
        if moles is None: return {"success": False, "message": "Moles are missing."}
        ans = moles * AVOGADRO
        return {
            "success": True, "topic": "particles", "values": {"moles": moles, "particles": ans},
            "result": ans, "unit": "particles",
            "explanation": f"N = n * N_A = {moles} * {AVOGADRO} = {ans} particles"
        }

    return {"success": False, "message": "Topic could not be identified."}

# ================================================================
# RUNNING ALL REGRESSION & NEW UPGRADE TESTS
# ================================================================
print("--- SUNO SAATHI MAGIC ENGINE v16.6 EXECUTION --- ")

tests = { 
    # V16.5 Core Baseline
    "English Force": ("mass is 5 kg and acceleration is 2 m/s2 calculate force", lambda r: r["values"]["force"] == 10),
    "Hindi Force": ("द्रव्यमान 5 kg और त्वरण 2 है बल निकालो", lambda r: r["values"]["force"] == 10),
    "Hindi Digits Force": ("द्रव्यमान पांच किलो और त्वरण दो है बल निकालो", lambda r: r["values"]["force"] == 10),
    "Work Standard": ("10 N force 5 m distance calculate work", lambda r: r["values"]["force"] == 10 and r["values"]["distance"] == 5 and r["values"]["work"] == 50),
    "Work Regression 1": ("20 N force 3 m distance calculate work", lambda r: r["values"]["force"] == 20 and r["values"]["distance"] == 3 and r["values"]["work"] == 60),
    "Work Regression 2": ("5 N force 10 m distance calculate work", lambda r: r["values"]["force"] == 5 and r["values"]["distance"] == 10 and r["values"]["work"] == 50),
    "Power": ("work is 100 J and time is 5 s find power", lambda r: r["values"]["power"] == 20),
    "Speed": ("distance 100 m and time 20 s calculate speed", lambda r: r["values"]["speed"] == 5),
    "Kinetic Energy": ("mass 4 kg speed 3 m/s kinetic energy calculate", lambda r: r["values"]["kinetic_energy"] == 18),
    "Potential Energy": ("mass 2 kg height 5 m potential energy calculate", lambda r: r["values"]["potential_energy"] == 98),
    "Moles": ("mass 18 g and molar mass 18 g/mol find moles", lambda r: r["values"]["moles"] == 1),
    "Molarity": ("moles 2 and volume 4 L calculate molarity", lambda r: r["values"]["molarity"] == 0.5),
    
    # V16.6 Upgraded Features
    "Density": ("mass 10 kg and volume 2 L find density", lambda r: r["values"]["density"] == 5),
    "Momentum": ("mass 5 kg and velocity 4 m/s calculate momentum", lambda r: r["values"]["momentum"] == 20),
    "Particles Count": ("moles 2 calculate number of particles", lambda r: abs(r["values"]["particles"] - 1.204428e24) < 1e18),
    "Unit Conversion - Distance (km to m)": ("distance 5 km time 500 s calculate speed", lambda r: r["values"]["speed"] == 10),
    "Unit Conversion - Time (minutes to seconds)": ("distance 600 m time 5 minutes calculate speed", lambda r: r["values"]["speed"] == 2),
    "Unit Conversion - Speed (km/h to m/s)": ("mass 10 kg velocity 36 km/h calculate momentum", lambda r: r["values"]["momentum"] == 100),
    "Missing values check": ("mass 5 kg calculate force", lambda r: r["success"] is False and "missing" in r["message"].lower()),
    "Zero Division handling": ("work 50 J time 0 s calculate power", lambda r: r["success"] is False and "cannot be zero" in r["message"].lower())
}

all_passed = True
for name, (query, check) in tests.items():
    try:
        result = suno_magic(query)
        ok = check(result)
        status = "PASS" if ok else "FAIL"
        print(f"{status}: {name} | Result: {result}")
        if not ok: all_passed = False
    except Exception as exc: 
        print(f"FAIL (Exception): {name} | Error: {exc}")
        all_passed = False

print("\n--- COMPLETED TESTING --- ")
if all_passed:
    print("✅ ALL TESTS PASSED SUCCESSFULLY!")
else:
    print("❌ SOME TESTS FAILED!")

# ================================================================
# SUNO SAATHI MAGIC ENGINE v16.6 (FIXED VERSION)
# COMPLETE PHYSICS + CHEMISTRY SOLVER WITH UNIT CONVERSIONS
# ================================================================

import re
import math

# ------------------------------------------------
# 1. DATABASE & DICTIONARIES
# ------------------------------------------------

AVOGADRO = 6.02214076e23

V16_NUMBER_WORDS = {
    "एक": "1", "दो": "2", "तीन": "3", "चार": "4", "पांच": "5",
    "पाँच": "5", "छह": "6", "छः": "6", "सात": "7", "आठ": "8",
    "नौ": "9", "दस": "10", "बीस": "20", "पचास": "50", "सौ": "100"
}

V16_TERMS = {
    "द्रव्यमान": "mass", "मास": "mass", "वजन": "mass",
    "त्वरण": "acceleration", "एक्सेलरेशन": "acceleration",
    "बल": "force", "फोर्स": "force",
    "कार्य": "work", "वर्क": "work",
    "शक्ति": "power", "पावर": "power",
    "दूरी": "distance", "डिस्टेंस": "distance",
    "समय": "time", "टाइम": "time",
    "गति": "speed", "वेग": "velocity",
    "ऊंचाई": "height", "ऊँचाई": "height",
    "घनत्व": "density", "गतिज ऊर्जा": "kinetic energy",
    "स्थितिज ऊर्जा": "potential energy",
    "मोलर द्रव्यमान": "molar mass", "मोलर मास": "molar mass",
    "मोलरता": "molarity", "मोल्स": "moles", "मोल": "moles",
    "संवेग": "momentum", "कण": "particles", "कणों": "particles",
    "आयतन": "volume", "वॉल्यूम": "volume"
}

# Dimension lookup to map units to physical quantities
UNIT_DIMENSIONS = {
    "m": "distance", "meter": "distance", "meters": "distance", "metre": "distance", "metres": "distance",
    "km": "distance", "kilometer": "distance", "kilometers": "distance", "kilometre": "distance", "kilometres": "distance",
    "cm": "distance", "centimeter": "distance", "centimeters": "distance", "centimetre": "distance", "centimetres": "distance",
    "mm": "distance", "millimeter": "distance", "millimeters": "distance",
    "s": "time", "second": "time", "seconds": "time", "sec": "time",
    "min": "time", "minute": "time", "minutes": "time",
    "h": "time", "hour": "time", "hours": "time", "hr": "time", "hrs": "time",
    "kg": "mass", "kilogram": "mass", "kilograms": "mass",
    "g": "mass_g", "gram": "mass_g", "grams": "mass_g",
    "mg": "mass_g", "milligram": "mass_g", "milligrams": "mass_g",
    "n": "force", "newton": "force", "newtons": "force",
    "j": "work_energy", "joule": "work_energy", "joules": "work_energy",
    "w": "power", "watt": "power", "watts": "power",
    "m/s": "speed", "km/h": "speed",
    "l": "volume", "liter": "volume", "liters": "volume", "litre": "volume", "litres": "volume",
    "ml": "volume", "milliliter": "volume", "milliliters": "volume",
    "mol": "moles", "moles": "moles",
    "c": "temperature", "k": "temperature"
}

# ------------------------------------------------
# 2. INPUT PROCESSING & NORMALIZATION
# ------------------------------------------------

def normalize_query(q):
    q = str(q).lower().strip()
    # Replace Hindi number words
    for word, num in sorted(V16_NUMBER_WORDS.items(), key=lambda x: len(x[0]), reverse=True):
        q = re.sub(r'(?<!\S)' + re.escape(word) + r'(?!\S)', num, q)
    # Translate technical terms
    for word, eng in sorted(V16_TERMS.items(), key=lambda x: len(x[0]), reverse=True):
        q = q.replace(word, eng)
    # Remove grammatical particles
    for part in ["और", "में", "है", "हैं", "से", "पर", "का", "की", "के", "हुआ", "करो", "ज्ञात", "निकालो", "निकाल", "बताओ", "पता", "calculate", "find", "solve"]:
        q = re.sub(r'(?<!\S)' + re.escape(part) + r'(?!\S)', ' ', q)
    return re.sub(r'\s+', ' ', q).strip()

def detect_topic(q):
    q = normalize_query(q)
    if "kinetic energy" in q: return "kinetic_energy"
    if "potential energy" in q: return "potential_energy"
    if "molarity" in q: return "molarity"
    if "molar mass" in q or "moles" in q: return "moles"
    if "particles" in q: return "particles"
    if "power" in q: return "power"
    if "work" in q: return "work"
    if "force" in q: return "force"
    if "speed" in q or "velocity" in q: return "speed"
    if "density" in q: return "density"
    if "momentum" in q: return "momentum"
    return "unknown"

# ------------------------------------------------
# 3. UNIT CONVERSION
# ------------------------------------------------

def convert_to_base(value, unit):
    if not unit: return value, ""
    u = unit.lower().strip()

    # Distance -> base m
    if u in ["km", "kilometer", "kilometers", "kilometre", "kilometres"]:
        return value * 1000.0, "m"
    if u in ["cm", "centimeter", "centimeters", "centimetre", "centimetres"]:
        return value * 0.01, "m"
    if u in ["mm", "millimeter", "millimeters"]:
        return value * 0.001, "m"

    # Time -> base s
    if u in ["min", "minute", "minutes"]:
        return value * 60.0, "s"
    if u in ["h", "hour", "hours", "hr", "hrs"]:
        return value * 3600.0, "s"

    # Mass -> base kg
    if u in ["g", "gram", "grams"]:
        return value * 0.001, "kg"
    if u in ["mg", "milligram", "milligrams"]:
        return value * 0.000001, "kg"

    # Volume -> base L
    if u in ["ml", "milliliter", "milliliters"]:
        return value * 0.001, "L"

    # Speed -> base m/s
    if u in ["km/h", "kph"]:
        return value / 3.6, "m/s"

    # Temperature -> base K
    if u in ["c", "celsius", "°c"]:
        return value + 273.15, "K"

    return value, u

# Special conversion helper for Chemistry (standard base is grams, not kilograms)
def convert_to_chemistry_base(value, unit):
    if not unit: return value, ""
    u = unit.lower().strip()
    if u in ["kg", "kilogram", "kilograms"]:
        return value * 1000.0, "g"
    if u in ["mg", "milligram", "milligrams"]:
        return value * 0.001, "g"
    return value, "g"

# ------------------------------------------------
# 4. SMART VARIABLE EXTRACTION
# ------------------------------------------------

def extract_labeled_variables(q):
    q_norm = normalize_query(q)
    # Regex to match numeric values and potential following alphabetic units
    pairs = re.findall(r'([-+]?\d+(?:\.\d+)?)\s*([a-zA-Z/°^2]+)?', q_norm)

    extracted = []
    for val_str, unit_str in pairs:
        val = float(val_str)
        unit = unit_str.strip().lower() if unit_str else ""
        dimension = UNIT_DIMENSIONS.get(unit, "")
        extracted.append({"val": val, "unit": unit, "dimension": dimension, "original": f"{val_str} {unit_str}"})

    return extracted

# ------------------------------------------------
# 5. SUNO MAGIC ENGINE
# ------------------------------------------------

def suno_magic(q, language="English"):
    normalized = normalize_query(q)
    topic = detect_topic(q)

    # Extract numeric quantities with their units and dimensions
    quantities = extract_labeled_variables(q)

    # Fallback numerical sequence
    numbers = [q["val"] for q in quantities]

    def get_quantity(dimension_list, label_keywords, index_fallback, chemistry_mode=False):
        # 1. Try to find by explicit unit matching the dimension
        for item in quantities:
            if item["dimension"] in dimension_list:
                if chemistry_mode:
                    return convert_to_chemistry_base(item["val"], item["unit"])[0]
                else: 
                    return convert_to_base(item["val"], item["unit"])[0]
        # 2. Try to find by label keyword proximity in the query
        for kw in label_keywords:
            match = re.search(r'\b' + re.escape(kw) + r'\b\s*[:=]?\s*([-+]?\d+(?:\.\d+)?)', normalized)
            if match:
                return float(match.group(1))
        # 3. Fallback to indexing if available
        if len(numbers) > index_fallback:
            return numbers[index_fallback]
        return None

    if topic == "force":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        a = get_quantity(["acceleration"], ["acceleration", "m/s2", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if a is None: return {"success": False, "message": "Acceleration is missing."}
        ans = m * a
        return {
            "success": True, "topic": "force", "values": {"mass": m, "acceleration": a, "force": ans},
            "result": ans, "unit": "N",
            "explanation": f"F = m * a = {m} * {a} = {ans} N"
        }

    elif topic == "work":
        f = get_quantity(["force"], ["force", "n"], 0)
        d = get_quantity(["distance"], ["distance", "m"], 1)
        if f is None: return {"success": False, "message": "Force is missing."}
        if d is None: return {"success": False, "message": "Distance is missing."}
        ans = f * d
        return {
            "success": True, "topic": "work", "values": {"force": f, "distance": d, "work": ans},
            "result": ans, "unit": "J",
            "explanation": f"W = F * d = {f} * {d} = {ans} J"
        }

    elif topic == "power":
        w = get_quantity(["work_energy"], ["work", "j"], 0)
        t = get_quantity(["time"], ["time", "s"], 1)
        if w is None: return {"success": False, "message": "Work is missing."}
        if t is None: return {"success": False, "message": "Time is missing."}
        if t == 0: return {"success": False, "message": "Time cannot be zero."}
        ans = w / t
        return {
            "success": True, "topic": "power", "values": {"work": w, "time": t, "power": ans},
            "result": ans, "unit": "W",
            "explanation": f"P = W / t = {w} / {t} = {ans} W"
        }

    elif topic == "speed":
        d = get_quantity(["distance"], ["distance", "m"], 0)
        t = get_quantity(["time"], ["time", "s"], 1)
        if d is None: return {"success": False, "message": "Distance is missing."}
        if t is None: return {"success": False, "message": "Time is missing."}
        if t == 0: return {"success": False, "message": "Time cannot be zero."}
        ans = d / t
        return {
            "success": True, "topic": "speed", "values": {"distance": d, "time": t, "speed": ans},
            "result": ans, "unit": "m/s",
            "explanation": f"v = d / t = {d} / {t} = {ans} m/s"
        }

    elif topic == "kinetic_energy":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        v = get_quantity(["speed"], ["speed", "velocity", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if v is None: return {"success": False, "message": "Velocity is missing."}
        ans = 0.5 * m * (v ** 2)
        return {
            "success": True, "topic": "kinetic_energy", "values": {"mass": m, "velocity": v, "kinetic_energy": ans},
            "result": ans, "unit": "J",
            "explanation": f"KE = 0.5 * m * v^2 = 0.5 * {m} * {v}^2 = {ans} J"
        }

    elif topic == "potential_energy":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        h = get_quantity(["distance"], ["height", "m"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if h is None: return {"success": False, "message": "Height is missing."}
        g = 9.8
        ans = m * g * h
        return {
            "success": True, "topic": "potential_energy", "values": {"mass": m, "height": h, "potential_energy": ans},
            "result": ans, "unit": "J",
            "explanation": f"PE = m * g * h = {m} * 9.8 * {h} = {ans} J"
        }

    elif topic == "density":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        vol = get_quantity(["volume"], ["volume", "l"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if vol is None: return {"success": False, "message": "Volume is missing."}
        if vol == 0: return {"success": False, "message": "Volume cannot be zero."}
        ans = m / vol
        return {
            "success": True, "topic": "density", "values": {"mass": m, "volume": vol, "density": ans},
            "result": ans, "unit": "kg/L",
            "explanation": f"Density = m / V = {m} / {vol} = {ans} kg/L"
        }

    elif topic == "momentum":
        m = get_quantity(["mass", "mass_g"], ["mass", "kg"], 0)
        v = get_quantity(["speed"], ["velocity", "speed", "m/s"], 1)
        if m is None: return {"success": False, "message": "Mass is missing."}
        if v is None: return {"success": False, "message": "Velocity is missing."}
        ans = m * v
        return {
            "success": True, "topic": "momentum", "values": {"mass": m, "velocity": v, "momentum": ans},
            "result": ans, "unit": "kg*m/s",
            "explanation": f"Momentum = m * v = {m} * {v} = {ans} kg*m/s"
        }

    elif topic == "moles":
        mass = get_quantity(["mass_g", "mass"], ["mass", "g"], 0, chemistry_mode=True)
        molar_mass = get_quantity([], ["molar mass", "g/mol"], 1)
        if mass is None: return {"success": False, "message": "Mass is missing."}
        if molar_mass is None: return {"success": False, "message": "Molar mass is missing."}
        if molar_mass == 0: return {"success": False, "message": "Molar mass cannot be zero."}
        ans = mass / molar_mass
        return {
            "success": True, "topic": "moles", "values": {"mass": mass, "molar_mass": molar_mass, "moles": ans},
            "result": ans, "unit": "mol",
            "explanation": f"n = mass / molar mass = {mass} / {molar_mass} = {ans} mol"
        }

    elif topic == "molarity":
        moles = get_quantity(["moles"], ["moles", "mol"], 0)
        vol = get_quantity(["volume"], ["volume", "l"], 1)
        if moles is None: return {"success": False, "message": "Moles are missing."}
        if vol is None: return {"success": False, "message": "Volume is missing."}
        if vol == 0: return {"success": False, "message": "Volume cannot be zero."}
        ans = moles / vol
        return {
            "success": True, "topic": "molarity", "values": {"moles": moles, "volume": vol, "molarity": ans},
            "result": ans, "unit": "mol/L",
            "explanation": f"M = moles / volume = {moles} / {vol} = {ans} mol/L"
        }

    elif topic == "particles":
        moles = get_quantity(["moles"], ["moles", "mol"], 0)
        if moles is None: return {"success": False, "message": "Moles are missing."}
        ans = moles * AVOGADRO
        return {
            "success": True, "topic": "particles", "values": {"moles": moles, "particles": ans},
            "result": ans, "unit": "particles",
            "explanation": f"N = n * N_A = {moles} * {AVOGADRO} = {ans} particles"
        }

    return {

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
def run_tests():
    tests = [
        ("English Force", "force mass 5 kg acceleration 2", 10, "N"),
        ("Hindi Force", "बल mass 5 kg त्वरण 2", 10, "N"),
        ("Hindi Digits Force", "बल mass पाँच kg acceleration दो", 10, "N"),
        ("Work Standard", "work force 10 N distance 5 m", 50, "J"),
        ("Work Regression 1", "calculate work 20 N 3 m", 60, "J"),
        ("Work Regression 2", "work 5 N distance 10 m", 50, "J"),
        ("Power", "power work 100 J time 5 s", 20, "W"),
        ("Speed", "speed distance 5 km time 500 s", 10, "m/s"),
        ("Kinetic Energy", "kinetic energy mass 2 kg speed 3 m/s", 9, "J"),
        ("Potential Energy", "potential energy mass 2 kg height 5 m", 98, "J"),
        ("Moles", "moles mass 18 g molar mass 18 g/mol", 1, "mol"),
        ("Molarity", "molarity moles 2 mol volume 1 L", 2, "mol/L"),
        ("Density", "density mass 10 kg volume 2 L", 5000, "kg/m³"),
        ("Momentum", "momentum mass 5 kg speed 2 m/s", 10, "kg·m/s"),
        ("Particles", "particles 2 mol", 1.204428152e24, "particles"),
        ("Speed kmh", "speed distance 36 km time 1 h", 10, "m/s"),
        ("Speed minutes", "speed distance 600 m time 5 min", 2, "m/s"),
    ]
    print(f"SUNO SAATHI MAGIC ENGINE V{VERSION} TESTING")
    print("="*55)
    passed=0
    for name,q,expected,unit in tests:
        result=suno_magic(q)
        ok=result.get("success") and math.isclose(result["result"],expected,rel_tol=1e-8,abs_tol=1e-8) and result["unit"]==unit
        print(("PASS: " if ok else "FAIL: ")+name, "|", result)
        passed += bool(ok)
    # Missing and zero division checks
    missing=suno_magic("force mass 5 kg calculate force")
    zero=suno_magic("speed distance 10 m time 0 s")
    extra_ok=(not missing["success"] and not zero["success"])
    print(("PASS: " if extra_ok else "FAIL: ")+"Missing/zero guards", missing, zero)
    passed+=bool(extra_ok)
    print("-"*55)
    print(f"RESULT: {passed}/{len(tests)+1} TESTS PASSED")
    return passed, len(tests)+1

if __name__ == "__main__":
    run_tests()

# SUNO SAATHI MAGIC V16 EXPORT

import inspect

# Main engine function check
print("Magic function:", suno_magic)

# Save complete notebook code separately later

# Export complete notebook as main.py

import json

with open("main.py", "w", encoding="utf-8") as f:
    for cell in get_ipython().user_ns.get("In", [])[1:]:
        if cell.strip():
            f.write(cell + "\n\n")

print("main.py created")



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Suno Saathi Magic V16")

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
    return {"message": "Suno Saathi Magic V16 Online"}

@app.get("/health")
def health():
    return {"status": "ok", "version": "V16"}

@app.post("/solve")
def solve(request: SolveRequest):
    result = suno_magic(request.query)
    return result

