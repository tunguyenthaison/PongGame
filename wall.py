from turtle import Turtle

SIZE = 20
MOVE_DISTANCE = 20
WIDTH = 1000
HEIGHT = 600
LEFT_CENTER = - WIDTH // 2 + 3 * SIZE
RIGHT_CENTER = WIDTH // 2 - 3 * SIZE

TOP_PADDING = HEIGHT // 2 - 2 * SIZE
BOTTOM_PADDING = -HEIGHT // 2 + 2 * SIZE

LENGTH_PADDLE = 9
MID = (LENGTH_PADDLE - 1) // 2


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []

    def add_segment(self, x, y):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.goto(x, y)
        self.segments.append(new_segment)

    def create(self, pos):
        if pos == "top":
            for i in range(0, 45):
                self.add_segment(LEFT_CENTER + i * SIZE, TOP_PADDING)

        elif pos == "bottom":
            for i in range(0, 45):
                self.add_segment(LEFT_CENTER + i * SIZE, BOTTOM_PADDING)

