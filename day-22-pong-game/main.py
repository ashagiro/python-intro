# TODO
# 1. draw a line in the middle
# 2. score 1 and score 2
# 3. player 1 move in keys AWSD and player 2 move on keys up, down, left and right.
# 4. ball move side from side ?? HOW
# 4. detect collision with the ball and increase score, move ball accordingly

from turtle import Screen, time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Epic Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with the wall (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

    # detect no collision with paddle
    if ball.xcor() > 380:
        scoreboard.increase_score_l()
        ball.reset_position()
    elif ball.xcor() < -380:
        scoreboard.increase_score_r()
        ball.reset_position()


screen.exitonclick()