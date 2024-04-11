import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

class GridVisualizer:
    def __init__(self, grid):
        self.grid = grid
        self.fig, self.ax = plt.subplots()
        self.squares = None
        self.repeat_anim = True
        self.turn = 0

    def init_plot(self):
        self.squares = np.empty((self.grid.rows, self.grid.columns), dtype=object)
        for i in range(self.grid.rows):
            for j in range(self.grid.columns):
                square = Rectangle((j, self.grid.rows - i - 1), 1, 1, edgecolor='black', lw=0.5)
                self.ax.add_patch(square)
                self.squares[i, j] = square
        self.ax.set_xlim(0, self.grid.columns)
        self.ax.set_ylim(0, self.grid.rows)

    def update_vis_grid(self):
        for i in range(self.grid.rows):
            for j in range(self.grid.columns):
                cell = self.grid.grid[i][j]
                if cell is None:
                    color = 'white'  # Empty cell
                elif cell.state == 'Susceptible':
                    color = 'green' if not cell.facemask else 'lightgreen'  # Susceptible with or without facemask
                elif cell.state == 'Infected':
                    color = 'red' if not cell.facemask else 'pink' # Infected
                elif cell.state == 'Recovered':
                    color = 'blue'  # Recovered
                elif cell.state == 'Dead':
                    continue
                self.squares[i, j].set_facecolor(color)

    def update_plot1(self, frame):
        self.update_vis_grid()
        self.grid.advance_turn_sim1()
        self.turn += 1
        if self.grid.all_sick():
            self.update_vis_grid()
            self.repeat_anim = False
            return False

    def update_plot2(self, frame):
        self.update_vis_grid()
        self.grid.advance_turn_sim2()
        self.turn += 1
        if self.grid.all_recovered_dead_or_healthy():
            self.update_vis_grid()
            self.repeat_anim = False
            return False

    def update_plot3(self, frame):
        self.update_vis_grid()
        self.grid.advance_turn_sim3()
        self.turn += 1
        if self.grid.all_recovered_dead_or_healthy():
            self.update_vis_grid()
            self.repeat_anim = False
            return False
        
            

    def animate1(self):
        self.init_plot()  # Initialize the plot
        anim = animation.FuncAnimation(self.fig, self.update_plot1,interval=1000, repeat=self.repeat_anim)
        plt.show()

    def animate2(self):
        self.init_plot()  # Initialize the plot
        anim = animation.FuncAnimation(self.fig, self.update_plot2, interval=1000, repeat=self.repeat_anim)
        plt.show()

    def animate3(self):
        self.init_plot()  # Initialize the plot
        anim = animation.FuncAnimation(self.fig, self.update_plot3, interval=1000, repeat=self.repeat_anim)
        plt.show()
