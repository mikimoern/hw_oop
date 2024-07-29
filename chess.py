class Figure:
    def __init__(self, color: str, position: tuple[int, int]):
        """
        Initializes a figure with a color and position.

        :param color: Color of the figure ('white' or 'black').
        :param position: Position of the figure on the board as a tuple (column, row).
        """
        self.color = color
        self.position = position

    def change_color(self) -> None:
        """
        Changes the color of the figure to the opposite color.
        """
        if self.color == "black":
            self.color = "white"
        else:
            self.color = "black"

    def change_position(self, new_position: tuple[int, int]) -> None:
        """
        Changes the position of the figure to the new position if it's valid.

        :param new_position: New position of the figure as a tuple (column, row).
        :raises ValueError: If the new position is invalid.
        """
        if self._is_valid_position(new_position):
            self.position = new_position
        else:
            raise ValueError("Invalid position format or position is out of bounds")

    def _is_valid_position(self, new_position: tuple[int, int]) -> bool:
        """
        Checks if the new position is valid.

        :param new_position: New position as a tuple (column, row).
        :return: True if the position is valid, otherwise False.
        """
        if isinstance(new_position, tuple) and len(new_position) == 2:
            col, row = new_position
            return 1 <= col <= 8 and 1 <= row <= 8
        return False

    def can_move_to(self, new_position: tuple[int, int]) -> bool:
        """
        Determines if the figure can move to the specified position.

        :param new_position: Position as a tuple (column, row).
        :return: True if the figure can move to the specified position, otherwise False.
        :raises NotImplementedError: Method should be implemented by subclasses.
        """
        raise NotImplementedError("This method should be implemented by subclasses")


class Pawn(Figure):

    def can_move_to(self, new_position: tuple[int, int]) -> bool:
        """
        Determines if the pawn can move to the specified position.

        :param new_position: Position as a tuple (column, row).
        :return: True if the pawn can move to the specified position, otherwise False.
        """
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

    def can_move_to(self, new_position: tuple[int, int]) -> bool:
        """
        Determines if the knight can move to the specified position.

        :param new_position: Position as a tuple (column, row).
        :return: True if the knight can move to the specified position, otherwise False.
        """
        if not self._is_valid_position(new_position):
            return False

        col_diff = abs(new_position[0] - self.position[0])
        row_diff = abs(new_position[1] - self.position[1])
        return (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2)


class Bishop(Figure):
    def can_move_to(self, new_position: tuple[int, int]) -> bool:
        """
        Determines if the bishop can move to the specified position.

        :param new_position: Position as a tuple (column, row).
        :return: True if the bishop can move to the specified position, otherwise False.
        """
        if not self._is_valid_position(new_position):
            return False

        col_diff = abs(new_position[0] - self.position[0])
        row_diff = abs(new_position[1] - self.position[1])
        return col_diff == row_diff


class Rook(Figure):

    def can_move_to(self, new_position: tuple[int, int]) -> bool:
        """
        Determines if the rook can move to the specified position.

        :param new_position: Position as a tuple (column, row).
        :return: True if the rook can move to the specified position, otherwise False.
        """
        if not self._is_valid_position(new_position):
            return False

        col_diff = new_position[0] - self.position[0]
        row_diff = new_position[1] - self.position[1]
        return col_diff == 0 or row_diff == 0


class Queen(Figure):

    def can_move_to(self, new_position: tuple[int, int]) -> bool:
        """
        Determines if the queen can move to the specified position.

        :param new_position: Position as a tuple (column, row).
        :return: True if the queen can move to the specified position, otherwise False.
        """
        if not self._is_valid_position(new_position):
            return False

        col_diff = abs(new_position[0] - self.position[0])
        row_diff = abs(new_position[1] - self.position[1])
        return col_diff == row_diff or col_diff == 0 or row_diff == 0


class King(Figure):

    def can_move_to(self, new_position: tuple[int, int]) -> bool:
        """
        Determines if the king can move to the specified position.

        :param new_position: Position as a tuple (column, row).
        :return: True if the king can move to the specified position, otherwise False.
        """
        if not self._is_valid_position(new_position):
            return False

        col_diff = abs(new_position[0] - self.position[0])
        row_diff = abs(new_position[1] - self.position[1])
        return col_diff <= 1 and row_diff <= 1


def get_figures_that_can_move(figures: list, new_position: tuple[int, int]) -> list:
    """
    Returns a list of figures that can move to the specified position.

    :param figures: List of figures.
    :param new_position: Position as a tuple (column, row).
    :return: List of figures that can move to the specified position.
    """
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
