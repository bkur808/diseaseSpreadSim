import random

class Individual:
    def __init__(self, position):
        self.position = position
        self.state = 'Susceptible'
        self.sickCounter = None
        self.deadly = None
        self.next_to_sick = None
        self.facemask = None

    def infect(self, num = 1000, d_status = False, first_turn = True):
        if self.facemask == None or first_turn == True:
            self.state = 'Infected'
            self.sickCounter = num
            self.deadly = d_status
        elif self.facemask == True and first_turn != True:
            if random.random() <= 0.5:
                self.state = 'Infected'
                self.sickCounter = num
                self.deadly = d_status

    def recover(self):
        self.state = 'Recovered'

    def die(self):
        self.state = 'Dead'

    def reduce_sick_count(self):
        if self.deadly and random.random()  <= 0.0052541741:
            self.die()
        if self.state == 'Infected':
            self.sickCounter -= 1


    def move_person(self, grid):
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

    def remove_person(self, grid):
        x, y = self.position
        self.position = None
        grid.grid[x][y] = None

   

    

    





