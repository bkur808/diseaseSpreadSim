import random 
import sickPeople

class Grid:
    def __init__(self, rows, columns, person_count):
        self.rows = rows
        self.columns = columns
        self.size = rows * columns
        self.grid = [[None for _ in range(columns)] for _ in range(rows)]
        self.occupied_positions = set()
        self.turn = 1
        self.population = 0
        self.healthyPopulation = 0
        self.sickPopulation = 0
        self.recoveredPopulation = 0
        self.deadPopulation = 0
        self.statLog = []
        self.create_population(person_count)
        self.updateStats()

    def updateStats(self):
        self.stats = (self.turn, self.population, self.healthyPopulation, self.sickPopulation, self.recoveredPopulation, self.deadPopulation)
        self.statLog.append(self.stats)

    def printStats(self):
        print('Turn: ',self.stats[0])
        print('Population: ', self.stats[1])
        print('Healthy Count: ', self.stats[2])
        print('Sick Count: ', self.stats[3])
        print('Recovered Count: ', self.stats[4]) 
        print('Death Count: ', self.stats[5])
        
    def create_population(self, person_count):
        self.population = person_count
        self.healthyPopulation = person_count
        self.updateStats()
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
        self.sickPopulation = num
        self.healthyPopulation -= num
        self.updateStats()
        for i in range(num):
            if (i < len(self.people)):
             self.people[i].infect()

    def allSick(self):
        if self.sickPopulation + self.recoveredPopulation >= self.population:
            return True
        else:
            return False

    def advanceTime(self):
        self.turn += 1
        self.updateStats()
        for i in range(len(self.people)):
            self.people[i].move(self)
             
        for i in range(len(self.people)):
            if(self.people[i].state == 'Sick'):
                self.people[i].reduceSickCount()
                if(self.people[i].sickCounter == 0):
                 self.people[i].recover()
                 self.sickPopulation -= 1
                 self.recoveredPopulation += 1
                 self.updateStats()
            elif(self.people[i].state == 'Not Sick (Yet)'):
                if(self.check_neighbors_sick(self.people[i].position)):
                    self.people[i].infect()
                    self.healthyPopulation -= 1
                    self.sickPopulation += 1
                    self.updateStats()
            elif(self.people[i].state == 'Over it - Immune'):
                #TODO ?
                pass
            pass

    def runSim1(self):
        while not self.allSick():
            self.printStats()
            self.advanceTime()
        print('Final Stats: ')
        self.printStats()
            