import art
from game_data import data
import random
import os 


def random_data():
    index = random.randint(0, 49)
    return data[index]
# list_used = []

def check_answer(num1, num2, guess):
    """ Functions takes two numbers and a guess A or B and returns if the guess was correct."""
    if num1 > num2:
        return guess == "a"
    else:
        return guess == "b"

A = random_data()
# list_used.append(A)
B = random_data()
# list_used.append(B)

while A == B:
    B = random_data()
    # list_used.pop()
    # list_used.append(B)

play = True
score = 0
os.system('cls||clear')
print(art.logo)

while play:
    B = random_data()
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
    print(art.vs)
    print(f"Against B: {B['name']}, {B['description']}, from {B['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    if check_answer(A['follower_count'], B['follower_count'], answer):
        os.system('cls||clear')
        score+=1
        print(art.logo)
        print(f"You're right! Current score: {score}.")
        A = B
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        play = False
