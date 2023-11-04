def combination_sum(k, n):
    results = []

    def backtrack(remain, num_list, pivot):
        if remain == 0 and len(num_list) == k:
            results.append(list(num_list))
            return
        elif remain < 0 or len(num_list) == k:
            return

        for i in range(pivot, 10):
            num_list.append(i)
            backtrack(remain - i, num_list, i + 1)
            num_list.pop()

    backtrack(n, [], 1)
    return results


def test_combination_sum():
    assert combination_sum(3, 7) == [[1, 2, 4]]
    assert combination_sum(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert combination_sum(4, 1) == []
