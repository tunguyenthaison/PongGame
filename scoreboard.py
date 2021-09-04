from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")
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

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_LEFT = 0
        self.score_RIGHT = 0
        self.goto(0, HEIGHT//2 - 1.3 * SIZE)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score_LEFT} vs {self.score_RIGHT}", False, align=ALIGNMENT, font=FONT)

    def add_score_LEFT(self):
        self.score_LEFT += 1
        self.update_score()

    def add_score_RIGHT(self):
        self.score_RIGHT += 1
        self.update_score()

    def game_over_LEFT(self):
        self.goto(0, 0)
        self.write("GAME OVER, PLAYER LEFT WIN!", False, align=ALIGNMENT, font=FONT)

    def game_over_RIGHT(self):
        self.goto(0, 0)
        self.write("GAME OVER, PLAYER RIGHT WIN!", False, align=ALIGNMENT, font=FONT)