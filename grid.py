import random
import string

class grid:

    def __init__(self) -> None:
        self.game_grid = []

    def generate_grid(self, grid_size):
        grid_elements = [i // 2 for i in range(grid_size * grid_size)]
        random.shuffle(grid_elements)
        self.game_grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        for i in range(grid_size):
            for j in range(grid_size):
                self.game_grid[i][j] = grid_elements.pop()
        return self.game_grid

    def display_grid(self, positions, reveal_flag = False):
        rows_size = len(self.game_grid)
        cols_size = len(self.game_grid[0])
        columns = [f' [{col}]' for col in string.ascii_uppercase[:cols_size]]
        rows = [f'[{row}]' for row in range(rows_size)]
        column_width = max(len(col) for col in columns)
        column_format = '{:>{}}' 
        print(' ' * column_width + ' ' + ' '.join(column_format.format(col, column_width) for col in columns))
        for i in range(rows_size):
            print(rows[i], end = ' ')
            for j in range(cols_size):
                if reveal_flag or (i, j) in positions:
                    print(column_format.format(self.game_grid[i][j], column_width), end = ' ')
                else:
                    print(column_format.format('X', column_width), end = ' ')
            print()

    def get_coordinates(self, coordinate, grid_size):
        columns = string.ascii_uppercase[:grid_size]
        if len(coordinate) < 2:
            print("Invalid coordinate format.")
            return None
        col = coordinate[0].upper()
        if col not in columns:
            print("Input error: column entry is out of range for this grid. Please try again.")
            return None
        row = int(coordinate[1:])
        if not (0 <= row <= grid_size - 1):
            print("Input error: row entry is out of range for this grid. Please try again.")
            return None
        return row, columns.index(col)

    def calculate_score(self, grid_size, actual_guesses):
        minimum_possible_guesses = (grid_size * grid_size) / 2
        score = (minimum_possible_guesses / actual_guesses) * 100
        return round(score, 2)