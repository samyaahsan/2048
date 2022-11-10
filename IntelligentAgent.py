import random
from BaseAI import BaseAI
import time
import numpy as np
class IntelligentAgent(BaseAI):

    def __init__(self):
        pass

    def getMove(self, grid):
    # Selects a random move and returns it
        #start = time.time()
        moveset = self.maximize(grid, 0, float('-inf'), float('inf'))[0]
        return moveset

    def heuristic(self, grid):
        #snake
        grid_copy = grid.clone()
        grid_copy = grid_copy.map
        matrix = []


        weights = [[4 ** 15, 4 **  14, 4 **  13, 4 **  12], [4 ** 8, 4 ** 9, 4 ** 10, 4 ** 11], [4 ** 7, 4 ** 6, 4 ** 5, 4 ** 4], [4 ** 0, 4 ** 1, 4 ** 2, 4 ** 3]]
        weighted_grid = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        sum = 0

        for i in range(4):
            # iterating by column by B
            for j in range(4):
                sum += (weights[i][j] * grid_copy[i][j])



        return sum

    #computer's move
    def minimize(self, grid, depth, alpha, beta):
        if self.terminal_test(grid):
            return (None, self.heuristic(grid)) #heuristic == number of empty cells

        if depth >= 3:
            #print("here")
            return (None, self.heuristic(grid))

        (min_child, min_utility) = (None, float('inf'))

        for cell in grid.getAvailableCells():
            grid2 = grid.clone()
            grid2.insertTile(cell, 2)
            grid4 = grid.clone()
            grid4.insertTile(cell, 4)
            #print("before")
            utility = (0.9 * self.maximize(grid2, depth + 1, alpha, beta)[1]) + (0.1 * self.maximize(grid4, depth + 1, alpha, beta)[1])
            #print("after")
            #(__, utility) = self.maximize(cell, depth + 1)

            if utility < min_utility:
                (min_child, min_utility) = (cell, utility)

            if min_utility <= alpha:
                break

            if min_utility < beta:
                beta = min_utility

        return (min_child, min_utility)

    #player's move
    def maximize(self, grid, depth, alpha, beta):
        if not grid.getAvailableMoves():
            return (None, self.heuristic(grid))

        if depth >= 3:
            return (None, self.heuristic(grid))

        (max_child, max_utility) = (None, float('-inf'))

        #TODO: change naming
        for cell in grid.getAvailableMoves():
            utility = self.minimize(cell[1], depth + 1, alpha, beta)[1]

            if utility > max_utility:
                (max_child, max_utility) = (cell[0], utility)

            if max_utility >= beta:
                break

            if max_utility > alpha:
                alpha = max_utility

        #child = (move, grid w/ move)
        return (max_child, max_utility)


    def terminal_test(self, grid):
        if not(grid.canMove()):
            #or grid.getMaxTile() >= 2048
            return True
        else:
            return False
        # def getMove(self, grid):
        #     (child, __) =  maximize(grid)
        #     return child




