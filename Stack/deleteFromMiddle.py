class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def delete_middle(self):
        if not self.is_empty():
            self.stack.pop(len(self.stack) // 2)

# Usage:

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.stack)
s.delete_middle()
print(s.stack)