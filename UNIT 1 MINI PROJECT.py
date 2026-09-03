# ============================================================
# MINI PROJECT
# SMART UNIT CONVERTER
# ============================================================

import math

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------

def header():
    print("\n" + "=" * 75)
    print("                  SMART UNIT CONVERTER")
    print("=" * 75)
    print("Convert length, weight, temperature, time and speed.")
    print("=" * 75)


# ------------------------------------------------------------
# LENGTH CONVERTER
# ------------------------------------------------------------

def length_converter():

    print("\n" + "-" * 65)
    print("                    LENGTH CONVERTER")
    print("-" * 65)

    print("1. Meter to Kilometer")
    print("2. Kilometer to Meter")
    print("3. Meter to Centimeter")
    print("4. Centimeter to Meter")
    print("5. Kilometer to Miles")
    print("6. Miles to Kilometer")
    print("7. Feet to Meter")
    print("8. Meter to Feet")

    choice = input("\nChoose conversion: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = value / 1000
        unit = "km"

    elif choice == "2":
        result = value * 1000
        unit = "m"

    elif choice == "3":
        result = value * 100
        unit = "cm"

    elif choice == "4":
        result = value / 100
        unit = "m"

    elif choice == "5":
        result = value * 0.621371
        unit = "miles"

    elif choice == "6":
        result = value * 1.60934
        unit = "km"

    elif choice == "7":
        result = value * 0.3048
        unit = "m"

    elif choice == "8":
        result = value * 3.28084
        unit = "feet"

    else:
        print("Invalid choice.")
        return

    print("\nConverted Value:", round(result, 4), unit)


# ------------------------------------------------------------
# WEIGHT CONVERTER
# ------------------------------------------------------------

def weight_converter():

    print("\n" + "-" * 65)
    print("                    WEIGHT CONVERTER")
    print("-" * 65)

    print("1. Kilogram to Gram")
    print("2. Gram to Kilogram")
    print("3. Kilogram to Pound")
    print("4. Pound to Kilogram")
    print("5. Gram to Milligram")
    print("6. Milligram to Gram")

    choice = input("\nChoose conversion: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 1000
        unit = "grams"

    elif choice == "2":
        result = value / 1000
        unit = "kg"

    elif choice == "3":
        result = value * 2.20462
        unit = "pounds"

    elif choice == "4":
        result = value * 0.453592
        unit = "kg"

    elif choice == "5":
        result = value * 1000
        unit = "mg"

    elif choice == "6":
        result = value / 1000
        unit = "grams"

    else:
        print("Invalid choice.")
        return

    print("\nConverted Value:", round(result, 4), unit)


# ------------------------------------------------------------
# TEMPERATURE CONVERTER
# ------------------------------------------------------------

def temperature_converter():

    print("\n" + "-" * 65)
    print("                  TEMPERATURE CONVERTER")
    print("-" * 65)

    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("\nChoose conversion: ")
    value = float(input("Enter temperature: "))

    if choice == "1":
        result = (value * 9 / 5) + 32
        unit = "°F"

    elif choice == "2":
        result = (value - 32) * 5 / 9
        unit = "°C"

    elif choice == "3":
        result = value + 273.15
        unit = "K"

    elif choice == "4":
        result = value - 273.15
        unit = "°C"

    else:
        print("Invalid choice.")
        return

    print("\nConverted Temperature:", round(result, 2), unit)


# ------------------------------------------------------------
# TIME CONVERTER
# ------------------------------------------------------------

def time_converter():

    print("\n" + "-" * 65)
    print("                     TIME CONVERTER")
    print("-" * 65)

    print("1. Hours to Minutes")
    print("2. Minutes to Hours")
    print("3. Minutes to Seconds")
    print("4. Seconds to Minutes")
    print("5. Hours to Seconds")
    print("6. Seconds to Hours")

    choice = input("\nChoose conversion: ")
    value = float(input("Enter value: "))

    if choice == "1":
        result = value * 60
        unit = "minutes"

    elif choice == "2":
        result = value / 60
        unit = "hours"

    elif choice == "3":
        result = value * 60
        unit = "seconds"

    elif choice == "4":
        result = value / 60
        unit = "minutes"

    elif choice == "5":
        result = value * 3600
        unit = "seconds"

    elif choice == "6":
        result = value / 3600
        unit = "hours"

    else:
        print("Invalid choice.")
        return

    print("\nConverted Value:", round(result, 4), unit)


# ------------------------------------------------------------
# SPEED CONVERTER
# ------------------------------------------------------------

def speed_converter():

    print("\n" + "-" * 65)
    print("                    SPEED CONVERTER")
    print("-" * 65)

    print("1. km/h to m/s")
    print("2. m/s to km/h")
    print("3. km/h to mph")
    print("4. mph to km/h")

    choice = input("\nChoose conversion: ")
    value = float(input("Enter speed: "))

    if choice == "1":
        result = value / 3.6
        unit = "m/s"

    elif choice == "2":
        result = value * 3.6
        unit = "km/h"

    elif choice == "3":
        result = value * 0.621371
        unit = "mph"

    elif choice == "4":
        result = value * 1.60934
        unit = "km/h"

    else:
        print("Invalid choice.")
        return

    print("\nConverted Speed:", round(result, 4), unit)


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

while True:

    header()

    print("\n1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Time Conversion")
    print("5. Speed Conversion")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        length_converter()

    elif choice == "2":
        weight_converter()

    elif choice == "3":
        temperature_converter()

    elif choice == "4":
        time_converter()

    elif choice == "5":
        speed_converter()

    elif choice == "6":
        print("\n" + "=" * 75)
        print("       Thank you for using Smart Unit Converter!")
        print("=" * 75)
        break

    else:
        print("\nInvalid choice. Please try again.")

    input("\nPress ENTER to return to the main menu...")