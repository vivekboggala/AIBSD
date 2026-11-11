import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()
def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
 
def test_subtract(calc):
    assert calc.subtract(10, 4) == 6
 
def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(5, 0) == 0
 
def test_divide(calc):
    assert calc.divide(10, 2) == 5
 
def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(5, 0)
 
def test_is_even(calc):
    assert calc.is_even(4) is True
    assert calc.is_even(7) is False
 
def test_factorial(calc):
    assert calc.factorial(0) == 1
    assert calc.factorial(5) == 120
 
def test_factorial_negative(calc):
    with pytest.raises(ValueError):
        calc.factorial(-3)
