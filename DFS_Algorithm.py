from collections import deque
from Useful_Functions import *
from colors import lightBlue


def DFS(matrix, src: Point, dest: Point):
    visited = [[False for i in range(COL)]
               for j in range(ROW)]

    visited[src.x][src.y] = True

    stack = deque()
    prev = {}

    s = queueNode(src)
    stack.append(s)

    while stack:

        curr = stack.pop()
        pt = curr.pt

        if pt.x == dest.x and pt.y == dest.y:
            break

        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            if isValid(row, col) and not matrix[row][col].is_blocked() and not visited[row][col]:
                visited[row][col] = True
                adjacent_cell = queueNode(Point(row, col))
                stack.append(adjacent_cell)
                prev[(row, col)] = (pt.x, pt.y)

    ptr = (12, 0)
    while prev.get(ptr) != (6, 0):
        ptr = prev.get(ptr)
        matrix[ptr[0]][ptr[1]].set_color(lightBlue)

    return -1
