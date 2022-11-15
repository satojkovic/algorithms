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
