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
