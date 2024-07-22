class Figure:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def change_color(self):
        if self.color == "black":
            self.color = "white"
        else:
            self.color = "black"

    def change_position(self, new_position):
        if type(new_position) == tuple and len(new_position) == 2:
            col, row = new_position
            if 1 <= col <= 8 and 1 <= row <= 8:
                self.position = new_position
            else:
                raise ValueError("Position is out of bounds")
        else:
            raise ValueError("Invalid position format")

    def _is_valid_position(self, new_position):
        if type(new_position) == tuple and len(new_position) == 2:
            col, row = new_position
            return 1 <= col <= 8 and 1 <= row <= 8
        return False

    def can_move_to(self, new_position):
        raise NotImplementedError("This method should be implemented by subclasses")


class Pawn(Figure):
    def can_move_to(self, new_position):
        if not self._is_valid_position(new_position):
            return False

        col_diff = new_position[0] - self.position[0]
        row_diff = new_position[1] - self.position[1]
        if self.color == "white":
            return col_diff == 0 and (
                row_diff == 1 or (self.position[1] == 2 and row_diff == 2)
            )
        else:
            return col_diff == 0 and (
                row_diff == -1 or (self.position[1] == 7 and row_diff == -2)
            )


class Knight(Figure):
    def can_move_to(self, new_position):
        if not self._is_valid_position(new_position):
            return False

        col_diff = abs(new_position[0] - self.position[0])
        row_diff = abs(new_position[1] - self.position[1])
        return (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)


class Bishop(Figure):
    def can_move_to(self, new_position):
        if not self._is_valid_position(new_position):
            return False

        col_diff = abs(new_position[0] - self.position[0])
        row_diff = abs(new_position[1] - self.position[1])
        return col_diff == row_diff


class Rook(Figure):
    def can_move_to(self, new_position):
        if not self._is_valid_position(new_position):
            return False

        col_diff = new_position[0] - self.position[0]
        row_diff = new_position[1] - self.position[1]
        return col_diff == 0 or row_diff == 0


class Queen(Figure):
    def can_move_to(self, new_position):
        if not self._is_valid_position(new_position):
            return False

        col_diff = abs(new_position[0] - self.position[0])
        row_diff = abs(new_position[1] - self.position[1])
        return col_diff == row_diff or col_diff == 0 or row_diff == 0


class King(Figure):
    def can_move_to(self, new_position):
        if not self._is_valid_position(new_position):
            return False

        col_diff = abs(new_position[0] - self.position[0])
        row_diff = abs(new_position[1] - self.position[1])
        return col_diff <= 1 and row_diff <= 1


def get_figures_that_can_move(figures, new_position):
    return [figure for figure in figures if figure.can_move_to(new_position)]


figures = [
    Pawn("white", (5, 2)),
    Knight("black", (2, 1)),
    Bishop("white", (3, 1)),
    Rook("black", (1, 8)),
    Queen("white", (4, 1)),
    King("black", (5, 8)),
]

new_position = (5, 3)
mov_figures = get_figures_that_can_move(figures, new_position)
for figure in mov_figures:
    print(
        f"{figure.__class__.__name__} at {figure.position} can move to {new_position}"
    )
