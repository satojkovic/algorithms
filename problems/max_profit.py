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