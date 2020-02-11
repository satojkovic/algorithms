class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

def deep_copy_linked_list(head):
    def _deep_copy_linked_list(head, visited={}):
        if head is None:
            return visited, None
        if head in visited:
            return visited, visited[head]
        node = Node(head.val, None, None)
        visited[head] = node
        visited, node.next = _deep_copy_linked_list(head.next, visited)
        visited, node.random = _deep_copy_linked_list(head.random, visited)
        return visited, node
    visited, cloned_head = _deep_copy_linked_list(head)
    return cloned_head