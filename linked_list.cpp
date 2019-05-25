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
        int size;

    public:
        LinkedList() {
            head = nullptr;
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
                head = new ListElement(value);
            } else {
                ListElement *node = new ListElement(value);
                node->next_elem = head;
                head = node;
            }
            size++;
        }

        void insertAtTail(int value) {
            if (isEmpty()) {
                head = new ListElement(value);
            } else {
                ListElement* node = head;
                while (node->next_elem != nullptr) {
                    node = node->next_elem;
                }
                node->next_elem = new ListElement(value);
            }
            size++;
        }

        int removeAtHead(int& removed) {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            ListElement* node = head;
            removed = node->data;
            head = node->next_elem;
            delete node;
            size--;
            return SUCCESS;
        }

        bool deleteAtHead(void) {
            if (isEmpty()) {
                return false;
            }
            ListElement* node = head;
            head = node->next_elem;
            delete node;
            size--;
            return true;
        }

        int removeAtTail(int& removed) {
            if (isEmpty()) {
                return ERR_EMPTY;
            }

            ListElement* trav1 = head;
            ListElement* trav2 = head->next_elem;
            if (trav2 == nullptr) {
                return removeAtHead(removed);
            }

            while (trav2->next_elem != nullptr) {
                trav1 = trav1->next_elem;
                trav2 = trav2->next_elem;
            }

            removed = trav2->data;
            trav1->next_elem = trav2->next_elem;
            delete(trav2);
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

            ListElement* trav1 = head;
            ListElement* trav2 = head->next_elem;
            while (trav2 != nullptr) {
                if (trav2->data == target) {
                    ListElement* tmp = trav2;
                    trav2 = trav2->next_elem;
                    trav1->next_elem = trav2;
                    delete(tmp);
                    size--;
                    return SUCCESS;
                }
                trav1 = trav1->next_elem;
                trav2 = trav2->next_elem;
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
            ListElement* node = head;
            while (node->next_elem != nullptr) {
                node = node->next_elem;
            }
            value = node->data;
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