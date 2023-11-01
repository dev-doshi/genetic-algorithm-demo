# Maze Solver using Pygame and Genetic Algorithm

This Python script utilizes Pygame and a genetic algorithm to simulate maze solving by entities in a labyrinth. The entities evolve by learning and adapting their movement patterns to navigate through the maze towards a specified goal.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

This program creates a simulated labyrinth environment using an image as the maze layout. Entities are spawned within the maze and use a genetic algorithm to evolve their movement instructions towards reaching a designated goal. The program employs Pygame for visualization and genetic algorithm principles for evolving entity movement strategies.

## Features

- **Genetic Algorithm:** Entities evolve by learning from their movements and adapt their strategies to navigate the maze.
- **Pygame Visualization:** Utilizes Pygame to render the maze environment and the movements of entities in real-time.
- **Fitness Calculation:** Entities' fitness is calculated based on their distance to the goal and penalized for collisions with maze walls.
- **Population Evolution:** Each generation, the fittest entity's movements are used to create a new generation, potentially with mutations, promoting continuous learning.

## Getting Started

To get started with this program, follow these steps:

1. **Clone Repository:**
   ```bash
   git clone https://github.com/your-username/maze-solver.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install pygame numpy pillow
   ```

3. **Run the Program:**
   ```bash
   python maze_solver.py
   ```

## Dependencies

- **Pygame:** 
- **NumPy:** 
- **Pillow:** 

Make sure to have these dependencies installed before running the script.

## Usage

The usage of this program involves starting the script, which initializes entities within the maze. Entities learn and adapt their movement strategies towards reaching the goal by evolving with each generation.

## Configuration

The script provides various configuration options that can be adjusted:

- `UPDATES_RATE`: Determines the screen update rate for visualizing entities' movements.
- `POPULATION_SIZE`: Number of entities in each generation.
- `MUTATION_CHANCE`: Probability of mutation for entity movements.
- `DISTANCE_PENALTY`: Penalty factor for entities colliding with maze walls.

Adjust these constants to customize the simulation and optimize the maze-solving process.

## Contributing

Contributions are welcome! To contribute to this project, fork the repository, make your changes, and submit a pull request. Please ensure your code follows the existing style and passes all tests.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.

---
