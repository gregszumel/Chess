from pieces import *

class ChessBoard(object):

    def __init__(self):
        self.board = [[None for i in range (0,8)] for j in range(0,8)]
        self.setup_board()

    def print_board(self):
        for row in self.board:
            print("")
            for column in row:
                if column == None:
                    print("  .  ", end = "")
                else:
                    print(" "+column.get_color()+ "-"
                        + column.get_name()+" ", end = "")

    def get_piece(self, pos_x, pos_y):
        return self.board[pos_x][pos_y]

    def move_piece(self, piece, new_pos_x, new_pos_y):
        if(piece.get_position()[0] != None):
            old_pos_x = piece.get_position()[0]
            old_pos_y = piece.get_position()[1]
            self.board[old_pos_x][old_pos_y] = None
        self.board[new_pos_x][new_pos_y] = piece
        piece.set_position(new_pos_x, new_pos_y)

    def setup_board(self):
        for letter,pos in zip(["B", "W"],[0,7] ):
            self.move_piece(Rook(letter), pos,0)
            self.move_piece(Knight(letter), pos,1)
            self.move_piece(Bishop(letter), pos,2)
            self.move_piece(Queen(letter), pos,3)
            self.move_piece(King(letter), pos,4)
            self.move_piece(Bishop(letter), pos,5)
            self.move_piece(Knight(letter), pos,6)
            self.move_piece(Rook(letter), pos,7)
        for letter,pos in zip(["B", "W"],[1,6] ):
            for column in range(0,8):
                self.move_piece(Pawn(letter), pos,column)
