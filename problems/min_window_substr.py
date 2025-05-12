def minWindow(s: str, t: str) -> str:
    left, right = 0, 0
    t_count = {}
    for c in t:
        t_count[c] = 1 + t_count.get(c, 0)

    window = {}
    cond_match, cond = 0, len(t_count)

    res, res_len = [-1, -1], len(s) + 1
    while right < len(s):
        c = s[right]
        window[c] = 1 + window.get(c, 0)

        if c in t_count and window[c] == t_count[c]:
            cond_match += 1

        while cond_match == cond:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1
            # update
            window[s[left]] -= 1
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                cond_match -= 1
            left += 1
        right += 1

    ans = s[res[0] : res[1] + 1]
    return ans if res_len != len(s) + 1 else ''


def test_min_window():
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("a", "a") == "a"
    assert minWindow("a", "aa") == ""
    assert minWindow("aa", "aa") == "aa"
