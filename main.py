from turtle import Turtle, Screen
from paddle import *
from ball import *
from separation import *
from wall import *
from scoreboard import *
import time

SIZE = 20
WIDTH = 1000
HEIGHT = 600
TOP_PADDING = HEIGHT // 2 - 2 * SIZE
BOTTOM_PADDING = -HEIGHT // 2 + 2 * SIZE

# TODO. Setting up the screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
separation = Separation()

top_wall = Wall()
top_wall.create("top")
bottom_wall = Wall()
bottom_wall.create("bottom")

left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    # Reflect with wall
    if ball.ycor() >= TOP_PADDING - 15:
        print(f"ycor = {ball.ycor()} and TOP = {TOP_PADDING}")
        ball.reflect_wall()
    elif ball.ycor() <= BOTTOM_PADDING + 15:
        ball.reflect_wall()

    # Reflect with paddles
    if ball.xcor() <= LEFT_CENTER + 15:
        if left_paddle.bottom.ycor() - 10 <= ball.ycor() <= left_paddle.top.ycor() + 10:
            ball.reflect_paddle()
            scoreboard.add_score_LEFT()
        else:
            print("Game over!")
            # scoreboard.game_over_RIGHT()
            game_is_on = False
    elif ball.xcor() >= RIGHT_CENTER - 15:
        if right_paddle.bottom.ycor() - 10 <= ball.ycor() <= right_paddle.top.ycor() + 10:
            ball.reflect_paddle()
            scoreboard.add_score_RIGHT()
        else:
            print("Game over!")
            # scoreboard.game_over_LEFT()
            game_is_on = False

screen.exitonclick()
