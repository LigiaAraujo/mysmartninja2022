#exercise 1.1 - The mood checker

mood = input("Tell me how you feel today: ")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("What would make you feel better?")
elif mood == "excited":
    print("Loving your energy! You go!")
elif mood == "relaxed":
    print("What an amazing feeling!")
else:
    print("I don't recognize this mood")