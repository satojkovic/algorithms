class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_intersection_node(head_a, head_b):
    if head_a is None or head_b is None:
        return None
    ha = head_a
    hb = head_b
    while ha is not hb:
        ha = head_b if ha is None else ha.next
        hb = head_a if hb is None else hb.next
    return ha

def get_intersection_node2(head_a, head_b):
    if not head_a or not head_b:
        return None
    nodes = set()
    ha = head_a
    while ha:
        nodes.add(ha)
        ha = ha.next
    hb = head_b
    while hb:
        if hb in nodes:
            return hb
        hb = hb.next
    return None

def get_intersection_node3(head_a, head_b):
    tail_a, length_a = get_list_length(head_a)
    tail_b, length_b = get_list_length(head_b)
    if tail_a != tail_b:
        return None
    diff = abs(length_a - length_b)
    longer = head_a if length_a > length_b else head_b
    shorter = head_b if length_a > length_b else head_a
    while diff > 0:
        longer = longer.next
        diff -= 1

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
    return longer

def get_list_length(head):
    if head is None:
        return None, 0
    length = 0
    while head.next:
        length += 1
        head = head.next
    return head, length