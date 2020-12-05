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
        // Having a tail pointer, insertAtTail and delteAtTail are just as fast as insertAtHead and deleteAtHead.
        //DoublyListElement* tail;
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

        void insertAtHead(int value) {
            if (isEmpty()) {
                head = new DoublyListElement(value);
            } else {
                DoublyListElement* node = new DoublyListElement(value);
                node->prevElement = nullptr;
                node->nextElement = head;
                head->prevElement = node;
                head = node;
            }
            size++;
        }

        bool deleteAtHead() {
            if (isEmpty()) {
                return false;
            }
            head = head->nextElement;
            head->prevElement = nullptr;
            size--;
            return true;
        }

        bool deleteAtTail() {
            if (isEmpty()) {
                return false;
            }
            DoublyListElement* node = head;
            while (node->nextElement != nullptr) {
                node = node->nextElement;
            }
            node->prevElement->nextElement = nullptr;
            delete node;
            size--;
            return true;
        }

        bool deleteNode(int value) {
            if (isEmpty()) {
                return false;
            }

            if (head->data == value) {
                return deleteAtHead();
            }

            DoublyListElement* node = head;
            while (node != nullptr) {
                if (node->data == value) {
                    node->prevElement->nextElement = node->nextElement;
                    if (node->nextElement != nullptr) {
                        node->nextElement->prevElement = node->prevElement;
                    }
                    size--;
                    delete node;
                    return true;
                }
                node = node->nextElement;
            }
            return false;
        }

        int length() {
            // return size;
            int length = 0;
            DoublyListElement* node = head;
            while (node != nullptr) {
                length++;
                node = node->nextElement;
            }
            return length;
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

    int insert_value = 100;
    printf("insertAtHead: %d\n", insert_value);
    dl.insertAtHead(insert_value);
    dl.printList();

    if (dl.deleteAtHead()) {
        printf("deleteAtHead\n");
        dl.printList();
    } else {
        printf("List is empty");
    }

    if (dl.deleteAtTail()) {
        printf("deleteAtTail\n");
        dl.printList();
    } else {
        printf("List is empty");
    }

    int target = 5;
    if (dl.deleteNode(target)) {
        printf("deleteNode: %d\n", target);
        dl.printList();
    } else {
        printf("Not found: %d\n", target);
    }

    target = 8;
    if (dl.deleteNode(target)) {
        printf("deleteNode: %d\n", target);
        dl.printList();
    } else {
        printf("Not found: %d\n", target);
    }

    target = 100;
    if (dl.deleteNode(target)) {
        printf("deleteNode: %d\n", target);
        dl.printList();
    } else {
        printf("deleteNode: target %d not found\n", target);
    }
}