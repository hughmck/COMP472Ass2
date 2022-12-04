class Board:
    def __init__(self, cost, board_state, ):
        self.cost = cost
        self.board_state = board_state

    def add_cost(self):
        self.cost = self.cost + 1

    def clone_board(self):
        cloned = Board(0, None)
        cloned.board_state = self.board_state
        cloned.cost = self.cost
        return cloned
