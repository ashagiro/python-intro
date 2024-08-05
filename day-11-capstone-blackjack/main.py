from art import logo
import random
import os

def distribute_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list):
    # func to calculate score and return value
    if sum(list) == 21:
        return 0
    if 11 in list and sum(list) > 21:  
        list.remove(11)
        list.append(1)
        return sum(list)  
    return sum(list)

def get_winner(user, computer):
    score_user = calculate_score(user)
    score_computer = calculate_score(computer)
    print(f"Your final cards: {user}, final score: {score_user}")
    print(f"Computers final cards: {computer}, final score: {score_computer}")
    if score_computer == 0 and score_user == 0:
        return "Computer has blackjack!\nYou lose!"
    elif score_computer == 0:
        return "You lose :( 1"
    elif score_user == 0:
        return "You win!"
    elif score_computer > score_user and score_computer < 21:
        return "You lose :( 2"
    elif score_user > 21:
        return "You lose :( 3"
    elif score_computer > 21  or (score_computer < score_user and score_user < 21):
        return "You win!"
    elif score_user == score_computer:
        return "It is a draw"
    
def blackjack():
    print(logo)
    user = []
    computer = []
    user.append(distribute_card())
    user.append(distribute_card())
    computer.append(distribute_card())
    computer.append(distribute_card())
    if (calculate_score(user) or calculate_score(computer)) == 0:
        print(get_winner(user, computer))
        return
    print(f"Your cards: {user}, current score: {sum(user)}")
    print(f"Computer's first card: {computer[0]}")

    get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while get_card == 'y':
        user.append(distribute_card())
        if calculate_score(user) > 20:
            print(get_winner(user, computer))
            break
        print(f"Your cards: {user}, current score: {sum(user)}")
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if get_card == 'n':
        if sum(computer) < 17:
            computer.append(distribute_card())
        print(get_winner(user, computer))

    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if answer == 'n':
        return
    elif answer == 'y':
        os.system('cls||clear')
        blackjack()
# 

blackjack()