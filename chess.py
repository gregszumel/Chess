# print(" . ".join([str(x) for x in range(0,10)]))



from chessboard import *

board = ChessBoard(test= "test")
# board.initialize_piece(Bishop("W"), 4, 4)
print(board)

# for piece,moveset in board.get_moves().items():
#     print(str(piece) + ": " +str(piece.x) + ", " + str(piece.y))
#     print(moveset)
board.initialize_piece(Pawn("W"), 4, 3)
board.initialize_piece(King("W"), 4, 4)
board.initialize_piece(Queen("W"), 4, 5)
board.initialize_piece(Knight("W"), 4, 6)
print(board)
