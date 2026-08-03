
print("😊 Welcome to the Mood Checker 😊")

name = input("Enter your name: ")
mood = input("How are you feeling today? (happy/sad/angry/excited): ").lower()

print("\nHello,", name)

if mood == "happy":
    print("😄 That's wonderful! Keep smiling.")
elif mood == "sad":
    print("💙 Don't worry. Better days are coming.")
elif mood == "angry":
    print("😌 Take a deep breath and relax.")
elif mood == "excited":
    print("🎉 Awesome! Enjoy your day.")
else:
    print("🤔 Every feeling is valid. Have a great day!")

print("\n✨ Thanks for using the Mood Checker!")