class Grid:
    def __init__(self, num_rows, num_cols, init_value) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols 
        self.grid = []
        for row in range(num_rows):
            self.grid.append([])
            for column in range(num_cols):
                self.grid[row].append(init_value)

    def get_value(self, pos):
        try:
            return self.grid[pos[0]][pos[1]]
        except:
            return None

    def set_value(self, pos, value):
        self.grid[pos[0]][pos[1]] = value
        return self.grid
    
    def get_num_cells(self):
        return self.num_rows * self.num_cols
    