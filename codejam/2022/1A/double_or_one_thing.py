def counts(S):
    # there is something wrong with the following code...
    #
    # counts = []
    # count = 1
    # label = S[0]
    # for i in range(1, len(S)):
    #     if S[i] == S[i-1]:
    #         count += 1
    #     else:
    #         counts.append((label, count))
    #         label = S[i]
    #         count = 1
    #     if i == len(S) - 1:
    #         counts.append((label, count))
    # return counts
    import itertools
    return [(label, len(list(group))) for label, group in itertools.groupby(S)]


T = int(input())
for t in range(1, T + 1):
    S = input()
    s_counts = counts(S)
    res = []
    for i in range(len(s_counts)):
        if i < len(s_counts) - 1 and s_counts[i][0] < s_counts[i+1][0]:
            res.extend([s_counts[i][0] for _ in range(s_counts[i][1] * 2)])
        else:
            res.extend([s_counts[i][0] for _ in range(s_counts[i][1])])
    print('Case #{}: {}'.format(t, ''.join(res)))
