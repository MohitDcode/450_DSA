# Implementing Stack using collections.deque(called deck)

from collections import deque as dq

stack  = dq()

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial Stack:')
print(stack)

# pop function
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after all elements popped:')
print(stack)