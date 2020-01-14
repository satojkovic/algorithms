def dominant_index(nums):
    if len(nums) == 1:
        return 0
    max_num = -1
    next_max_num = -1
    max_idx = 0
    for i, n in enumerate(nums):
        if n >= max_num:
            next_max_num = max_num
            max_num = n
            max_idx = i
        elif n > next_max_num:
            next_max_num = n
    return max_idx if max_num >= next_max_num * 2 else -1