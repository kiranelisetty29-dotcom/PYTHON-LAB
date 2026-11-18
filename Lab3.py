
import random

while True:
    print("\n--- Dice Simulator ---")
    print("1. Roll Dice")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        dice = random.randint(1, 6)
        print("Dice Result:", dice)

    elif choice == "2":
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice!")
