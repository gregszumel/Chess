# print(" . ".join([str(x) for x in range(0,10)]))
from chessboard import *
import random

# Class to play a game of chess
class Chess():
    def non_check_moves(moves, board):
        for move in moves:
            piece, moveset = move
            if piece.get_name() == "K":
                king_x, king_y = king_pos[str(piece)]
                king_x, king_y = king_x + moveset.x, king_y +moveset.y
            else:
                #self.turn should not have changed yet, this is for
                #calculating the same colors turn possibilites, given
                #opponents follow-up moves
                king_x, king_y = king_pos[self.turn +"-K"]
            opp_moves = self.get_future_state(piece, moveset, board)
            if ("Take", king_x, king_y) in opp_moves:
                moves.remove(move)
        return moves

    def get_future_state(self, piece, move, board):
        new_board = self.move_piece(piece, move.x, move.y, board)
        new_turn = new_board.get_other_turn()
        return new_board.get_moves(board = new_board, turn = new_turn)

    def take_turn(self):
        piece, move = random.choice(self.get_moves())
        piece_repr = str(piece), piece.x, piece.y
        self.board = self.move_piece(piece = piece, new_pos_x= move.x,
            new_pos_y = move.y, board = self.board)
        self.turn = self.get_other_turn()
        return piece_repr, move

    def get_moves(self, board, turn):
        moves = []
        for piece in self.piece_set:
            if piece.get_color() == turn:
                self.piece_moves = piece.get_moves(board)
                if self.piece_moves:
                    self.moves.extend(
                        [(piece, move) for move in self.piece_moves])
        return self.non_check_moves(moves, board)

    def get_moves(self):
        moves = []
        for piece in self.piece_set:
            if piece.get_color() == self.turn:
                self.piece_moves = piece.get_moves(self.board)
                if self.piece_moves:
                    self.moves.extend(
                        [(piece, move) for move in self.piece_moves])
        return self.non_check_moves(moves, board)
