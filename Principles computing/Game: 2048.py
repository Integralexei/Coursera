"""
Clone of 2048 game.
"""

# http://www.codeskulptor.org/#user40_r9Wd9QuZz6KBplk.py

import poc_2048_gui
import random

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    Order of execution + another shift.
    """
    shift_line = shift(line)
    merge_shift_line = merge_shifted_line(shift_line)
    return shift(merge_shift_line)


def shift(line):
    """
    Shifts numbers greater than 0 to the left.
    """
    shifted_line = [digit_from_line for digit_from_line in line if digit_from_line != 0]
    while len(line) > len(shifted_line):
        shifted_line.append(0)
    return shifted_line


def merge_shifted_line(shifted_line):
    """
    Merges the elements.
    """
    for index in range(len(shifted_line) - 1):
        if shifted_line[index] == shifted_line[index + 1]:
            shifted_line[index] *= 2
            shifted_line[index + 1] = 0
    return shifted_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):

        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for self._col in range(self._grid_width)]
                      for self._row in range(self._grid_height)]
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return '\n'.join(str(row) for row in self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        start_cell_up = [(0, 0 + count) for count in range(self._grid_height)]
        start_cell_down = [(self._grid_height-1, 0 + count) for count in range(self._grid_height)]
        start_cell_left = [(0+count, 0) for count in range(self._grid_width)]
        start_cell_right = [(0 + count, self._grid_width-1) for count in range(self._grid_width)]

        start_cells = {UP: start_cell_up,
                       DOWN: start_cell_down,
                       LEFT: start_cell_left,
                       RIGHT: start_cell_right}

        if direction == 1 or direction == 2:
            num_steps = self._grid_height
        else:
            num_steps = self._grid_width
        for start_cell in start_cells.get(direction):
            temporary_list = []
            for step in range(num_steps):
                row = start_cell[0] + step * OFFSETS.get(direction)[0]
                col = start_cell[1] + step * OFFSETS.get(direction)[1]
                temporary_list.append(self._grid[row][col])
            temporary_list = merge(temporary_list)
            for merged_values, step in zip(temporary_list, range(num_steps)):
                row = start_cell[0] + step * OFFSETS.get(direction)[0]
                col = start_cell[1] + step * OFFSETS.get(direction)[1]
                self._grid[row][col] = merged_values
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        new_tiles = self.random_tiles()
        row_first_tile = new_tiles[0][0]
        col_first_tile = new_tiles[0][1]
        row_second_tile = new_tiles[1][0]
        col_second_tile = new_tiles[1][1]
        if random.randrange(0, 10) == 4:
            self._grid[row_first_tile][col_first_tile] = 4
        else:
            self._grid[row_first_tile][col_first_tile] = 2
        if random.randrange(0, 10) == 4:
            self._grid[row_second_tile][col_second_tile] = 4
        else:
            self._grid[row_second_tile][col_second_tile] = 2

    def random_tiles(self):
        new_random_tiles = []
        while len(new_random_tiles) < 2:
            row = random.randrange(0, self._grid_height)
            col = random.randrange(0, self._grid_width)
            if self._grid[row][col] == 0:
                new_tile_first = (row, col)
                new_random_tiles.append(new_tile_first)
        return new_random_tiles

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
            Return the value of the tile at position row, col.
            """
        return self._grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))






