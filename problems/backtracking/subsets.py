# Algorithm:
#  Using backtrack.
#  Starting from the element of index 0, concat other elements until the last element.
#  (At each step, append the concatenated list to the result list)
#  When this recursive search reach the last element, repeating the following step.
#    Go back one step, replace the element with the next element of current index (until the last index)
def subsets(nums):
    res = []

    def backtrack(i, subset):
        res.append(subset[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            subset.append(nums[j])
            backtrack(j + 1, subset)
            subset.pop()

    nums.sort()
    backtrack(0, [])
    return res


# Time complexity is O(N * 2^N) because there are O(2^N) nodes in the recursion tree and each subset copy has length O(N)
# Space complexity is also O(N * 2^N) because there are 2^N subsets and the mean of subset length is N/2.
def subsets_bf(nums):
    res = set()

    def backtrack(i, subset):
        if i == len(nums):
            res.add(tuple(subset))
            return

        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()
        backtrack(i + 1, subset)

    nums.sort()
    backtrack(0, [])
    return [list(s) for s in sorted(res, key=lambda subset: (len(subset), subset))]


def assert_subsets_equal(actual, expected):
    normalized_actual = sorted(tuple(sorted(subset)) for subset in actual)
    normalized_expected = sorted(tuple(sorted(subset)) for subset in expected)
    assert normalized_actual == normalized_expected


def test_subsets():
    assert_subsets_equal(subsets([1, 2, 3]), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
    assert_subsets_equal(subsets([5, 4]), [[], [5], [5, 4], [4]])
    assert_subsets_equal(subsets([1]), [[], [1]])
    assert_subsets_equal(subsets([]), [[]])
    assert_subsets_equal(subsets([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])


def test_subsets_bf():
    assert_subsets_equal(subsets_bf([1, 2, 3]), [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]])
    assert_subsets_equal(subsets_bf([5, 4]), [[], [5], [5, 4], [4]])
    assert_subsets_equal(subsets_bf([1]), [[], [1]])
    assert_subsets_equal(subsets_bf([]), [[]])
    assert_subsets_equal(subsets_bf([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
