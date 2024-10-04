import random

random_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10. Try to guess it!")

while True:

    user_guess = input("Enter your guess: ")

    try:
        guess = int(user_guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number!")
        break
