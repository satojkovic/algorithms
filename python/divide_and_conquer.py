#!/usr/bin/env python
# -*- coding=utf-8 -*-

# Time complexity: O(nlog(n))
def trade(prices):
    if len(prices) == 1:
        return 0

    mid = len(prices) // 2
    former = prices[:mid]
    latter = prices[mid:]
    case3 = max(latter) - min(former) # Check n elements
    return max(trade(former), trade(latter), case3) # log(n) recursive call


if __name__ == "__main__":
    prices = [27, 53, 7, 25, 33, 2, 32, 47, 43]
    print('max_trade: {}'.format(trade(prices)))