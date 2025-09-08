import pytest
from invert_binary_tree import invert_binary_tree, invertTree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        return (self.val == other.val and 
                self.left == other.left and 
                self.right == other.right)

def tree_to_list(root):
    """ツリーをレベル順のリストに変換（テスト用）"""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # 末尾のNoneを削除
    while result and result[-1] is None:
        result.pop()
    
    return result

class TestInvertBinaryTree:
    
    def test_empty_tree(self):
        """空のツリーのテスト"""
        assert invert_binary_tree(None) is None
    
    def test_single_node(self):
        """単一ノードのテスト"""
        root = TreeNode(1)
        inverted = invert_binary_tree(root)
        assert inverted.val == 1
        assert inverted.left is None
        assert inverted.right is None
    
    def test_two_nodes(self):
        """2つのノードのテスト"""
        root = TreeNode(1)
        root.left = TreeNode(2)

        inverted = invert_binary_tree(root)
        expected = [1, None, 2]
        result = tree_to_list(inverted)
        assert result == expected

    def test_complete_binary_tree(self):
        """完全二分木のテスト"""
        # 元のツリー:     4
        #              /   \
        #             2     7
        #            / \   / \
        #           1   3 6   9

        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        inverted = invert_binary_tree(root)

        # 反転後:       4
        #              /   \
        #             7     2
        #            / \   / \
        #           9   6 3   1

        expected = [4, 7, 2, 9, 6, 3, 1]
        result = tree_to_list(inverted)
        assert result == expected

    def test_unbalanced_tree(self):
        """不均衡なツリーのテスト"""
        # 元のツリー:   1
        #              /
        #             2
        #            /
        #           3

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)

        inverted = invert_binary_tree(root)

        # 反転後:     1
        #              \
        #               2
        #                \
        #                 3

        expected = [1, None, 2, None, 3]
        result = tree_to_list(inverted)
        assert result == expected

    def test_right_skewed_tree(self):
        """右に偏ったツリーのテスト"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        inverted = invert_binary_tree(root)
        expected = [1, 2, None, 3]
        result = tree_to_list(inverted)
        assert result == expected

if __name__ == "__main__":
    pytest.main([__file__])
