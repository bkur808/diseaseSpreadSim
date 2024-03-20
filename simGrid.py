import random 
import sickPeople

class Individual:
    def __init__(self, position):
        self.position = position
        self.state = 'Not Sick (Yet)'

    def infect(self):
        self.state = 'Sicko Mode'

    def recover(self):
        self.state = 'Over it and Immune'

class Grid:
    def __init__(self, rows, columns, person_count):
        self.rows = rows
        self.columns = columns
        self.size = rows * columns
        self.grid = [[None for _ in range(columns)] for _ in range(rows)]
        self.occupied_positions = set()
        self.create_population(person_count)
        self.people = []
        
    def create_population(self, person_count):
        for _ in range(person_count):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            while (x, y) in self.occupied_positions:
                x = random.randint(0, self.rows - 1)
                y = random.randint(0, self.columns - 1)
            self.occupied_positions.add((x, y))
            individual = Individual((x,y))
            self.people.append(individual)
            self.grid[x][y] = individual


    def is_position_occupied(self, position):
        return position in self.occupied_positions
    
    