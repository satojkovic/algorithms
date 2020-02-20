def walls_and_gates(rooms):
    if len(rooms) == 0:
        return
    m = len(rooms)
    n = len(rooms[0])
    for row in range(m):
        for col in range(n):
            visited = [n * [0] for _ in range(m)]
            dist = [n * [0] for _ in range(m)]
            if rooms[row][col] != 0 and rooms[row][col] != -1:
                rooms[row][col] = bf(row, col, rooms, visited, dist)

def bf(row, col, rooms, visited, dist):
    q = [(row, col)]
    visited[row][col] = 1
    while q:
        r, c = q.pop(0)
        if rooms[r][c] == 0:
            return dist[r][c]
        elif rooms[r][c] == -1:
            continue
        if r - 1 >= 0 and visited[r-1][c] == 0:
            q.append((r-1, c))
            visited[r-1][c] = 1
            dist[r-1][c] = dist[r][c] + 1
        if r + 1 < len(rooms) and visited[r+1][c] == 0:
            q.append((r+1, c))
            visited[r+1][c] = 1
            dist[r+1][c] = dist[r][c] + 1
        if c - 1 >= 0 and visited[r][c-1] == 0:
            q.append((r, c-1))
            visited[r][c-1] = 1
            dist[r][c-1] = dist[r][c] + 1
        if c + 1 < len(rooms[0]) and visited[r][c+1] == 0:
            q.append((r, c+1))
            visited[r][c+1] = 1
            dist[r][c+1] = dist[r][c] + 1
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