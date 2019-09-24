# Time complexity: O(n)
#
# Space complexity: O(n)
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_symmetry1(root):
    if not root:
        return True
    q = []
    q.append([root.left, root.right])
    while q:
        t1, t2 = q.pop(0)
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        q.append([t1.left, t2.right])
        q.append([t1.right, t2.left])
    return True
