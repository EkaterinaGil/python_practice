import pytest
from calculator import Calculator

calculator = Calculator()

@pytest.mark.parametrize('num1, num2, result', [
    (4, 5, 9),
    (-6, -10, -16),
    (-6, 6, 0),
    (15.84, 0.05, 15.89),
    (112, 0, 112),
    (-10000, 1876, -8124)
    ])
def test_sum_numbers(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result


# def test_sum_negative_nums():
#     calculator = Calculator()
#     res = calculator.sum(-6, -10)
#     assert res == -16

# def test_sum_positive_and_negative_nums():
#     calculator = Calculator()
#     res = calculator.sum(-6, 6) 
#     assert res == 0 

# def test_sum_float_nums():
#     calculator = Calculator()
#     res = calculator.sum(15.84, 0.05)
#     assert res == 15.89    

# def test_sum_zero_nums():
#     calculator = Calculator()
#     res = calculator.sum(112, 0)
#     assert res == 112

def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 5)
    assert res == 2

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        res = calculator.div(125, 0)

@pytest.mark.parametrize('list, result', [ ([], 0), ([1, 2, 3, 4, 5, 6, 7, 8, 9,5], 5)])
def test_avg_list(list, result):
    calculator = Calculator()
    res = calculator.avg(list)
    assert res == result

# def test_avg_positive():
#     calculator = Calculator()
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,5]
#     res = calculator.avg(numbers)   
#     assert res == 5 