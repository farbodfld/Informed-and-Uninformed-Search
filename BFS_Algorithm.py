from collections import deque
from Useful_Functions import *
from colors import red


def BFS(mat, src: Point, dest: Point):
    # check source and destination cell of the matrix is block or not
    if mat[src.x][src.y].is_blocked() or mat[dest.x][dest.y].is_blocked():
        return -1

    visited = [[False for i in range(COL)]
               for j in range(ROW)]

    # Mark the source cell as visited
    visited[src.x][src.y] = True

    # Create a queue for BFS and dictionary for printing the shortest path
    q = deque()
    prev = {}

    # Distance of source cell is 0
    s = queueNode(src)
    q.append(s)

    while q:

        curr = q.popleft()
        pt = curr.pt

        # If we have reached the destination cell, we are done
        if pt.x == dest.x and pt.y == dest.y:
            break

        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # if adjacent cell is valid, has path and not visited yet, enqueue it.
            if isValid(row, col) and not mat[row][col].is_blocked() and not visited[row][col]:
                visited[row][col] = True
                adjacent_cell = queueNode(Point(row, col))
                q.append(adjacent_cell)
                prev[(row, col)] = (pt.x, pt.y)

    # Printing the shortest path from destination to source
    ptr = (12, 0)
    while prev.get(ptr) != (6, 0):
        ptr = prev.get(ptr)
        mat[ptr[0]][ptr[1]].set_color(red)

    return -1
