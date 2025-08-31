# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head):
    org_to_copy = {None : None}
    curr = head
    while curr:
        org_to_copy[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        copy = org_to_copy[curr]
        copy.next = org_to_copy[curr.next]
        copy.random = org_to_copy[curr.random]
        curr = curr.next

    return org_to_copy[head]

def test_copy_random_list():
    # Create a linked list with random pointers
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.random = head.next
    head.next.random = head

    # Copy the linked list
    copied_head = copy_random_list(head)

    # Check if the copied list is correct
    assert copied_head.val == 1
    assert copied_head.next.val == 2
    assert copied_head.next.next.val == 3
    assert copied_head.random == copied_head.next
    assert copied_head.next.random == copied_head
