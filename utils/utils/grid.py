class Grid:
    def __init__(self, num_rows, num_cols, init_value) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols 
        self.grid = []
        for row in range(num_rows):
            self.grid.append([])
            for column in range(num_cols):
                self.grid[row].append(init_value)

    def get(self, row, col):
        return self.grid[row][col]

    def set(self, row, col, value):
        self.grid[row][col] = value
        return self.grid