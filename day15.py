secret_number = 7

print("Guess the Secret Number")

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! You found the secret number.")
        break

    elif guess < secret_number:
        print("Try a bigger number.")

    else:
        print("Try a smaller number.")