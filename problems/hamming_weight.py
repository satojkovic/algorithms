# Time complexity: O(1)
#  The runtime depends on the number of 1 bits in n but the length of n is fixed normally.
#
# Space complexity: O(1)
#  No additional space is allocated.
#
# Algorithm:
#  (n & n-1) flip the least significant 1 bit of number to 0.
#  Therefore you can get the answer by repeating this procedure and add 1 to the sum until (n & n-1) equal to 0.
def hamming_weight(n):
    ret = 0
    while n:
        n &= n - 1
        ret += 1
    return ret