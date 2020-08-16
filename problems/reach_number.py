from collections import deque
def reach_number(target):
    q = deque([(0, 0, 0)])
    while q:
        n, move, prev = q.popleft()
        if n * move + prev == target:
            return n
        prev = n * move + prev
        q.append((n + 1, 1, prev))
        q.append((n + 1, -1, prev))