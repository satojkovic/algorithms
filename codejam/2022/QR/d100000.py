# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     ds = list(map(int, input().split()))
#     ds = sorted(ds, reverse=True)
#     max_len = 0
#     for d in range(ds[0], 1, -1):
#         end = d
#         for n in range(N):
#             if end != 0 and end <= ds[n]:
#                 end -= 1
#             else:
#                 break
#         max_len = max(max_len, d - end)
#     print('Case #{}: {}'.format(t, max_len))

def calc_maxlen(ds, N):
    curr = ds[0]
    n = 0
    while curr >= 1 and n < N:
        if curr <= ds[n]:
            curr -= 1
        else:
            curr = ds[n] - 1
        n += 1
    return n


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ds = list(map(int, input().split()))
    ds = sorted(ds, reverse=True)
    print('Case #{}: {}'.format(t, calc_maxlen(ds, N)))
