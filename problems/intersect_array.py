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