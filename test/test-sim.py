import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Traffic Intersection Simulation")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Traffic light states
class TrafficLight:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 20)

# Create traffic lights
light1 = TrafficLight(350, 250, red)
light2 = TrafficLight(450, 250, green)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update traffic light logic (e.g., change colors based on a timer)
    # ...

    # Draw
    screen.fill(black)
    pygame.draw.rect(screen, white, (300, 200, 200, 100))  # Intersection
    light1.draw()
    light2.draw()
    pygame.display.flip()

pygame.quit()