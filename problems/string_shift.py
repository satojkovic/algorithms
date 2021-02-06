def string_shift(s, shift):
    left_shifts = 0
    for direction, amount in shift:
        left_shifts = left_shifts + amount if direction == 0 \
            else left_shifts - amount
    left_shifts %= len(s)
    return s[left_shifts:] + s[:left_shifts]

if __name__ == '__main__':
    print('abcd => {}'.format(string_shift('abcd', [[0, 1], [1, 4], [0, 5]])))