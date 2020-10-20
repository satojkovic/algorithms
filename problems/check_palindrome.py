from collections import deque
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def isPalindrome(head):
    # When the head pointer is None,
    # slow is also None and nodes is empty.
    # isPalindrome(None) returns True surely because while loop is skipped.
    slow, nodes = get_slow_pointer(head)
    while slow:
        node = nodes.pop()
        if node.val != slow.val:
            return False
        slow = slow.next
    return True

def get_slow_pointer(head):
    nodes = deque([])
    fast = head
    slow = head
    while fast and fast.next:
        nodes.append(slow)
        fast = fast.next.next
        slow = slow.next
    # After fast pointer move N times, 
    # if fast pointer is at last node, then the length of list is odd.
    # On the other hand, if fast pointer is None, the length of list is even.
    # So the length of list is odd(`if fast` condition is true),
    # slow pointer moves next because slow is at middle position.
    # But the length is even, slow pointer stay at that position(already at next to middle node).
    return (slow.next, nodes) if fast else (slow, nodes)

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(1)

    print(isPalindrome(head))