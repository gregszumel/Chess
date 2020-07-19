from pieces import *
from os import system

class ChessBoard():

    def __init__(self, test = False):
        self.board = [[None for i in range (0,8)] for j in range(0,8)]
        self.turn = "W"
        self.piece_set = set()
        if test == False: self.setup_board()
        print("The game has started!")

    def __str__(self):
        repr = ""
        for i in reversed(range(0,8)):
            repr += "  "+ str(i) +"  "
            for j in range(0,8):
                if self.get_position(i,j) == None:
                     repr += ("  -  ")
                else:
                    repr += (" "+str(self.get_position(i,j))+" ")
            repr += "\n"
        repr += "       "+ "    ".join([str(num) for num in range(0,8)])
        return repr


    def initialize_piece(self, piece, new_pos_x, new_pos_y):
        self.piece_set.add(piece)
        self.board[new_pos_y][new_pos_y] = piece
        piece.set_position(new_pos_x, new_pos_y)

    def change_turn(self):
        self.turn = "W" if self.turn == "B" else "B"

    def get_position(self, x, y):
        return self.board[y][x]

    def move_piece(self, piece, new_pos_x, new_pos_y):
        ##set old position to None
        self.board[piece.y, piece.x] = None

        ##if piece is being taken, set the piece as taken
        if self.get_position(new_pos_x, new_pos_y) != None:
            self.board[new_pos_y][new_pos_x].taken()

        self.board[new_pos_x][new_pos_y] = piece
        piece.x, piece.y = new_pos_x, new_pos_y
        self.change_turn()

    def setup_board(self):
        ## add pieces to the board and set up empty-square tracker
        for letter,pos in zip(["W", "B"],[0,7] ):
            self.initialize_piece(King(letter), pos,4)
            self.initialize_piece(Queen(letter), pos,3)
            self.initialize_piece(Rook(letter), pos,0)
            self.initialize_piece(Rook(letter), pos,7)
            self.initialize_piece(Bishop(letter), pos,2)
            self.initialize_piece(Bishop(letter), pos,5)
            self.initialize_piece(Knight(letter), pos,1)
            self.initialize_piece(Knight(letter), pos,6)
        for letter,pos in zip(["W", "B"],[1,6] ):
            for column in range(0,8):
                self.initialize_piece(Pawn(letter), pos,column)

    def take_turn(self):
        moves = self.get_moveset()
        random = 0 ## todo: update to random number
        self.move_piece(moves[random])
        if self.turn == "W":
            self.turn = "B"
        else:
            selft.turn = "W"
        pass

    def get_moves(self):
        moves = {}
        for piece in self.piece_set:
            if piece.get_color() == self.turn:
                moves[piece] = piece.get_moves(self.board)
        return moves
