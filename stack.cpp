#include <iostream>

using namespace std;

class Stack
{
    public:
        static const int SUCCESS = 0;
        static const int ERR_STACK_EMPTY = 1;

    private:
        int* arr;
        int capacity;
        int numElements;
        int top;

    public:
        Stack(int size);
        bool isEmpty();
        int peek(int& value);
        int getSize();
};

Stack::Stack(int size) {
    capacity = size;
    arr = new int[size];
    numElements = 0;
}

bool Stack::isEmpty() {
    if (numElements == 0) {
        return true;
    } else {
        return false;
    }
}

int Stack::peek(int& value) {
    if (numElements == 0) {
        cout << "Stack is empty." << endl;
        return -1;
    } else {
        value = top;
        return SUCCESS;
    }
}

int Stack::getSize() {
    return numElements;
}

int main() {
    Stack s(10);
    int top_value = 0;
    int ret = s.peek(top_value);
    if (ret == Stack::SUCCESS) {
        cout << "top() : " << top_value << endl;
    }

    cout << "getSize() : " << s.getSize() << endl;

    return 0;
}