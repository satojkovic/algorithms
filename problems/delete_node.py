def delete_node(node):
    if node.next is None:
        node = None
    else:
        trav1 = node
        trav2 = node.next
        while trav2 is not None:
            trav1.data = trav2.data
            if trav2.next is not None:
                trav1 = trav2
            else:
                trav1.next = None
            trav2 = trav2.next

def delete_node2(node):
    node.data = node.next.data
    node.next = node.next.next
