# String Case
def lastOccurance(arr, target, index):
    # base case
    if index >= len(arr):
        return -1

    # processing
    for i in range(len(arr), 1):
        if arr[i] == target:
            index = i
    
    # recursive relation
    ans = lastOccurance(arr, target, index+1)
    if ans != -1:
        return ans
    else:
        return index-1


arr = 'abcddefdg'
target = 'd'
print(lastOccurance(arr, target, len(arr)-1))