import heapq
from typing import List

# This function returns the maximum value in each sliding window of size k
# in the given list of integers nums.
# It uses a max heap to keep track of the maximum values in the current window.
# The time complexity is O(n log k) and the space complexity is O(k).
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    heap = []
    output = []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        if i >= k - 1:
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            output.append(-heap[0][0])
    return output


def test_max_sliding_window():
    assert maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert maxSlidingWindow([1], 1) == [1]
    assert maxSlidingWindow([1, -1], 1) == [1, -1]
    assert maxSlidingWindow([9, 11, 0, 3, 5, 11], 6) == [11]
    assert maxSlidingWindow([4, -2], 2) == [4]

