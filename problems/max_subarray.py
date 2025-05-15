# O(n^3)
# This function returns the maximum sum of a contiguous subarray in the given list of integers.
# It uses a brute-force approach with three nested loops.
# The time complexity is O(n^3) and the space complexity is O(1).
# The function iterates through all possible subarrays and calculates their sums.
# The maximum sum is updated whenever a larger sum is found.
def max_subarray_o3(data):
    maxsofar = 0
    n = len(data)
    for i in range(0, n):
        for j in range(i, n):
            temp_sum = 0
            for k in range(i, j + 1):
                temp_sum += data[k]
            maxsofar = max(maxsofar, temp_sum)
    return maxsofar

# O(n^2)
# This function returns the maximum sum of a contiguous subarray in the given list of integers.
# It uses a brute-force approach with two nested loops.
# The time complexity is O(n^2) and the space complexity is O(1).
# The function iterates through all possible subarrays and calculates their sums.
# The maximum sum is updated whenever a larger sum is found.
# The function uses a cumulative sum array to optimize the calculation of subarray sums.
# The cumulative sum array is built in O(n) time, and the subarray sums are calculated in O(1) time.
# The overall time complexity is O(n^2) and the space complexity is O(n).
def max_subarray_o2(data):
    maxsofar = 0
    n = len(data)
    for i in range(0, n):
        sum = 0
        for j in range(i, n):
            sum += data[j]
            maxsofar = max(maxsofar, sum)
    return maxsofar

def max_subarray_o2_another(data):
    maxsofar = 0
    n = len(data)
    cumsum = (n + 1) * [0]
    for i in range(n):
        cumsum[i + 1] = cumsum[i] + data[i]
    for i in range(0, n):
        for j in range(i, n):
            sum = cumsum[j-1] - cumsum[i]
            maxsofar = max(maxsofar, sum)
    return maxsofar

# O(nlogn)
def max_subarray_divide_and_conquer(data):
    def maxsum(data, l, u):
        if l > u:
            return 0
        if l == u:
            return max(0, data[l])
        m = (l + u) // 2
        lmax, sum = 0, 0
        for i in range(m, l - 1, -1):
            sum += data[i]
            lmax = max(lmax, sum)
        rmax, sum = 0, 0
        for i in range(m + 1, u + 1):
            sum += data[i]
            rmax = max(rmax, sum)
        return max(lmax + rmax, maxsum(data, l, m), maxsum(data, m + 1, u))

    n = len(data)
    return maxsum(data, 0, n - 1)

def max_subarray_linear(data):
    maxsofar, maxendinghere = 0, 0
    n = len(data)
    for i in range(n):
        maxendinghere = max(maxendinghere + data[i], 0)
        maxsofar = max(maxsofar, maxendinghere)
    return maxsofar

def test_max_subarray():
    data = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    assert max_subarray_o3(data) == 187
    assert max_subarray_o2(data) == 187
    assert max_subarray_o2_another(data) == 187
    assert max_subarray_divide_and_conquer(data) == 187
    assert max_subarray_linear(data) == 187
