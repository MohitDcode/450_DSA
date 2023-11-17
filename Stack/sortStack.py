def sort_stack(stack):
    if len(stack) == 0:
        return

    top = stack.pop()
    sort_stack(stack)

    sorted_insert(stack, top)

def sorted_insert(stack, element):
    if len(stack) == 0 or element > stack[-1]:
        stack.append(element)
    else:
        top = stack.pop()
        sorted_insert(stack, element)
        stack.append(top)

stack = [5, 15, 10, 30, 20]
print('Original Stack:', stack)
sort_stack(stack)
print("Sorted Stack:", stack)