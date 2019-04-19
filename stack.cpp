#include <iostream>

using namespace std;

class Stack
{
    private:
        int* arr;
        int capacity;
        int numElements;
        int top;

    public:
        Stack(int size);
        bool isEmpty();
        int peek();
        int getSize();
        bool push(int value);
        int pop();
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

int Stack::peek() {
    if (numElements == 0) {
        std::cout << "Stack is empty." << endl;
        exit(EXIT_FAILURE);
    } else {
        return top;
    }
}

int Stack::getSize() {
    return numElements;
}

bool Stack::push(int value) {
    if (numElements < capacity) {
        arr[numElements] = value;
        numElements++;
        top = value;
        return true;
    } else {
        std::cout << "Stack is full" << endl;
        return false;
    }
}

int Stack::pop() {
    if(numElements == 0) {
        std::cout << "Stack is empty" << endl;
        exit(EXIT_FAILURE);
    } else {
        numElements--;
        top = arr[numElements - 1];
        return arr[numElements];
    }
}


int main() {
    Stack s(10);
    s.push(5);
    s.push(10);
    s.push(15);
    std::cout << "getSize() : " << s.getSize() << endl;
    std::cout << "top : " << s.peek() << endl;
    std::cout << "pop : " << s.pop() << endl;
    std::cout << "pop : " << s.pop() << endl;
    std::cout << "pop : " << s.pop() << endl;
    std::cout << "getSize() : " << s.getSize() << endl;

    return 0;
}