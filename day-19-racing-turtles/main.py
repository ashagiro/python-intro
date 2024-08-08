from turtle import Turtle, Screen
from random import randint

bet_is_on = False
all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
position_y = -110
screen = Screen()
screen.setup(width = 500, height = 400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
if user_bet:
    bet_is_on = True 

for color in colors:
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-220,position_y)
    position_y += 40
    all_turtles.append(new_turtle)

while bet_is_on:
    for turtle in all_turtles:
        distance = randint(1, 10)
        turtle.forward(distance)




screen.exitonclick()