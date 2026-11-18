
import json

logs = []

while True:
    print("\n--- JSON Log Analyzer ---")
    print("1. Add Log")
    print("2. View Logs")
    print("3. Analyze Logs")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        message = input("Enter log message: ")
        level = input("Enter type (INFO/ERROR/WARNING): ").upper()

        log = {
            "message": message,
            "level": level
        }

        logs.append(log)

        with open("logs.json", "w") as file:
            json.dump(logs, file, indent=4)

        print("Log saved successfully!")

    elif choice == "2":
        try:
            with open("logs.json", "r") as file:
                logs = json.load(file)

            for log in logs:
                print(log)

        except FileNotFoundError:
            print("No log file found!")

    elif choice == "3":
        try:
            with open("logs.json", "r") as file:
                logs = json.load(file)

            info = 0
            error = 0
            warning = 0

            for log in logs:
                if log["level"] == "INFO":
                    info += 1
                elif log["level"] == "ERROR":
                    error += 1
                elif log["level"] == "WARNING":
                    warning += 1

            print("\n--- Log Analysis ---")
            print("INFO:", info)
            print("ERROR:", error)
            print("WARNING:", warning)
            print("Total Logs:", len(logs))

        except FileNotFoundError:
            print("No log file found!")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
