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
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return -1
        # Pop last: O(1)
        return self.stack.pop(-1)

if __name__ == "__main__":
    stack = StackByList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())