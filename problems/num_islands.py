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
    rows = len(grid)
    cols = len(grid[0])
    while q:
        r, c = q.popleft()
        grid[r][c] = '0'
        for delta_r, delta_c in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= r + delta_r < rows and 0 <= c + delta_c < cols and grid[r + delta_r][c + delta_c] == '1':
                q.append((r + delta_r, c + delta_c))
                grid[r + delta_r][c + delta_c] = '0'
