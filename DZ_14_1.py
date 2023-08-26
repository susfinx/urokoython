class NigaSideException(Exception):
    def __init__(self, side: str, side_niga):
        self.side_niga = side_niga
        self.side = side

    def __str__(self):
        return f'storona {self.side} ravna {self.side_niga}, eto otricatelnoe znachenie, neobhodimo polozhitelnoe chislo'

class ZeroSideException(NigaSideException):
    def __init__(self, side: str, side_niga: int):
        super().__init__(side, side_niga)

    def __str__(self):
        return f'storona {self.side} = {self.side_niga}, znachenie dolzhno byt bolshe'

class Rectangle:
    """
    This class represents a rectangle.

    :param side_a: The length of one side.
    :param side_b: The length of the other side. If not provided, it's assumed to be equal to side_a.
    :raises NigaSideException: If any side is negative.
    :raises ZeroSideException: If any side is zero.

    >>> rect_1 = Rectangle(2, 4)
    >>> rect_1.get_perim()
    12
    >>> rect_1.get_square()
    8

    >>> rect_2 = Rectangle(5)
    >>> rect_2.get_perim()
    20
    >>> rect_2.get_square()
    25

    >>> rect_3 = Rectangle(-2, 4)
    Traceback (most recent call last):
        ...
    __main__.NigaSideException: storona a ravna -2, eto otricatelnoe znachenie, neobhodimo polozhitelnoe chislo

    >>> rect_4 = Rectangle(0, 4)
    Traceback (most recent call last):
        ...
    __main__.ZeroSideException: storona a = 0, znachenie dolzhno byt bolshe
    """
    def __init__(self, side_a: int, side_b: int = None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b
        if self.side_a < 0:
            raise NigaSideException('a', side_a)
        if self.side_b < 0:
            raise NigaSideException('b', side_b)
        if self.side_a == 0:
            raise ZeroSideException('a', 0)
        if self.side_b == 0:
            raise ZeroSideException('b', 0)

    def get_perim(self) -> int:
        return 2 * self.side_a + 2 * self.side_b

    def get_square(self) -> int:
        return self.side_a * self.side_b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
