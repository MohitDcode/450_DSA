'''
LC 104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
'''

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.data = key

def maxDepth(root) -> int:
    if not root:
        return 0
    leftSubtree = maxDepth(root.left)
    RightSubtree = maxDepth(root.right)
    return max(leftSubtree, RightSubtree) + 1

# Driver Program to test above function
if __name__ == '__main__':
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.left.left = Node(None)
    root.left.right = Node(None)
    root.left.left = Node(15)
    root.left.right = Node(7)
    print(maxDepth(root))
