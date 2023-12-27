'''
LC 113. Path Sum II
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths 
where the sum of the node values in the path equals targetSum.
'''

# Solution using Depth-First Search(DFS)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):
        def dfs(node, arr):
            if not node:
                return None
            arr.append(node.val)

            if not node.left and not node.right and sum(arr) == targetSum:
                ans.append(arr[::])
                        
            dfs(node.left, arr)
            dfs(node.right, arr)
            arr.pop()

        ans = []
        dfs(root, [])
        return ans
    
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
    print(Solution().pathSum(root, 22))


