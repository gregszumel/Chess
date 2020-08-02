from chessboard import *
import engine


game = engine.Chess()
# duped_game_state = game.game_state.duplicate_board()


for i in range(0, 2):
    game.take_turn()
    print(game.game_state)

# print(game.game_state.)
# print(duped_game_state)
