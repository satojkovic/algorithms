class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
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
        new_head = removeNthFromEnd(head, n)
        result = linked_list_to_list(new_head)
        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
