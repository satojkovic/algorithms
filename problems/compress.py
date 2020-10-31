def compress(s):
    length_s = len(s)
    prev_ch = ''
    count = 0
    res = []
    for ch in s:
        if prev_ch != '' and ch != prev_ch:
            res.append(prev_ch)
            res.append(str(count))
            prev_ch = ch
            count = 1
        else:
            count += 1
            prev_ch = ch if prev_ch == '' else prev_ch
    res.append(prev_ch)
    res.append(str(count))
    return ''.join(res) if length_s > len(res) else s

def compress2(s):
    count = 0
    res = []
    for i, ch in enumerate(s):
        count += 1
        # If next char is different than current, append current and count to result
        if i + 1 >= len(s) or ch != s[i + 1]:
            res.append(ch)
            res.append(str(count))
            count = 0
    return ''.join(res) if len(s) > len(res) else s

if __name__ == "__main__":
    print(compress('aabcccccaaa'))
    print(compress('aabccd')) # Return original string
    print(compress('AaBBBBB'))
    print(compress('X'))
    print(compress(''))

    print(compress2('aabcccccaaa'))
    print(compress2('aabccd')) # Return original string
    print(compress2('AaBBBBB'))
    print(compress2('X'))
    print(compress2(''))
