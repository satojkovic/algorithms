class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# This function detects if a linked list has a cycle.
# It uses two pointers, slow and fast. The slow pointer moves one step at a time,
# while the fast pointer moves two steps at a time. If there is a cycle, the fast pointer
# will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list.
# The time complexity is O(n) and the space complexity is O(1).
# The function returns True if a cycle is detected, otherwise it returns False.
def hasCycle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


def test_hasCycle():
    # Test case 1: No cycle
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    assert not hasCycle(head1)

    # Test case 2: Cycle exists
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = head2  # Creating a cycle
    assert hasCycle(head2)

    # Test case 3: Single node with no cycle
    head3 = ListNode(1)
    assert not hasCycle(head3)

    # Test case 4: Single node with cycle
    head4 = ListNode(1)
    head4.next = head4  # Creating a cycle
    assert hasCycle(head4)

    # Test case 5: Empty list
    head5 = None
    assert not hasCycle(head5)
