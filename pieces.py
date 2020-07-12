

class Piece(object):
    def __init__(self, color):
        self.color = color
        self.position = [None,None]

    def set_position(self, pos_x, pos_y):
        self.position = [pos_x, pos_y]

    def get_name(self):
        pass

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def get_moves(self):
        return None

class King(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)

    def get_name(self):
        return "K"

    def get_moves(self):
        return None

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



x = King("B")
x.get_position()
