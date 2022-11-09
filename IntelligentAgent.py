import random
from BaseAI import BaseAI
class IntelligentAgent(BaseAI):

    def __init__(self):
        pass

    def getMove(self, grid):
    # Selects a random move and returns it
        moveset = self.maximize(grid, 0)[0][0]
        return moveset

    def heuristic(self, grid):
        return grid.getMaxTile()

    #computer's move
    def minimize(self, grid, depth):
        if self.terminal_test(grid):
            return (None, self.heuristic(grid)) #heuristic == number of empty cells

        if depth >= 3:
            print("here")
            return (None, self.heuristic(grid))

        (min_child, min_utility) = (None, float('inf'))

        for cell in grid.getAvailableCells():
            grid2 = grid.clone()
            grid2.insertTile(cell, 2)
            grid4 = grid.clone()
            grid4.insertTile(cell, 4)
            #issue HERE?
            print("before")
            utility = (0.9 * self.maximize(grid2, depth + 1)[1]) + (0.1 * self.maximize(grid4, depth + 1)[1])
            print("after")
            #(__, utility) = self.maximize(cell, depth + 1)

            if utility < min_utility:
                (min_child, min_utility) = (cell, utility)

        return (min_child, min_utility)

    #player's move
    def maximize(self, grid, depth):
        if not grid.getAvailableMoves():
            return (None, self.heuristic(grid))

        if depth >= 3:
            return (None, self.heuristic(grid))

        (max_child, max_utility) = (None, float('-inf'))

        for cell in grid.getAvailableMoves():
            utility = self.minimize(grid, depth + 1)[1]

            if utility > max_utility:
                (max_child, max_utility) = (cell, utility)

        #child = (move, grid w/ move)
        return (max_child, max_utility)


    def terminal_test(self, grid):
        if not(grid.canMove()) or grid.getMaxTile() >= 2048:
            return True
        else:
            return False
        # def getMove(self, grid):
        #     (child, __) =  maximize(grid)
        #     return child




