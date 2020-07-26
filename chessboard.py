from pieces import *
from os import system
import random
from copy import deepcopy


class ChessBoard(object):
    def __init__(self, duplicate = False):
        self.board = [[None for i in range (0,8)] for j in range(0,8)]
        self.piece_set = set()
        self.move_stack = []
        if duplicate == False: self.setup_board()
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

    def get(self, x, y):
        return self.board[y][x]

    def move_piece(self, piece, new_pos_x, new_pos_y):
        ##set old position to None
        board = self.board
        board[piece.y][piece.x] = None
        ##if piece is being taken, set the piece as taken
        self.move_stack.append((piece, piece.x, piece.y, new_pos_x, new_pos_y,
            self.get(new_pos_x, new_pos_y)))
        if self.get(new_pos_x, new_pos_y) != None:
            self.get(new_pos_x,new_pos_y).taken = True
            self.piece_set.remove(self.get(new_pos_x,new_pos_y))
        self.board[new_pos_y][new_pos_x] = piece
        piece.set_position(new_pos_x, new_pos_y)
        return board

    def undo_move(self):
        board = self.board
        move = self.move_stack.pop()
        piece, old_x, old_y, moved_x, moved_y, captured_piece = move
        board[old_y][old_x] = piece
        piece.set_position(old_x, old_y)
        board[moved_y][moved_x] = captured_piece
        if captured_piece:
            captured_piece.set_position(moved_x, moved_y)
            captured_piece.taken = False
            self.piece_set.add(captured_piece)


    def initialize_piece(self, piece, new_pos_x, new_pos_y):
        self.piece_set.add(piece)
        self.board[new_pos_y][new_pos_x] = piece
        piece.set_position(new_pos_x, new_pos_y)
        piece.moved = False

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

    def duplicate_board(self):
        return deepcopy(self)
