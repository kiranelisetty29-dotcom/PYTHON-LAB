
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        marks = input("Enter marks: ")

        with open("students.txt", "a") as file:
            file.write(name + "," + roll + "," + marks + "\n")

        print("Student added successfully!")

    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                print("\nStudent Details:")
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No student records found!")

    elif choice == "3":
        print("Exiting program!")
        break

    else:
        print("Invalid choice!")
