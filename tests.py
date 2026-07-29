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
    
    def test_break_entrance_and_exit(self):
        num_cols = 4
        num_rows = 3

        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        maze._Maze__break_entrance_and_exit()

        top_left_cell = maze._Maze__cells[0][0]
        bottom_right_cell = maze._Maze__cells[num_cols - 1][num_rows - 1]

        self.assertEqual(top_left_cell.has_top_wall, False)
        self.assertEqual(bottom_right_cell.has_bottom_wall, False)
        
    def test_reset_cells_visited(self):
        maze = Maze(0, 0, 3, 4, 10, 10)

        for column in maze._Maze__cells:
            for cell in column:
                cell.visited = True

        maze._Maze__reset_cells_visited()

        for column in maze._Maze__cells:
            for cell in column:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()