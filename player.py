from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(
        self,
    ) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def moveup(self):
        self.setheading(90)
        self.forward(15)

    def movedown(self):
        self.setheading(270)
        self.forward(10)

    def next_round(self):
        self.goto(0, -280)
