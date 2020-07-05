import numpy as np
from scipy import signal
import random

class Game:
    """Implementation of Conway's Game of Life using a list of ints.

    Args:
        x (int): X-Axis size.
        y (int): Y-Axis size.
        seed (int, optional): Grid generator seed.
    """    
    
    def __init__(self, x, y):
        self.grid = np.random.randint(2, size=(y, x))
    
    def print_grid(self):
        """Print out the grid into the console."""
        
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                print(self.grid[row][col], end=" ")
            print("\n", end="")
        print("\n", end="")
    
    def cycle(self):
        """Cycle through all of the positions in the grid."""

        kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
        neighbors = signal.convolve2d(self.grid, kernel, "same")

        for row in range(self.grid.shape[0]):
            for col in range(self.grid.shape[1]):
                if self.grid[row,col] == 1 and (neighbors[row,col] == 2 or neighbors[row,col] == 3):
                    self.grid[row,col] = 1
                elif self.grid[row,col] == 0 and neighbors[row,col] == 3:
                    self.grid[row,col] = 1
                else:
                    self.grid[row,col] = 0

    def clear(self):
        self.grid = np.zeros((self.grid.shape[1], self.grid.shape[0]))