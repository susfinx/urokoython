import unittest

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

class TestRectangle(unittest.TestCase):
    def test_valid_rectangle(self):
        rect_1 = Rectangle(2, 4)
        self.assertEqual(rect_1.get_perim(), 12)
        self.assertEqual(rect_1.get_square(), 8)

    def test_square_only_one_side(self):
        rect_2 = Rectangle(5)
        self.assertEqual(rect_2.get_perim(), 20)
        self.assertEqual(rect_2.get_square(), 25)

    def test_negative_side(self):
        with self.assertRaises(NigaSideException):
            rect = Rectangle(-2, 4)

    def test_zero_side(self):
        with self.assertRaises(ZeroSideException):
            rect = Rectangle(0, 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
