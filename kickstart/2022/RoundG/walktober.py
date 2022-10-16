import numpy as np

T = int(input())
for t in range(1, T + 1):
    M, N, P = list(map(int, input().split()))
    board = []
    for _ in range(M):
        b = list(map(int, input().split()))
        board.append(b)
    board = np.array(board)
    total = 0
    for n in range(N):
        top = sorted(board[:, n], reverse=True)[0]
        diff = top - board[P-1, n]
        total = total + diff if diff > 0 else total
    print('Case #{}: {}'.format(t, total))
