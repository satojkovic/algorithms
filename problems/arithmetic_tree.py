class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def calc(root):
    def ops(op, a, b):
        if op == '*':
            return a * b
        elif op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '/':
            return a // b
    if root.right is None and root.left is None:
        return root.val
    return ops(root.val, calc(root.left), calc(root.right))

if __name__ == "__main__":
    root = TreeNode('*')
    root.left = TreeNode('+')
    root.right = TreeNode('+')
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print(calc(root))