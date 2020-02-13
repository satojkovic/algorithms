# Algorithms and Data structures

Algorithms and Data structures implemented in Python.

## Linked Lists

* A linked list is a data structure that represents a sequence of nodes.
* In a singly linked list, each node has a pointer to the next node in the list, whereas a doubly linked list gives each node pointers to both the next and previous node.
* Time Complexity

| operations      | Singly linked list | Doubly linked list | Array |
| :-------------: | :----------------: | :----------------: | ----- |
| Search          | O(n)               | O(n)               | O(1)  |
| Add(at head)    | O(1)               | O(1)               | O(n)  |
| Remove(at head) | O(1)               | O(1)               | O(n)  |

* As indicated in the above table, you can add or remove nodes from the head of the list in constant time, but a linked list does not provide constant time access to arbitrary node within the list.
* A linked list can be used to implement stack and queue.

## Stack

* A stack is a one-ended linear data structure which have two primary operations, namely push and pop.
* The most recent item is added to the stack is removed first. (i.e. LIFO(last-in-first-out))
* Unlike an array, a stack does not offer constant-time access to the i-th item. It does allow constant time adds and removes, as it doesn't require shifting elements around.
* Time complexity

| operations | time complexity |
| :--------: | :-------------: |
| pushing    | O(1)            |
| popping    | O(1)            |
| peeking    | O(1)            |
| searching  | O(n)            |

## Queue

* A queue is just a linear data structure.
* There are two primary operations, which are enqueuing and dequeuing.
* Items are removed from a queue in the same order that they are added. (i.e. FIFO(first-in-first-out))
* Enqueuing(adds) and dequeuing(removes) are constant time operations. There is also another constant time operation, peeking. Peeking means that we are looking at the value at the front of the queue without removing it.
* But checking if the element is contained within a queue is linear time because we would potentially need to scan through all of the elements.
* Removing the element from the queue also requires linear time.
* Time complexity

| operations | time complexity |
| :--------: | :-------------: |
| enqueuing  | O(1)            |
| dequeuing  | O(1)            |
| peeking    | O(1)            |
| searching  | O(n)            |
| removing   | O(n)            |

## Binary Heaps

* A heap is a tree-based data structure which satisfies the heap property.
* In min-heap, each node is smaller than its children, and the root, therefore, is the minimum element in the tree.
* Conversely in max-heap, each node is greater than its children, and the root is the maximum element in the tree.
* Build a heap
  * To build a heap, we apply 'heapify' to all nodes except the leaf nodes, so as to maintain the heap property.
  * 'heapify' is the process that swap a node with its left or right child if a node and its children don't satify with the heap priority. If the heap priority is satisfied, do nothing.
  * In min-heap, if the left(right) child is smallest, then the left(right) child is swapped with its parent.
  * In max-heap, if the left(right) child is largest, then the left(right) child is swapped with its parent.
  * Time complexity
    * 'heapify': O(h) at worst case, where h is the height of the tree.
    * Therefore, building heap takes O(2<sup>0</sup> * h + 2<sup>1</sup> * (h-1) + ... + 2<sup>h-1</sup> * 1) = O(2<sup>h</sup>) time, which is the sum of the 'heapify' for all internal node.
    * We need to know the height of the tree h.
      * 2<sup>0</sup> + 2<sup>1</sup> + ... + 2<sup>h-1</sup> + 2<sup>h</sup> = n
      * 1 + 2 * (2<sup>h</sup> - 1) = n
      * 2<sup>h+1</sup> = n + 1
      * h + 1 = log(n + 1)
      * h = log(n + 1) - 1
    * Therefore, time complexity is O(n) at worst case, 'heapify' takes O(log(n)) time.
    
## Binary Trees

* Trees are hierarchical data structures.
* A tree whose elements have at most 2 children is called a binary tree, where each node contains a left and a right node.
* The topmost node is called root of the tree.
* The nodes that are directory under a node are called its children. Conversely, the node that is directory above a node is called its parent.
* The nodes with no children are called leaves.
* Other tree terminologies
    * The depth of a node is the number of edges from the root to the node.
    * The height of a node is the number of edges from the node to the deepest leaf node.

* Trie
* Graphs
* Sort