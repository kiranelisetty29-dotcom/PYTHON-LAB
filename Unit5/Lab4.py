
import csv
import matplotlib.pyplot as plt

sales = []

while True:
    print("\n--- Retail Sales Dashboard ---")
    print("1. Add Sale")
    print("2. View Sales")
    print("3. Show Dashboard")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        amount = float(input("Enter sales amount: "))

        sales.append([product, amount])

        with open("sales.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([product, amount])

        print("Sale added successfully!")

    elif choice == "2":
        try:
            with open("sales.csv", "r") as file:
                reader = csv.reader(file)

                print("\nProduct | Sales")

                for row in reader:
                    print(row[0], "|", row[1])

        except FileNotFoundError:
            print("No sales data found!")

    elif choice == "3":
        try:
            products = []
            amounts = []

            with open("sales.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    products.append(row[0])
                    amounts.append(float(row[1]))

            if products:
                print("Total Sales:", sum(amounts))

                plt.bar(products, amounts)
                plt.xlabel("Products")
                plt.ylabel("Sales Amount")
                plt.title("Retail Sales Dashboard")
                plt.show()
            else:
                print("No sales data available!")

        except FileNotFoundError:
            print("No sales data found!")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
