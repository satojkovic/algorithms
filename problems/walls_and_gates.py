from collections import deque
from typing import List

def wallsAndGates(rooms: List[List[int]]) -> None:
    """
    Do not return anything, modify rooms in-place instead.
    """
    INF = 2147483647
    queue = deque()
    rows, cols = len(rooms), len(rooms[0])
    for row in range(rows):
        for col in range(cols):
            if rooms[row][col] == 0:
                queue.append((row, col))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        row, col = queue.popleft()
        dist = rooms[row][col]
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            if 0 <= next_row < rows and 0 <= next_col < cols and rooms[next_row][next_col] == INF:
                rooms[next_row][next_col] = dist + 1
                queue.append((next_row, next_col))


def test_wallsAndGates():
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    wallsAndGates(rooms)
    expected = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4]
    ]
    assert rooms == expected