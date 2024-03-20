import random

class Grid:
    def __init__(self, rows, columns, person_count):
        self.rows = rows
        self.columns = columns
        self.size = rows * columns
        self.grid = [[None for _ in range(columns)] for _ in range(rows)]
        self.occupied_positions = set()
        self.create_population(person_count)
        
    def create_population(self, person_count):
        for _ in range(person_count):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            while (x, y) in self.occupied_positions:
                x = random.randint(0, self.rows - 1)
                y = random.randint(0, self.columns - 1)
            self.grid[x][y] = 'individual'
            self.occupied_positions.add((x, y))

    def is_position_occupied(self, position):
        return position in self.occupied_positions
    
    