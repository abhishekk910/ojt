import pytest
import math

@pytest.mark.demo1
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

@pytest.mark.demo2
def testsquare():
   num = 7
   assert 7*7 == 40

