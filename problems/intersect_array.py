# Time complexity: O(m + n)
#  iterate over each arrays(the length of num1 and num2 are m, n, respectively)
# Space complexity: O(m + n)
def intersect1(nums1, nums2):
    freq = {}
    for num1 in nums1:
        if num1 in freq:
            freq[num1] += 1
        else:
            freq[num1] = 1
    ret = []
    for num2 in nums2:
        if num2 in freq and freq[num2] > 0:
            ret.append(num2)
            freq[num2] -= 1
    return ret

# Time complexity:
#   O(m + n), O(m) time is used to convert `num1` to `set1` and O(n) time is used to convert `num2`
#   `in` operations are O(1) in average time.
# Space complexity: O(m + n) in the worst case when all elements in the arrays are different
def intersect2(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    if len(set1) <= len(set2):
        return [x for x in set1 if x in set2]
    else:
        return [x for x in set2 if x in set1]
