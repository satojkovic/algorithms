def numIslands(grid):
    def dfs(row, col):
        if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] != '1':
            return
        grid[row][col] = '0'
        dfs(row + 1, col)
        dfs(row, col + 1)
        dfs(row - 1, col)
        dfs(row, col - 1)

    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                num_islands += 1
                dfs(row, col)

    return num_islands


from collections import deque
def num_islands_bfs(grid):
    def bfs(row, col):
        q = deque([(row, col)])
        grid[row][col] = '0'
        rows = len(grid)
        cols = len(grid[0])
        while q:
            row, col = q.popleft()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1':
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = '0'

    num_islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                num_islands += 1
                bfs(row, col)

    return num_islands

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
