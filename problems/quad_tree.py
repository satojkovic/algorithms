import itertools


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def gen_quad_tree(grid):
    def quad_tree(grid, top, left, bottom, right):
        if all_same(grid, top, left, bottom, right):
            return Node(grid[top][left], True, None, None, None, None)

        # isLeaf is False
        curr_root = Node(0, False, None, None, None, None)
        mid_row = (top + bottom) // 2
        mid_col = (left + right) // 2
        curr_root.topLeft = quad_tree(grid, top, left, mid_row, mid_col)
        curr_root.bottomLeft = quad_tree(grid, mid_row, left, bottom, mid_col)
        curr_root.topRight = quad_tree(grid, top, mid_col, mid_row, right)
        curr_root.bottomRight = quad_tree(grid, mid_row, mid_col, bottom, right)
        return curr_root

    return quad_tree(grid, 0, 0, len(grid), len(grid))


def all_same(grid, top, left, bottom, right):
    grid_sum = sum(
        [
            grid[row][col]
            for row, col in itertools.product(range(top, bottom), range(left, right))
        ]
    )
    n = bottom - top
    return True if grid_sum == 0 or grid_sum == n**2 else False


def test_gen_quad_tree():
    import deepdiff

    grid = [[0, 1], [1, 0]]
    assert deepdiff.DeepDiff(
        gen_quad_tree(grid), [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]
    )

    grid = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ]
    assert deepdiff.DeepDiff(
        gen_quad_tree(grid),
        [
            [0, 1],
            [1, 1],
            [0, 1],
            [1, 1],
            [1, 0],
            None,
            None,
            None,
            None,
            [1, 0],
            [1, 0],
            [1, 1],
            [1, 1],
        ],
    )
