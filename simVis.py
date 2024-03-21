import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

class GridVisualizer:
    def __init__(self, grid):
        self.grid = grid
        self.fig, self.ax = plt.subplots()
        self.rectangles = []
        self.turn = 0
        self.frames = 0

    def init_plot(self):
        for i in range(self.grid.rows):
            for j in range(self.grid.columns):
                rect = Rectangle((j, self.grid.rows - i - 1), 1, 1, edgecolor='black', lw=0.5)
                self.ax.add_patch(rect)
                self.rectangles.append(rect)
        self.ax.set_xlim(0, self.grid.columns)
        self.ax.set_ylim(0, self.grid.rows)

    def animate(self, frames):
       self.init_plot()  # Initialize the plot
       anim = animation.FuncAnimation(self.fig, self.update_plot, frames=frames, fargs=(self.grid,), interval=1000, repeat=False)
       plt.show()

    def update_plot(self, _, grid):
       grid.advanceTime()  # Progress the simulation by one turn
       self.turn += 1
       for i, individual in enumerate(grid.people):
          x, y = individual.position
          index = x * grid.columns + y
          self.rectangles[index].set_xy((y, grid.rows - x - 1))
          state = individual.state
          color = 'green' if state == 'Not Sick (Yet)' else 'red' if state == 'Sick' else 'blue' if state == 'Over it - Immune' else 'white'
          self.rectangles[index].set_facecolor(color)
       self.fig.suptitle(f'Turn: {self.turn}')
       if grid.all_sick():
          self.anim.event_source.stop()
       elif self.turn >= self.frames:
          self.anim.event_source.stop()

 

