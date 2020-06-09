package linkedlist

import "testing"

func TestSinglyLinkedList_IsEmpty(t *testing.T) {
	sll := SinglyLinkedList{nil, 0}
	if !sll.IsEmpty() {
		t.Error("Not an empty")
	}
}
