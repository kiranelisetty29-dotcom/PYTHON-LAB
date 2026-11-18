
import csv

while True:
    print("\n1. Add Employee")
    print("2. View Payroll")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter employee name: ")
        salary = float(input("Enter basic salary: "))
        bonus = float(input("Enter bonus: "))

        total = salary + bonus

        with open("payroll.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, salary, bonus, total])

        print("Employee added successfully!")

    elif choice == "2":
        try:
            with open("payroll.csv", "r") as file:
                reader = csv.reader(file)

                print("\nName | Salary | Bonus | Total")

                for row in reader:
                    print(" | ".join(row))

        except FileNotFoundError:
            print("Payroll file not found!")

    elif choice == "3":
        print("Exiting Payroll System!")
        break

    else:
        print("Invalid choice!")
