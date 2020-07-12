from chessboard import *

board = ChessBoard()
board.print_board()
print("")

print(to_move.get_position())
board.move_piece(to_move, 2,5)
board.print_board()
for piece in board.piece_list:
    print(piece.get_color() + "-" + piece.get_name())
