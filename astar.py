from heapq import *

import numpy
import colors
from main import gameBoard


def make_helper_array(matrix, row: int, col: int):
    helper = []
    for i in range(row):
        arr = []
        for j in range(col):
            arr.append(0)
        helper.append(arr)

    for k in range(row):
        for L in range(col):
            if matrix[k][L].is_blocked():
                helper[L][k] = 0
            else:
                helper[L][k] = 1

    return helper


def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def astar_algorithm(array, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    close_set = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    o_heap = []

    data = []

    heappush(o_heap, (f_score[start], start))

    while o_heap:

        current = heappop(o_heap)[1]

        if current == goal:
            # data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = g_score[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 0:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= g_score.get(neighbor, 0):
                continue

            if tentative_g_score < g_score.get(neighbor, 0) or neighbor not in [i[1] for i in o_heap]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(o_heap, (f_score[neighbor], neighbor))

    return False
