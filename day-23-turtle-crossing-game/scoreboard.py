from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.pu()
        self.hideturtle()
        self.goto(POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def update_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align = "center", font = FONT)
