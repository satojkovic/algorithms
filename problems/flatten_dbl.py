class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten2(head):
    def _preorder(root):
        if root is None:
            return []
        left = _preorder(root.child)
        right = _preorder(root.next)
        return [root] + left + right

    def _create_flatten_list(lst):
        for i in range(len(lst)):
            lst[i].prev = lst[i - 1] if i != 0 else None
            lst[i].next = lst[i + 1] if i != len(lst) - 1 else None
            lst[i].child = None
        return lst[0]

    lst = _preorder(head)
    return _create_flatten_list(lst) if len(lst) != 0 else None

def flatten(head):
    def _flatten(prev, curr):
        if curr is None:
            return prev
        curr.prev = prev
        prev.next = curr
        tmp = curr.next
        tail = _flatten(curr, curr.child)
        curr.child = None
        return _flatten(tail, tmp)

    if head is None:
        return head

    sentinel = Node(None, None, head, None)
    tail = _flatten(sentinel, head)
    head.prev = None
    return head
