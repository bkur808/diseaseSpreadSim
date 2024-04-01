import random

INFECTIOUS_PERIOD = 1000

class Individual:
    def __init__(self, position):
        self.position = position
        self.state = 'Not Sick (Yet)'
        self.sickCounter = None
        self.lifestatus = 'Living'

    def infect(self):
        self.state = 'Sick'
        self.sickCounter = INFECTIOUS_PERIOD

    def recover(self):
        self.state = 'Over it - Immune'

    def reduceSickCount(self):
        self.sickCounter -= 1

    def move(self, grid):
        x, y = self.position
        neighbors = grid.get_neighbors((x, y))
        if neighbors:
            new_position = random.choice(neighbors)
            # Check if the new position is not occupied
        if grid.grid[new_position[0]][new_position[1]] is None:
            # Update grid and individual's position
            grid.grid[x][y] = None
            grid.grid[new_position[0]][new_position[1]] = self
            self.position = new_position

    

    





