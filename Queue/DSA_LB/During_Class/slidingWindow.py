# https://www.geeksforgeeks.org/first-negative-integer-every-window-size-k/

from collections import deque 
def printFirstNegative(arr, n, k):

	# Create an empty deque to store the indices of negative integers
	negIndices = deque()
	res = []

	# Traverse through the array
	for i in range(n):
		# If the deque is not empty and
		# the leftmost element is out of
		# the current window, then remove it from the deque
		if negIndices and negIndices[0] == i - k:
			negIndices.popleft()

		# If the current element is negative, add its index to the deque
		if arr[i] < 0:
			negIndices.append(i)

		# If the current window is of size k,
		# print the first negative integer (if present)
		if i >= k - 1:
			# If the deque is not empty,
			# the leftmost element is the first negative integer
			if negIndices:
				res.append(arr[negIndices[0]])
				# print(arr[negIndices[0]], end=" ")
			else:
				print("0", end=" ")
	return res
# Main
if __name__=='__main__': 
    arr = [2, -5, 4, -1, -2, 0, 5]
    size = len(arr)
    k = 3
    print('Result:',printFirstNegative(arr, size, k))
    # [-5, -5, -1, -1, -2]