class TreeNode():
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
class Solution():
    def buildTreeHelper(self, postOrder, left, right):
        if left > right:
            return None
        rootValue = postOrder[self.postOrderIndex]
        self.postOrderIndex -= 1
        root = TreeNode(rootValue)
        inOrderPivotIndex = self.inOrderIndexMap[rootValue]
        
        root.right = self.buildTreeHelper(postOrder, inOrderPivotIndex+1, right)
        root.left = self.buildTreeHelper(postOrder, left, inOrderPivotIndex-1)
        return root

    def buildTree(self, postOrder, inOrder):
        self.postOrderIndex = len(postOrder)-1
        self.inOrderIndexMap = {val:idx for idx, val in enumerate(inOrder)}
        return self.buildTreeHelper(postOrder, 0, len(postOrder)-1)

# driver code    
t = Solution()
preOrder = [3,9,20,15,7]
inOrder = [9,3,15,20,7]

t.root = t.buildTree(preOrder, inOrder)
print("Inorder traversal of the constructed tree is : ")
print(t.root)