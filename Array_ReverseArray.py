# Python program to reverse an array
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)

# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print("Original list is",A)
reverseList(A, 0, len(A)-1)
print("Reversed list is",A)
#ends here