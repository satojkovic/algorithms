class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def delete_middle_node(node):
    if node is None or node.next is None:
        return False
    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next
    return True