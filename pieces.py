class Piece(object):
    def __init__(self, color):
        self.color = color
        self.x = None
        self.y = None
        self.taken = False

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_name(self):
        pass

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def get_moves(self):
        return None

    def taken(self):
        self.taken = True


class King(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)

    def get_name(self):
        return "K"

    def get_moves(board):
        return 


class Queen(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)

    def get_name(self):
        return "Q"

    def get_moves(self):
        return None


class Rook(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)

    def get_name(self):
        return "R"

    def get_moves(self):
        return None


class Knight(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)

    def get_name(self):
        return "N"

    def get_moves(self):
        return None


class Bishop(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)

    def get_name(self):
        return "B"

    def get_moves(self):
        return None


class Pawn(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)

    def get_name(self):
        return "P"

    def get_moves(self):
        return None
