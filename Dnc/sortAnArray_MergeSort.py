def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # Dividing the array elemens in two halves
        L = arr[:mid]
        R = arr[mid:]

        # Sort both parts of the array
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L and R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Check if any element was left out
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print

if __name__ == '__main__':
    arr = [12, 11, 13, 5,6,7]
    print('Given array is:')
    printList(arr)
    mergeSort(arr)
    print('\n\nSorted array is:')
    printList(arr)