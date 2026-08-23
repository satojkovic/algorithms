from typing import List

def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    out = []

    def backtrack(start, path, current_sum):
        if current_sum == target:
            out.append(list(path))
            return
        if current_sum > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            path.append(candidates[i])
            backtrack(i + 1, path, current_sum + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return out

def test_combination_sum2():
    import deepdiff

    assert not deepdiff.DeepDiff(
        combinationSum2([2,5,2,1,2], 5), [[1, 2, 2], [5]], ignore_order=True
    )

    assert not deepdiff.DeepDiff(
        combinationSum2([10,1,2,7,6,1,5], 8), [[1,1,6],[1,2,5],[1,7],[2,6]], ignore_order=True
    )
