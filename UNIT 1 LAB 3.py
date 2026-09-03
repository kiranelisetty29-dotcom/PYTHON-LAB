# ============================================================
# LAB EXERCISE 3
# SIMPLE CALCULATOR AND AREA CALCULATION
# ============================================================

import math

# ------------------------------------------------------------
# FUNCTION: DISPLAY HEADER
# ------------------------------------------------------------

def display_header():
    print("\n" + "=" * 70)
    print("             SMART CALCULATOR & AREA TOOL")
    print("=" * 70)


# ------------------------------------------------------------
# BASIC CALCULATOR
# ------------------------------------------------------------

def basic_calculator():

    print("\n" + "-" * 60)
    print("                 BASIC CALCULATOR")
    print("-" * 60)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modulus")
    print("7. Power")

    choice = input("\nEnter your choice: ")

    first = float(input("Enter first number : "))
    second = float(input("Enter second number: "))

    if choice == "1":
        result = first + second
        symbol = "+"

    elif choice == "2":
        result = first - second
        symbol = "-"

    elif choice == "3":
        result = first * second
        symbol = "*"

    elif choice == "4":
        if second == 0:
            print("Error: Division by zero is not allowed.")
            return

        result = first / second
        symbol = "/"

    elif choice == "5":
        if second == 0:
            print("Error: Division by zero is not allowed.")
            return

        result = first // second
        symbol = "//"

    elif choice == "6":
        if second == 0:
            print("Error: Division by zero is not allowed.")
            return

        result = first % second
        symbol = "%"

    elif choice == "7":
        result = first ** second
        symbol = "**"

    else:
        print("Invalid choice.")
        return

    print("\nCalculation:")
    print(first, symbol, second, "=", result)


# ------------------------------------------------------------
# CIRCLE AREA
# ------------------------------------------------------------

def circle_area():

    print("\n" + "-" * 60)
    print("                     CIRCLE")
    print("-" * 60)

    radius = float(input("Enter radius: "))

    if radius < 0:
        print("Radius cannot be negative.")
        return

    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius

    print("Radius          :", radius)
    print("Area            :", round(area, 2))
    print("Circumference   :", round(circumference, 2))


# ------------------------------------------------------------
# RECTANGLE AREA
# ------------------------------------------------------------

def rectangle_area():

    print("\n" + "-" * 60)
    print("                   RECTANGLE")
    print("-" * 60)

    length = float(input("Enter length : "))
    width = float(input("Enter width  : "))

    area = length * width
    perimeter = 2 * (length + width)

    print("Length          :", length)
    print("Width           :", width)
    print("Area            :", round(area, 2))
    print("Perimeter       :", round(perimeter, 2))


# ------------------------------------------------------------
# TRIANGLE AREA
# ------------------------------------------------------------

def triangle_area():

    print("\n" + "-" * 60)
    print("                    TRIANGLE")
    print("-" * 60)

    base = float(input("Enter base   : "))
    height = float(input("Enter height : "))

    area = 0.5 * base * height

    print("Base            :", base)
    print("Height          :", height)
    print("Area            :", round(area, 2))


# ------------------------------------------------------------
# SQUARE AREA
# ------------------------------------------------------------

def square_area():

    print("\n" + "-" * 60)
    print("                     SQUARE")
    print("-" * 60)

    side = float(input("Enter side: "))

    area = side * side
    perimeter = 4 * side

    print("Side            :", side)
    print("Area            :", round(area, 2))
    print("Perimeter       :", round(perimeter, 2))


# ------------------------------------------------------------
# CYLINDER CALCULATION
# ------------------------------------------------------------

def cylinder_calculation():

    print("\n" + "-" * 60)
    print("                    CYLINDER")
    print("-" * 60)

    radius = float(input("Enter radius : "))
    height = float(input("Enter height : "))

    base_area = math.pi * radius * radius
    volume = base_area * height
    curved_surface_area = 2 * math.pi * radius * height
    total_surface_area = (
        2 * math.pi * radius * (radius + height)
    )

    print("Base Area               :", round(base_area, 2))
    print("Volume                  :", round(volume, 2))
    print("Curved Surface Area     :", round(curved_surface_area, 2))
    print("Total Surface Area      :", round(total_surface_area, 2))


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------

while True:

    display_header()

    print("\nMAIN MENU")
    print("-" * 70)

    print("1. Basic Calculator")
    print("2. Circle Area")
    print("3. Rectangle Area")
    print("4. Triangle Area")
    print("5. Square Area")
    print("6. Cylinder Calculation")
    print("7. Exit")

    print("-" * 70)

    choice = input("Enter your choice: ")

    if choice == "1":
        basic_calculator()

    elif choice == "2":
        circle_area()

    elif choice == "3":
        rectangle_area()

    elif choice == "4":
        triangle_area()

    elif choice == "5":
        square_area()

    elif choice == "6":
        cylinder_calculation()

    elif choice == "7":
        print("\nThank you for using Smart Calculator!")
        print("Program terminated successfully.")
        break

    else:
        print("\nInvalid choice!")
        print("Please select a number from 1 to 7.")

    input("\nPress ENTER to continue...")