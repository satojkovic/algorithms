class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Time complexity: O(n)
#  traverse an input list once
# Space complexity: O(log2(n))
#  recursively call with half length of nums to build left and right subtree
def sorted_array_to_bst1(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return TreeNode(nums[0])

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst1(nums[:mid])
    root.right = sorted_array_to_bst1(nums[mid+1:])
    return root