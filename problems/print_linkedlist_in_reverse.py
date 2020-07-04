def print_linkedlist_in_reverse(head):
    if head is None:
        return
    print_linkedlist_in_reverse(head.getNext())
    head.printValue()
    return

def print_linkedlist_in_reverse_(head):
    tail = None
    while head != tail:
        curr = head
        while curr.getNext() != tail:
            curr = curr.getNext()
        tail = curr
        tail.printValue()