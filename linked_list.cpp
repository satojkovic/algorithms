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
    public:
        LinkedList() {
            head = nullptr;
            tail = nullptr;
        }

        bool isEmpty() {
            // check whether head is nullptr
            if (head == nullptr) {
                return true;
            } else {
                return false;
            }
        }

        void insertAtTail(int value) {
            if (isEmpty()) {
                head = tail = new ListElement(value);
            } else {
                tail->next_elem = new ListElement(value);
                tail = tail->next_elem;
            }
        }

        void printList() {
            if (isEmpty()) {
                std::cout << "List is empty." << std::endl;
                return;
            }

            ListElement* temp = head;
            std::cout << "List: ";
            while (temp != nullptr) {
                std::cout << temp->data << "->";
                temp = temp->next_elem;
            }
            std::cout << "null " << std::endl;
            return;
        }
};

int main(int argc, char* argv[]) {
    LinkedList l;
    for (int i = 0; i < 10; i++) {
        l.insertAtTail(i);
    }
    l.printList();
}