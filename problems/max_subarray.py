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

# O(n^2)
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


def test_max_subarray():
    data = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
    assert max_subarray_o3(data) == 187
    assert max_subarray_o2(data) == 187
    assert max_subarray_o2_another(data) == 187
