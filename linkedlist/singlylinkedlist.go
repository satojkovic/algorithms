package linkedlist

type Node struct {
	value int
	next  *Node
}

type SinglyLinkedList struct {
	head *Node
	size int
}

func (l *SinglyLinkedList) AddHead(value int) {
	node := Node{value: value}
	node.next = l.head
	l.head = &node
	l.size += 1
}
