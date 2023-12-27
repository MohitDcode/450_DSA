'''
LC 112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if 
the tree has a root-to-leaf path such that adding up all the values along 
the path equals targetSum.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        leftSum = self.hasPathSum(root.left, targetSum-root.val)
        rightSum = self.hasPathSum(root.right, targetSum-root.val)

        return leftSum or rightSum
    
# Driver Code
if __name__ == '__main__':
    # Constructing the Binary Tree
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(9)
    print("Has path with sum", 22, "? ", end="")
    print(Solution().hasPathSum(root, 22))


