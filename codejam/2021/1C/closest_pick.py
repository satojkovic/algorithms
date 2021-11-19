def calc_prob(a, b, K, sold_tickets):
    count = 0
    for c in range(1, K + 1):
        if c in set(sold_tickets):
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
    unsold_tickets = []
    for k in range(1, K + 1):
        if not k in set(sold_tickets):
            unsold_tickets.append(k)
    res = 0.0
    if len(unsold_tickets) == 0:
        res = 0.0
    elif len(unsold_tickets) == 1:
        res = 1 / K
    else:
        for i in range(len(unsold_tickets)-1):
            for j in range(i+1, len(unsold_tickets)):
                prob = calc_prob(
                    unsold_tickets[i], unsold_tickets[j], K, sold_tickets)
                res = max(res, prob)
    print('Case #{}: {}'.format(t, res))
