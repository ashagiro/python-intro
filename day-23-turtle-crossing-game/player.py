from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("slate blue")
        self.pu()
        self.setheading(90)
        self.go_to_start()

    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        return self.ycor() > FINISH_LINE_Y

