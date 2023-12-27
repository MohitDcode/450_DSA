from createTree import *

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def leftViewUtil(root, level, maxLevel):
    if root is None:
        return
    # If this is the first node of its level
    if(maxLevel[0] < level):
        print(root.val, end=" ")
        maxLevel[0] = level
    
    # Recur for left and right subtree
    leftViewUtil(root.left, level+1, maxLevel)
    leftViewUtil(root.right, level+1, maxLevel)
        
def leftView(root):
    maxLevel = [0]
    leftViewUtil(root, 1, maxLevel)

def rightViewUtil(root, level, maxLevel):
    if root is None:
        return
    # If this is the first node of its level
    if(maxLevel[0] < level):
        print(root.val, end=" ")
        maxLevel[0] = level
    
    # Recur for left and right subtree
    rightViewUtil(root.right, level+1, maxLevel)
    rightViewUtil(root.left, level+1, maxLevel)
        
def rightView(root):
    maxLevel = [0]
    rightViewUtil(root, 1, maxLevel)

# Driver program to test above function
if __name__ == '__main__':
    arr = [10,20,40,None,None,50,70,110,None,None,111,None,None,80,None,None,30,None,60,None,90,112,None,None,113,None,None]
    root = to_binary_tree(arr)
    print('Left View:')
    leftView(root)
    print('\nRight View:')
    rightView(root)