import pygame
import random
import math
import time

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and icon
pygame.display.set_caption("Maze Solver")

last_time = time.time()
deltatime = 0
time_since_last_generation = 0

class Labyrinth:
    def draw(self):
        # Line on the top
        pygame.draw.line(screen, (0, 0, 0), (10, 10), (SCREEN_WIDTH - 10, 10), 20)
        # Line on the bottom
        pygame.draw.line(screen, (0, 0, 0), (10, SCREEN_HEIGHT - 10), (SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10), 20)
        # Line on the left
        pygame.draw.line(screen, (0, 0, 0), (10, 10), (10, SCREEN_HEIGHT - 10), 20)
        # Line on the right
        pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH - 10, 10), (SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10), 20)
        # Vertical line in the middle
        pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH / 2, 100), (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10), 20)
        # Goal on the bottom right
        pygame.draw.rect(screen, (0, 255, 0), (SCREEN_WIDTH - 60, SCREEN_HEIGHT - 60, 19, 19))

    def willCollide(self, x, y, dx, dy):
        if x + dx < 0 or x + dx > SCREEN_WIDTH - 20 or y + dy < 0 or y + dy > SCREEN_HEIGHT - 20 or (
                x + dx > SCREEN_WIDTH / 2 - 20 and y + dy > 100 and x + dx < SCREEN_WIDTH / 2 + 20):
            return True
        else:
            return False

# The entity class
class Entity:
    def __init__(self, x, y, color, fitness=0, active=True, steps=None, wall_touches=None):
        if wall_touches is None:
            wall_touches = []
        if steps is None:
            steps = []
        else:
            for step in steps:
                x += step[0]
                y += step[1]

        self.x = x
        self.y = y
        self.color = color
        self.fitness = fitness
        self.active = active
        self.steps = steps
        self.wall_touches = wall_touches

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 19, 19))

    def calculateFitness(self):
        STEPCOST = 0.1
        DISTANCECOST = 0.2
        WALLCOST = 0.4

        distanceToGoal = math.sqrt((SCREEN_WIDTH - 60 - self.x) ** 2 + (SCREEN_HEIGHT - 60 - self.y) ** 2)

        # Get the distance to the goal when the entity touched a wall
        for touch in self.wall_touches:
            self.fitness += math.sqrt((SCREEN_WIDTH - 60 - (self.x + touch[0])) ** 2 + (SCREEN_HEIGHT - 60 - (self.y + touch[1])) ** 2)

        print(self.fitness)

    def move(self, dx, dy):
        if self.active:
            # Check if the entity is not going out to the wall
            labyrinth = Labyrinth()
            if not labyrinth.willCollide(self.x, self.y, dx, dy):
                self.x += dx
                self.y += dy
                self.steps.append((dx, dy))
            else:
                self.wall_touches.append((dx, dy))
                print(len(self.wall_touches))
        else:
            self.calculateFitness()

def updateScreen(entities):
    global deltatime
    global last_time
    global time_since_last_generation

    deltatime = time.time() - last_time
    last_time = time.time()
    time_since_last_generation += deltatime

    screen.fill((255, 255, 255))

    # Draw the labyrinth
    labyrinth = Labyrinth()
    labyrinth.draw()

    # Place the entities
    for entity in entities:
        entity.draw()

    # Set colors for entities based on their active state
    for entity in entities:
        if entity.fitness >= 0:
            entity.color = (0, entity.fitness / 100000, 0)
        else:
            entity.color = (0, 0, 0)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Update the screen
    pygame.display.flip()

entities = []

# Create the entities on the bottom left
for i in range(100):
    entities.append(Entity(SCREEN_WIDTH/4, SCREEN_HEIGHT-SCREEN_HEIGHT/4, (0, 0, 0)))

def main():
    global time_since_last_generation

    while True:
        while time_since_last_generation < 3:
            updateScreen(entities)

            # Move every entity randomly
            for entity in entities:
                xMove = random.choice([-1, 1])
                yMove = random.choice([-1, 1])

                entity.move(xMove * 5, yMove * 5)


if __name__ == "__main__":
    main()
