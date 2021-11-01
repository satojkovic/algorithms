# Time complexity: O(n)
#  iterate over a string
# Space complexity: O(1)
def title_to_number(s):
    s = s.upper()
    number = 0
    for i in range(len(s)):
        ch_val = ord(s[i]) - ord('A') + 1
        number += (ch_val * 26 ** (len(s) - i - 1))
    return number


def test_title_to_number():
    assert title_to_number('ZY') == 701
    assert title_to_number('A') == 1
    assert title_to_number('') == 0
    assert title_to_number('zy') == 701
    assert title_to_number('zY') == 701
    assert title_to_number('Zy') == 701
