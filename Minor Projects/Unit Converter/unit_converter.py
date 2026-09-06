"""
Unit Converter
--------------
Converts between common units of length, weight, and temperature.

Usage: python 3_unit_converter.py
"""

LENGTH_TO_METERS = {
    "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000,
    "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.34
}

WEIGHT_TO_GRAMS = {
    "mg": 0.001, "g": 1, "kg": 1000,
    "oz": 28.3495, "lb": 453.592
}


def convert_length(value, from_unit, to_unit):
    meters = value * LENGTH_TO_METERS[from_unit]
    return meters / LENGTH_TO_METERS[to_unit]


def convert_weight(value, from_unit, to_unit):
    grams = value * WEIGHT_TO_GRAMS[from_unit]
    return grams / WEIGHT_TO_GRAMS[to_unit]


def convert_temperature(value, from_unit, to_unit):
    # Normalize to Celsius first
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        raise ValueError("Unknown temperature unit")

    if to_unit == "c":
        return celsius
    elif to_unit == "f":
        return celsius * 9 / 5 + 32
    elif to_unit == "k":
        return celsius + 273.15
    else:
        raise ValueError("Unknown temperature unit")


def length_menu():
    print(f"Available units: {', '.join(LENGTH_TO_METERS.keys())}")
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    value = float(input("Value to convert: "))
    result = convert_length(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")


def weight_menu():
    print(f"Available units: {', '.join(WEIGHT_TO_GRAMS.keys())}")
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    value = float(input("Value to convert: "))
    result = convert_weight(value, from_unit, to_unit)
    print(f"{value} {from_unit} = {result:.4f} {to_unit}")


def temperature_menu():
    print("Available units: c (Celsius), f (Fahrenheit), k (Kelvin)")
    from_unit = input("From unit: ").strip().lower()
    to_unit = input("To unit: ").strip().lower()
    value = float(input("Value to convert: "))
    result = convert_temperature(value, from_unit, to_unit)
    print(f"{value}{from_unit.upper()} = {result:.2f}{to_unit.upper()}")


def main():
    menu = """
=== UNIT CONVERTER ===
1. Length
2. Weight
3. Temperature
4. Exit
"""
    while True:
        print(menu)
        choice = input("Choose a category (1-4): ").strip()
        try:
            if choice == "1":
                length_menu()
            elif choice == "2":
                weight_menu()
            elif choice == "3":
                temperature_menu()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
        except (ValueError, KeyError):
            print("Invalid input. Please check your units/values and try again.")


if __name__ == "__main__":
    main()
