def ways_to_fair(nums):
    left_sum_odd, left_sum_even = 0, 0
    right_sum_odd = sum(nums[1::2])
    right_sum_even = sum(nums[0::2])
    res = 0
    for i, num in enumerate(nums):
        if i % 2 == 0:
            left_sum_odd = left_sum_odd + nums[i-1] if i != 0 else left_sum_odd
            right_sum_odd, right_sum_even = \
                right_sum_even - num, right_sum_odd
            sum_odd = left_sum_odd + right_sum_odd
            sum_even = left_sum_even + right_sum_even
        else:
            left_sum_even = left_sum_even + nums[i-1] if i != 0 else left_sum_even
            right_sum_odd, right_sum_even = \
                right_sum_even - num, right_sum_odd
            sum_odd = left_sum_odd + right_sum_even
            sum_even = left_sum_even + right_sum_odd
        if sum_odd == sum_even:
            res += 1
    return res

if __name__ == "__main__":
    print(ways_to_fair([2, 1, 6, 4]))
