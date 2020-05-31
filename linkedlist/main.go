package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

type SinglyLinkedList struct {
	head *Node
	size int
}

func (l *SinglyLinkedList) IsEmpty() bool {
	return l.size == 0
}

func (l *SinglyLinkedList) AddHead(value int) {
	node := Node{value: value}
	node.next = l.head
	l.head = &node
	l.size += 1
}

func (l *SinglyLinkedList) PeekHead() (int, bool) {
	if l.IsEmpty() {
		return -1, false
	}
	return l.head.value, true
}

func (l *SinglyLinkedList) RemoveHead() (int, bool) {
	if l.IsEmpty() {
		return -1, false
	}
	value := l.head.value
	l.head = l.head.next
	l.size -= 1
	return value, true
}

func main() {
	sll := SinglyLinkedList{nil, 0}
	fmt.Println(sll.IsEmpty())
	sll.AddHead(10)
	fmt.Println(sll.head.value)
	sll.AddHead(20)
	fmt.Println(sll.head.value)
	sll.RemoveHead()
	fmt.Println(sll.head.value)
	fmt.Println(sll.size)
	fmt.Println(sll.IsEmpty())
}
