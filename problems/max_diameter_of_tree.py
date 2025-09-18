class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
#  we visit each node once, where n is the number of nodes in the tree.
# Space complexity: O(h)
#  the space complexity is O(h), where h is the height of the tree.
#  This space is used by the recursion stack during the depth-first search (DFS).
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0

        def get_depth(root):
            if not root:
                return 0
            left_depth = get_depth(root.left)
            right_depth = get_depth(root.right)
            self.max_diameter = max(left_depth + right_depth, self.max_diameter)
            return max(left_depth, right_depth) + 1

        get_depth(root)
        return self.max_diameter


def diameterOfBinaryTree(root: TreeNode) -> int:
    max_diameter = 0

    def get_depth(root):
        nonlocal max_diameter
        if not root:
            return 0
        left_depth = get_depth(root.left)
        right_depth = get_depth(root.right)
        max_diameter = max(left_depth + right_depth, max_diameter)
        return max(left_depth, right_depth) + 1

    get_depth(root)
    return max_diameter


def test_max_diameter_of_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    assert solution.diameterOfBinaryTree(root) == 3

    root2 = TreeNode(1)
    root2.left = TreeNode(2)

    assert solution.diameterOfBinaryTree(root2) == 1

    root3 = None
    assert solution.diameterOfBinaryTree(root3) == 0


def test_max_diameter_of_tree_function():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    assert diameterOfBinaryTree(root) == 3

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    assert diameterOfBinaryTree(root2) == 1

    root3 = None
    assert diameterOfBinaryTree(root3) == 0
