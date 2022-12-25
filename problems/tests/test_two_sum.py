from src.two_sum import *

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


def test_two_sum_all_pairs():
    assert two_sum_all_pairs([5, 5, 5], 10) == [(5, 5)]
    assert two_sum_all_pairs([5, 5, 5, 5], 10) == [(5, 5), (5, 5)]
