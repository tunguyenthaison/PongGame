from turtle import Screen, Turtle

SIZE = 20
MOVE_DISTANCE = 20
WIDTH = 1000
HEIGHT = 600
LEFT_CENTER = - WIDTH // 2 + 3 * SIZE
RIGHT_CENTER = WIDTH // 2 - 3 * SIZE

TOP_PADDING = HEIGHT//2 - 2*SIZE
BOTTOM_PADDING = -HEIGHT//2 + 2*SIZE

STARTING_POSITIONS = []
LENGTH = 27
MID = (LENGTH - 1) // 2

for _ in range(0, LENGTH):
    STARTING_POSITIONS.append((0, (-MID + _) * SIZE))


class Separation:
    def __init__(self) -> object:
        self.segments = []
        self.create_separation()
        self.center = self.segments[MID + 1]
        self.top = self.segments[-1]
        self.bottom = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.shapesize(stretch_wid=0.05)
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_separation(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

