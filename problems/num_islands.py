def numIslands(grid):
    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                dfs(grid, row, col)
                num_islands += 1
    return num_islands

def dfs(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1':
        return
    grid[row][col] = '0'
    dfs(grid, row + 1, col)
    dfs(grid, row, col + 1)
    dfs(grid, row - 1, col)
    dfs(grid, row, col - 1)

from collections import deque
def bfs(grid, row, col):
    q = deque([(row, col)])
    grid[row][col] = '0'
    rows = len(grid)
    cols = len(grid[0])
    while q:
        r, c = q.popleft()
        for delta_r, delta_c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= r + delta_r < rows and 0 <= c + delta_c < cols and grid[r + delta_r][c + delta_c] == '1':
                q.append((r + delta_r, c + delta_c))
                grid[r + delta_r][c + delta_c] = '0'


def num_islands_union_find(grid):
    def union(p, q):
        root_p = find(p)
        root_q = find(q)
        if root_p != root_q:
            parent[root_q] = root_p

    def find(p):
        while parent[p] != p:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    parent = {}
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    id_grid = [[0] * cols for _ in range(rows)]
    island_id = 1
    num_islands = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                current_id = island_id
                parent[island_id] = current_id
                id_grid[row][col] = current_id
                num_islands += 1
                island_id += 1

                if row > 0 and grid[row - 1][col] == '1':
                    neighbor_id = id_grid[row - 1][col]
                    if find(current_id) != find(neighbor_id):
                        union(current_id, neighbor_id)
                        num_islands -= 1

                if col > 0 and grid[row][col - 1] == '1':
                    neighbor_id = id_grid[row][col - 1]
                    if find(current_id) != find(neighbor_id):
                        union(current_id, neighbor_id)
                        num_islands -= 1

    return num_islands

def test_num_islands():
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert numIslands([row[:] for row in grid1]) == 3
    assert num_islands_union_find([row[:] for row in grid1]) == 3

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["0", "1", "0", "0", "1"],
        ["1", "0", "0", "1", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "0", "1", "0", "1"]
    ]
    assert numIslands([row[:] for row in grid2]) == 6
    assert num_islands_union_find([row[:] for row in grid2]) == 6

    grid3 = [["1","1","1"],["0","1","0"],["1","1","1"]]
    assert numIslands([row[:] for row in grid3]) == 1
    assert num_islands_union_find([row[:] for row in grid3]) == 1
