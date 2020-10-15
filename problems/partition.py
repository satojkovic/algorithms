class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def partition(head, x):
    before_head, before_tail = None, None
    after_head, after_tail = None, None
    while head:
        next_head = head.next
        head.next = None
        if head.val < x:
            if before_head is None:
                before_head = head
                before_tail = before_head
            else:
                before_tail.next = head
                before_tail = head
        else:
            if after_head is None:
                after_head = head
                after_tail = after_head
            else:
                after_tail.next = head
                after_tail = head
        head = next_head
    if before_head is None:
        return after_head
    before_tail.next = after_head
    return before_head

if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(5)
    head.next.next = ListNode(8)
    head.next.next.next = ListNode(2)
    partitioned = partition(head, 5)
    while partitioned:
        print(partitioned.val)
        partitioned = partitioned.next