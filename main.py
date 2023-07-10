import pygame
import random
import math
import numpy
from PIL import Image

# Load Image
IMAGEPATH = "main.png"
IMAGE = Image.open(IMAGEPATH)

# Pygame Constants
SCREEN_WIDTH, SCREEN_HEIGHT = IMAGE.size

# Initialize pygame
pygame.init()
bg = pygame.image.load(IMAGEPATH)

# View constants
UPDATES_RATE = 20 # Updates the screen every UPDATES_RATE generations
SHOW_FITNESS = True # Whether to view the fitness of the entities

# Genetic algorithm constants
POPULATION_SIZE = 50
ORG_MUTATION_CHANCE = 0.1
MUTATION_CHANCE = ORG_MUTATION_CHANCE
ORG_MAX_STEPS = 7000
MAX_STEPS = ORG_MAX_STEPS
STEP_SIZE = 10
# MAX_GENERATIONS = 100

# Fitness constants
DISTANCE_PENALTY = 0.5

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Labyrinth Bounding-boxes
bounding_boxes = []

# Title and icon
pygame.display.set_caption("Maze Solver")

def get_maxsteps():
    return MAX_STEPS

def mutate(steps):
    mutated_steps = []
    for step in steps:
        _step = [step[0], step[1]]
        if random.randrange(100) < MUTATION_CHANCE*100:
            _step[0] = step[0]*random.randint(-1, 1)
            _step[1] = step[1]*random.randint(-1, 1)
        mutated_steps.append(_step)
    return mutated_steps

class Labyrinth:
    entity_x = SCREEN_WIDTH/4
    entity_y = SCREEN_HEIGHT - SCREEN_HEIGHT/4

    walls = []

    @staticmethod
    def will_collide(x, y, dx, dy):
        if x + dx < 0 or \
                x + dx > SCREEN_WIDTH - 20 or \
                y + dy < 0 or \
                y + dy > SCREEN_HEIGHT - 20:
            return True
        else:
            if IMAGE.getpixel((x+dx, y+dy)) == (0, 0, 0):
                return True
            else:
                return False

# The entity class
class Entity:
    def __init__(self, x, y, color, fitness=0, steps=None, wall_touches=None, steps_instructions=None):
        if steps is None: steps = []
        if wall_touches is None: wall_touches = []
        self.x = x
        self.y = y
        self.color = color
        self.fitness = fitness
        self.steps = steps
        self.wall_touches = wall_touches
        self.steps_instructions = steps_instructions

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 19, 19))

    def get_distance_to_goal(self, x=None, y=None):
        if x is None: x = self.x
        if y is None: y = self.y

        distance = math.sqrt((SCREEN_WIDTH - 60 - x) ** 2 + (SCREEN_HEIGHT - 60 - y) ** 2) + 0.01  # Pythagorean Theorem + 0.01 to counter divide by 0 error
        return distance

    def calculate_absolute_fitness(self):
        self.fitness = DISTANCE_PENALTY * 1/self.get_distance_to_goal()

        # The percentage of its fitness it looses
        percent = 0
        for wall_touch in self.wall_touches:
            percent += numpy.clip(1000 / (self.get_distance_to_goal(wall_touch[0], wall_touch[1]) + 100), 1, 10) / (MAX_STEPS/1000)

        self.fitness -= self.fitness * percent / 100

    def get_relative_fitness(self):
        return numpy.clip(self.fitness / max(entity.fitness for entity in entities), 0, 1)

    def move(self, dx, dy):
        # Check if the entity is not going out to the wall
        labyrinth = Labyrinth()
        if not labyrinth.will_collide(self.x, self.y, dx, dy):
            self.x += dx
            self.y += dy
        else:
            self.wall_touches.append((self.x, self.y))

        self.steps.append((dx, dy))


def update_screen(_entities):
    screen.blit(bg, (0, 0))

    # Place the entities
    for entity in _entities:
        entity.draw()

    # Set colors for entities based on their active state
    for entity in _entities:
        if entity.fitness >= 0:
            entity.color = (0, entity.fitness / 100000, 0)
        else:
            entity.color = (0, 0, 0)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # quit()

    # Update the screen
    pygame.display.flip()



entities = []

# Create the entities on the bottom left
for i in range(POPULATION_SIZE):
    entities.append(Entity(Labyrinth.entity_x, Labyrinth.entity_y, (0, 0, 0)))

def main():
    global MAX_STEPS
    global MUTATION_CHANCE

    generation = 0
    best_entity = entities[0]

    while True:
        touched_goal = False

        while not touched_goal and len(entities[0].steps) < MAX_STEPS:
            # Move every entity according to its steps made and instructions
            for entity in entities:
                if generation == 0:
                    entity.move(random.randint(-1, 1) * STEP_SIZE, random.randint(-1, 1) * STEP_SIZE)
                else:
                    # The next step which is to be made
                    next_step = entity.steps_instructions[len(entity.steps)]
                    entity.move(next_step[0], next_step[1])

                    # If at wall
                    if entity.get_distance_to_goal() < 10:
                        touched_goal = True
                        MAX_STEPS = len(entity.steps)
                        MUTATION_CHANCE = ORG_MUTATION_CHANCE*(MAX_STEPS/ORG_MAX_STEPS)
            if generation % UPDATES_RATE == 0:
                update_screen(entities)


        for entity in entities:
            entity.calculate_absolute_fitness()
        for entity in entities:
            entity.color = (255*entity.get_relative_fitness(), 0, 0)
            if entity.get_relative_fitness() == 1:
                entity.color = (0, 255, 0)
                best_entity = entity

        if generation % UPDATES_RATE == 0 and SHOW_FITNESS:
            update_screen(entities)

        # Create a new generation
        entities.clear()

        # Create the entities with the steps of the best entity
        entities.append(Entity(Labyrinth.entity_x, Labyrinth.entity_y, (0, 0, 0), steps_instructions=best_entity.steps))
        for _ in range(POPULATION_SIZE-1):
            mutation = mutate(best_entity.steps)
            entities.append(Entity(Labyrinth.entity_x, Labyrinth.entity_y, (0, 0, 0), steps_instructions=mutation))

        generation += 1

        # print (generation, best_entity.fitness)

        print(MAX_STEPS, MUTATION_CHANCE)

if __name__ == "__main__":\
    main()
