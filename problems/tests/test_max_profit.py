from src.max_profit import *

def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([5, 3, 1]) == 0
    assert max_profit([100]) == 0
    assert max_profit([5, 10]) == 5
    assert max_profit([10, 10, 10, 10]) == 0
