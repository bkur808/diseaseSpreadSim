Disease Spread Simulator
4/9

HOW TO RUN CODE CURRENTLY:
    import simGrid_redo ; test = simGrid_redo.Grid() ; test.runSim1(100) # This will run the first sim 100 times
    import simGrid_redo ; test = simGrid_redo.Grid() ; test.runSim2(100) # This will run the second sim 100 times
    import simGrid_redo ; test = simGrid_redo.Grid() ; test.runSim3(100) # This will run the third sim 100 times

If you want to mess around with testing a grid you can do as follows:
    test.test1() ; test.print_grid() ; test.print_stats() ; test.stat_log ; test.advance_turn_sim1()
    .......... OUTPUT WILL GO HERE WHEN YOU RUN ABOVE CODE
    .......... YOU CAN TEST A SIMULATION TURN BY TURN WITH THE FOLLOWING LINE
    test.print_grid() ; test.print_stats() ; test.stat_log ; test.advance_turn_sim1()

    The above code can be used for sim 1, 2, or 3 - just swap out the number in the appropriate spot i.e. test.test2() or test.advance_turn_sim3()

You can also instantiate a grid through the following steps below:

1 - import simGrid_redo
2 - test = simGrid_redo.Grid(X,Y,Z,Masks?) 
        In place of X put the rows
        In place of Y put the columns
        In place of Z put the starting population
        Optional Boolean for masks True/False (F default)
3 - test.infect_lot(X,Y,Deadly?)
        In place of X put the # of people to infect
        In place of Y put the # of turns people will be sick
            - Default is 1000 turns
        Optional Boolean for deadly virus
4 - test.print_grid() ; test.print_stats() ; test.stat_log ; test.advance_turn_sim3()
        This will advance you through the simulation turn by turn with printouts of grid and stats



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

