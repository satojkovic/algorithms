class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def rot_right_linked_list(head, k):
    if head is None:
        return head
    tail = head
    n = 0
    while tail.next:
        tail = tail.next
        n += 1
    tail.next = head
    n += 1

    new_tail = head
    step = n - k % n - 1
    while step > 0:
        new_tail = new_tail.next
        step -= 1
    head = new_tail.next
    new_tail.next = None
    return head