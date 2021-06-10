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
        if num in freqs:
            freqs[num] += 1
        else:
            freqs[num] = 1
    ret = sorted(freqs, key=freqs.get, reverse=True)
    return ret[:k]
