from turtle import Turtle, Screen
import random

# Constants for car movement
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20

class CarManager(Turtle):
    CAR_IMAGE = "200w!.gif"  # Change this to match the filename of your picture file
    IMAGE_WIDTH = 0.00001 # Adjust the width of the image
    IMAGE_HEIGHT = 0.00001  # Adjust the height of the image

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")  # Set color to white initially (for invisible turtle)
        
        # Load car image as shape
        screen = Screen()
        screen.register_shape(self.CAR_IMAGE)
        self.shape(self.CAR_IMAGE)

        self.setheading(180)  # Set initial heading to face left
        self.speed("fastest")  # Set speed to fastest for smooth movement

        random_y = random.randint(-230, 230)
        self.goto(320, random_y)  # Start car off-screen to the right

        # Adjust the size of the image
        self.shapesize(stretch_wid=self.IMAGE_HEIGHT / 20, stretch_len=self.IMAGE_WIDTH / 20)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.forward(MOVE_INCREMENT)
