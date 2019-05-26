#include <iostream>

class DoublyListElement {
    public:
        int data;
        DoublyListElement* nextElement;
        DoublyListElement* prevElement;
        DoublyListElement() {
            nextElement = nullptr;
            prevElement = nullptr;
        }
        DoublyListElement(int value) {
            nextElement = nullptr;
            prevElement = nullptr;
            data = value;
        }
};

class DoublyLinkedList {
    private:
        DoublyListElement* head;
        int size;
    public:
        DoublyLinkedList() {
            head = nullptr;
            size = 0;
        }

        bool isEmpty() {
            return head == nullptr;
        }

        // Same implementation of LinkedList class(Singly)
        void insertAtTail(int value) {
            if (isEmpty()) {
                head = new DoublyListElement(value);
            } else {
                DoublyListElement* node = head;
                while (node->nextElement != nullptr) {
                    node = node->nextElement;
                }
                node->nextElement = new DoublyListElement(value);
            }
            size++;
        }

        void printList() {
            if (isEmpty()) {
                std::cout << "List is empty." << std::endl;
                return;
            }
            
            DoublyListElement* node = head;
            std::cout << "List(size=" << size << "): ";
            while (node != nullptr) {
                std::cout << node->data << "->";
                node = node->nextElement;
            }
            std::cout << "null" << std::endl;
            return;
        }
};

int main() {
    DoublyLinkedList dl;
    for (int i = 0; i < 10; i++) {
        dl.insertAtTail(i);
    }
    dl.printList();
}