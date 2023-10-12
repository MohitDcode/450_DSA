# Representation of a node 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Function to insert node 
def insert(root, item):
    temp = Node(0)
    temp.data = item
    temp.next = root
    root = temp
    return root

def arrayToList(arr, n): 
	root = None
	for i in range(n-1, -1, -1): 
		root = insert(root, arr[i]) 
	return root 

def display(root): 
	while (root != None) : 
		print(root.data, end = " ") 
		root = root.next
		
# Driver code 
if __name__=='__main__': 
	arr = [1, 2, 3, 4, 5] 
	n = len(arr) 
	root = arrayToList(arr, n) 
	display(root) 