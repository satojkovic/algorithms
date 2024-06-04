# Use the sorted string as hash key
# O(m * nlogn)
def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        key = str(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return anagrams.values()


# Use the count of 26 lower english letters as hash key.
# O(m * n * 26)
def group_anagrams2(strs):
    from collections import defaultdict

    anagrams = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        anagrams[tuple(count)].append(s)
    return anagrams.values()


def assert_nested_lists_equal_ignore_order(list1, list2):
    def sort_nested_lists(nested_list):
        # 内側のリストをソート
        sorted_inner_lists = [sorted(inner_list) for inner_list in nested_list]
        # 外側のリストをソート
        sorted_inner_lists.sort()
        return sorted_inner_lists

    sorted_list1 = sort_nested_lists(list1)
    sorted_list2 = sort_nested_lists(list2)

    assert (
        sorted_list1 == sorted_list2
    ), f"Lists do not match: {sorted_list1} != {sorted_list2}"


def test_group_anagrams():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = group_anagrams(strs)
    assert_nested_lists_equal_ignore_order(
        res, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )

    strs = ["a"]
    res = group_anagrams(strs)
    assert_nested_lists_equal_ignore_order(res, [["a"]])

    strs = [""]
    res = group_anagrams(strs)
    assert_nested_lists_equal_ignore_order(res, [[""]])


def test_group_anagrams2():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = group_anagrams2(strs)
    assert_nested_lists_equal_ignore_order(
        res, [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )

    strs = ["a"]
    res = group_anagrams2(strs)
    assert_nested_lists_equal_ignore_order(res, [["a"]])

    strs = [""]
    res = group_anagrams2(strs)
    assert_nested_lists_equal_ignore_order(res, [[""]])
