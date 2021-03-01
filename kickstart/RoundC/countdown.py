def countdown(N, K, data):
    res = 0
    i = N - 1
    while i >= 0:
        if data[i] != 1:
            i -= 1
            continue
        j = i - 1
        up = 1
        while j >= 0:
            if data[i] + up != data[j]:
                break
            up += 1
            j -= 1
        if up >= K:
            res += 1
        i = j
    print('Case #: {}'.format(res))

if __name__ == '__main__':
    N, K = 12, 3
    data = [1, 2, 3, 7, 9, 3, 2, 1, 8, 3, 2, 1]
    countdown(N, K, data)
