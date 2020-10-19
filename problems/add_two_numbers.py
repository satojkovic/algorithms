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

def add_two_numbers2(l1, l2):
    if l1 is None or l2 is None:
        return l1 if l2 is None else l2
    head = None
    prev_head = None
    carry = -1
    while l1 or l2 or carry:
        # Calculate addition
        total = l1.val if l1 else 0
        total += l2.val if l2 else 0
        total += carry if carry != -1 else 0
        # Create node
        node = ListNode(total % 10)
        if prev_head:
            prev_head.next = node
        prev_head = node
        if head is None:
            head = node
        # Prepare next iteration
        carry = total // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return head

def add_two_numbers3(l1, l2):
    def addition(l1, l2, carry):
        if l1 is None and l2 is None and carry == 0:
            return None
        total = l1.val if l1 else 0
        total += l2.val if l2 else 0
        total += carry
        node = ListNode(total % 10)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        node.next = addition(l1, l2, total // 10)
        return node
    return addition(l1, l2, 0)
