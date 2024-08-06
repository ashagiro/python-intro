# Procedural Programming vs Object Oriented Programming

from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("SlateBlue2")
timmy.forward(100)

# HERE only pen is moving to form a square (use 120 degrees to form a triangle)
forward(100)
# HERE lifting the pen to stop drawing
up()
left(90)
forward(100)
left(90)
# HERE putting pen down to start drawing again
down()
forward(100)
left(90)
forward(100)

# To get the position of the turtle
print(pos())
# Get to the starting position
home()
# Remove all painting from the screen
clearscreen()
color('red')
fillcolor('yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()

# HERE changing the color of the pen and its thickness
color('yellow')
width(5)
my_screen = Screen()
my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Pokemon element", ["Electric", "Water", "Fire"] )
# table.align = "l"
# print(table)