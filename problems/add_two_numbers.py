class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None or l2 is None:
        return l1 if l2 is None else l2
    res = ListNode(None)
    head = res
    carry = 0
    while l1 or l2:
        total = l1.val if l1 else 0
        total += l2.val if l2 else 0
        total += carry
        head.next = ListNode(total % 10)
        carry = total // 10
        head = head.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry != 0:
        head.next = ListNode(carry)
        head = head.next
    return res.next
