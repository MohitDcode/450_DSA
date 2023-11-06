def mergeInPlace(v, start, mid, end):
    total_len = len(v) #end - start + 1
    gap = total_len/2 + total_len%2

    while gap > 0:
        i = start
        j = start + gap
        while j <= end:
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
            i += 1
            j += 1
        if gap <= 1:
            gap = 0
        else:
            gap = gap/2 + gap%2


def mergeSort(v, start, end):
    if start >= end:
        return
    
    mid = (start + end) / 2
    mergeSort(v, start, mid)
    mergeSort(v, mid+1, end)
    mergeInPlace(v, start, mid, end)


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print('Given array is:')
    printList(arr)
    mergeSort(arr, 0, len(arr)-1)
    print('\n\nSorted array is:')
    printList(arr)