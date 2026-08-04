import random

name = input("Enter your name: ")

lucky_number = random.randint(1, 100)

print("\nHello,", name)
print("Your lucky number today is:", lucky_number)

if lucky_number >= 80:
    print("Excellent! Today looks very lucky for you.")
elif lucky_number >= 50:
    print("Good luck! Something nice might happen today.")
else:
    print("Stay positive! Tomorrow may be your lucky day.")