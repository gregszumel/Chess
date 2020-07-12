from pieces import *

class ChessBoard(object):

    def __init__(self):
        self.board = [[None for i in range (0,8)] for j in range(0,8)]
        self.color_turn = "W"
        self.piece_list = []
        self.setup_board()
        print("The game has started!")
        self.print_board()

    def print_board(self):
        for row in self.board:
            print("")
            for column in row:
                if column == None:
                    print("  .  ", end = "")
                else:
                    print(" "+column.get_color()+ "-"
                        + column.get_name()+" ", end = "")

    def initialize_piece(self, piece, new_pos_x, new_pos_y):
        self.piece_list.append(piece)
        self.board[new_pos_x][new_pos_y] = piece
        piece.set_position(new_pos_x, new_pos_y)

    def change_turn(self):
        self.color_turn = "W" if self.color_turn = "B" else "B"

    def move_piece(self, piece, new_pos_x, new_pos_y):
        ##set old position to None
        self.board[piece.x][piece.y] = None

        ##if piece is being taken, set the piece as taken
        if self.board[new_pos_x,][new_pos_y] != None:
            self.board[new_pos_x][new_pos_y].taken()

        self.board[new_pos_x][new_pos_y] = piece
        piece.set_position(new_pos_x, new_pos_y)
        self.change_turn()

    def setup_board(self):
        ## add pieces to the board and set up empty-square tracker
        for letter,pos in zip(["B", "W"],[0,7] ):
            self.initialize_piece(Rook(letter), pos,0)
            self.initialize_piece(Knight(letter), pos,1)
            self.initialize_piece(Bishop(letter), pos,2)
            self.initialize_piece(Queen(letter), pos,3)
            self.initialize_piece(King(letter), pos,4)
            self.initialize_piece(Bishop(letter), pos,5)
            self.initialize_piece(Knight(letter), pos,6)
            self.initialize_piece(Rook(letter), pos,7)
        for letter,pos in zip(["B", "W"],[1,6] ):
            for column in range(0,8):
                self.initialize_piece(Pawn(letter), pos,column)

    def take_turn(self):
        moves = self.get_moveset()
        random = 0 ## todo: update to random number
        self.move_piece(moves[random])
        if self.turn = "W":
            self.turn = "B"
        else:
            selft.turn = "W"
        pass

    def get_moves(self):
        moves = []
        for piece in self.piece_list:
            if piece.get_color() = self.turn:
                moves.extend(piece.get_moves(self.board))
        return moves
