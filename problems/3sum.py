# This code implements the 3Sum problem, which is to find all unique triplets
# in an array that sum to zero.
# Brute Force: Check all combinations of triplets.
def three_sum_bf(nums):
    nums.sort()
    triplets = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if sum([nums[i], nums[j], nums[k]]) == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
    return list(triplets)


def test_three_sum_bf():
    assert three_sum_bf([-1,0,1,2,-1,-4]) == [(-1, 0, 1), (-1, -1, 2)]
    assert not three_sum_bf([0,1,1])
    assert three_sum_bf([0,0,0]) == [(0,0,0)]


def three_sum_by_two_sum(nums):
    nums.sort()
    res = []
    for i, num in enumerate(nums):
        # tripletの重複を排除するために最初の要素の重複を確認
        if i > 0 and num == nums[i-1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            three_sum = num + nums[left] + nums[right]
            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                res.append((num, nums[left], nums[right]))
                # tripletの重複を排除するために真ん中の要素の重複を確認
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return res


def test_three_sum_by_two_sum():
    assert three_sum_by_two_sum([-1,0,1,2,-1,-4]) == [(-1, -1, 2), (-1, 0, 1)]
    assert not three_sum_by_two_sum([0,1,1])
    assert three_sum_by_two_sum([0,0,0]) == [(0,0,0)]


if __name__ == '__main__':
    print(three_sum_by_two_sum([-1,0,1,2,-1,-4]) == [(-1, -1, 2), (-1, 0, 1)]
