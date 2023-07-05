def max_wealth(accounts):
    max_wealth = 0
    for i in range(len(accounts)):
        w = sum(accounts[i])
        max_wealth = max(max_wealth, w)
    return max_wealth


def test_max_wealth():
    accounts = [[1, 2, 3], [4, 5, 6]]
    assert max_wealth(accounts) == 15

    accounts = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert max_wealth(accounts) == 42

    accounts = [[1, 0], [0, 1]]
    assert max_wealth(accounts) == 1

    accounts = [[0]]
    assert max_wealth(accounts) == 0
