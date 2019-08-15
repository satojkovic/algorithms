# Time complexity: O(n)
#  iterate over nums once, len() is O(1)
# Space complexity: O(1)
#  max_num and total, loop variable
# Algorithm:
#  n equals length of an input array
#  calculate sum of n distinct numbers (Note: this has the risk of overflow, but intergers do normally not overflow in python3)
#  when we iterate over nums, reminder of total is missing number
def missing_number1(nums):
    max_num = len(nums)
    total = (max_num * (max_num + 1)) // 2
    for num in nums:
        total -= num
    return total

# Time complexity: O(n)
# Space complexity: O(1)
#
# Algorithm:
#  XOR of a number itself is 0
#  XOR of a number with 0 is the number itself
#  The order of an XOR operation is inconsequential
#  So every number from 0..n XOR with itself except the missing number, the result will be the missing number
#  example:
#   [3, 0, 1]
#   [0, 1, 2 ] + [3] (come from i and res)
#   [3, 0, 1, 2] ^ [3, 0, 1]
#   -> 3 ^ 0 ^ 3 ^ 1 ^ 0 ^ 2 ^ 1
#   -> (3 ^ 3) ^ (0 ^ 0) ^ (1 ^ 1) ^ 2
#   -> 0 ^ 0 ^ 0 ^ 2
#   ==> 2 
def missing_number2(nums):
    res = len(nums)
    for i, num in enumerate(nums):
        res ^= i
        res ^= num
    return res