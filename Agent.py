import heapq

import colors


class Agent:
    def __init__(self, board):
        self.position = board.get_agent_pos()
        self.current_state = board.get_current_state()

    def get_position(self):
        return self.position

    def set_position(self, position, board):
        self.position = position
        board.set_agent_pos(position)
        board.update_board(self.current_state)

    def percept(self, board):
        # perception :
        # sets the current state
        # Use get_current_state function to get the maze matrix. - make your state
        self.current_state = board.get_current_state()

        pass

    def move(self, direction):
        # make your next move based on your perception
        # check if the move destination is not blocked
        # if not blocked , move to destination - set new position
        # something like :
        self.set_position(self.get_position() + direction)

        pass

    @staticmethod
    def get_actions():
        actions = []
        # returns a list of valid actions
        return actions

    def bfs(self, environment):
        self.percept(environment)
        # now go on !
        pass

    def dfs(self, environment):
        pass

    def a_star(self, environment):
        pass
