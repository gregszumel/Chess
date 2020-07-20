# print(" . ".join([str(x) for x in range(0,10)]))
from chessboard import *
import random

board = ChessBoard()


for x in range(0,1000000):
    system('clear')

    potential_moves = board.get_moves()

    piece, move = board.take_turn()
    print(board)
    for combo in sorted(potential_moves):
        print(combo)
    print("Selected move: "+ str([piece, move]))
    input()
