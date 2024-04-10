import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

class GridVisualizer:
    def __init__(self, grid):
        self.grid = grid
        self.fig, self.ax = plt.subplots()
        self.squares = None
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

    def update_plot1(self, frame):
        for i in range(self.grid.rows):
            for j in range(self.grid.columns):
                cell = self.grid.grid[i][j]
                if cell is None:
                    color = 'white'  # Empty cell
                elif cell.state == 'Susceptible':
                    color = 'green' if not cell.facemask else 'lightgreen'  # Susceptible with or without facemask
                elif cell.state == 'Infected':
                    color = 'red'  # Infected
                elif cell.state == 'Recovered':
                    color = 'blue'  # Recovered
                elif cell.state == 'Dead':
                    None
                self.squares[i, j].set_facecolor(color)
        self.grid.advance_turn_sim1()
        self.turn += 1
        if self.grid.all_sick():
            return

    def update_plot2(self, frame):
        for i in range(self.grid.rows):
            for j in range(self.grid.columns):
                cell = self.grid.grid[i][j]
                if cell is None:
                    color = 'white'  # Empty cell
                elif cell.state == 'Susceptible':
                    color = 'green' if not cell.facemask else 'lightgreen'  # Susceptible with or without facemask
                elif cell.state == 'Infected':
                    color = 'red'  # Infected
                elif cell.state == 'Recovered':
                    color = 'blue'  # Recovered
                elif cell.state == 'Dead':
                    None
                self.squares[i, j].set_facecolor(color)
        self.grid.advance_turn_sim2()
        self.turn += 1
        if self.grid.all_sick_dead_or_healthy():
            return

    def update_plot3(self, frame):
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
                    None
                self.squares[i, j].set_facecolor(color)
        self.grid.advance_turn_sim3()
        self.turn += 1
        if self.grid.all_sick_dead_or_healthy():
            return

    def animate1(self, frames):
        self.init_plot()  # Initialize the plot
        anim = animation.FuncAnimation(self.fig, self.update_plot1, frames=frames, interval=1000, repeat=False)
        plt.show()

    def animate2(self, frames):
        self.init_plot()  # Initialize the plot
        anim = animation.FuncAnimation(self.fig, self.update_plot2, frames=frames, interval=1000, repeat=False)
        plt.show()

    def animate3(self, frames):
        self.init_plot()  # Initialize the plot
        anim = animation.FuncAnimation(self.fig, self.update_plot3, frames=frames, interval=1000, repeat=False)
        plt.show()
