import turtle as t
import random

tim = t.Turtle()
tim.shape("circle")
t.colormode(255)

colors = ["dark turquoise", "aquamarine", "deep sky blue", "lime", "tomato", "indian red", "medium purple", "violet", "medium violet red", "green yellow"]
screen = t.Screen()
def random_color():
    num1 = (random.randint(0, 255))
    num2 = (random.randint(0, 255))
    num3 = (random.randint(0, 255))
    return (num1, num2, num3)


# PROJECT #1
# Let's turtle draw different shapes from a triangle to a decagon.
# def draw_shapes(sides):
#     for _ in range(sides):
#         tim.forward(100)
#         tim.left(360/sides)
# for sides_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shapes(sides_n)   


# PROJECT #2
# Let's turtle take random steps in random colors
# tim.width(10)
# tim.speed(0)
# def choose_side():
#     sides =[0, 90, 180, 270]
#     tim.setheading(random.choice(sides))
# for repeats in range(200):
#     choose_side()
#     tim.pencolor(random_color())
#     tim.forward(30)


# PROJECT #3
# Spirograph. Draws 100 circles with the diameter of 100px
# tim.width(2)
# tim.speed(0)
# def spirograph(num):
#     angle = 0
#     for _ in range(0, int(360/num)+1):
#         tim.pencolor(random_color())
#         tim.circle(100)
#         tim.setheading(angle)
#         angle+=num
# spirograph(15)

screen.exitonclick()