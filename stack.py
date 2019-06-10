class StackElem:
    def __init__(self, data):
        self.data = data
        self.next_elem = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return not self.top

    def pop(self):
        if self.is_empty():
            return None
        ret = self.top.data
        self.top = self.top.next_elem
        return ret

    def push(self, data):
        elem = StackElem(data)
        elem.next_elem = self.top
        self.top = elem

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def print_stack(self):
        if self.is_empty():
            print('Stack is empty.')
            return

        print('Current Stack:')
        elem = self.top
        while elem:
            print(elem.data)
            elem = elem.next_elem

if __name__ == "__main__":
    s = Stack()
    s.print_stack()

    print('push(3)')
    s.push(3)
    print('push(1)')
    s.push(1)
    print('push(100)')
    s.push(100)
    s.print_stack()

    print('pop():', s.pop())
    print('peek():', s.peek())
    print('pop():', s.pop())
    s.print_stack()