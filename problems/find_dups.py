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

# Time complexity: O(nlogn)
#  Using binary search about 1 to n numbers.
#  if the number of elements equal or less than mid value, the search space will be [mid+1, n], otherwise [1, mid]
#  Repeat this process until search space is only one.
#  binary search costs O(log(n)) and traverse entire list is O(n), therefore time complexity is O(nlog(n))
#
# Space complexity: O(1)
#  no extra space is needed.
def find_dups3(nums):
    low = 1
    high = len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        count = 0
        for num in nums:
            if num <= mid:
                count += 1
        if count <= mid:
            low = mid + 1
        else:
            high = mid
    return low