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

def delete_middle_node2(head):
    if head is None or head.next is None:
        return False
    slow = head
    prev_slow = head
    count = 0
    while head:
        if count and count % 2 == 0:
            prev_slow = slow
            slow = slow.next
        head = head.next
        count += 1
    if slow.next and slow != prev_slow:
        prev_slow.next = slow.next

if __name__ == "__main__":
    head = ListNode('a')
    head.next = ListNode('b')
    head.next.next = ListNode('c')
    head.next.next.next = ListNode('d')
    head.next.next.next.next = ListNode('e')
    head.next.next.next.next.next = ListNode('f')
    delete_middle_node2(head)
    while head:
        print(head.val)
        head = head.next

