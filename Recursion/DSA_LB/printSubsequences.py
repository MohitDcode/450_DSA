def printSubsequences(arr, index, subarr):
    
    # base case
    if index >= len(arr):
        # if len(subarr) != 0: #avoid empty subsequence
        print(subarr)

    # processing
    else: 
        # Subsequence without including  
        # the element at current index 
        printSubsequences(arr, index + 1, subarr) 
           
        # Subsequence including the element 
        # at current index 
        printSubsequences(arr, index + 1, subarr+[arr[index]]) 
    return

arr = 'abc'
printSubsequences(arr, 0, []) 