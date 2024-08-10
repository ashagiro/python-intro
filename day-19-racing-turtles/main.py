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
        if turtle.xcor() > 230:
            bet_is_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
        distance = randint(1, 10)
        turtle.forward(distance)

screen.exitonclick()