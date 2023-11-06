# String Case
def lastOccurance(arr, n, target):
    # base case
    if n == 0:
        return -1
    
    # recursive relation
    ans = lastOccurance(arr[1:],n-1,target)

    # processing
    if ans !=- 1:
        return ans+1
    else:
        if arr[0] == target:
            return 0
        else:
            return -1

arr = 'abcddefdg'
target = 'd'
print(lastOccurance(arr, len(arr), target))


# Array Case
def lastIndexOfNumberInArray(a,n,x):
    if n == 0: # Base case
        return -1
    ans=lastIndexOfNumberInArray(a[1:],n-1,x) #recursive call
# smaLl work
    if ans !=- 1:
        return ans+1
    else:
        if a[0] == x:
            return 0
        else:
            return -1
a=[9,8,10,8] # 3
x=8
print(lastIndexOfNumberInArray(a, len(a),x))