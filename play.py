from chessboard import *
import engine


game = engine.Chess()
# duped_game_state = game.game_state.duplicate_board()
print(game.game_state)
for i in range(0, 10):
    game.take_turn()
# print(piece, move)
# for opp_move in game.get_opponent_moves(piece, move):
#     print(opp_move)
# game.game_state.move_piece(piece, move.x, move.y)
print(game.game_state)
piece, new_move = game.get_moves(game.turn)[-1]
print(piece, new_move)

for move in game.get_opponent_moves(piece, new_move):
    print(move)
# for move in game.get_opponent_moves():

# print(game.game_state.)
# print(duped_game_state)
