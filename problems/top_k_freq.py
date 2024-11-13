# Time complexity: O(nlog(n))
#  iteration of the list is O(n)
#  the built-in sorting algorithm of python uses Timsort, which runs in O(nlog(n)).
#  get sliced list is O(k). (k is less than n)
#  Therefore the overall time complexity is O(nlog(n))
#
# Space complexity: O(n)
#  depends on the length of nums, which is O(n).
#
# Algorithm:
#  Two step algorithm.
#  1. Count the frequency and stores the freq to the dictionary.
#  2. Sort the dictionary by value
#  Finally return the top k element from the sorted list.
def top_k_freq1(nums, k):
    freqs = {}
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1
    ret = sorted(freqs, key=freqs.get, reverse=True)
    return ret[:k]


def test_top_k_freq1():
    assert top_k_freq1([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_freq1([1], 1) == [1]
    assert top_k_freq1([1, 2], 2) == [1, 2]
    assert top_k_freq1([3, 3, 1, 1, 10, 2, 10, 1], 3) == [1, 3, 10]


def top_k_freq_heap(nums, k):
    from collections import Counter
    import heapq
    freqs = Counter(nums)
    return heapq.nlargest(k, freqs.keys(), key=freqs.get)


def top_k_freq_heap2(nums, k):
    import heapq
    freqs = {}
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1
    heap = []
    for num, freq in freqs.items():
        heapq.heappush(heap, (-freq, num))
    res = []
    while len(res) < k:
        res.append(heapq.heappop(heap)[1])
    return res


def test_top_k_freq_heap():
    assert top_k_freq_heap([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_freq_heap([1], 1) == [1]
    assert top_k_freq_heap([1, 2], 2) == [1, 2]
    assert top_k_freq_heap([3, 3, 1, 1, 10, 2, 10, 1], 3) == [1, 3, 10]


def test_top_k_freq_heap2():
    assert top_k_freq_heap2([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_freq_heap2([1], 1) == [1]
    assert top_k_freq_heap2([1, 2], 2) == [1, 2]
    assert top_k_freq_heap2([3, 3, 1, 1, 10, 2, 10, 1], 3) == [1, 3, 10]


def top_k_freq_bucketsort(nums, k):
    freqs = {}
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freqs.items():
        buckets[freq].append(num)
    res = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res


def test_top_k_freq_bucketsort():
    assert top_k_freq_bucketsort([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_freq_bucketsort([1], 1) == [1]
    assert top_k_freq_bucketsort([1, 2], 2) == [1, 2]
    assert top_k_freq_bucketsort([3, 3, 1, 1, 10, 2, 10, 1], 3) == [1, 3, 10]


if __name__ == '__main__':
    print(top_k_freq1([1, 1, 1, 2, 2, 3], 2))
