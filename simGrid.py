import random 
import sickPeople

class Grid:
    def __init__(self, rows, columns, person_count):
        self.rows = rows
        self.columns = columns
        self.size = rows * columns
        self.grid = [[None for _ in range(columns)] for _ in range(rows)]
        self.occupied_positions = set()
        self.create_population(person_count)
        
    def create_population(self, person_count):
        self.people = []
        for _ in range(person_count):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            while (x, y) in self.occupied_positions:
                x = random.randint(0, self.rows - 1)
                y = random.randint(0, self.columns - 1)
            self.occupied_positions.add((x, y))
            individual = sickPeople.Individual((x,y))
            self.people.append(individual)
            self.grid[x][y] = individual

    def is_position_occupied(self, position):
        return position in self.occupied_positions
    

    def get_neighbors(self, position):
        x, y = position
        neighbors = []
        for i in range(max(0, x - 1), min(self.rows, x + 2)):
            for j in range(max(0, y - 1), min(self.columns, y + 2)):
                if (i, j) != position:
                    neighbors.append((i, j))
        return neighbors

    def check_neighbors_sick(self, position):
        x, y = position
        neighbors = self.get_neighbors(position)
        for neighbor in neighbors:
            nx, ny = neighbor
            if self.grid[nx][ny] is not None and self.grid[nx][ny].state == 'Sick':
                return True
        return False
     
    def printGrid(self):
        for row in self.grid:
            for cell in row:
                if cell is None:
                    print("-", end=" ")  # Print dash for empty space
                elif isinstance(cell, sickPeople.Individual):
                    if cell.state == 'Not Sick (Yet)':
                        print("$", end=" ")  # Print $ for individual
                    elif cell.state == 'Sick':
                        print("@", end=" ")
                    elif cell.state == 'Over it - Immune':
                        print(":)", end=" ")        
            print()  # Move to next line at end of each row

    def infectLot(self, num):
        for i in range(num):
            if (i < len(self.people)):
             self.people[i].infect()

    def advanceTime(self):
        for i in range(len(self.people)):
            self.people[i].move(self) 
            if(self.people[i].state == 'Sick'):
                self.people[i].reduceSickCount()
            elif(self.people[i].state == 'Not Sick (Yet)'):
                if(self.check_neighbors_sick(self.people[i].position)):
                    self.people[i].infect()
            elif(self.people[i].state == 'Over it - Immune'):
                #TODO ?
                pass
            pass