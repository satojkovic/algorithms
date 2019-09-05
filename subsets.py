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
