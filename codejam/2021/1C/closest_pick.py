# def calc_prob(a, b, K, sold_tickets):
#     count = 0
#     for c in range(1, K + 1):
#         if c in sold_tickets:
#             continue
#         elif c == a or c == b:
#             count += 1
#         else:
#             diff_sold = min([abs(t-c) for t in sold_tickets])
#             diff_purchased = min(abs(a - c), abs(b - c))
#             if diff_sold > diff_purchased:
#                 count += 1
#     return count / K

# T = int(input())
# for t in range(1, T + 1):
#     N, K = list(map(int, input().split()))
#     sold_tickets = list(map(int, input().split()))
#     # Pick K^2 possible pairs and calc probability
#     for i in range(1, K):
#         for j in range(i+1, K+1):
#             prob = calc_prob(i, j, K, sold_tickets)
#             res = max(res, prob)
#     print('Case #{}: {}'.format(t, res))

def calc_prob(N, K, sold_tickets):
    prob_a = [sold_tickets[0] - 1, K - sold_tickets[-1]]
    prob_b = [sold_tickets[0] - 1, K - sold_tickets[-1]]
    for i in range(N-1):
        diff = sold_tickets[i+1] - sold_tickets[i]
        prob_a.append(diff // 2)
        prob_b.append(diff - 1)
    prob_a.sort(reverse=True)
    prob_b.sort(reverse=True)
    return max((prob_a[0] + prob_a[1]) / K, prob_b[0] / K)


T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    sold_tickets = list(map(int, input().split()))
    prob = calc_prob(N, K, sorted(sold_tickets))
    print('Case #{}: {}'.format(t, prob))
