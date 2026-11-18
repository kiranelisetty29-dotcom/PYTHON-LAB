
sales = {}

while True:
    print("\n--- Sales Data Analyzer ---")
    print("1. Add Product Sales")
    print("2. View Sales")
    print("3. Calculate Total Sales")
    print("4. Find Highest Sale")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        amount = float(input("Enter sales amount: "))

        sales[name] = sales.get(name, 0) + amount
        print("Sales added successfully!")

    elif choice == "2":
        print("\nSales Report:")

        for name, amount in sales.items():
            print(name, ":", amount)

    elif choice == "3":
        total = sum(sales.values())
        print("Total Sales:", total)

    elif choice == "4":
        if sales:
            product = max(sales, key=sales.get)
            print("Highest Selling Product:", product)
            print("Sales Amount:", sales[product])
        else:
            print("No sales data available!")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
