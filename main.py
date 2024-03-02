import time 
import random
import pygame
import sys
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize pygame
pygame.init()

# Set up screen dimensions
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Function to display text on screen
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Main menu loop
def main_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Main Menu", WHITE, screen_width // 2, screen_height // 4)
        draw_text("1. Start Game", GREEN, screen_width // 2, screen_height // 2)
        draw_text("2. Options", WHITE, screen_width // 2, screen_height // 2 + 50)
        draw_text("3. Quit", WHITE, screen_width // 2, screen_height // 2 + 100)
        
        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Start game
                    return
                elif event.key == pygame.K_2:
                    # Options (to be implemented)
                    pass
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

# Main game code
def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.bgcolor("black")

    screen.listen()
    player = Player()
    scoreboard = Scoreboard()
    screen.onkeypress(player.moveup, "w")
    screen.onkeypress(player.movedown, "s")

    scoreboard.update_score()

    game_is_on = True
    cars = []
    while game_is_on:
        time.sleep(scoreboard.difficulty)
        if random.randint(1, 3) == 1:
            car = CarManager()
            cars.append(car)
        for car in cars:
            car.move()
            if player.distance(car) < 20:
                game_is_on = False
        if player.ycor() >= 285:
            player.next_round()
            scoreboard.increase_difficulty()
            scoreboard.update_score()

        screen.update()

    screen.exitonclick()

# Run the main menu
main_menu()

# Once the user selects "Start Game" from the main menu, the main function will be called
main()
