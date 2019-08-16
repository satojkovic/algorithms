# Time complexity: O(n) for loop, hash table operation(get) is O(1) at average case
# Space complexity: O(n)
def single_number1(nums):
    uniq = {}
    for num in nums: # O(n)
        uniq[num] = uniq.get(num, 0) + 1 # O(1)
    for k, v in uniq.items(): # O(n)
        if v == 1:
            return k

# Time complexity: O(n) for loop
# Space complexity: O(1)
def single_number2(nums):
    c = 0
    for num in nums:
        c ^= num
    return c