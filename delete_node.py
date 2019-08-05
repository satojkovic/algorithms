from linked_list import ListElement

def delete_node(node):
    if node.next_elem is None:
        node = None
    else:
        trav1 = node
        trav2 = node.next_elem
        while trav2 is not None:
            trav1.data = trav2.data
            if trav2.next_elem is not None:
                trav1 = trav2
            else:
                trav1.next_elem = None
            trav2 = trav2.next_elem
