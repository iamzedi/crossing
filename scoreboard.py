from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.difficulty = 0.1
        self.hideturtle()
        self.penup()
        self.goto(-180, 290)
        self.color("white")

    def increase_difficulty(self):
        self.difficulty *= 0.7

    def update_score(self):
        self.clear()  # Clear the previous score
        self.write(f"Score: {self.level}", align="center", font=FONT)
        self.level += 1
