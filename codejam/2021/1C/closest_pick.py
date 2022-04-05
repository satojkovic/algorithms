def calc_prob(a, b, K, sold_tickets):
    count = 0
    for c in range(1, K + 1):
        if c in sold_tickets:
            continue
        elif c == a or c == b:
            count += 1
        else:
            diff_sold = min([abs(t-c) for t in sold_tickets])
            diff_purchased = min(abs(a - c), abs(b - c))
            if diff_sold > diff_purchased:
                count += 1
    return count / K


T = int(input())
for t in range(1, T + 1):
    N, K = list(map(int, input().split()))
    sold_tickets = list(map(int, input().split()))
    sold_tickets = set(sold_tickets)
    res = 0.0
    # Pick K^2 possible pairs and calc probability
    for i in range(1, K):
        for j in range(i+1, K+1):
            prob = calc_prob(i, j, K, sold_tickets)
            res = max(res, prob)
    print('Case #{}: {}'.format(t, res))
