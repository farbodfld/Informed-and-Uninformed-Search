ROW = 13
COL = 13


# For storing the position of each tile in board.
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# Creating node for each tile to save it in queue.
class queueNode:
    def __init__(self, pt: Point):
        self.pt = pt  # The coordinates of the cell

def isValid(row: int, col: int):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# These arrays are used to get row and column of 4 neighbours of a given cell
rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]