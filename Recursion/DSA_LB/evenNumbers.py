# even_nos  = [num for num in arr if num % 2 == 0]
def evennumbers(list, n=0):
	# base case
	if n == len(list):
		exit()
		
    # processing
	if list[n] % 2 == 0:
		print(list[n], end=" ")
	
	# calling function recursively
	evennumbers(list, n+1)

# Initializing list 
list1 = [10, 21, 4, 45, 66, 93]

print("Even numbers in the list:", end=" ")
evennumbers(list1)