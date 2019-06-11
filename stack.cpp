#include <iostream>

using namespace std;

class StackElem {
    public:
        int data;
        StackElem* next_elem;

        StackElem() {
            next_elem = nullptr;
        }

        StackElem(int value) {
            data = value;
            next_elem = nullptr;
        }
};

class Stack
{
    static const int SUCCESS = 0;
    static const int ERR_EMPTY = 1;

    private:
        StackElem* top;

    public:
        Stack() {top = nullptr;}
        bool isEmpty() {
            return top == nullptr;
        }

        int pop() {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            int ret = top->data;
            top = top->next_elem;
            return ret;
        }

        void push(int data) {
            StackElem* elem = new StackElem(data);
            elem->next_elem = top;
            top = elem;
        }

        int peek() {
            if (isEmpty()) {
                return ERR_EMPTY;
            }
            return top->data;
        }

        void printStack() {
            if (isEmpty()) {
                printf("Stack is empty.\n");
                return;
            }

            printf("Current Stack:\n");
            StackElem* elem = top;
            while (elem != nullptr) {
                printf("%d\n", elem->data);
                elem = elem->next_elem;
            }
        }
};

int main() {
    Stack* s = new Stack();
    s->printStack();

    printf("push(3)\n");
    s->push(3);
    printf("push(1)\n");
    s->push(1);
    printf("push(100)\n");
    s->push(100);
    s->printStack();

    return 0;
}