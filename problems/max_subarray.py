# O(n^3)
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


def test_max_subarray():
    data = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    assert max_subarray_o3(data) == 187
