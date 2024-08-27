from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 70, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.goto(0, 220)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"{self.l_score}   :   {self.r_score}", False, align = ALIGNMENT, font = FONT)


    def increase_score_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
