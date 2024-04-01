import random 
import sickPeople

class Grid:

    def __init__(self, rows = 0, columns = 0, person_count = 0):
        self.rows = rows
        self.columns = columns
        self.size = rows * columns
        self.grid = [[None for _ in range(columns)] for _ in range(rows)]
        self.occupied_positions = set()
        self.turn = 0
        self.population = 0
        self.healthyPopulation = 0
        self.sickPopulation = 0
        self.recoveredPopulation = 0
        self.deadPopulation = 0
        self.statLog = []
        self.create_population(person_count)
        self.updateStats()

    def test1(self):
        self.__init__(100, 100, 6000)
        self.infectLot(1)


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
        print()


    def sim1Print(self):
        print('Turn: ',self.stats[0])
        print('Population: ', self.stats[1])
        #print('Healthy Count: ', self.stats[2])
        print('Sick Count: ', self.stats[3])
        #print('Recovered Count: ', self.stats[4]) 
        #print('Death Count: ', self.stats[5])
        print()        
        
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
                        print("O", end=" ")  # Print $ for individual
                    elif cell.state == 'Sick':
                        print("X", end=" ")
                    elif cell.state == 'Over it - Immune':
                        print("0", end=" ")        
            print()  # Move to next line at end of each row

    def infectLot(self, num, infectiousPeriod = 1000):
        self.sickPopulation = num
        self.healthyPopulation -= num
        self.updateStats()
        for i in range(num):
            if (i < len(self.people)):
             self.people[i].infect(infectiousPeriod)

    def allSick(self):
        if self.sickPopulation + self.recoveredPopulation + self.deadPopulation >= self.population:
            return True
        else:
            return False

    def advanceTime(self, infectiousPeriod = 1000):
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
                    self.people[i].infect(infectiousPeriod)
                    self.healthyPopulation -= 1
                    self.sickPopulation += 1
                    self.updateStats()
            elif(self.people[i].state == 'Over it - Immune'):
                #TODO ?
                pass
            pass

    def runSim1(self, n):
        infectiousPeriod = 1000
        infected_counts = []  # List to store infected counts at each step
        max_steps = 0  # Initialize max_steps to 0

        for i in range(n): 
            self.test1()
            infected_count_step = [(self.turn, 1, self.sickPopulation)]  # Store initial infected count
            prev_sick_population = self.sickPopulation  # Store previous sick population
            while not self.allSick():
                self.advanceTime(infectiousPeriod)
                new_sick_population = self.sickPopulation - prev_sick_population  # Calculate newly infected count
                total_sick_population = self.sickPopulation  # Calculate total sick population
                infected_count_step.append((self.turn, new_sick_population, total_sick_population))  # Append tuple
                prev_sick_population = total_sick_population  # Update previous sick population
            infected_counts.append(infected_count_step)  # Append infected count at each step for this run
            print('Simulation ', i + 1, ' Final Stats: ')
            self.sim1Print()
            max_steps = max(max_steps, len(infected_count_step))  # Update max_steps

        #return infected_counts
        # Calculate averages up to the length of the longest simulation run
        avg_new_infected = [1] * max_steps  # Initialize list to store average new infected counts
        avg_total_infected = [1] * max_steps  # Initialize list to store average total infected counts
        num_simulations = len(infected_counts)
    
        # Calculate average new infected and average total infected at each step
        for step in range(1, max_steps):  # Skip initial step
            total_new_infected = 0
            total_total_infected = 0
            for infected_count_step in infected_counts:
                if step < len(infected_count_step):
                    total_new_infected += infected_count_step[step][1]
                    total_total_infected += infected_count_step[step][2]
                else:
                    # Assuming sickPopulation remains constant once it reaches the maximum
                    total_total_infected += infected_count_step[-1][2]
            avg_new_infected[step] = total_new_infected / num_simulations
            avg_total_infected[step] = total_total_infected / num_simulations

        # Print averages
        print("Average number of new people infected at each step:")
        for step, count in enumerate(avg_new_infected, start=1):
            print(f"Step {step}: {count:.2f}")

        print("\nAverage number of people who are infected at each step:")
        for step, count in enumerate(avg_total_infected, start=1):
            print(f"Step {step}: {count:.2f}")


    def advance_time_sim2(self, infectiousPeriod=20, d_status=True):
        self.turn += 1
        self.updateStats()
    
        # Move individuals
        for person in self.people:
            person.move(self)
    
    # Iterate over a copy of the people list to avoid modifying it during iteration
        for person in self.people[:]:
            if person.state == 'Sick':
                person.reduceSickCount()
                if person.sickCounter == 0:
                    person.recover()
                    self.sickPopulation -= 1
                    self.recoveredPopulation += 1
                    self.updateStats()
            elif person.state == 'Not Sick (Yet)':
                if self.check_neighbors_sick(person.position):
                    person.infect(infectiousPeriod, d_status)
                    self.healthyPopulation -= 1
                    self.sickPopulation += 1
                    self.updateStats()
            elif person.state == 'Dead':
            # Remove the person from the people list
                self.people.remove(person)
                self.sickPopulation -= 1
                self.deadPopulation += 1
            pass


    def runSim2(self, n): #TODO FIX STAT TRACKING - NOT SAME AS SIMULATION 1
        infected_counts = []  # List to store infected counts at each step
        max_steps = 0  # Initialize max_steps to 0

        for i in range(n): 
            self.test1()
            infected_count_step = [(self.turn, 1, self.sickPopulation)]  # Store initial infected count
            prev_sick_population = self.sickPopulation  # Store previous sick population
            while not self.allSick():
                self.advance_time_sim2()
                new_sick_population = self.sickPopulation - prev_sick_population  # Calculate newly infected count
                total_sick_population = self.sickPopulation  # Calculate total sick population
                infected_count_step.append((self.turn, new_sick_population, total_sick_population))  # Append tuple
                prev_sick_population = total_sick_population  # Update previous sick population
            infected_counts.append(infected_count_step)  # Append infected count at each step for this run
            print('Simulation ', i + 1, ' Final Stats: ')
            self.printStats()
            max_steps = max(max_steps, len(infected_count_step))  # Update max_steps

        #return infected_counts
        # Calculate averages up to the length of the longest simulation run
        avg_new_infected = [1] * max_steps  # Initialize list to store average new infected counts
        avg_total_infected = [1] * max_steps  # Initialize list to store average total infected counts
        num_simulations = len(infected_counts)
    
        # Calculate average new infected and average total infected at each step
        for step in range(1, max_steps):  # Skip initial step
            total_new_infected = 0
            total_total_infected = 0
            for infected_count_step in infected_counts:
                if step < len(infected_count_step):
                    total_new_infected += infected_count_step[step][1]
                    total_total_infected += infected_count_step[step][2]
                else:
                    # Assuming sickPopulation remains constant once it reaches the maximum
                    total_total_infected += infected_count_step[-1][2]
            avg_new_infected[step] = total_new_infected / num_simulations
            avg_total_infected[step] = total_total_infected / num_simulations

        # Print averages
        print("Average number of new people infected at each step:")
        for step, count in enumerate(avg_new_infected, start=1):
            print(f"Step {step}: {count:.2f}")

        print("\nAverage number of people who are infected at each step:")
        for step, count in enumerate(avg_total_infected, start=1):
            print(f"Step {step}: {count:.2f}")    

            