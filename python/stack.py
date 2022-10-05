class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack implemented by linked list


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return not self.top

    def pop(self):
        if self.is_empty():
            return None
        ret = self.top.data
        self.top = self.top.next
        return ret

    def push(self, data):
        node = ListNode(data)
        node.next = self.top
        self.top = node

    def peek(self):
        return self.top.data if not self.is_empty() else None

    def print_stack(self):
        if self.is_empty():
            print('Stack is empty.')
            return

        print('Current Stack:')
        node = self.top
        while node:
            print(node.data)
            node = node.next


class StackByList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.s = [0 for _ in range(self.capacity)]

    def is_empty(self):
        return self.top == 0

    def is_full(self):
        return self.top == self.capacity

    def push(self, data):
        if self.is_full():
            return None
        self.s[self.top] = data
        self.top += 1

    def pop(self):
        if self.is_empty():
            return None
        ret = self.s[self.top - 1]
        self.top -= 1
        return ret

    def size(self):
        return self.top

    def peek(self):
        return self.s[self.top - 1] if not self.is_empty() else None


def test_stack_by_list():
    sl = StackByList(6)
    sl.push(4)
    sl.push(1)
    sl.push(3)
    sl.pop()
    sl.push(8)
    sl.pop()
    assert sl.size() == 2
    assert sl.peek() == 1

    sl.pop()
    sl.pop()
    assert sl.size() == 0
    assert sl.is_empty() is True
    assert sl.pop() is None

    [sl.push(i*10) for i in range(6)]
    assert sl.size() == 6
    assert sl.is_full() is True
    assert sl.push(100) is None
