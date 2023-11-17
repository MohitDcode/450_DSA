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

    def insert_at_middle(self, value):
        middle_index = len(self.stack) // 2
        self.stack.insert(middle_index, value)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print('Original Stack:', stack.stack)
stack.insert_at_middle(666)

print('Element at the middle:', stack.stack) # Output: [1, 2, 666, 3, 4, 5]