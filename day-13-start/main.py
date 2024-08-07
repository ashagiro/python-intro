############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 20+1):
    if i == 20:
      print("You got it")
    # range omits last number
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6-1)
# index starts from 0 and count doesnt reach 6, but random includes number 6.
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
  # 1994 was not being included
elif year > 1994-1:
  print("You are a Gen Z.")

# Fix the Errors
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
    # missing identation bug and input is not an int but str. 

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(pages)
print(word_per_page)
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])