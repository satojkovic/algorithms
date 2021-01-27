class TreeNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

def unique_bst(n):
    if n is None or n <= 0:
        return []
    return unique_bst_creator(1, n)

def unique_bst_creator(start, end):
    if start > end:
        return [None]
    all_trees = []
    for i in range(start, end + 1):
        left = unique_bst_creator(start, i - 1)
        right = unique_bst_creator(i + 1, end)
        for l in left:
            for r in right:
                root = TreeNode(i)
                root.left = l
                root.right = r
                all_trees.append(root)
    return all_trees

if __name__ == "__main__":
    trees = unique_bst(3)
    print('unique_bst(3) => ', len(trees))
