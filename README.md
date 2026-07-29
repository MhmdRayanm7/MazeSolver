# MazeSolver

A simple maze generator and solver built with Python and Tkinter.

## Features

- Generates a random maze
- Displays the maze in a window
- Solves the maze using Depth-First Search
- Shows forward moves and backtracking
- Supports custom maze size and seed

## Run the Project

```bash
python3 main.py
```

## Run the Tests

```bash
python3 tests.py
```

## Configuration

You can change these values inside `main.py`:

```python
num_rows = 12
num_cols = 16
screen_x = 800
screen_y = 600
seed = 12
```

Using the same seed creates the same maze each time.

## Future Ideas

- Add BFS and A* algorithms
- Improve the colours and visuals
- Add different animation speeds
- Add Tkinter controls for maze settings
- Support larger mazes
- Turn it into a playable game
- Race the player against an algorithm
- Create a 3D maze
- Compare the speed of different algorithms