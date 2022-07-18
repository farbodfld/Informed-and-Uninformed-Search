import pygame
import colors
from params import *
from Environment import Board
from Agent import Agent

from Useful_Functions import Point
from DFS_Algorithm import DFS
from BFS_Algorithm import BFS
from astar import *

# initialize:
FPS = 60
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Search Game")

# setting start and end point :
start = {'x': 6, 'y': 0}
end = {'x': 12, 'y': 0}

gameBoard = Board(start, end)
agent = Agent(gameBoard)

source = Point(6, 0)
dest = Point(12, 0)


def main():
    run = True
    clock = pygame.time.Clock()
    WIN.fill(colors.black)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        gameBoard.draw_world(WIN)

        '''####################################################'''
        '''You can check the algorithm by uncommenting each of them!
            By default A* algorithm is running.'''

        "BFS(gameBoard.boardArray, source, dest)"

        DFS(gameBoard.boardArray, source, dest)

        # board_game = numpy.array(make_helper_array(gameBoard.boardArray, 13, 13))
        # path_list = astar_algorithm(board_game, (0, 6), (0, 12))
        # del path_list[0]
        # for pointer in range(len(path_list)):
        #     current_path = path_list[pointer]
        #     gameBoard.boardArray[current_path[1]][current_path[0]].set_color(colors.white)

        '''#####################################################'''
    pygame.quit()


if __name__ == "__main__":
    main()
