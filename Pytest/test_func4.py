# def test_divisible_by_10(input_value):
#    assert input_value % 10 == 0
#
# def test_divisible_by_20(input_value):
#    assert input_value % 20 == 0

# import pytest
#
# @pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
# def test_multiplication_11(num, output):
#    assert 11*num == output


import pytest
import math

def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 6

def test_square_failure():
   num = 7
   assert 7*7 == 40

def test_equality_failure():
   assert 10 == 11