import random

print("=" * 35)
print("        OTP GENERATOR")
print("=" * 35)

name = input("Enter your name: ")

otp = random.randint(100000, 999999)

print(f"\nHello {name}!")
print("Your OTP is:", otp)

entered = int(input("Enter OTP: "))

if entered == otp:
    print("OTP Verified Successfully!")
else:
    print(" Invalid OTP!")