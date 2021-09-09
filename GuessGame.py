from random import random
from random import randint
import random

random_number = random.randint(0, 10)
guesses = [0]

while True:
    print("I am thinking of a number, try to guess what I am thinking about")
    guess = int(input("Enter the number you are thinking about" + " "))
    if guess == random_number:
        print(f'Congratulations, you have guessed the right number only {len(guesses)} times')
    elif guess != random_number:
        guesses = guesses.append(guess)
    elif guess < random_number:
        print("Your number is lesser than my guess")
    elif guess > random_number:
        print("Your number is more than my guess")

        break
