class ListElement:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_every_two_nodes(head):
    # Swap nodes backward
    def swap(head, index):
        if not head or head.next is None:
            return head
        ret_head = swap(head.next, index + 1)
        if index % 2 == 0:
            head.next = ret_head.next
            ret_head.next = head
            return ret_head
        else:
            head.next = ret_head
            return head
    return swap(head, 0)

if __name__ == "__main__":
    head = ListElement(1)
    head.next = ListElement(2)
    head.next.next = ListElement(3)
    head.next.next.next = ListElement(4)
    ret_head = swap_every_two_nodes(head)
    while ret_head:
        print('{}->'.format(ret_head.data))
        ret_head = ret_head.next
    print('None')