def isSorted(arr):
    # Base case: An empty or single-element array
    #            is always sorted.
    if len(arr) <= 1:
        return True

    # For an array to be sorted, the next element must be <=
    # than the previous element.
    elif arr[1] > arr[0]:
        return False

    # Tail recursion for the remaining elements
    return isSorted(arr[1:])

def printIsSorted(arr):
    if isSorted(arr):
        print("yes")
    else:
        print("no")

printIsSorted([1, 9, 9, 4, 5]) # prints no
printIsSorted([7, 5, 3, 2, 1]) # prints yes

