class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def path_count_with_sum(root, target_sum):
    def count(root, target_sum):
        if root is None:
            return 0, []
        left_count, left_nodes = count(root.left, target_sum)
        right_count, right_nodes = count(root.right, target_sum)
        res = left_count + right_count
        nodes = left_nodes + right_nodes
        node_sums = [root.val] if len(nodes) == 0 else []
        for node in nodes:
            if node + root.val == target_sum:
                res += 1
            node_sums.append(node + root.val)
        return res, node_sums
    res, res_nodes = count(root, target_sum)
    return res

if __name__ == "__main__":
    root = TreeNode(11)
    root.left = TreeNode(3)
    root.left.left = TreeNode(9)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(-1)
    root.right.right = TreeNode(20)
    print(path_count_with_sum(root, 18))

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(1)
    root.right = TreeNode(-3)
    root.right.right = TreeNode(11)
    print(path_count_with_sum(root, 8))
