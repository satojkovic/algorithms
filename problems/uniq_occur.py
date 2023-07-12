def uniq_occur(arr):
    from collections import defaultdict

    occur = defaultdict(int)
    for d in arr:
        occur[d] += 1
    seen = set()
    for _, v in occur.items():
        if v in seen:
            return False
    return True


def test_uniq_occur():
    arr = [1, 2, 2, 1, 1, 3]
    uniq_occur(arr) is True

    arr = [1, 2]
    uniq_occur(arr) is False

    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    uniq_occur(arr) is True
