# Time complexity: O(n)
#  we iterate over an input list(nums) once and make a constant time hash table insertion on each iteration.
#  we iterate over the hash table.
# Space complexity: O(n)
#  we have (floor(n/2) + 1) key value pairs
def major_elem1(nums):
    elems = {}
    for num in nums:
        if not num in elems:
            elems[num] = 1
        else:
            elems[num] += 1

    for k, v in elems.items():
        if v > len(nums) // 2:
            return k