class ListNode:
    def __init__(self, x=0):
        self.val = x
        self.next = None


# Time complexity: O(m + n)
#  we need to traverse each element within two lists
#
# Space complexity: O(m + n)
#  m + n recursive calls


def merge_two_sorted_list(l1, l2):
    # Edge case:
    # If l1 or l2 is initially None, there is no merge to perform.
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val <= l2.val:
        l1.next = merge_two_sorted_list(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_list(l1, l2.next)
        return l2


def merge_two_sorted_list_iter(l1, l2):
    dummy_head = ListNode()
    curr_head = dummy_head
    while l1 and l2:
        if l1.val <= l2.val:
            curr_head.next = l1
            l1 = l1.next
        else:
            curr_head.next = l2
            l2 = l2.next
        curr_head = curr_head.next
    curr_head.next = l1 if l1 else l2
    return dummy_head.next
