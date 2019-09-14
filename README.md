# algorithms

Algorithms implemented in Python.

## Linked Lists

* A linked list is a data structure that represents a sequence of nodes.
* Time Complexity

| operations      | Singly linked list | Doubly linked list | Array |
| :-------------: | :----------------: | :----------------: | ----- |
| Search          | O(n)               | O(n)               | O(1)  |
| Add(at head)    | O(1)               | O(1)               | O(n)  |
| Remove(at head) | O(1)               | O(1)               | O(n)  |

## Stack

* A stack is a one-ended linear data structure which have two primary operations, namely push and pop.
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