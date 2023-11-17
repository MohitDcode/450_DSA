from Stack import Stack

# Reverse string s
def reverse(s):
	my_stack = Stack()
	# For each character in string s
	for c in s:
		my_stack.push(c)
	result = ""
	while not my_stack.is_empty():
		result += my_stack.pop()
	return result