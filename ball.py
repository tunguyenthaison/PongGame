from turtle import Turtle
import random

SIZE = 20
MOVE_DISTANCE = 8
WIDTH = 1000
HEIGHT = 600
LEFT_CENTER = - WIDTH // 2 + 3 * SIZE
RIGHT_CENTER = WIDTH // 2 - 3 * SIZE

TOP_PADDING = HEIGHT // 2 - 2 * SIZE
BOTTOM_PADDING = -HEIGHT // 2 + 2 * SIZE

LEFT_STARTING_POSITIONS = []
RIGHT_STARTING_POSITIONS = []
LENGTH_PADDLE = 9
MID = (LENGTH_PADDLE - 1) // 2

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.penup()
        self.direction()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")

    def direction(self):
        initial_direction = random.choice([45, 135, 225, 315])
        self.setheading(initial_direction)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reflect_wall(self):
        if self.heading() == 45:
            self.setheading(315)
        elif self.heading() == 315:
            self.setheading(45)
        elif self.heading() == 135:
            self.setheading(225)
        elif self.heading() == 225:
            self.setheading(135)

    def reflect_paddle(self):
        if self.heading() == 45:
            self.setheading(135)
        elif self.heading() == 135:
            self.setheading(45)
        elif self.heading() == 315:
            self.setheading(225)
        elif self.heading() == 225:
            self.setheading(315)


