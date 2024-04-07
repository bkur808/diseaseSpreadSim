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
        self.healthy_population = 0
        self.sick_population = 0
        self.recovered_population = 0
        self.dead_population = 0
        self.stat_log = []
        self.infected_this_turn = 0
        self.recovered_this_turn = 0
        self.died_this_turn = 0
        self.mask_count = 0
        self.create_population(person_count)
        self.update_stats()

    def __init__3(self, rows = 0, columns = 0, person_count = 0):
        self.rows = rows
        self.columns = columns
        self.size = rows * columns
        self.grid = [[None for _ in range(columns)] for _ in range(rows)]
        self.occupied_positions = set()
        self.turn = 0
        self.population = 0
        self.healthy_population = 0
        self.sick_population = 0
        self.recovered_population = 0
        self.dead_population = 0
        self.stat_log = []
        self.infected_this_turn = 0
        self.recovered_this_turn = 0
        self.died_this_turn = 0
        self.mask_count = 0
        self.create_population_with_masks(person_count)
        self.update_stats()

    def create_population(self, person_count):
        self.population = person_count
        self.healthy_population = person_count
        self.update_stats()
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

    def create_population_with_masks(self, person_count):
        self.population = person_count
        self.healthy_population = person_count
        self.people = []
        for _ in range(person_count):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            while (x, y) in self.occupied_positions:
                x = random.randint(0, self.rows - 1)
                y = random.randint(0, self.columns - 1)
            self.occupied_positions.add((x, y))
            individual = sickPeople.Individual((x,y))
            if random.random() <= 0.5:
                individual.facemask = True
                self.mask_count += 1
            self.people.append(individual)
            self.grid[x][y] = individual
        self.update_stats()            

    def reset_turn_stats(self):
        self.infected_this_turn = 0
        self.recovered_this_turn = 0
        self.died_this_turn = 0

    def update_stats(self):
        self.stats = (self.turn, self.population, self.healthy_population, self.sick_population, self.recovered_population, self.dead_population, self.infected_this_turn, self.recovered_this_turn, self.died_this_turn)

    def print_stats(self):
        print('Turn: ',self.stats[0])
        print('Population: ', self.stats[1])
        print('Healthy Count: ', self.stats[2])
        print('Sick Count: ', self.stats[3])
        print('Recovered Count: ', self.stats[4]) 
        print('Death Count: ', self.stats[5])
        print('Infected this turn: ', self.stats[6])
        print('Recovered this turn: ', self.stats[7])
        print('Died this turn: ', self.stats[8])
        print()

    def sim1_print(self):
        print('Turn: ',self.stats[0])
        print('Population: ', self.stats[1])
        #print('Healthy Count: ', self.stats[2])
        print('Infected this turn: ', self.infected_this_turn)
        print('Sick Count: ', self.stats[3])
        #print('Recovered Count: ', self.stats[4]) 
        #print('Death Count: ', self.stats[5])
        print() 
    
    def sim2_print(self):
        print('Turn: ',self.stats[0])
        print('Population: ', self.stats[1])
        print('Healthy Count: ', self.stats[2])
        print('Infected this turn: ', self.stats[6])
        print('Recovered this turn: ', self.stats[7])
        print('Died this turn: ', self.stats[8])
        print('Total Sick Count: ', self.stats[3])
        print('Total Recovered Count: ', self.stats[4]) 
        print('Total Death Count: ', self.stats[5])
        print()

    def sim3_print(self):
        print('Turn: ',self.stats[0])
        print('Population: ', self.stats[1])
        print('Healthy Count: ', self.stats[2])
        print('Infected this turn: ', self.stats[6])
        print('Recovered this turn: ', self.stats[7])
        print('Died this turn: ', self.stats[8])
        print('Total Sick Count: ', self.stats[3])
        print('Total Recovered Count: ', self.stats[4]) 
        print('Total Death Count: ', self.stats[5])
        print('Mask Count =', self.mask_count)
        print()

    def print_grid(self):
        for row in self.grid:
            for cell in row:
                if cell is None:
                    print("-", end=" ")  # Print dash for empty space
                elif isinstance(cell, sickPeople.Individual):
                    if cell.state == 'Susceptible' and cell.facemask == True:
                        print("8", end=" ")  # Print $ for individual
                    elif cell.state == 'Susceptible' and cell.facemask == None:
                        print("O", end=" ")
                    elif cell.state == 'Infected' and cell.facemask == True:
                        print("?", end=" ")
                    elif cell.state == 'Infected' and cell.facemask == None:
                        print("X", end=" ")
                    elif cell.state == 'Recovered':
                        print("0", end=" ")        
            print()  # Move to next line at end of each row         

    def infect_lot(self, num, infectiousPeriod = 1000, d_status = False): 
        self.sick_population += num
        self.healthy_population -= num
        self.infected_this_turn += num
        for i in range(num):
            if (i < len(self.people)):
             self.people[i].infect(infectiousPeriod, d_status)
        self.update_stats()
        self.stat_log.append(self.stats)    #  record last turn's stats in stat_log

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
            if self.grid[nx][ny] is not None and self.grid[nx][ny].state == 'Infected':
                return True
        return False
    
    def check_neighbors_sick_with_mask(self, position): #for sim3
        x, y = position
        neighbors = self.get_neighbors(position)
        for neighbor in neighbors:
            nx, ny = neighbor
            this_neighbor = self.grid[nx][ny]
            if self.grid[nx][ny] is not None and this_neighbor.state == 'Infected':
                if this_neighbor.facemask:
                    if random.random() <= 0.5:
                        return True
                else: 
                    return True
        return False

    def all_sick(self):
        if self.sick_population + self.recovered_population + self.dead_population >= self.population:
            return True
        else:
            return False
        
    def all_recovered_or_dead(self):
        if self.recovered_population + self.dead_population >= self.population:
            return True
        else:
            return False
        
    def all_recovered_or_dead_or_healthy(self):
        if self.recovered_population + self.dead_population + self.healthy_population >= self.population:
            return True
        else:
            return False

    def advance_turn_sim1(self):
        self.turn += 1                      #  advance a turn in stats
        self.reset_turn_stats()              #  reset the turn_stats to 0's 
        self.infect_list = []               #  reset the infect_list to empty

        # First - move everyone on the board
        for i in range(len(self.people)):
            self.people[i].move_person(self)

        # Second - Go through population and either do nothing (infected) or add to infect_list (susceptible and next to sick)     
        for i in range(len(self.people)):
            if(self.people[i].state == 'Susceptible' and self.check_neighbors_sick(self.people[i].position) == True):
                self.infect_list.append(self.people[i])
  
        # Third - Infect (separate loop to prevent sick chaining) - update all stats
        for i in range(len(self.infect_list)):
            self.infect_list[i].infect()
            self.infected_this_turn += 1
            self.healthy_population -= 1
            self.sick_population += 1
        self.update_stats()
        self.stat_log.append(self.stats)    #  record last turn's stats in stat_log    
        
    def test1(self):
        self.__init__(100, 100, 6000)
        self.infect_lot(1)  
        # Turn 1: P - 6000, HP 5999, SP 1, RP 0, DP 0, IT = 1, RT = 0, DT = 0

    def run_sim1(self, n):
        all_sim_counts = []  # List to store infected counts at each step
        max_steps = 0  # Initialize max_steps to 0

        # This loop will run a full simulation until every person is sick n times
        for i in range(n): 
            # Instantiate a grid 100x100 w/ population 6000
            self.test1()
            # We also infect_lot which leaves us w/ Turn 1: P - 6000, HP 5999, SP 1, RP 0, DP 0, IT = 1, RT = 0, DT = 0
            while not self.all_sick():
                self.advance_turn_sim1()
            all_sim_counts.append(self.stat_log)  # Append infected count at each step for this run
            print('Simulation ', i + 1, ' Final Stats: ')
            self.sim1_print()
            #print(self.stat_log)
            max_steps = max(max_steps, self.turn)  # Update max_steps

        avg_new_infected = [0] * (max_steps+1)
        avg_total_infected = [0] * (max_steps+1)
        # number of infected is stored in stats[6] or stat_log[n][6], # total infections is stored in stats[3] or stat_log[n][6]
        for i in range(n):
            for j in range(max_steps+1):
                    if j < len(all_sim_counts[i]):  # Check if the simulation has data for this turn (if j is within the length of the current sim)
                        avg_new_infected[j] += all_sim_counts[i][j][6]
                        avg_total_infected[j] += all_sim_counts[i][j][3]
                    else:
                            # If simulation data ends, assume no new infections and total infected remains constant
                        avg_total_infected[j] += self.population

        for i in range(max_steps+1):
            avg_new_infected[i] /= float(n)
            avg_total_infected[i] /= float(n)

        with open('disease_stats_sim1.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Turn', 'Avg_New_Infections', 'Avg_Total_Infected'])
            for i in range(0, max_steps+1):
                writer.writerow([i, avg_new_infected[i], avg_total_infected[i]])
                
        print("CSV file 'disease_stats_sim1.csv' has been generated successfully.")

    
    def test2(self): # for sim2
        self.__init__(100, 100, 6000)
        self.infect_lot(1, 20, True)  
        # Turn 1: P - 6000, HP 5999, SP 1, RP 0, DP 0, IT = 1, RT = 0, DT = 0

    def advance_turn_sim2(self): # for sim2
        self.turn += 1                      #  advance a turn in stats
        self.reset_turn_stats()              #  reset the turn_stats to 0's 
        self.infect_list = []               #  reset the infect_list to empty

        # First - move everyone on the board
        for person in self.people:
            if(person.state != 'Dead'):
                person.move_person(self)

        # Second - Go through population and either do nothing (infected) or add to infect_list (susceptible and next to sick)     
        for person in self.people:
            if(person.state == 'Susceptible' and self.check_neighbors_sick(person.position) == True):
                self.infect_list.append(person)
            elif(person.state == 'Infected'):
                person.reduce_sick_count()
                if(person.sickCounter == 0):
                    person.recover()
                    self.recovered_this_turn += 1
                    self.recovered_population += 1
                if(person.state == 'Dead'):
                    person.remove_person(self)
                    self.died_this_turn += 1
                    self.dead_population += 1    
            elif(person.state == 'Recovered'):
                None

        # Third - Infect (separate loop to prevent sick chaining) - update all stats
        for i in range(len(self.infect_list)):
            self.infect_list[i].infect(20, True)
            self.infected_this_turn += 1
            self.healthy_population -= 1
            self.sick_population += 1
        self.update_stats()
        self.stat_log.append(self.stats)    #  record last turn's stats in stat_log  


    def run_sim2(self, n): # for sim2
        all_sim_counts = []  # List to store infected counts at each step
        max_steps = 0  # Initialize max_steps to 0

        # This loop will run a full simulation until every person is sick n times
        for i in range(n): 
            # Instantiate a grid 100x100 w/ population 6000
            self.test2()
            # We also infect_lot which leaves us w/ Turn 1: P - 6000, HP 5999, SP 1, RP 0, DP 0, IT = 1, RT = 0, DT = 0
            while not self.all_recovered_or_dead():
                self.advance_turn_sim2()
            all_sim_counts.append(self.stat_log)  # Append infected count at each step for this run
            print('Simulation ', i + 1, ' Final Stats: ')
            self.sim2_print()
            #print(self.stat_log)
            max_steps = max(max_steps, self.turn)  # Update max_steps

        avg_total_infected = [0] * (max_steps+1)
        avg_total_recovered = [0] * (max_steps+1)
        avg_total_dead = [0] * (max_steps+1)

        avg_new_infected = [0] * (max_steps+1)
        avg_new_dead = [0] * (max_steps+1)
        avg_new_recovered = [0] * (max_steps+1)

        # number of infected is stored in stats[6] or stat_log[n][6], # total infections is stored in stats[3] or stat_log[n][6]
        for i in range(n):
            for j in range(max_steps+1):
                    if j < len(all_sim_counts[i]):  # Check if the simulation has data for this turn (if j is within the length of the current sim)
                        avg_total_infected[j] += all_sim_counts[i][j][3]
                        avg_total_recovered[j] += all_sim_counts[i][j][4]
                        avg_total_dead[j] += all_sim_counts[i][j][5]

                        avg_new_infected[j] += all_sim_counts[i][j][6]
                        avg_new_recovered[j] += all_sim_counts[i][j][7]
                        avg_new_dead[j] += all_sim_counts[i][j][8]
                        
                    else:
                            # If simulation data ends, assume no new infections and total infected remains constant
                        avg_total_infected[j] += all_sim_counts[i][-1][3]
                        avg_total_recovered[j] += all_sim_counts[i][-1][4]
                        avg_total_dead[j] += all_sim_counts[i][-1][5]

        for i in range(max_steps+1):
            avg_new_infected[i] /= float(n)
            avg_new_recovered[i] /= float(n)
            avg_new_dead[i] /= float(n)
            
            avg_total_infected[i] /= float(n)
            avg_total_recovered[i] /= float(n)
            avg_total_dead[i] /= float(n)

        with open('disease_stats_sim2.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Turn', 'Avg_New_Infections', 'Avg_New_Recoveries', 'Avg_New_Deaths','Avg_Total_Infected', 'Avg_Total_Recoveries','Avg_New_Deaths'])
            for i in range(0, max_steps+1):
                writer.writerow([i, avg_new_infected[i], avg_new_recovered[i], avg_new_dead[i], avg_total_infected[i], avg_total_recovered[i], avg_total_dead[i]])
                
        print("CSV file 'disease_stats_sim2.csv' has been generated successfully.")
    


    def test3(self): # for sim3
        self.__init__3(100, 100, 6000)
        self.infect_lot(1, 20, True)  
        # Turn 1: P - 6000, HP 5999, SP 1, RP 0, DP 0, IT = 1, RT = 0, DT = 0

    def advance_turn_sim3(self): # for sim3
        self.turn += 1                      #  advance a turn in stats
        self.reset_turn_stats()             #  reset the turn_stats to 0's 
        self.infect_list = []               #  reset the infect_list to empty
        self.update_stats()

        # First - move everyone on the board
        for person in self.people:
            if(person.state != 'Dead'):
                person.move_person(self)

        # Second - Go through population and either do nothing (infected) or add to infect_list (susceptible and next to sick)     
        for person in self.people:
            if(person.state!= 'Dead'):
                x,y = person.position
                if(person.state == 'Susceptible' and self.check_neighbors_sick_with_mask((x,y)) == True):
                    self.infect_list.append(person)
                elif(person.state == 'Infected'):
                    person.reduce_sick_count()
                    if(person.sickCounter == 0):
                        person.recover()
                        self.recovered_this_turn += 1
                        self.recovered_population += 1
                    if(person.state == 'Dead'):
                        person.remove_person(self)
                        self.died_this_turn += 1
                        self.dead_population += 1    
                elif(person.state == 'Recovered'):
                    None

        # Third - Infect (separate loop to prevent sick chaining) - update all stats
        for person in self.infect_list:
            person.infect(20, True, False)
            if person.state == 'Infected':
                self.infected_this_turn += 1
                self.healthy_population -= 1
                self.sick_population += 1
        self.update_stats()
        self.stat_log.append(self.stats)    #  record last turn's stats in stat_log  


    def run_sim3(self, n): # for sim3
        all_sim_counts = []  # List to store infected counts at each step
        max_steps = 0  # Initialize max_steps to 0
        avg_mask_count = 0

        # This loop will run a full simulation until every person is sick n times
        for i in range(n): 
            # Instantiate a grid 100x100 w/ population 6000
            self.test3()
            # We also infect_lot which leaves us w/ Turn 1: P - 6000, HP 5999, SP 1, RP 0, DP 0, IT = 1, RT = 0, DT = 0
            while not self.all_recovered_or_dead_or_healthy():
                self.advance_turn_sim3()
            all_sim_counts.append(self.stat_log)  # Append infected count at each step for this run
            print('Simulation ', i + 1, ' Final Stats: ')
            self.sim3_print()
            #print(self.stat_log)
            max_steps = max(max_steps, self.turn)  # Update max_steps
            avg_mask_count += self.mask_count

        avg_total_infected = [0] * (max_steps+1)
        avg_total_recovered = [0] * (max_steps+1)
        avg_total_dead = [0] * (max_steps+1)

        avg_new_infected = [0] * (max_steps+1)
        avg_new_dead = [0] * (max_steps+1)
        avg_new_recovered = [0] * (max_steps+1)

        # number of infected is stored in stats[6] or stat_log[n][6], # total infections is stored in stats[3] or stat_log[n][6]
        for i in range(n):
            for j in range(max_steps+1):
                    if j < len(all_sim_counts[i]):  # Check if the simulation has data for this turn (if j is within the length of the current sim)
                        avg_total_infected[j] += all_sim_counts[i][j][3]
                        avg_total_recovered[j] += all_sim_counts[i][j][4]
                        avg_total_dead[j] += all_sim_counts[i][j][5]

                        avg_new_infected[j] += all_sim_counts[i][j][6]
                        avg_new_recovered[j] += all_sim_counts[i][j][7]
                        avg_new_dead[j] += all_sim_counts[i][j][8]
                        
                    else:
                            # If simulation data ends, assume no new infections and total infected remains constant
                        avg_total_infected[j] += all_sim_counts[i][-1][3]
                        avg_total_recovered[j] += all_sim_counts[i][-1][4]
                        avg_total_dead[j] += all_sim_counts[i][-1][5]

        for i in range(max_steps+1):
            avg_new_infected[i] /= float(n)
            avg_new_recovered[i] /= float(n)
            avg_new_dead[i] /= float(n)
            
            avg_total_infected[i] /= float(n)
            avg_total_recovered[i] /= float(n)
            avg_total_dead[i] /= float(n)

        avg_mask_count /= float(n)

        with open('disease_stats_sim3.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Turn', 'Avg_New_Infections', 'Avg_New_Recoveries', 'Avg_New_Deaths','Avg_Total_Infected', 'Avg_Total_Recoveries','Avg_New_Deaths', 'Avg_Mask_Count', avg_mask_count])
            for i in range(0, max_steps+1):
                writer.writerow([i, avg_new_infected[i], avg_new_recovered[i], avg_new_dead[i], avg_total_infected[i], avg_total_recovered[i], avg_total_dead[i]])
                
        print("CSV file 'disease_stats_sim3.csv' has been generated successfully.")
