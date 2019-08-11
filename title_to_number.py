def title_to_number1(s):
    s = s.upper()
    number = 0
    for i in range(len(s)):
        ch_val = ord(s[i]) - ord('A') + 1
        number += (ch_val * 26 ** (len(s) - i - 1))
    return number