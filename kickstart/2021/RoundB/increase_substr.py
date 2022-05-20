def increase_substr():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        s = input()
        res = []
        max_len = 0
        for i, c in enumerate(s):
            if i != 0 and s[i-1] < s[i]:
                max_len += 1
            else:
                max_len = 1
            res.append(max_len)
        print('Case #{}: {}'.format(t, ' '.join(list(map(str, res)))))


if __name__ == '__main__':
    increase_substr()
