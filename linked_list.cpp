#include <iostream>

class ListElement {
    private:
        int data;
        ListElement* next_elem;
    public:
        ListElement() {
            next_elem = nullptr;
        }
};

class LinkedList {
    private:
        ListElement* head;
    public:
        LinkedList() {
            head = nullptr;
        }

        bool isEmpty() {
            // check whether head is nullptr
            if (head == nullptr) {
                return true;
            } else {
                return false;
            }
        }
};

int main(int argc, char* argv[]) {
    LinkedList l;
}