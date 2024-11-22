def two_sum2(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        two_sum = numbers[left] + numbers[right]
        if two_sum == target:
            return [left + 1, right + 1]
        elif two_sum > target:
            right -= 1
        elif two_sum < target:
            left += 1


def test_two_sum2():
    assert two_sum2([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum2([2, 3, 4], 6) == [1, 3]
    assert two_sum2([-1, 0], -1) == [1, 2]
    assert two_sum2([1, 2, 3, 4], 7) == [3, 4]
    assert two_sum2([1, 1, 1, 1, 1, 1], 2) == [1, 6]
