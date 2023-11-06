def quickSort(arr, start, end):
    # base case
    if start >= end:
        return

    # processing
    pivot = end
    i = start - 1
    j = start

    while j < pivot:
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]

    # left partition
    quickSort(arr, start, i-1)

    # right partition
    quickSort(arr, i+1, end)

# driver code
if __name__ == "__main__":
    arr = [7,2,1,8,6,3,5,4]
    n = len(arr)
    quickSort(arr, 0, n-1)
    print(arr)