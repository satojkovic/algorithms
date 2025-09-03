class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end_onepass(head: ListNode|None, n: int) -> ListNode|None:
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    for _ in range(n + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next

def remove_nth_from_end(head: ListNode|None, n: int) -> ListNode|None:
    length = 0
    current = head
    while current:
        current = current.next
        length += 1

    if length == n:
        return head.next

    node_before_removed_index = length - n - 1
    current = head
    for _ in range(node_before_removed_index):
        current = current.next

    current.next = current.next.next

    return head

def removeNthFromEnd(head: ListNode|None, n: int) -> ListNode|None:
    fast = head
    for _ in range(n):
        fast = fast.next
    slow = head
    dummy = None

    while fast:
        fast = fast.next
        dummy = slow
        slow = slow.next

    if dummy:
        dummy.next = slow.next
        slow.next = None
    else:
        head = slow.next

    return head

def test_remove_nth_from_end():
    # Helper function to create a linked list from a list
    def create_linked_list(lst):
        dummy = ListNode()
        current = dummy
        for value in lst:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Helper function to convert a linked list to a list
    def linked_list_to_list(head):
        lst = []
        current = head
        while current:
            lst.append(current.val)
            current = current.next
        return lst

    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ]

    for i, (lst, n, expected) in enumerate(test_cases):
        head = create_linked_list(lst)
        new_head = remove_nth_from_end_onepass(head, n)
        result = linked_list_to_list(new_head)
        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
