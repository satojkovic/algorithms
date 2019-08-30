class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time complexity: O(n)
#  We need to visit every node in the tree.
#
# Space complexity: O(log(n)) at average case, O(n) at worst case
#  Maximum depth of recursion tree is log(n) or n
#
# Algorithm:
#  Visit left node, and add current value to the list, and then visit right node.
#  Return the concatenated list.
def tree_inorder_trav1(root):
    if root is None:
        return []
    
    left = tree_inorder_trav1(root.left)
    val = [root.val]
    right = tree_inorder_trav1(root.right)
    return left + val + right

# Time complexity: O(n)
# Space complexity: O(n) 
def tree_inorder_trav2(root):
    ret = []
    s = []
    while s or root:
        if root:
            s = [root] + s
            root = root.left
        else:
            cur = s.pop(0)
            ret.append(cur.val)
            root = cur.right
    return ret