from pieces import *
from os import system
import random

class ChessBoard():
    def __init__(self, test = False):
        self.board = [[None for i in range (0,8)] for j in range(0,8)]
        self.turn = "W"
        self.piece_set = set()
        if test == False: self.setup_board()
        print("The game has started!")

    def __str__(self):

        repr = ""
        for y in reversed(range(0,8)):
            repr += "  "+ str(y) +"  "
            for x in range(0,8):
                if self.get(x,y) == None:
                     repr += ("  -  ")
                else:
                    repr += (" "+str(self.get(x,y))+" ")
            repr += "\n"
        repr += "       "+ "    ".join([str(num) for num in range(0,8)])
        return repr

    def initialize_piece(self, piece, new_pos_x, new_pos_y):
        self.piece_set.add(piece)
        self.board[new_pos_y][new_pos_x] = piece
        piece.set_position(new_pos_x, new_pos_y)
        piece.moved = False

    def change_turn(self):
        self.turn = "W" if self.turn == "B" else "B"

    def get(self, x, y):
        return self.board[y][x]

    def move_piece(self, piece, new_pos_x, new_pos_y):
        ##set old position to None
        self.board[piece.y][piece.x] = None

        ##if piece is being taken, set the piece as taken
        if self.get(new_pos_x, new_pos_y) != None:
            self.get(new_pos_x,new_pos_y).taken == True

        self.board[new_pos_y][new_pos_x] = piece
        piece.set_position(new_pos_x, new_pos_y)
        self.change_turn()

    def setup_board(self):
        ## add pieces to the board and set up empty-square tracker
        for letter,pos in zip(["W", "B"],[0,7] ):
            self.initialize_piece(King(letter), 4, pos)
            self.initialize_piece(Queen(letter), 3, pos)
            self.initialize_piece(Rook(letter), 0, pos)
            self.initialize_piece(Rook(letter), 7, pos)
            self.initialize_piece(Bishop(letter), 2, pos)
            self.initialize_piece(Bishop(letter), 5, pos)
            self.initialize_piece(Knight(letter), 1, pos)
            self.initialize_piece(Knight(letter), 6, pos)
        for letter,y in zip(["W", "B"],[1,6] ):
            for x in range(0,8):
                self.initialize_piece(Pawn(letter),x, y)

    def take_turn(self):
        piece, move = random.choice(self.get_moves())
        piece_repr = str(piece), piece.x, piece.y
        self.move_piece(piece, move.x, move.y)
        return piece_repr, move

    def get_moves(self):
        self.moves = []
        for piece in self.piece_set:
            if piece.get_color() == self.turn:
                self.piece_moves = piece.get_moves(self)
                if self.piece_moves:
                    self.moves.extend(
                        [(piece, move) for move in self.piece_moves])
        return self.moves
