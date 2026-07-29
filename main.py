from graphics import Window
from maze import Maze


def main() -> None:
    # Number of rows in the maze
    num_rows = 12

    # Number of columns in the maze
    num_cols = 16

    # Space between the maze and the window edges
    margin = 50

    # Window width and height
    screen_x = 800
    screen_y = 600

    # Calculate each cell size automatically
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    # The same seed creates the same maze each time
    # Change the number for a different maze
    seed = 12

    win = Window(screen_x, screen_y)

    maze = Maze(
        margin,
        margin,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        seed,
    )

    maze.solve()
    win.wait_for_close()


main()