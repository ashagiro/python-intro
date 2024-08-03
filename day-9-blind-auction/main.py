import art
import os

play_again = True
bidders = {}
print(art.logo)
print("Welcome to the secret auction program.")
while play_again:
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    bidders[name] = bid
    answer = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if not answer == "yes":
        play_again = False
    else:
        os.system('cls||clear')
bid_list = []
name_list =[]
for person in bidders:
   bid_list.append(int(''.join(filter(str.isdigit, bidders[person]))))
   name_list.append(person) 
winner = name_list[bid_list.index(max(bid_list))]
print(f"The winner is {winner} with a bid of ${max(bid_list)}")