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
    public:
        static const int SUCCESS = 0;
        static const int ERR_EMPTY = 1;
        static const int ERR_NOT_FOUND = 2;

    private:
        ListElement* head;
        ListElement* tail;
        int size;

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

        int removeAtHead(int& removed) {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            removed = head->data;
            head = head->next_elem;
            size--;

            if (isEmpty()) {
                tail = nullptr;
            }
            return SUCCESS;
        }

        int removeAtTail(int& removed) {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            ListElement* ptr = head;
            while (ptr->next_elem->data != tail->data) {
                ptr = ptr->next_elem;
            }
            removed = tail->data;
            ptr->next_elem = tail->next_elem;
            delete(tail);
            tail = ptr;
            size--;
            return SUCCESS;
        }

        int remove(int target) {
            if (isEmpty()) {
                return ERR_EMPTY;
            }

            int removed;
            if (target == head->data) {
                return removeAtHead(removed);
            }
            if (target == tail->data) {
                return removeAtTail(removed);
            }

            ListElement* ptr = head;
            while (ptr->next_elem != nullptr) {
                if (target == ptr->next_elem->data) {
                    ListElement* tmp = ptr->next_elem;
                    ptr->next_elem = ptr->next_elem->next_elem;
                    delete(tmp);
                    size--;
                    return SUCCESS;
                }
                ptr = ptr->next_elem;
            }
            return ERR_NOT_FOUND;
        }

        int peekFirst(int& value) {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            value = head->data;
            return SUCCESS;
        }

        int peekLast(int& value) {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            value = tail->data;
            return SUCCESS;
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
};

int main(int argc, char* argv[]) {
    LinkedList l;
    for (int i = 0; i < 10; i++) {
        l.insertAtTail(i);
    }
    l.printList();
    int value = 0;
    int ret = l.peekFirst(value);
    if (ret == LinkedList::SUCCESS) {
        printf("peekFirst: %d\n", value);
    } else if (ret == LinkedList::ERR_EMPTY) {
        printf("List is empty");
    }

    ret = l.peekLast(value);
    if (ret == LinkedList::SUCCESS) {
        printf("peekLast: %d\n", value);
    } else if (ret == LinkedList::ERR_EMPTY) {
        printf("List is empty");
    }

    int insert_value = 100;
    printf("insertAtHead: %d\n", insert_value);
    l.insertAtHead(insert_value);
    l.printList();

    int removed = 0;
    ret = l.removeAtHead(removed);
    if (ret == LinkedList::SUCCESS) {
        printf("removeAtHead: %d\n", removed);
        l.printList();
    } else if (ret == LinkedList::ERR_EMPTY) {
        printf("List is empty");
    }

    ret = l.removeAtTail(removed);
    if (ret == LinkedList::SUCCESS) {
        printf("removeAtTail: %d\n", removed);
        l.printList();
    } else if (ret == LinkedList::ERR_EMPTY) {
        printf("List is empty");
    }

    int target = 5;
    ret = l.remove(target);
    if (ret == LinkedList::SUCCESS) {
        printf("remove: %d\n", target);
        l.printList();
    } else if (ret == LinkedList::ERR_EMPTY) {
        printf("List is empty");
    } else if (ret == LinkedList::ERR_NOT_FOUND) {
        printf("Not found: %d\n", target);
    }

    target = 10;
    ret = l.remove(target);
    if (ret == LinkedList::SUCCESS) {
        printf("remove: %d\n", target);
        l.printList();
    } else if (ret == LinkedList::ERR_EMPTY) {
        printf("List is empty");
    } else if (ret == LinkedList::ERR_NOT_FOUND) {
        printf("Not found(remove): %d\n", target);
    }
}