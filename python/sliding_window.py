def find_average_subarrays(k, arr):
    result = []
    for i in range(len(arr) - k + 1):
        avr = sum(arr[i:i+k]) / k
        result.append(avr)
    return result


def find_average_subarrays_window(k, arr):
    result = []
    window_sum, left = 0.0, 0
    for right in range(len(arr)):
        window_sum += arr[right]
        if right >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[left]
            left += 1
    return result


def test_find_average_subarrays():
    k = 5
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    ans = [2.2, 2.8, 2.4, 3.6, 2.8]
    assert find_average_subarrays(k, arr) == ans
    assert find_average_subarrays_window(k, arr) == ans

    assert find_average_subarrays(1, [10]) == [10]
    assert find_average_subarrays_window(1, [10]) == [10]

    assert find_average_subarrays(2, [123]) == []
    assert find_average_subarrays_window(2, [123]) == []


def max_sum_subarray(k, arr):
    import sys
    max_sum = -sys.maxsize
    curr_sum, left = 0.0, 0
    for right in range(len(arr)):
        curr_sum += arr[right]
        if right >= k - 1:
            max_sum = curr_sum if curr_sum > max_sum else max_sum
            curr_sum -= arr[left]
            left += 1
    return max_sum


def test_max_sum_subarray():
    assert max_sum_subarray(3, [2, 1, 5, 1, 3, 2]) == 9
    assert max_sum_subarray(2, [2, 3, 4, 1, 5]) == 7
    assert max_sum_subarray(2, [1, 2, -3]) == 3
    assert max_sum_subarray(2, [-3, 2, -5, -9]) == -1
    assert max_sum_subarray(2, [1, 2, -3, 9]) == 6
