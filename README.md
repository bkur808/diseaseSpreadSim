Disease Spread Simulation:

Presented in this simulator are three distinct scenarios which we are testing:

        Scenario 1: 100x100 grid with 60% grid-population density - 0% fatality, running until all infected

        Scenario 2: Same grid + population. 10% fatality for 20 turn sickness - running until all recovered, healthy, or dead (no more current sick)

        Scenario 3: Same parameters as scenario 2 - implementation of masks with 50% adherence and 50% effectiveness  for both healthy and sick wearers (prevent healthy from catching and sick from spreading)
        Additionally during the peak of their sickness (turns 15-3 of 20 turn sickness) people stop moving (quarantine)

There are three basic ways to run our simulations, each will be explained below:

        1 - Manually - turn-by-turn
        2 - Automatically with Visual
        3 - For Statistical Analysis
        *For all scenarios assuming running a terminal with python3 installed, and all source files in source directory 

1 - Manually:

        Initializing - terminal commands below
                import simGrid ; test = simGrid.Grid() 
                test.test1()    (or test2()/test3() for other premade scenarios)
                
        Running and Printing (visual + stats)
                test.print_grid() ; test.print_stats() ; test.stat_log ; test.advance_turn_sim1()   
                - (or advance_turn_sim2()/advance_turn_sim3() for other premade scenarios)
                - This can be repeated as many times as wanted for testing

        If you want to initialize a custom grid you can do so with the following: 
                (filling in custom values for variables below)

                import simGrid 
                test = simGrid.Grid(# Rows, # Columns, Person Count, With/Without Masks Boolean, Mask adherance rate (0-1))
                test.infect_lot(n, # turns for infectious period, deadly disease boolean, first sick people immortal boolean)

                In custom scenarios I would recommend advancing turns using advance_turn_sim3() as presented above. 
                (sim3 methods include the most functionality implementations) - although sick people also stop moving during the middle of their sickness

2 - Automatically with Visual - for scenarios 1-3 (not implemented for custom scenarios as of yet):

        import simGrid ; test = simGrid.Grid() ; test.run_sim1_vis() (or run_sim2_vis()/run_sim3_vis())

        *Note - couldn't figure out how to end animations automatically given conditions (remnants in code to figure out later), so this may cause issue - can just x out of visuals at end for now...

3 - Running Simulations for statistical analysis:

        import simGrid
        test = simGrid.Grid()
        test.run_sim1(n)        # where n is the number of simulations you want to run
                                # can also use run_sim2(n) or run_sim3(n)
                                # results are recored in a csv file for analysis later
                                # Recorded is the average stats for each turn in the simulation over n trials
                                # WARNING THE FILE NAMES ARE CURRENTLY HARDCODED AND WILL SAVE OVER OLD RUNS
                                # OUR STATISTICS FOR OUR PRESENTATIONS ARE SAVED IN OUTSIDE FILES

Updated 5/7/24
