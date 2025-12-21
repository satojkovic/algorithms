from collections import defaultdict

H, W, N = list(map(int, input().split()))
mat = []
for row in range(H):
    line = list(map(int, input().split()))
    mat.append(line)
Bs = []
for n in range(N):
    num = int(input())
    Bs.append(num)

ans = defaultdict(int)
for row in range(H):
    for b in Bs:
        if b in mat[row]:
            ans[row] += 1

max_value = -1
for row in range(H):
    max_value = max(max_value, ans[row])

print(max_value)
