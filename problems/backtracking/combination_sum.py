def combination_sum(candidates, target):
    def backtrack(remain, start_index, current_combination):
        if remain == 0:
            results.append(current_combination[:])
            return
        if remain < 0:
            return

        for i in range(start_index, len(candidates)):
            current_combination.append(candidates[i])
            backtrack(remain - candidates[i], i, current_combination)
            current_combination.pop()

    results = []
    backtrack(target, 0, [])
    return results


def test_combination_sum():
    import deepdiff

    assert not deepdiff.DeepDiff(
        combination_sum([2, 3, 6, 7], 7), [[7], [2, 2, 3]], ignore_order=True
    )
    assert not deepdiff.DeepDiff(
        combination_sum([2, 3, 5], 8),
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        ignore_order=True,
    )
    assert not deepdiff.DeepDiff(
        combination_sum([2], 1), [], ignore_order=True
    )
    assert not deepdiff.DeepDiff(
        combination_sum([1], 1), [[1]], ignore_order=True
    )
    assert not deepdiff.DeepDiff(
        combination_sum([1], 2), [[1, 1]], ignore_order=True
    )
