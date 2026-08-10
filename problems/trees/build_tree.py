from tree_common import TreeNode, build_tree

def build_tree1(inorder, postorder):
    def _build_tree(root, inorder, postorder):
        if len(inorder) == 0 and len(postorder) == 0:
            return None
        if len(inorder) == 1 and len(postorder) == 1:
            return TreeNode(inorder[0])

        if root is None:
            root = TreeNode(postorder[-1])
        parent = postorder[-1]
        parent_idx = inorder.index(parent)
        root.left = _build_tree(
            root.left, inorder[:parent_idx], postorder[:len(inorder[:parent_idx])])
        root.right = _build_tree(
            root.right, inorder[parent_idx + 1:], postorder[len(postorder) - len(inorder[parent_idx + 1:]) - 1: -1])
        return root
    if len(postorder) == 0:
        return None
    return _build_tree(None, inorder, postorder)

def build_tree2(inorder, postorder):
    def _build_tree(root, inorder, postorder, left_in, right_in, left_post, right_post):
        if right_in < 0 or left_in >= len(inorder) or left_in > right_in:
            return None
        if left_in == right_in:
            return TreeNode(inorder[left_in])
        if root is None:
            root = TreeNode(postorder[right_post])
        parent_idx = inorder.index(postorder[right_post])
        left_len = parent_idx - left_in
        right_len = right_in - parent_idx
        root.left = _build_tree(
            root.left, inorder, postorder, left_in, parent_idx - 1, 
            left_post, left_post + left_len - 1)
        root.right = _build_tree(
            root.right, inorder, postorder, parent_idx + 1, right_in,
            left_post + left_len, left_post + left_len + right_len - 1
        )
        return root
    return _build_tree(None, inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

def build_tree_pre_in(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = inorder.index(root_val)

    root.left = build_tree_pre_in(preorder[1 : mid + 1], inorder[: mid])
    root.right = build_tree_pre_in(preorder[mid + 1 :], inorder[mid + 1 :])

    return root

def build_tree_pre_in2(preorder, inorder):
    # inorderの値とインデックスの対応表を事前に作成しておく (O(1)で位置を特定するため)
    in_map = {val: i for i, val in enumerate(inorder)}

    # preorderを先頭から順に消費するためのポインタ
    pre_iter = iter(preorder)

    # inorderにおける範囲 [left_in, right_in] を引数にする
    def helper(left_in, right_in):
        if left_in > right_in:
            return None

        # 現在のRootの値を取り出す
        root_val = next(pre_iter)
        root = TreeNode(root_val)

        # inorderにおけるRootの位置
        mid = in_map[root_val]

        # 左右の範囲を狭めて再帰呼び出し
        root.left = helper(left_in, mid - 1)
        root.right = helper(mid + 1, right_in)

        return root

    return helper(0, len(inorder) - 1)
