def binary_search(sorted_data, target, l, r):
    while r - l > 1:
        mid = l + (r - l) // 2
        if sorted_data[mid] <= 2 * target:
            l = mid
        else:
            r = mid
    return l

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    sorted_data = sorted(data)
    res = []
    for target in data:
        idx = binary_search(sorted_data, target, 0, N)
        if sorted_data[idx] != target:
            res.append(sorted_data[idx])
        else:
            ans = sorted_data[idx - 1] if idx != 0 else -1
            res.append(ans)
    print(f"Case #{t}: {' '.join(list(map(str, res)))}")
