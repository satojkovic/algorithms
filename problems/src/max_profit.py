# Time complexity: O(n)
#  we iterate over prices once.
# Space complexity: O(1)
#
# Algorithm:
#  min price is updated in each day.
#  profit is calculated by the price of current day and min price at the same time.
#  max profit is updated if the profit is greater than the existing max profit.

def max_profit(prices):
    import sys
    min_price, max_profit = sys.maxsize, 0
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([5, 3, 1]) == 0
    assert max_profit([100]) == 0
    assert max_profit([5, 10]) == 5
    assert max_profit([10, 10, 10, 10]) == 0
