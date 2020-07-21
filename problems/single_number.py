# Time complexity: `for` loop is O(n), hash table operation(pop) is O(1)
# Space complexity: The space required by `hash table` is equal to the number of elements in `nums`
def single_number1(nums):
    uniq = {}
    for num in nums: # O(n)
        try:
            uniq.pop(num)
        except:
            uniq[num] = 1
    return uniq.popitem()[0]

def single_number1a(nums):
    once = set()
    for num in nums:
        if not num in once:
            once.add(num)
        else:
            once.remove(num)
    return list(once)

# If we take XOR of two same bits, it will return 0
# If we take XOR of zero and some bit, it will return that bit
# So we can XOR all bits together to find unique number.
#
# Time complexity: `for` loop is O(n)
# Space complexity: O(1)
def single_number2(nums):
    c = 0
    for num in nums:
        c ^= num
    return c

# Time complexity: list.sort is O(nlogn), and `for` loop is O(n)
# Space complexity: O(1)
def single_number3(nums):
    nums.sort()
    for i in range(0, len(nums), 2):
        if i == len(nums) - 1 or nums[i] != nums[i + 1]:
            return nums[i]
    return None

def single_number3a(nums):
    nums = sorted(nums)
    res = []
    for i, num in enumerate(nums):
        if (i == 0 and nums[i] < nums[i + 1]) or \
            (i == len(nums) - 1 and nums[i -1] < nums[i]) or \
                (nums[i - 1] < nums[i] < nums[i + 1]):
                res.append(nums[i])
    return res