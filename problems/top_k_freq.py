# Algorithm:
#  Two step algorithm. 
#  1. Count the frequency and stores the freq to a dictionary.
#  2. Sort the dictionary by value
#  Finally return the top k element from the sorted list.
def top_k_freq1(nums, k):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    ret = sorted(freq, key=freq.get, reverse=True)
    return ret[:k]
