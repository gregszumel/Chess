# print(" . ".join([str(x) for x in range(0,10)]))
from chessboard import *
import random

# Class to play a game of chess
class Chess():

    def __init__(self):
        self.game_state = ChessBoard()
        self.turn = "W"

    def get_other_turn(self):
        if self.turn == "B":
            return "W"
        else:
            return "B"

    def get_moves(self, turn):
        #takes a game state and returns the possible set of moves
        board = self.game_state.board
        moves = []
        for piece in self.game_state.piece_set:
            if piece.get_color() == turn:
                piece_moves = piece.get_moves(board)
                if piece_moves:
                    moves.extend(
                        [(piece, move) for move in piece_moves])
        return moves

    def get_opponent_moves(self, piece, move):
        #makes a move, checks to see what the opponent moves are,
        #undoes move
        self.game_state.move_piece(piece, move.x, move.y)
        moves = self.get_moves(self.get_other_turn())
        self.game_state.undo_move()
        return moves

    def non_check_moves(self, moves):
        #takes a set of moves and evaluates if those moves allow the
        #king to be captured next move
        non_check_moves = []
        for piece, move in moves:
            opp_moves = self.get_opponent_moves(piece, move)
            for _, opp_move in opp_moves:
                if opp_move.movetype == "Take":
                    print(opp_move)
                    if piece.get_name() != "K":
                        non_check_moves.append((piece, move))
                else:
                    non_check_moves.append((piece, move))
        return non_check_moves

    def get_legal_moves(self):
        all_moves = self.get_moves(self.turn)
        print(all_moves)
        print(self.non_check_moves(all_moves))
        return self.non_check_moves(all_moves)

    def take_turn(self):
        piece, move = random.choice(self.get_legal_moves())
        piece_repr = str(piece), piece.x, piece.y
        self.board = self.game_state.move_piece(piece = piece,
            new_pos_x= move.x, new_pos_y = move.y)
        self.turn = self.get_other_turn()
        return piece_repr, move
