# def highlight(S, S2):
#     for i in range(len(S) - 1):
#         if S[i] <= S[i+1]:
#             S2[2 * i + 1] = S[i]
#     return ''.join(S2)


# def get_dup_tail_len(S):
#     tail_len = 1
#     for i in range(len(S) - 1, 0, -1):
#         if S[i] != S[i - 1]:
#             break
#         tail_len += 1
#     return tail_len


# def get_tail_idx(S, S2):
#     dup_tail_len = get_dup_tail_len(S)
#     tail_idx = len(S2) - 1
#     while S2[tail_idx] == S2[tail_idx-1]:
#         tail_idx -= 1
#     for _ in range(dup_tail_len - 1):
#         tail_idx += 1
#     return tail_idx


# def get_dup_head_len(S2):
#     head_len = 1
#     for i in range(0, len(S2) - 1):
#         if S2[i] != S2[i + 1]:
#             break
#         head_len += 1
#     return head_len


# def update_prefix(S, S2):
#     dup_head_len = get_dup_head_len(S2)
#     S2 = list(S2)
#     for i in range(dup_head_len):
#         if i < len(S) and S2[i] > S[i]:
#             S2[i] = ''
#     return ''.join(S2)


# T = int(input())
# for t in range(1, T + 1):
#     S = input().rstrip()
#     S2 = [S[i//2] if i % 2 == 0 else '' for i in range(len(S) * 2)]
#     if len(set(S)) == 1:
#         print('Case #{}: {}'.format(t, S))
#         continue
#     S2 = highlight(S, S2)
#     S2 = update_prefix(S, S2)
#     tail_idx = get_tail_idx(S, S2)
#     print('Case #{}: {}'.format(t, S2[:tail_idx + 1]))


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
