# Time complexity:
#  reset => O(1)
#  shuffle => O(n)
#
# Space complexity: O(n)
import random
class ShuffleAnArray:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums

    def shuffle(self):
        ret = self.nums.copy()
        for i in reversed(range(1, len(self.nums))):
            j = random.randrange(0, i+1) # end is exclusive unlike randint
            ret[i], ret[j] = ret[j], ret[i]
        return ret
