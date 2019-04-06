#include <iostream>

class ListElement {
    public:
        int data;
        ListElement* next_elem;
        ListElement() {
            next_elem = nullptr;
        }
        ListElement(int value) {
            data = value;
            next_elem = nullptr;
        }
};

class LinkedList {
    private:
        ListElement* head;
        ListElement* tail;
        int size;

        static const int ERR_EMPTY = 0;
        static const int SUCCESS = 1;
    public:
        LinkedList() {
            head = nullptr;
            tail = nullptr;
            size = 0;
        }

        bool isEmpty() {
            // check whether head is nullptr
            if (head == nullptr) {
                return true;
            } else {
                return false;
            }
        }

        void insertAtHead(int value) {
            if (isEmpty()) {
                head = tail = new ListElement(value);
            } else {
                ListElement *node = new ListElement(value);
                node->next_elem = head;
                head = node;
            }
            size++;
        }

        void insertAtTail(int value) {
            if (isEmpty()) {
                head = tail = new ListElement(value);
            } else {
                tail->next_elem = new ListElement(value);
                tail = tail->next_elem;
            }
            size++;
        }

        void printList() {
            if (isEmpty()) {
                std::cout << "List is empty." << std::endl;
                return;
            }

            ListElement* temp = head;
            std::cout << "List(size=" << size << "): ";
            while (temp != nullptr) {
                std::cout << temp->data << "->";
                temp = temp->next_elem;
            }
            std::cout << "null " << std::endl;
            return;
        }

        int peekFirst() {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            return head->data;
        }

        int peekLast() {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            return tail->data;
        }
};

int main(int argc, char* argv[]) {
    LinkedList l;
    for (int i = 0; i < 10; i++) {
        l.insertAtTail(i);
    }
    l.printList();
    printf("peekFirst: %d\n", l.peekFirst());
    printf("peekLast: %d\n", l.peekLast());

    l.insertAtHead(100);
    l.printList();
}