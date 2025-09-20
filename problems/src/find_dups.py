# Time complexity: O(n)
#  iterate over nums once
#  For every loop, hash set lookup is O(1), hash set insertion is also O(1) in average case.
# Space complexity: O(n)
#  the space used by a hash set is linear
def find_dups1(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


def find_dups1a(nums):
    return False if len(set(nums)) == len(nums) else True


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


# Time complexity: O(n)
#  Floyd's Tortoise and Hare (Cycle Detection) algorithm
#  The algorithm uses two pointers that move at different speeds to detect a cycle in a linked list.
#  In this case, the array is treated as a linked list where each index points to the value at that index.
#  The slow pointer moves one step at a time, while the fast pointer moves two steps at a time.
#  If there is a cycle, the two pointers will eventually meet.
#  Once a cycle is detected, a new pointer is initialized at the start of the array, and both pointers move one step at a time until they meet again.
#  The meeting point is the duplicate number.
# Space complexity: O(1)
#  only a constant amount of extra space is used for the pointers.
def find_dups4(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


def test_find_dups():
    assert find_dups1([1, 3, 4, 2, 2]) == 2
    assert find_dups1([1, 1]) == 1
    assert find_dups1([3, 2, 1, 3]) == 3

    assert find_dups2([1, 2, 3, 1]) is True
    assert find_dups2([1, 2, 3, 4]) is False
    assert find_dups2([1]) is False

    assert find_dups3([1, 3, 4, 2, 2]) == 2
    assert find_dups3([1, 1]) == 1
    assert find_dups3([3, 2, 1, 3]) == 3

    assert find_dups4([1, 3, 4, 2, 2]) == 2
    assert find_dups4([1, 1]) == 1
    assert find_dups4([3, 2, 1, 3]) == 3
