class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time complexity: O(m + n)
#  we need to traverse each element within two lists
#
# Space complexity: O(m + n)
#  m + n recursive calls
def merge_two_sorted_list1(l1, l2):
    head = None
    return merge_list(head, l1, l2)

def merge_list(head, l1, l2):
    if l1 is None and l2 is None:
        return None
    if l1 is None:
        head = ListNode(l2.val)
        head.next = merge_list(head.next, l1, l2.next)
    elif l2 is None:
        head = ListNode(l1.val)
        head.next = merge_list(head.next, l1.next, l2)
    else:
        if l1.val <= l2.val:
            head = ListNode(l1.val)
            head.next = merge_list(head.next, l1.next, l2)
        else:
            head = ListNode(l2.val)
            head.next = merge_list(head.next, l1, l2.next)
    return head

def merge_two_sorted_list2_0(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    if l1.val <= l2.val:
        head = ListNode(l1.val)
        head.next = merge_two_sorted_list2_0(l1.next, l2)
    else:
        head = ListNode(l2.val)
        head.next = merge_two_sorted_list2_0(l1, l2.next)
    return head

def merge_two_sorted_list2(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1

    if l1.val <= l2.val:
        l1.next = merge_two_sorted_list2(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_list2(l1, l2.next)
        return l2

def merge_two_sorted_list3(l1, l2):
    dummy_head = ListNode(-1)
    head = dummy_head
    # To avoid changing l1 and l2, new node is created from the value of l1 and l2.
    while l1 and l2:
        if l1.val <= l2.val:
            head.next = ListNode(l1.val)
            l1 = l1.next
        else:
            head.next = ListNode(l2.val)
            l2 = l2.next
        head = head.next
    remains = l1 if l1 else l2
    while remains:
        head.next = ListNode(remains.val)
        head = head.next
        remains = remains.next
    return dummy_head.next