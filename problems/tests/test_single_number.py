from src.single_number import *


def test_single_number_xor():
    assert single_number_xor([2, 2, 1]) == 1
    assert single_number_xor([4, 1, 2, 1, 2]) == 4
    assert single_number_xor([1]) == 1
    assert single_number_xor([10, 10, 3, 4, 4]) == 3
    assert single_number_xor([1, -1, 1, -10, -1]) == -10
