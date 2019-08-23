# Time complexity: O(2^n)
#  maximum size(number of nodes) of the recursion tree is O(2^n)
# 
# Space complexity: O(n)
#  the depth of the recursion tree is n
#
# Algorithm:
#  Think about the tree of root node n with two branches(n-1 and n-2).
#  When you calculate n-1 and n-2 for each branch repeatedly, the number of nodes with value 0 is the answer you want.
def climb_stairs1(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return climb_stairs1(n-1) + climb_stairs1(n-2)

# Time complexity: O(n)
#  You only have to calculate once for each n.
#  (lookup an array of index n is O(1))
#
# Space complexity: O(n)
#   You need to have an array with length n, and the depth of the recursion tree is n.
#
# Algorithm:
#  Algorithm1 with memoization
def climb_stairs2(n):
    memo = [0] * (n+1)
    def climb_stairs_memo(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if memo[n]:
            return memo[n]
        
        memo[n] = climb_stairs_memo(n-1) + climb_stairs_memo(n-2)
        return memo[n]
    return climb_stairs_memo(n)

# Time complexity: O(n)
#  Single for-loop up to n
#
# Space complexity: O(n)
#  You need to have memo array with length n+1
#
# Algorithm:
#  The total number of steps to reach n is equal to sum of ways of reaching n-1 and ways of reaching n-2.
def climb_stairs3(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    memo = [0] * (n+1)
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n + 1, 1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]