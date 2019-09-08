class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kth_smallest1(root, k):
    tree_nodes = []
    traverse(root, tree_nodes)
    return tree_nodes[k-1]

def kth_smallest2(root, k):
    tree_nodes = []
    traverse(root, tree_nodes)
    min_heap = build_min_heap(tree_nodes)
    for _ in range(k):
        min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
        ret = min_heap.pop()
        min_heap = heapify(min_heap, 0)
    return ret

def kth_smallest3(root, k):
    import heapq
    tree_nodes = []
    traverse(root, tree_nodes)
    heapq.heapify(tree_nodes)
    return heapq.nsmallest(k, tree_nodes)[-1]

def traverse(root, tree_nodes):
    if root is None:
        return
    traverse(root.left, tree_nodes)
    tree_nodes.append(root.val)
    traverse(root.right, tree_nodes)

def build_min_heap(data):
    last_pidx = len(data) // 2 - 1 if len(data) % 2 == 0 else len(data) // 2
    for p in reversed(range(0, last_pidx)):
        min_heap = heapify(data, p)
    return min_heap

def heapify(data, p):
    left_idx = 2 * p + 1
    right_idx = 2 * p + 2
    smallest = p
    if left_idx < len(data) and data[smallest] > data[left_idx]:
        smallest = left_idx
    if right_idx < len(data) and data[smallest] > data[right_idx]:
        smallest = right_idx

    if smallest != p:
        data[smallest], data[p] = data[p], data[smallest]
        data = heapify(data, smallest)
    return data