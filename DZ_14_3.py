import pytest
from DZ_13_1 import Rectangle, Niga_side_exception, Zero_side_exception

def test_valid_rectangle():
    rect_1 = Rectangle(2, 4)
    assert rect_1.get_perim() == 12
    assert rect_1.get_square() == 8

def test_square_only_one_side():
    rect_2 = Rectangle(5)
    assert rect_2.get_perim() == 20
    assert rect_2.get_square() == 25

def test_negative_side():
    with pytest.raises(Niga_side_exception):
        rect = Rectangle(-2, 4)

def test_zero_side():
    with pytest.raises(Zero_side_exception):
        rect = Rectangle(0, 4)

if __name__ =='__main__':
    pytest

