class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_two_numbers(l1, l2):
    dummy = ListNode(None)
    head = dummy
    carry = 0
    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        total = l1_val + l2_val + carry
        head.next = ListNode(total % 10)
        carry = total // 10
        head = head.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
    if carry:
        head.next = ListNode(carry)
    return dummy.next


def add_two_numbers_recursion(l1, l2):
    def addition(l1, l2, carry):
        if l1 is None and l2 is None and carry == 0:
            return None
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        total = l1_val + l2_val + carry
        node = ListNode(total % 10)
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
        node.next = addition(l1, l2, total // 10)
        return node
    return addition(l1, l2, 0)
