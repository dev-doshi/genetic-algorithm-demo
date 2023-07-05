import pygame
import random
import math

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and icon
pygame.display.set_caption("Maze Solver")

# The entity class
class Entity:
    def __init__(self, x, y, color, fitness=0, active=True, steps=[]):
        self.x = x
        self.y = y
        self.color = color
        self.fitness = fitness
        self.active = active
        self.steps = steps

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 19, 19))

    def calculateFitness(self, touchedGoal, touchedWall):
        # Give bonus depending on how many steps it took to reach the goal
        # Give bonus for getting more close to the goal
        # Give penalty depending on how early it touched the wall
        # Give minus points for every step

    def move(self, dx, dy):
        if self.active:
            self.calculateFitness(False, False)
            # Check if the entity is not going out to the wall
            if not (
                    self.x + dx < 0 or self.x + dx > SCREEN_WIDTH - 20 or self.y + dy < 0 or self.y + dy > SCREEN_HEIGHT - 20 or (
                    self.x + dx > SCREEN_WIDTH / 2 - 20 and self.y + dy > 100 and self.x < SCREEN_WIDTH / 2)):
                # Check if it touches a wall
                if self.x + dx < 10 or self.x + dx > SCREEN_WIDTH - 60 or self.y + dy < 10 or self.y + dy > SCREEN_HEIGHT - 30:
                    self.active = False
                    self.calculateFitness(False, True)
                elif self.x + dx > SCREEN_WIDTH - 60 and self.y + dy > SCREEN_HEIGHT - 60:
                    self.active = False
                    self.calculateFitness(True, False)
                else:
                    self.x += dx
                    self.y += dy
                    self.steps.append((dx, dy))
            else:
                self.active = False
                self.calculateFitness(False, True)

entities = []
# Place entities on start position (bottom left)
for i in range(10000):
    entities.append(Entity(60, SCREEN_HEIGHT - 60, (0, 0, 255)))

# Main loop
while True:
    screen.fill((255, 255, 255))

    # Line on the top
    pygame.draw.line(screen, (0, 0, 0), (10, 10), (SCREEN_WIDTH-10, 10), 5)
    #Line on the bottom
    pygame.draw.line(screen, (0, 0, 0), (10, SCREEN_HEIGHT-10), (SCREEN_WIDTH-10, SCREEN_HEIGHT-10), 5)
    #Line on the left
    pygame.draw.line(screen, (0, 0, 0), (10, 10), (10, SCREEN_HEIGHT-10), 5)
    #Line on the right
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH-10, 10), (SCREEN_WIDTH-10, SCREEN_HEIGHT-10), 5)
    # Vertical line in the middle
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH / 2, 100), (SCREEN_WIDTH / 2, SCREEN_HEIGHT-10), 5)
    # Goal on the bottom right
    pygame.draw.rect(screen, (0, 255, 0), (SCREEN_WIDTH - 60, SCREEN_HEIGHT - 60, 19, 19))

    # Place the entities
    for entity in entities:
        entity.draw()

    # Set colors for entities based on their active state
    for entity in entities:
        print(entity.fitness)
        entity.color = (0,  entity.fitness/100000, 0)

    # Move every entity randomly
    for entity in entities:
        xMove = random.randint(-10, 10)
        yMove = random.randint(-10, 10)

        entity.move(xMove, yMove)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the screen
    pygame.display.flip()