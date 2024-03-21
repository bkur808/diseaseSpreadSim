Disease Spread Simulator

SAMPLE TEST CODE TO TRY OUT PROJECT - GUI NOT CURRENTLY SETUP IN simVis.py FILE (TODO)

import simGrid
myTest = simGrid.Grid(20,20,50) ; myTest.infectLot(1) ; myTest.printGrid()

myTest.advanceTime() ; myTest.printGrid()
myTest.advanceTime() ; myTest.printGrid()
........can repeat as many times as wanted to test

Current class structures:

Grid structure can be initialized with any # or rows, columns, and residents.
 -there are methods for infecting lot (# of initial infections)
 -getting neighbors
 -advancing time forward one step (all people move and can be infected)
 -infections occur after all individuals have moved in advanceTime

 People structure are initialized with position and sickness state. There is a global infectious-period constant variable for sickness length. 
 They have a move method, which as of now works by choosing a random empty neighbor position to move into. Can be changed by situation.
