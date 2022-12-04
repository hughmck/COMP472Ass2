from Board import Board
from State import State

s1 = State()

s1.puzzle_input()
s1.print_board()

all_moves = s1.get_moves()
s1.get_moves(all_moves[0])
