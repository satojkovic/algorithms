class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_dups_from_linked_list(head):
    if head is None:
        return head
    dummy_head = ListNode('dummy')
    prev_head = dummy_head
    prev_head.next = head
    curr_head = head
    dups = set()
    while curr_head:
        if curr_head.val in dups:
            prev_head.next = curr_head.next
        else:
            dups.add(curr_head.val)
            prev_head = curr_head
        curr_head = curr_head.next
    return dummy_head.next


def test_remove_dups_from_linked_list():
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(4)
    head.next.next.next = ListNode(1)
    no_dups_head = remove_dups_from_linked_list(head)

    assert no_dups_head.val == 1
    assert no_dups_head.next.val == 3
    assert no_dups_head.next.next.val == 4
    assert no_dups_head.next.next.next is None
