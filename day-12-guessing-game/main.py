from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
number = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Not a valid entry. You lose!")
    exit()
for i in range(0, attempts):
    # guess = int(input("Make a guess: "))
    print(f"You have {attempts-i} attempts remaining to guess the number.")
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Not a valid entry. You lose!")
        exit()
    if guess == number:
        print(f"You won! The asnwer was {number}")
        exit()
    elif guess > number:
        print("Too high.")
    elif guess < number:
        print("Too low.")
print("You have run out of guesses, you lose.")

# A game where you need to win the game by finding the right number
# Easy mode 10 attempts, and Hard mode 5 attempts