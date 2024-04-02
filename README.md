Disease Spread Simulator

4/1 
    TODO: FINISH SIM 1-3 - fix stat tracking in Sim 2 advance_turn logic

    SIM 1 is somewhat complete w/o visualizations. 
    SIM 2 is done other than stat tracking - needs logic to be fixed for recovering/dying
    SIM 3 is yet to be started - but only adds one logic component 
            -all stat tracking should work the same

    Can test scenarios with the following prompts:
    import simGrid
    test1 = simGrid.Grid() ; test2 = simGrid.Grid()
    test1.runSim1(10)
    test2.runSim2(10)



3/31

I have updated stuff so that the first simulation can be run non-stop - just have to add stuff 
for averaging statistics and then the graphing portion. 

Simulation can be run by the following code:
import simGrid ; test = simGrid.Grid() ; test.runSim1(1000)

As it stands I am just printing the final stats print-out (on turn when all people infected).

3/21

SAMPLE TEST CODE TO TRY OUT PROJECT - GUI NOT CURRENTLY SETUP IN simVis.py FILE (TODO)

import simGrid ; 
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
