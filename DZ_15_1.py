import unittest
import logging
import argparse

logging.basicConfig(filename='rectangle_test.log', level=logging.INFO)
logger = logging.getLogger(__name__)

class Rectangle:
    def __init__(self, side_a: int, side_b: int = None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b

    def get_perim(self) -> int:
        perimeter = 2 * self.side_a + 2 * self.side_b
        logger.info(f'Perimeter calculated: {perimeter}')
        return perimeter

    def get_square(self) -> int:
        square = self.side_a * self.side_b
        logger.info(f'Square calculated: {square}')
        return square

    def __eq__(self, other):
        equal = self.side_a == other.side_a and self.side_b == other.side_b
        logger.info(f'Equality check: {equal}')
        return equal

    def __add__(self, other):
        result = Rectangle(self.side_a + other.side_a, self.side_b + other.side_b)
        logger.info(f'Addition result: {result.side_a}x{result.side_b}')
        return result

    def __sub__(self, other):
        result = Rectangle(abs(self.side_a - other.side_a), abs(self.side_b - other.side_b))
        logger.info(f'Subtraction result: {result.side_a}x{result.side_b}')
        return result

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(3, 2)
        self.r2 = Rectangle(5, 4)
        self.r3 = Rectangle(7)
        self.r4 = Rectangle(1, 1)

    def test_create_rectangle(self):
        self.assertEqual(self.r1, Rectangle(3, 2))

    def test_perimeter(self):
        self.assertEqual(self.r2.get_perim(), 18)

    def test_square(self):
        self.assertEqual(self.r2.get_square(), 20)

    def test_add_rectangles(self):
        self.assertEqual(self.r2 + self.r3, Rectangle(12, 11))

    def test_subtract_rectangles(self):
        self.assertEqual(self.r2 - self.r4, Rectangle(4, 3))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Rectangle class unit tests')
    parser.add_argument('--log', action='store_true', help='Enable logging')

    args = parser.parse_args()

    if args.log:
        logger.disabled = False
    else:
        logger.disabled = True


