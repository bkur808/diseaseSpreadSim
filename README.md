Disease Spread Simulator

Current class structures:

People - Position and Disease Status
     - Need to add a counter for sickness which activates on infection (recover after 10 ticks?)
     - also add death status/removal from sim.

Grid - Can be initialized with any number of rows/colums/people-count
     - Initialize a simulation with 'object name here' = simGrid.Grid(# rows, # columns, # people in sim)
     - Begins with a random configuration of people
     - As of now, can infect a group of people at beginning with .infectLot(n) 
     - Can output current grid configuration to screen with .printGrid()

From here we can add a class to keep track of statistics.
We can implement different logic for the movements of the People turn by turn as well.