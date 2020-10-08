class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def kth_to_last(head, k):
    behind = head
    for i in range(k):
        if head is None:
            return None
        head = head.next
    while head:
        head = head.next
        behind = behind.next
    return behind

def kth_to_last2(head, k):
    def get_kth(head, k):
        if head is None:
            return None, 1
        kth_node, kth = get_kth(head.next, k)
        if kth == k:
            return (head, kth) if kth_node is None else (kth_node, kth)
        else:
            return None, kth + 1
    kth_node, kth = get_kth(head, k)
    return kth_node
