def replace_space(s, true_length):
    tail_pos = len(s) - 1
    i = true_length - 1
    while i >= 0:
        if s[i] == ' ':
            s[tail_pos] = '0'
            s[tail_pos - 1] = '2'
            s[tail_pos - 2] = '%'
            tail_pos -= 3
        else:
            s[tail_pos] = s[i]
            tail_pos -= 1
        i -= 1
    return

if __name__ == "__main__":
    s = 'Mr John Smith    '
    s_list = list(s)
    replace_space(s_list, 13)
    print(''.join(s_list))