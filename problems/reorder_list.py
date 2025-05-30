class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    left, right = 0, len(nodes) - 1
    while left < right:
        nodes[left].next = nodes[right]
        left += 1
        if left >= right:
            break
        nodes[right].next = nodes[left]
        right -= 1
    nodes[left].next = None


def test_reorder_list():
    # Create a linked list: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    reorderList(head)

    # Check the order: 1 -> 4 -> 2 -> 3
    assert head.val == 1
    assert head.next.val == 4
    assert head.next.next.val == 2
    assert head.next.next.next.val == 3
    assert head.next.next.next.next is None

    # Create a linked list: 1 -> 2 -> 3
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    reorderList(head)
    # Check the order: 1 -> 3 -> 2
    assert head.val == 1
    assert head.next.val == 3
    assert head.next.next.val == 2
    assert head.next.next.next is None

    # Create a linked list: 1 -> 2
    head = ListNode(1)
    head.next = ListNode(2)
    reorderList(head)
    # Check the order: 1 -> 2
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next is None

    # Create a linked list: 1
    head = ListNode(1)
    reorderList(head)
    # Check the order: 1
    assert head.val == 1
    assert head.next is None
