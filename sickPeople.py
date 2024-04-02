import random

class Individual:
    def __init__(self, position):
        self.position = position
        self.state = 'Not Sick (Yet)'
        self.sickCounter = None
        self.deadly = None
        self.next_to_sick = None

    def infect(self, num, d_status = False):
        self.state = 'Sick'
        self.sickCounter = num
        if d_status and random.random() <= 0.1:
            self.die()

    def recover(self):
        self.state = 'Over it - Immune'

    def die(self):
        self.state = 'Dead'

    def reduceSickCount(self):
        self.sickCounter -= 1

    def removePerson(self, grid):
        x, y = self.position
        self.position = None
        grid.grid[x][y] = None

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

    

    





