def maxNumber(arr, n=0):
	# base case
	if n == len(arr):
		exit()
		
    # processing
	maxNo = 0
	for n in range(len(arr)):
		maxNo = max(maxNo, arr[n])
	
	# calling function recursively
	maxNumber(arr, n+1)
	print(maxNo) 
	
arr = [10, 21, 4, 45, 66, 93]
maxNumber(arr)