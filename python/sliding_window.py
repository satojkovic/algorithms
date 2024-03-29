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


def max_substring_with_k_distinct_chars(k, s):
    from collections import defaultdict
    char_freqs = defaultdict(int)
    left = 0
    max_length = 0
    for right in range(len(s)):
        char_freqs[s[right]] += 1
        while len(char_freqs) > k:
            left_char = s[left]
            char_freqs[left_char] -= 1
            if char_freqs[left_char] == 0:
                del char_freqs[left_char]
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


def test_max_susbstring_with_k_distinct_chars():
    assert max_substring_with_k_distinct_chars(2, 'araaci') == 4
    assert max_substring_with_k_distinct_chars(1, 'araaci') == 2
    assert max_substring_with_k_distinct_chars(3, 'cbbebi') == 5
