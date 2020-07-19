class Piece(object):
    def __init__(self, color):
        self.color = color
        self.x = None
        self.y = None
        self.taken = False

    def __str__(self):
        return self.get_color()+ "-" + self.get_name()

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def moves_in_direction(self, x, y, board, direction):
        blocked = False
        x_dir, y_dir = direction
        while not blocked:
            x += x_dir
            y += y_dir
            valid, new_pos = self.valid_move(x,y,direction,board)
            if valid and new_pos != None:
                #append directly to self.moves
                self.moves.append([x,y])
                blocked = True
            elif valid:
                self.moves.append([x,y])
            else:
                blocked = True

    def valid_move(self, x,y, direction, board):
    # Returns if a moving a given x,y position
    # on a board is valid, and the value
        x_dir, y_dir = direction
        if 0 <= x+x_dir < 8 and 0 <= y+y_dir < 8:
            new_pos = board[y + y_dir][x + x_dir]
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
        self.directions = [(1,1), (1,0), (1,-1), (0,1), (-1,0)
            , (-1,1), (-1,0), (-1,-1)]

    def get_name(self):
        return "K"

    def get_moves(self, board):
        self.moves = []
        for direction in self.directions:
            valid, _ = self.valid_move(self.x, self.y, direction, board)
            if(valid):
                x_dir, y_dir = direction
                self.moves.append([self.x + x_dir, self.y + y_dir])
        return self.moves


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.directions = [(1,1), (1,0), (1,-1)
            , (0,1), (-1,0)
            , (-1,1), (-1,0), (-1,-1)]

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
        self.directions = [(1,0), (0,1), (-1,0), (-1,0)]

    def get_name(self):
        return "R"

    def get_moves(self, board):
        self.moves = []
        for direction in self.directions:
            self.moves_in_direction(self.x, self.y
                , board, direction)


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.directions = [(2,1), (2,-1), (-2,1), (-2,-1)
            , (1,2), (1,-2), (-1,2), (-1,-2)]

    def get_name(self):
        return "N"

    def get_moves(self, board):
        self.moves = []
        for direction in self.directions:
            (self.valid_move(self.x, self.y, direction, board))
        return self.moves

class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.directions = [(1,1), (1,1), (-1,1), (-1,1)]

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
        if color == "B":
            self.directions = [(0,1),(1,1),(-1,1)]
        else:
            self.directions = [(0,-1),(1,-1),(-1,-1)]

    def get_name(self):
        return "P"

    def get_moves(self, board):
        return None

    def promote(self):
        pass
