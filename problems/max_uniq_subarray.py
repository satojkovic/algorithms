def max_uniq_subarray(nums):
    prefix_sum = [0] * (len(nums) + 1)
    for i, num in enumerate(nums):
        prefix_sum[i+1] = prefix_sum[i] + num
    res = 0
    start = 0
    seen = {}
    for i, num in enumerate(nums):
        start = max(start, seen.get(num, -1) + 1)
        res = max(res, prefix_sum[i+1] - prefix_sum[start])
        seen[num] = i
    return res