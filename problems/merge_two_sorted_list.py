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