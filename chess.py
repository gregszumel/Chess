from chessboard import *

board = ChessBoard()
board.print_board()
print("")
to_move = board.get_piece(1,5)
print(to_move.get_position())
board.move_piece(to_move, 2,5)
board.print_board()
