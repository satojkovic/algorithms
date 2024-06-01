from src.score_of_string import *


def test_score_of_string():
    assert score_of_string("hello") == 13
    assert score_of_string("zaz") == 50
