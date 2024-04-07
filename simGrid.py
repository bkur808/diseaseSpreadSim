import random 
import csv
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
        
    def all_recovered_or_dead(self):
        if self.recoveredPopulation + self.deadPopulation >= self.population:
            return True
        else:
            return False

    def advanceTime(self, infectiousPeriod = 1000):
        self.turn += 1
        self.updateStats()
        for i in range(len(self.people)):
            self.people[i].move_person(self)
             
        for i in range(len(self.people)):
            if(self.people[i].state == 'Sick'):
                self.people[i].reduce_sick_count()
                if(self.people[i].sickCounter == 0):
                 self.people[i].recover()
                 self.sickPopulation -= 1
                 self.recoveredPopulation += 1
                 self.updateStats()
            elif(self.people[i].state == 'Not Sick (Yet)'):
                if(self.check_neighbors_sick(self.people[i].position)):
                    self.people[i].next_to_sick = True
            elif(self.people[i].state == 'Over it - Immune'):
                #TODO ?
                pass
            pass
        
        for i in range(len(self.people)):
            if self.people[i].next_to_sick == True and self.people[i].state != 'Sick':
                self.people[i].infect(infectiousPeriod)
                self.healthyPopulation -= 1
                self.sickPopulation += 1
                self.updateStats()


    def test1(self):
        self.__init__(100, 100, 6000)
        self.infectLot(1)
            

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
            self.printStats()
            max_steps = max(max_steps, len(infected_count_step))  # Update max_steps

        #return infected_counts
        # Calculate averages up to the length of the longest simulation run
        avg_new_infected = [1] * max_steps  # Initialize list to store average new infected counts
        avg_total_infected = [1] * max_steps  # Initialize list to store average total infected counts
        num_simulations = len(infected_counts)
    
        # Calculate average new infected and average total infected at each step
        for step in range(0, max_steps):  # Skip initial step
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
        #print("Average number of new people infected at each step:")
        #for step, count in enumerate(avg_new_infected, start=1):
        #    print(f"Step {step}: {count:.2f}")

        #print("\nAverage number of people who are infected at each step:")
        #for step, count in enumerate(avg_total_infected, start=1):
        #    print(f"Step {step}: {count:.2f}")
        with open('disease_stats.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['step', 'avg_new_infected', 'avg_total_infected'])
            for step in range(1, max_steps + 1):
             writer.writerow([step, avg_new_infected[step - 1], avg_total_infected[step - 1]])

        print("CSV file 'disease_stats.csv' has been generated successfully.")


    def advance_time_sim2(self, infectiousPeriod=20, d_status=True):
        self.turn += 1
        self.updateStats()
        self.infectList = []

        # Move all individuals step
        for i in range(len(self.people)):
            self.people[i].move_person(self)

        # Iterate over individuals
        for person in self.people:
            if person.state == 'Sick':
                person.reduce_sick_count()
                if person.sickCounter == 0:
                    person.recover()
                    self.recoveredPopulation += 1
                    self.sickPopulation -= 1
                    self.updateStats()    
            elif person.state == 'Not Sick (Yet)' and person.state != 'Over it - Immune':
                if self.check_neighbors_sick(person.position):
                    self.infectList.append(person)

        # Infect individuals next to sick individuals - if they die - remove
        for person in self.infectList:
                person.infect(infectiousPeriod, d_status)
                if person.state == 'Dead':
                    self.deadPopulation += 1
                    x, y = person.position
                    person.position = None
                    self.grid[x][y] = None
                    self.people.remove(person)
                elif person.state == 'Sick':
                    self.sickPopulation += 1
                self.healthyPopulation -= 1
                self.updateStats()

    def test2(self):
        self.__init__(100,100,6000)
        self.infectLot(1,20)

    def runSim2(self, n): 
        # List to store infected counts at each step
        infected_counts = []  
        # Initialize max_steps to 0
        max_steps = 0  
    
        for i in range(n): 
            self.test2()
            # For each step we record this tuple: 
            # (Turn, #infected this turn, # of those who have gotten sick, #died this turn, # of those who have died, #recovered this turn, #recovered overall)
            infected_count_step = [(self.turn, 1, self.sickPopulation, 0, 0, 0, 0)]  
            # Store initial infected count
            
            # Store previous sick population
            prev_recovered_population = 0
            prev_dead_population = 0
        
            while not self.all_recovered_or_dead():
                prev_sick_population = self.sickPopulation  
                new_recovered_population = self.recoveredPopulation - prev_recovered_population
                new_dead_population = self.deadPopulation - prev_dead_population
                new_sick_population = self.sickPopulation - prev_sick_population + new_recovered_population 
                total_sick_population = self.sickPopulation + self.recoveredPopulation + self.deadPopulation  
                infected_count_step.append((self.turn, new_sick_population, total_sick_population, new_dead_population, self.deadPopulation, new_recovered_population, self.recoveredPopulation))  
                prev_sick_population = total_sick_population  
                prev_dead_population = self.deadPopulation
                prev_recovered_population = self.recoveredPopulation
                self.advance_time_sim2()
            
            infected_counts.append(infected_count_step)  
            print('Simulation ', i + 1, ' Final Stats: ')
            self.printStats()
            max_steps = max(max_steps, len(infected_count_step))  

        # Initialize lists to store average values for each statistic
        avg_new_infected = [1] * max_steps
        avg_total_infected = [1] * max_steps
        avg_new_dead = [0] * max_steps
        avg_dead = [0] * max_steps
        avg_new_recoveries = [0] * max_steps
        avg_recovered = [0] * max_steps

        num_simulations = len(infected_counts)

        # Calculate average values for each statistic at each step
        for step in range(1, max_steps):  
            total_new_infected = 0
            total_total_infected = 0
            total_new_dead = 0
            total_dead = 0
            total_new_recoveries = 0
            total_recovered = 0

            for infected_count_step in infected_counts:
                if step < len(infected_count_step):
                    total_new_infected += infected_count_step[step][1]
                    total_total_infected += infected_count_step[step][2]
                    total_new_dead += infected_count_step[step][3]
                    total_dead += infected_count_step[step][4]
                    total_new_recoveries += infected_count_step[step][5]
                    total_recovered += infected_count_step[step][6]
                else:
                    total_total_infected += infected_count_step[-1][2]
                    total_dead += infected_count_step[-1][4]
                    total_recovered += infected_count_step[-1][6]

            avg_new_infected[step] = total_new_infected / num_simulations
            avg_total_infected[step] = total_total_infected / num_simulations
            avg_new_dead[step] = total_new_dead / num_simulations
            avg_dead[step] = total_dead / num_simulations
            avg_new_recoveries[step] = total_new_recoveries / num_simulations
            avg_recovered[step] = total_recovered / num_simulations

        # Print averages
        print("Average number of new people infected at each step:")
        for step, count in enumerate(avg_new_infected, start=1):
            print(f"Step {step}: {count:.2f}")

        print("\nAverage number of people who have been - or are - sick at each step:")
        for step, count in enumerate(avg_total_infected, start=1):
            print(f"Step {step}: {count:.2f}")    

        print("Average number of new deaths at each step:")
        for step, count in enumerate(avg_new_dead, start = 1):
            print(f"Step {step}: {count:.2f}")

        print("Average number of dead people at each step:")
        for step, count in enumerate(avg_dead, start=1):
            print(f"Step {step}: {count:.2f}")

        print("\nAverage number of new recoveries at each step:")
        for step, count in enumerate(avg_new_recoveries, start=1):
            print(f"Step {step}: {count:.2f}")    

        print("Average number of people who have recovered at each step:")
        for step, count in enumerate(avg_recovered, start = 1):
            print(f"Step {step}: {count:.2f}")    
