'''
LC 543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in 
a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.
'''

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def diameterOfBinaryTree(root) -> int:
    def height(root):
        nonlocal diameter
        if not root:
            return 0
        
        left = height(root.left)
        right = height(root.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1
    
    diameter = 0
    height(root)
    return diameter

# Driver Program to test above function
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.left.left = Node(None)
    root.left.right = Node(None)
    root.left.left = Node(15)
    root.left.right = Node(7)
    print(diameterOfBinaryTree(root))
