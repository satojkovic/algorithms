def power_set(S):
    def helper(S, i):
        if len(S[i:]) == 0:
            return [[]]
        ps = []
        for sub_ps in helper(S, i+1):
            ps.append(sub_ps)
            ps.append(sub_ps + [S[i]])
        return ps
    return helper(S, 0)

def total_weight(cand):
    return sum([weight for weight, value in cand])

def sales_value(cand):
    return sum([value for weight, value in cand])

def knapsack_brute_force(items, max_weight):
    best_value = 0
    best_cand = []
    for cand in power_set(items):
        if total_weight(cand) <= max_weight:
            if sales_value(cand) > best_value:
                best_value = sales_value(cand)
                best_cand = cand
    return best_cand

def knapsack_greedy(items, max_weight):
    bag_weight = 0
    bag_items = []
    for item in sorted(items, key=lambda x: x[1], reverse=True):
        if max_weight >= bag_weight + item[0]:
            bag_weight = bag_weight + item[0]
            bag_items.append(item)
    return bag_items

if __name__ == "__main__":
    ps = power_set(['a', 'b', 'c'])
    print(ps)

    # (weight, value)
    res = knapsack_brute_force([(2, 4), (2, 5), (1, 2), (3, 8)], 5)
    print(sum([value for weight, value in res]))

    res = knapsack_brute_force([(9, 5), (10, 4)], 20)
    print(sum([value for weight, value in res]))

    res = knapsack_greedy([(2, 4), (2, 5), (1, 2), (3, 8)], 5)
    print(sum([value for weight, value in res]))

    res = knapsack_greedy([(9, 5), (10, 4)], 20)
    print(sum([value for weight, value in res]))
