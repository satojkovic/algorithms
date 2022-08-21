import math

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print(f'Case #{t}: {math.ceil(N/5)}')
