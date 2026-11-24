import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(5, 3) == 8
    assert calc.add(-2, 2) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(4, 10) == -6

def test_multiply(calc):
    assert calc.multiply(5, 3) == 15
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 10) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(9, 3) == 3
    assert calc.divide(5, 2) == 2.5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)
