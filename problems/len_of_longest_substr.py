def len_of_longest_substr(s):
    i, ret = 0, 0
    seen = {}
    for j in range(len(s)):
        if s[j] in seen:
            # Update the pointer i to a position that have no duplicate chars.
            # That is, it will be next to the position where the same character as the current position
            # is found, or the current position i, whichever is larger.
            # (For example, 'abba', 'a' appears the first but reappears later than 'b'.)
            # (In this case, max(i, seen[s[j]] + 1) == i)
            i = max(i, seen[s[j]] + 1)
        # Update ret value with distance between start pointer i and end pointer j
        # only when the distance is greater than ret.
        ret = max(ret, j - i + 1)
        # New unique char's position is stored or existing char's position is updated.
        seen[s[j]] = j
    return ret


def test_len_of_longest_substr():
    assert len_of_longest_substr('abba') == 2
    assert len_of_longest_substr('') == 0
    assert len_of_longest_substr('s') == 1
    assert len_of_longest_substr('abcabcbb') == 3
    assert len_of_longest_substr('bbbbb') == 1
    assert len_of_longest_substr('abcadef') == 6


def brute_force(s):
    # Check all the substring one by one to see if it has no duplicate character.
    def check(s, start, end):
        seen = set()
        for i in range(start, end + 1):
            if s[i] in seen:
                return False
            seen.add(s[i])
        return True
    ret = 0
    # Create substrings. s[i:j+1]
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Check to see if the substring has no duplicate character.
            if check(s, i, j):
                ret = max(ret, j - i + 1)
    return ret


def test_brute_force():
    assert brute_force('abba') == 2
    assert brute_force('') == 0
    assert brute_force('s') == 1
    assert brute_force('abcabcbb') == 3
    assert brute_force('bbbbb') == 1
    assert brute_force('abcadef') == 6


def sliding_window(s):
    from collections import defaultdict
    left, right = 0, 0
    seen = defaultdict(int)
    ret = 0

    while right < len(s):
        # Move right until finding duplicate character.
        # If duplicate character is found, left pointer is moved to the right
        # until the count of current character is less equal than 1.
        # (guranteed that there is no duplicate characters in the window)
        seen[s[right]] += 1
        while seen[s[right]] > 1:
            seen[s[left]] -= 1
            left += 1
        ret = max(ret, right - left + 1)
        right += 1
    return ret


def test_sliding_window():
    assert sliding_window('abba') == 2
    assert sliding_window('') == 0
    assert sliding_window('s') == 1
    assert sliding_window('abcabcbb') == 3
    assert sliding_window('bbbbb') == 1
    assert sliding_window('abcadef') == 6
