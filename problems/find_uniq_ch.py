def find_uniq_ch(s):
    m = {}
    for i, ch in enumerate(s):
        if not ch in m:
            m[ch] = [i]
            continue
        m[ch].append(i)
    for ch in enumerate(s):
        if len(m[ch]) == 1:
            return m[ch][0]
    return -1