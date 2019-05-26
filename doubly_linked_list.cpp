#include <iostream>

class DoublyListElement {
    public:
        int data;
        DoublyListElement* nextElement;
        DoublyListElement* prevElement;
        DoublyListElement() {
            nextElement = nullptr;
            prevElement = nullptr;
            data = 0;
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

        // O(n)
        void insertAtTail(int value) {
            if (isEmpty()) {
                head = new DoublyListElement(value);
            } else {
                DoublyListElement* trav = head;
                while (trav->nextElement != nullptr) {
                    trav = trav->nextElement;
                }
                DoublyListElement* node = new DoublyListElement(value);
                node->nextElement = trav->nextElement;
                node->prevElement = trav;
                trav->nextElement = node;
            }
            size++;
        }

        void printList() {
            if (isEmpty()) {
                std::cout << "List is empty." << std::endl;
                return;
            }

            DoublyListElement* node = head;
            std::cout << "List(size=" << size << ")" << std::endl;
            std::cout << "  fwd: ";
            while (node->nextElement != nullptr) {
                std::cout << node->data << "->";
                node = node->nextElement;
            }
            std::cout << node->data << "->null" << std::endl;

            std::cout << "  bwd: null->";
            while (node->prevElement != nullptr) {
                std::cout << node->data << "->";
                node = node->prevElement;
            }
            std::cout << node->data << std::endl;
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