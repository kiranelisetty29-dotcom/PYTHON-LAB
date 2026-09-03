import random

print(" NUMBER HUNT GAME")
print("-" * 30)

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess == secret:
        print(f" Correct! You found it in {attempts} attempts.")
        break
    elif guess < secret:
        print(" Too low! Try higher.")
    else:
        print(" Too high! Try lower.")

print("Game Over! Thanks for playing.")