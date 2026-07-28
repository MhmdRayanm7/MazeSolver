import unittest
from maze import Maze


class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(maze._Maze__cells), num_cols)
        self.assertEqual(len(maze._Maze__cells[0]), num_rows)

    def test_maze_small_size(self):
        num_cols = 3
        num_rows = 5

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(maze._Maze__cells), num_cols)
        self.assertEqual(len(maze._Maze__cells[0]), num_rows)

    def test_maze_single_cell(self):
        num_cols = 1
        num_rows = 1

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(len(maze._Maze__cells), num_cols)
        self.assertEqual(len(maze._Maze__cells[0]), num_rows)


if __name__ == "__main__":
    unittest.main()