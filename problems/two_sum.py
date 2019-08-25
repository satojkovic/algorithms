# Time complexity: O(n)
#  We iterate over the list containing n elements only once.
#  Each lookup in the hash table is O(1)
#
# Space complexity: O(n)
#  The extra space depends on the number of elements in the hash table, which is at most n elements.
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if not target - num in seen:
            seen[num] = i
        else:
            return [seen[target - num], i]
    return [-1, -1]
