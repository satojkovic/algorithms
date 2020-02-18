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
