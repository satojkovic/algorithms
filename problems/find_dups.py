# Time complexity: O(n)
#  iterate over nums once
#  For every loop, hash set lookup is O(1), hash set insertion is also O(1) in average case.
# Space complexity: O(n)
#  the space used by a hash set is linear
def find_dups1(nums):
    elems = set()
    for num in nums:
        if not num in elems:
            elems.add(num)
        else:
            return True
    return False

# Time complexity: O(nlogn)
#  entire algorithm is dominated by the sorting step, which is O(nlogn)
# Space complexity: O(1)
#  depends on the sorting implementation
#  for example, heapsort is O(1)
def find_dups2(nums):
    nums.sort()
    for i in range(0, len(nums) - 1, 1):
        if nums[i] == nums[i + 1]:
            return True
    return False