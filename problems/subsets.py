# Algorithm:
#  Using backtrack.
#  Starting from the element of index 0, concat other elements until the last element.
#  (At each step, append the concatenated list to the result list)
#  When this recursive search reach the last element, repeating the following step.
#    Go back one step, replace the element with the next element of current index (until the last index)
def subsets1(nums):
    ret = []
    backtrack(ret, [], nums, 0)
    return ret


def backtrack(ret, tmp, nums, start):
    ret.append(tmp)
    for i in range(start, len(nums)):
        backtrack(ret, tmp + [nums[i]], nums, i + 1)


def subsets2(nums):
    res = [[]]
    for num in nums:
        res += [r + [num] for r in res]
    return res


def test_subsets1():
    assert subsets1([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert subsets1([1]) == [[], [1]]
    assert subsets1([]) == [[]]
    assert subsets1([5, 4]) == [[], [5], [5, 4], [4]]


def test_subsets2():
    import deepdiff

    assert not deepdiff.DeepDiff(
        subsets2([1, 2, 3]),
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]],
        ignore_order=True,
    )
    assert subsets2([1]) == [[], [1]]
    assert subsets2([]) == [[]]
