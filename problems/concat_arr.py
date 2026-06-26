def concat_arr(nums):
    n = len(nums)
    ans = [0] * (2 * n)

    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]

    return ans


def test_concat_arr():
    assert concat_arr([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert concat_arr([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
