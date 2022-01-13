#exercise 1.2 - Guess the secret number

secret = 3

guess = int(input("Type your guess: "))

if guess == secret:
    print("Amazing! You guessed the secret number!")
else:
    print("Not right! Please try again")