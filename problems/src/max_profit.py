# Time complexity: O(n)
#  we iterate over prices once.
# Space complexity: O(1)
#
# Algorithm:
#  min price is updated in each day.
#  profit is calculated by the price of current day and min price at the same time.
#  max profit is updated if the profit is greater than the existing max profit.

def max_profit_brute_force(prices):
    profit = 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            profit = max(profit, prices[j] - prices[i])
    return profit


def max_profit_partial_sort(prices):
    profit = 0
    for i in range(len(prices)):
        max_price = list(sorted(prices[i:]))[-1]
        profit = max(profit, max_price - prices[i])
    return profit


def max_profit_two_pointer(prices):
    left, right = 0, 1
    profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            profit = max(profit, prices[right] - prices[left])
        else:
            left = right
        right += 1
    return profit


def max_profit(prices):
    min_price, max_profit = prices[0], 0
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([5, 3, 1]) == 0
    assert max_profit([100]) == 0
    assert max_profit([5, 10]) == 5
    assert max_profit([10, 10, 10, 10]) == 0
