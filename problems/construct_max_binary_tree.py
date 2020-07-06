class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_max_binary_tree(self, nums):
    def construct(nums, left_idx, right_idx):
        if left_idx > right_idx:
            return None
        if left_idx == right_idx:
            return TreeNode(nums[left_idx])
        max_val = max(nums[left_idx:right_idx + 1])
        node = TreeNode(max_val)
        node.left = construct(nums, left_idx, nums.index(max_val) - 1)
        node.right = construct(nums, nums.index(max_val) + 1, right_idx)
        return node
    return construct(nums, 0, len(nums) - 1)