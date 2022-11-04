import random
from BaseAI import BaseAI
class IntelligentAgent(BaseAI):
    def getMove(self, grid):
    # Selects a random move and returns it
        moveset = grid.getAvailableMoves()
        return random.choice(moveset)[0] if moveset else None

    def heuristic(self, grid):
        return len(grid.getAvailableCells)

    def minimize(self, grid):
        if not grid.getAvailableCells():
            return (None, self.heuristic(grid)) #heuristic == number of empty cells

        (min_child, min_utility) = (None, float('inf'))

        for cell in grid.getAvailableCells():
            (__, utility) = self.maximize(cell)

            if utility <  min_utility:
                (min_child, min_utility) = (self.child, utility)

        return (min_child, min_utility)





