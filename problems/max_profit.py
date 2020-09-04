# Time complexity: O(n)
#  we iterate over prices once.
# Space complexity: O(1)
#
# Algorithm:
#  basic strategy is to target monotonic sequences, then calculate (peak - valley) in each seqs, and add them up.
#  for example, a <= b <= c <= d
#   profit is calculated by (d - a) ... (A)
#  another example, a <= b >= e <= c <= d
#   profit is calculated by (b - a) + (d - e) ... (B)
#
#  However 
#  profit (A) calculation is equal to (b - a) + (c - b) + (d - c)
#  profit (B) calculation is equal to (b - a) + (c - e) + (d - c)
#  so simply add (price of day i - price of day i-1) if the diff is positive
#  (you can't sell and buy at same day, so those days are canceled in the above eq.)
def max_profit1(prices):
    profit = 0
    for i in range(1, len(prices), 1):
        if prices[i] > prices[i - 1]:
            profit += (prices[i] - prices[i - 1])
    return profit

def max_profit(prices, size):
    if size <= 0:
        return 0
    max_value = -1
    for i in range(size):
        new_max = prices[i] + max_profit(prices, size - i - 1)
        max_value = new_max if max_value < new_max else max_value
    return max_value

def max_profit_memo(prices, size):
    def _max_profit_memo(prices, size, memo):
        if size <= 0:
            return 0
        if memo[size] >= 0:
            return memo[size]
        max_value = -1
        for i in range(size):
            new_max = prices[i] + _max_profit_memo(prices, size - i - 1, memo)
            max_value = new_max if max_value < new_max else max_value
        memo[size] = max_value
        return max_value
    memo = [-1] * (size + 1)
    return _max_profit_memo(prices, size, memo)

def max_profit_iter(prices, size):
    memo = [0] * (size + 1)
    for i in range(size + 1):
        max_value = -1
        for j in range(i):
            max_value = max(max_value, prices[j] + memo[i - j - 1])
            memo[i] = max_value
    return memo[size]

if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(max_profit(prices, 4))
    print(max_profit_memo(prices, 4))
    print(max_profit_iter(prices, 4))