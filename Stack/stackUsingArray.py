class Stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.stack = [None] * size

    def is_full(self):
        return self.top == self.size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, value):
        if self.is_full():
            print("Stack is full")
            return
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        return self.stack[self.top]

    def print_stack(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i], end=' ')
        print()

# Example usage
s = Stack(5)
s.push(1)
s.push(2)
s.push(3)
s.print_stack()
print("Peek:", s.peek())
s.pop()
s.print_stack()