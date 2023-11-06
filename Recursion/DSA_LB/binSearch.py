def binSearch(arr, s, e, target):
    # base case
    if s > e:
        return 'not found'
    
    # processing
    mid = s + (e-s)//2
    if arr[mid] == target:
        return mid
    
    # rr
    if arr[mid] < target: # moving right
        s = mid + 1
        return binSearch(arr, s, e, target)
    
    else: # moving left
        e = mid - 1
        return binSearch(arr, s, e, target)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80]
    s = 0
    e = len(arr)-1
    target = 80

    print('array search status:', binSearch(arr, s, e, target))