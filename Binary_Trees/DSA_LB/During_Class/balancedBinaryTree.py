'''
LC 110. Balanced Binary Tree
A height-balanced binary tree is a binary tree in which the depth of the 
two subtrees of every node never differs by more than one.'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        return self.height(root) >= 0

    def height(self, root):
        if root is None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
            return -1
        
        return max(leftHeight, rightHeight) + 1

# Driver Code
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
print("Is balanced?",Solution().isBalanced(tree)) # True</s>


