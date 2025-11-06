# Algorithm:
#  Using backtrack.
#  Starting from the element of index 0, concat other elements until the last element.
#  (At each step, append the concatenated list to the result list)
#  When this recursive search reach the last element, repeating the following step.
#    Go back one step, replace the element with the next element of current index (until the last index)
def subsets(nums):
    def backtrack(start_index, curr_subset):
        res.append(curr_subset[:])
        for i in range(start_index, len(nums)):
            curr_subset.append(nums[i])
            backtrack(i + 1, curr_subset)
            curr_subset.pop()

    res = []
    backtrack(0, [])
    return res



def test_subsets():
    assert subsets([1, 2, 3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert subsets([5, 4]) == [[], [5], [5, 4], [4]]
    assert subsets([1]) == [[], [1]]
    assert subsets([]) == [[]]
