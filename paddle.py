from turtle import Turtle

SIZE = 20
MOVE_DISTANCE = 20
WIDTH = 1000
HEIGHT = 600
LEFT_CENTER = - WIDTH // 2 + 3 * SIZE
RIGHT_CENTER = WIDTH // 2 - 3 * SIZE

TOP_PADDING = HEIGHT//2 - 2*SIZE
BOTTOM_PADDING = -HEIGHT//2 + 2*SIZE

LEFT_STARTING_POSITIONS = []
RIGHT_STARTING_POSITIONS = []
LENGTH_PADDLE = 9
MID = (LENGTH_PADDLE - 1) // 2

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

for _ in range(0, LENGTH_PADDLE):
    LEFT_STARTING_POSITIONS.append((LEFT_CENTER, (-MID + _) * SIZE))
    RIGHT_STARTING_POSITIONS.append((RIGHT_CENTER, (-MID + _) * SIZE))


class Paddle:
    def __init__(self, direction) -> object:
        self.segments = []
        self.create_paddle(direction)
        self.center = self.segments[MID + 1]
        self.top = self.segments[-1]
        self.bottom = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_paddle(self, direction):
        if direction == "left":
            for position in LEFT_STARTING_POSITIONS:
                self.add_segment(position)
        elif direction == "right":
            for position in RIGHT_STARTING_POSITIONS:
                self.add_segment(position)

    def move(self):
        for x in self.segments:
            x.forward(20)

    def up(self):
        if self.top.ycor() <= TOP_PADDING:
            self.top.setheading(UP)
            for i in range(0, LENGTH_PADDLE - 1):
                current_position = self.segments[i + 1].position()
                self.segments[i].goto(current_position)
            self.top.forward(MOVE_DISTANCE)

    def down(self):
        if self.bottom.ycor() >= BOTTOM_PADDING:
            self.bottom.setheading(DOWN)
            for i in range(LENGTH_PADDLE - 1, 0, -1):
                current_position = self.segments[i - 1].position()
                self.segments[i].goto(current_position)
            self.bottom.forward(MOVE_DISTANCE)
