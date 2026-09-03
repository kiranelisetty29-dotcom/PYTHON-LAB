# ============================================================
# LAB EXERCISE 2
# VARIABLES, OPERATORS AND INPUT/OUTPUT
# Personal Finance Calculator
# ============================================================

print("=" * 70)
print("                 PERSONAL FINANCE CALCULATOR")
print("=" * 70)

# ------------------------------------------------------------
# USER INPUT
# ------------------------------------------------------------

name = input("Enter your name              : ")

income = float(input("Enter your monthly income    : ₹"))
rent = float(input("Enter house rent             : ₹"))
food = float(input("Enter food expenses          : ₹"))
travel = float(input("Enter travel expenses        : ₹"))
education = float(input("Enter education expenses     : ₹"))
other = float(input("Enter other expenses         : ₹"))

# ------------------------------------------------------------
# ARITHMETIC OPERATORS
# ------------------------------------------------------------

total_expenses = rent + food + travel + education + other

remaining_money = income - total_expenses

average_expense = total_expenses / 5

# ------------------------------------------------------------
# PERCENTAGE CALCULATION
# ------------------------------------------------------------

if income > 0:
    expense_percentage = (total_expenses / income) * 100
    savings_percentage = (remaining_money / income) * 100
else:
    expense_percentage = 0
    savings_percentage = 0

# ------------------------------------------------------------
# DISPLAY CALCULATIONS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("                    FINANCIAL SUMMARY")
print("=" * 70)

print("Name                    :", name)
print("Monthly Income          : ₹", round(income, 2))

print("-" * 70)

print("Rent                    : ₹", round(rent, 2))
print("Food                    : ₹", round(food, 2))
print("Travel                  : ₹", round(travel, 2))
print("Education               : ₹", round(education, 2))
print("Other                   : ₹", round(other, 2))

print("-" * 70)

print("Total Expenses          : ₹", round(total_expenses, 2))
print("Remaining Money         : ₹", round(remaining_money, 2))
print("Average Expense         : ₹", round(average_expense, 2))
print("Expense Percentage      :", round(expense_percentage, 2), "%")
print("Savings Percentage      :", round(savings_percentage, 2), "%")

# ------------------------------------------------------------
# COMPARISON OPERATORS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("                    FINANCIAL STATUS")
print("=" * 70)

if remaining_money > 0:
    print("Status                  : You have money remaining.")

elif remaining_money == 0:
    print("Status                  : Your income and expenses are equal.")

else:
    print("Status                  : Your expenses are higher than income.")

# ------------------------------------------------------------
# LOGICAL OPERATORS
# ------------------------------------------------------------

if income > 0 and savings_percentage >= 20:
    print("Suggestion              : Excellent savings habit!")

elif income > 0 and savings_percentage > 0:
    print("Suggestion              : Try to increase your savings.")

else:
    print("Suggestion              : Review your expenses.")

# ------------------------------------------------------------
# ADDITIONAL OPERATOR DEMONSTRATION
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("                 OPERATOR DEMONSTRATION")
print("=" * 70)

a = 20
b = 7

print("Value A                 :", a)
print("Value B                 :", b)

print("Addition (A + B)        :", a + b)
print("Subtraction (A - B)     :", a - b)
print("Multiplication (A * B)  :", a * b)
print("Division (A / B)        :", a / b)
print("Floor Division (A // B) :", a // b)
print("Modulus (A % B)         :", a % b)
print("Power (A ** B)          :", a ** b)

print("\nComparison:")
print("A > B                   :", a > b)
print("A < B                   :", a < b)
print("A == B                  :", a == b)
print("A != B                  :", a != b)

print("=" * 70)
print("                     PROGRAM COMPLETED")
print("=" * 70)