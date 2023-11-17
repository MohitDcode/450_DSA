# Implementation using LIFO Queue

from queue import LifoQueue
stack = LifoQueue(maxsize=3)

print('Initial Size:',stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')

print('Full:', stack.full())
print('Size:', stack.qsize())

print('Elements popped from Queue: ')
print(stack.get())
print(stack.get())
print(stack.get())

print('\nEmpty Stack:', stack.empty())