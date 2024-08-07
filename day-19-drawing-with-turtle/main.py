from turtle import Screen, Turtle


tim = Turtle()
screen = Screen()
tim.speed("fastest")

# Requirements: W = Forward, s = backward, a = turn counterclockwise, d = turn clockwise, c = clear

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()

screen.listen()
screen.onkey(forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(backward, "s")
screen.onkey(clear, "c")

screen.exitonclick()