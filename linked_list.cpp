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

        int length() {
            // return size;
            int length = 0;
            ListElement* node = head;
            while (node != nullptr) {
                length++;
                node = node->next_elem;
            }
            return length;
        }

        bool reverseList() {
            if (isEmpty()) {
                return false;
            }

            ListElement* prev = nullptr;
            ListElement* current = head;
            while (current != nullptr) {
                ListElement* next = current->next_elem;
                current->next_elem = prev;
                prev = current;
                current = next;
            }
            head = prev;
            return true;
        }

        bool reverseList_r() {
            if (isEmpty()) {
                return false;
            }
            head = reverseList_r_(head);
            return head != nullptr;
        }

        ListElement* reverseList_r_(ListElement* head) {
            if (head->next_elem == nullptr) return head;
            ListElement* node = reverseList_r_(head->next_elem);
            head->next_elem->next_elem = head;
            head->next_elem = nullptr;
            return node;
        }

        bool makeLoop() {
            if (isEmpty()) {
                return false;
            }
            ListElement* node = head;
            while (node->next_elem != nullptr) {
                node = node->next_elem;
            }
            node->next_elem = head;
            return true;
        }

        bool detectLoop() {
            if (isEmpty()) {
                return false;
            }

            ListElement* slow = head;
            ListElement* fast = head;
            // We iterate the list once, hence the runtime of this algorithm is O(n)
            while (slow && fast && fast->next_elem) {
                slow = slow->next_elem;
                fast = fast->next_elem->next_elem;
                if (fast == slow) {
                    return true;
                }
            }
            return false;
        }

        int findMiddle(int& mid_data) {
            if (isEmpty()) {
                mid_data = -1;
                return ERR_EMPTY;
            }

            if (head->next_elem == nullptr) {
                mid_data = head->data;
                return SUCCESS;
            }

            ListElement* fast = head;
            ListElement* slow = head;
            while (fast->next_elem != nullptr && fast->next_elem->next_elem != nullptr) {
                fast = fast->next_elem->next_elem;
                slow = slow->next_elem;
            }
            mid_data = slow->data;
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

    int mid_data = 0;
    if (l.findMiddle(mid_data) == LinkedList::SUCCESS) {
        printf("Middle data: %d\n", mid_data);
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

    if (l.reverseList()) {
        printf("reversed:\n");
        l.printList();
    }

    if (l.reverseList_r()) {
        printf("reversed:\n");
        l.printList();
    }

    if (l.findMiddle(mid_data) == LinkedList::SUCCESS) {
        printf("Middle data: %d\n", mid_data);
        l.printList();
    }

    if (l.makeLoop()) {
        printf("makeLoop\n");
        printf("detectLoop: %s\n", l.detectLoop() ? "true" : "false");
    }
}