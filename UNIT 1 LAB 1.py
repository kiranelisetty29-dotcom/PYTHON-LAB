# ============================================================
# LAB EXERCISE 1
# BASIC PYTHON PROGRAM
# Student Profile and Result Analyzer
# ============================================================

print("=" * 65)
print("             STUDENT PROFILE & RESULT ANALYZER")
print("=" * 65)

# Taking student details
name = input("Enter Student Name       : ")
usn = input("Enter Student ID/USN     : ")
course = input("Enter Course Name        : ")
semester = input("Enter Semester           : ")

print("\n" + "-" * 65)
print("ENTER MARKS")
print("-" * 65)

# Taking marks
python = float(input("Enter Python Mark        : "))
maths = float(input("Enter Mathematics Mark   : "))
physics = float(input("Enter Physics Mark       : "))
english = float(input("Enter English Mark       : "))
computer = float(input("Enter Computer Mark      : "))

# Total calculation
total = python + maths + physics + english + computer

# Average calculation
average = total / 5

# Percentage calculation
percentage = (total / 500) * 100

# Grade calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B+"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Pass/Fail
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Displaying result
print("\n" + "=" * 65)
print("                    STUDENT RESULT")
print("=" * 65)

print("Student Name       :", name)
print("Student ID         :", usn)
print("Course             :", course)
print("Semester           :", semester)

print("-" * 65)

print("Python             :", python)
print("Mathematics        :", maths)
print("Physics            :", physics)
print("English            :", english)
print("Computer           :", computer)

print("-" * 65)

print("Total Marks        :", total, "/ 500")
print("Average            :", round(average, 2))
print("Percentage         :", round(percentage, 2), "%")
print("Grade              :", grade)
print("Result             :", result)

print("=" * 65)
print("             THANK YOU FOR USING THE PROGRAM")
print("=" * 65)