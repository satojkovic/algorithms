def walls_and_gates(rooms):
    if len(rooms) == 0:
        return
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] != 0 and rooms[row][col] != -1:
                rooms[row][col] = bfs(rooms, row, col)

def bfs(rooms, row, col):
    m = len(rooms)
    n = len(rooms[0])
    dist = [n * [0] for _ in range(m)]
    q = [(row, col)]
    while q:
        row, col = q.pop(0)
        for (r_step, c_step) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = row + r_step
            c = col + c_step
            if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] == -1:
                continue
            # Already visited
            if dist[r][c] != 0:
                continue
            dist[r][c] = dist[row][col] + 1
            if rooms[r][c] == 0:
                return dist[r][c]
            q.append((r, c))
    return rooms[row][col]

if __name__ == "__main__":
    INF = 2147483647
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]
    ]
    walls_and_gates(rooms)
    print(rooms)