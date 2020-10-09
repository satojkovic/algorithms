class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):
    if root is None:
        return False
    if root.val == target.val:
        return True
    return search(root.left, target) or search(root.right, target)

def first_common_ancestor(root, p, q):
    if root is None:
        return None
    if root.val == p.val:
        return root if search(root, q) else None
    if root.val == q.val:
        return root if search(root, p) else None
    
    cond_a = search(root.left, p)
    cond_b = search(root.right, q)
    cond_c = search(root.left, q)
    cond_d = search(root.right, p)
    
    if (cond_a and cond_b) or (cond_c and cond_d):
        return root
    elif cond_a and cond_c:
        return first_common_ancestor(root.left, p, q)
    elif cond_b and cond_d:
        return first_common_ancestor(root.right, p, q)
    else:
        return None

def first_common_ancestor2(root, p, q):
    def helper(root, p, q):
        if root is None or root.val == p.val or root.val == q.val:
            return root

        p_is_left = search(root.left, p)
        q_is_left = search(root.left, q)
        if p_is_left != q_is_left:
            return root

        return helper(root.left, p, q) if p_is_left else helper(root.right, p, q)

    if not search(root, p) or not search(root, q):
        return None
    return helper(root, p, q)
