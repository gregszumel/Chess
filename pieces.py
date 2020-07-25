from collections import namedtuple

class Piece():
    def __init__(self, color):
        self.color = color
        self.x = None
        self.y = None
        self.taken = False
        self.moved = False
        self.Moveset = namedtuple("Moveset", "movetype x y")
        self.value = None

    def __str__(self):
        return self.get_color()+ "-" + self.get_name()

    def __repr__(self):
        repr = self.get_color()+ "-" + self.get_name()
        repr += "(" + str(self.x) + "," + str(self.y) +")"
        return repr

    def __gt__(self, other_piece):
        same_piece = str(self) + str(self.x) + str(self.y)
        diff_piece = str(other_piece) + str(other_piece.x) + str(other_piece.y)
        return  same_piece > diff_piece

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.moved = True

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def moves_in_direction(self, x, y, board, direction):
        #Sends a piece in a direction and continues to add (x,y) coordinates to
        #the list *moved* until it hits a piece/edge of board
        blocked = False
        x_dir, y_dir = direction
        while not blocked:

            valid, new_pos = self.valid_move(x,y,direction,board)

            # print("X: " + str(x) + ". Y: " + str(y))
            # print(valid)

            if valid and new_pos:
                #append directly to self.moves
                self.moves.append(self.Moveset("Take", x + x_dir, y+y_dir))
                blocked = True
            elif valid:
                self.moves.append(self.Moveset("Move", x + x_dir, y+y_dir))
            else:
                blocked = True

            x += x_dir
            y += y_dir

    def valid_move(self, x,y, direction, board):
    # Returns if a moving a given x,y position
    # on a board is valid, and the value
        x_dir, y_dir = direction
        if 0 <= x+x_dir < 8 and 0 <= y+y_dir < 8:
            new_pos = board[y + y_dir][x+x_dir]
            if new_pos is None or new_pos.color != self.color:
                return True, new_pos
            else:
                return False, new_pos
        else:
            return False, None

    def taken(self):
        self.taken = True


class King(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.directions = [
            (1,1), (1,0), (1,-1), (0,1),
            (-1,0), (-1,1), (-1,0), (-1,-1)]
        self.value = 999

    def get_name(self):
        return "K"

    def get_moves(self, board):
        self.moves = []
        for direction in self.directions:
            valid, pos = self.valid_move(self.x, self.y, direction, board)
            if(valid):
                x_dir, y_dir = direction
                if pos:
                    self.moves.append(
                        self.Moveset("Take", self.x + x_dir, self.y + y_dir))
                else:
                    self.moves.append(
                        self.Moveset("Move", self.x + x_dir, self.y + y_dir))
        return self.moves


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.directions = [
            (1,1), (1,0), (1,-1),
            (0,1), (0,-1),
            (-1,1), (-1,0), (-1,-1)]
        self.value = 9
    def get_name(self):
        return "Q"

    def get_moves(self, board):
        self.moves = []
        for direction in self.directions:
            self.moves_in_direction(self.x, self.y
                , board, direction)
        return self.moves


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.directions = [(1,0), (0,1), (-1,0), (0,-1)]
        self.value = 5

    def get_name(self):
        return "R"

    def get_moves(self, board):
        self.moves = []
        for direction in self.directions:
            self.moves_in_direction(self.x, self.y
                , board, direction)
        return self.moves


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.directions = [
            (2,1), (2,-1), (-2,1), (-2,-1),
            (1,2), (1,-2), (-1,2), (-1,-2)]
        self.value = 3

    def get_name(self):
        return "N"

    def get_moves(self, board):
        self.moves = []
        for direction in self.directions:
            valid, pos = self.valid_move(self.x, self.y, direction, board)
            if valid:
                new_pos_x = self.x + direction[0]
                new_pos_y = self.y + direction[1]
                if pos:
                    self.moves.append(
                        self.Moveset("Take", new_pos_x, new_pos_y))
                else:
                    self.moves.append(
                        self.Moveset("Move", new_pos_x, new_pos_y))
        return self.moves

class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
        self.value = 4

    def get_name(self):
        return "B"

    def get_moves(self, board):
        self.moves = []
        for direction in self.directions:
            self.moves_in_direction(self.x, self.y
                , board, direction)
        return self.moves


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == "W":
            self.forward_directions = [(0,1), (0,2)]
            self.diagonal_directions = [(1,1),(-1,1)]
        else:
            self.forward_directions = [(0,-1), (0,-2)]
            self.diagonal_directions = [(1,-1),(-1,-1)]
        self.value = 1

    def get_name(self):
        return "P"

    def get_moves(self, board):
        # pawns move more simply, so all code is here
        self.moves = []
        #1 space forward movement
        for direction in self.forward_directions:
            # if haven't moved, check both 1 and 2 space moves
            if not(self.moved):
                valid, pos = self.valid_move(self.x, self.y, direction, board)
                if valid: self.moves.append(self.Moveset("Move", self.x
                , self.y + direction[1]))
            # if have moved, only check first direction
            elif abs(direction[1]) == 1:
                valid, pos = self.valid_move(self.x, self.y, direction, board)
                if valid: self.moves.append(self.Moveset("Move", self.x
                , self.y + direction[1]))

        #taking diagonally
        for direction in self.diagonal_directions:
            valid, pos = self.valid_move(self.x, self.y, direction
            , board)

            if valid and pos and pos.color != self.color:
                self.moves.append(self.Moveset("Take", pos.x, pos.y))

        return self.moves

    def promote(self):
        pass
