'''
Level Order Traversal technique is defined as a method to traverse a Tree such that all 
nodes present in the same level are traversed completely before traversing the next level.
'''

# Find height of tree. Then for each level, run a recursive function by maintaining current height.
from createTree import *

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)

# Print nodes at a current level
def printCurrentLevel(root, level):
    if root is None:
        return None
    if level == 1:
        print(root.val, end=" ")
    elif level>1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

# Compute the height of a tree--the number of nodes
# along the longest path from the root node down to
# the farthest leaf node
def height(node):
    if node is None:
        return 0
    else:
        leftHeight = height(node.left)
        rightHeight = height(node.right)

    if leftHeight > rightHeight:
        return leftHeight+1
    else:
        return rightHeight+1
            

# Driver program to test above function
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
 
    print("Level order traversal of binary tree is -")
    printLevelOrder(root)