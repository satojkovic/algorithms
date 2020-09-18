class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# O(nlog(n))
def min_tree(nums):
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    for i in range(len(nums)):
        if i == mid:
            continue
        root = insert(root, nums[i])
    return root

def insert(root, val):
    if root is None:
        return TreeNode(val)
    if root.val > val:
        left = insert(root.left, val)
        root.left = left
    elif root.val < val:
        right = insert(root.right, val)
        root.right = right
    return root

# O(n)
def min_tree2(nums):
    return create_min_tree(nums, 0, len(nums) - 1)
    
def create_min_tree(nums, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    root = TreeNode(nums[mid])
    root.left = create_min_tree(nums, left, mid - 1)
    root.right = create_min_tree(nums, mid + 1, right)
    return root

if __name__ == "__main__":
    nums = [1, 3, 10, 11, 25]
    root = min_tree(nums)
    print('min_tree =>', root.left.right.val, root.left.val, root.val, root.right.val, root.right.right.val)

    root = min_tree2(nums)
    print('min_tree2 =>', root.left.right.val, root.left.val, root.val, root.right.val, root.right.right.val)
