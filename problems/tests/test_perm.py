from src.perm import *


def test_perm_backtrack():
    assert perm_backtrack([1, 2, 3]) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]

    assert perm_backtrack([1, 2, 3]) == [[1, 2, 3],
                                        [1, 3, 2],
                                        [2, 1, 3],
                                        [2, 3, 1],
                                        [3, 1, 2],
                                        [3, 2, 1]]
    assert perm_backtrack([0, 1]) == [[0, 1], [1, 0]]
    assert perm_backtrack([1]) == [[1]]
