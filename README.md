# Free Kick Game

This is a simple interactive game simulating a free kick scenario, built with Python using the `turtle`, `pygame`, `math`, and `tkinter` libraries. The player can take a shot at a goal by specifying the velocity and angle of the kick. The game calculates the trajectory of the ball using projectile motion physics and displays whether the player scores a goal or misses.

## Features

- **Realistic Ball Motion**: The ball follows projectile motion based on the given velocity and angle.
- **Interactive GUI**: A graphical interface where the player can input the velocity and angle for the kick.
- **Game Setup**: The game starts with an introduction and visualizes the player, goalkeeper, and the ball on the screen.
- **Goal Detection**: The game checks if the ball crosses into the goal area, displaying "GOAL!!!" or "YOU MISSED!!!".

## Requirements

- Python 3.x
- `pygame` library
- `tkinter` library (usually included with Python)
- `math` library (standard library)

## Setup Instructions

1. Clone or download this repository to your local machine.
2. Install `pygame` if not already installed:

   ```bash
   pip install pygame
   ```

# Compile 

``` bash
python free_kick_game.py
```
