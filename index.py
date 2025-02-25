
import streamlit as st

st.title("Unit Converter")

units = [
    "Meters",
    "Centimeters",
    "Kilometers",
    "Millimeters",
    "Inches",
    "Feet",
    "Yards",
    "Miles"
]

from_unit = st.selectbox("From Unit:", units)
to_unit = st.selectbox("To Unit:", units)

value = st.number_input("Enter the value to convert:", value=0.0, format="%.4f")

conversion_factors = {
    "Meters": {
        "Meters": lambda x: x,
        "Centimeters": lambda x: x * 100,
        "Kilometers": lambda x: x / 1000,
        "Millimeters": lambda x: x * 1000,
        "Inches": lambda x: x * 39.3700787,
        "Feet": lambda x: x * 3.2808399,
        "Yards": lambda x: x * 1.0936133,
        "Miles": lambda x: x / 1609.344
    },
    "Centimeters": {
        "Meters": lambda x: x / 100,
        "Centimeters": lambda x: x,
        "Kilometers": lambda x: x / 100000,
        "Millimeters": lambda x: x * 10,
        "Inches": lambda x: x * 0.393700787,
        "Feet": lambda x: x * 0.032808399,
        "Yards": lambda x: x * 0.010936133,
        "Miles": lambda x: x / 160934.4
    },
    "Kilometers": {
        "Meters": lambda x: x * 1000,
        "Centimeters": lambda x: x * 100000,
        "Kilometers": lambda x: x,
        "Millimeters": lambda x: x * 1000000,
        "Inches": lambda x: x * 39370.0787,
        "Feet": lambda x: x * 3280.8399,
        "Yards": lambda x: x * 1093.6133,
        "Miles": lambda x: x / 1.609344
    },
    "Millimeters": {
        "Meters": lambda x: x / 1000,
        "Centimeters": lambda x: x / 10,
        "Kilometers": lambda x: x / 1000000,
        "Millimeters": lambda x: x,
        "Inches": lambda x: x * 0.0393700787,
        "Feet": lambda x: x * 0.0032808399,
        "Yards": lambda x: x * 0.0010936133,
        "Miles": lambda x: x / 1609344
    },
    "Inches": {
        "Meters": lambda x: x * 0.0254,
        "Centimeters": lambda x: x * 2.54,
        "Kilometers": lambda x: x * 2.54e-5,
        "Millimeters": lambda x: x * 25.4,
        "Inches": lambda x: x,
        "Feet": lambda x: x / 12,
        "Yards": lambda x: x / 36,
        "Miles": lambda x: x / 63360
    },
    "Feet": {
        "Meters": lambda x: x * 0.3048,
        "Centimeters": lambda x: x * 30.48,
        "Kilometers": lambda x: x * 0.0003048,
        "Millimeters": lambda x: x * 304.8,
        "Inches": lambda x: x * 12,
        "Feet": lambda x: x,
        "Yards": lambda x: x / 3,
        "Miles": lambda x: x / 5280
    },
    "Yards": {
        "Meters": lambda x: x * 0.9144,
        "Centimeters": lambda x: x * 91.44,
        "Kilometers": lambda x: x * 0.0009144,
        "Millimeters": lambda x: x * 914.4,
        "Inches": lambda x: x * 36,
        "Feet": lambda x: x * 3,
        "Yards": lambda x: x,
        "Miles": lambda x: x / 1760
    },
    "Miles": {
        "Meters": lambda x: x * 1609.344,
        "Centimeters": lambda x: x * 160934.4,
        "Kilometers": lambda x: x * 1.609344,
        "Millimeters": lambda x: x * 1.609344e+6,
        "Inches": lambda x: x * 63360,
        "Feet": lambda x: x * 5280,
        "Yards": lambda x: x * 1760,
        "Miles": lambda x: x
    }
}

converted_value = conversion_factors[from_unit][to_unit](value)

st.write(f"**Result:** {value} {from_unit} = {converted_value} {to_unit}")
