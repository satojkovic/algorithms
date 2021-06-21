def num_good_pairs(nums):
    from collections import Counter
    num_counts = Counter(nums)
    res = 0
    for num, count in num_counts.items():
        res += (count * (count - 1)) // 2
    return res


def test_num_good_pairs():
    assert num_good_pairs([1, 1, 1, 3, 2, 3]) == 4
    assert num_good_pairs([1, 1, 1]) == 3
    assert num_good_pairs([10]) == 0
