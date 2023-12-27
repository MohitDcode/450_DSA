class TreeNode():
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None
class Solution():
    def buildTreeHelper(self, preOrder, left, right):
        if left > right:
            return None
        rootValue = preOrder[self.preOrderIndex]
        self.preOrderIndex += 1
        root = TreeNode(rootValue)
        inOrderPivotIndex = self.inOrderIndexMap[rootValue]

        root.left = self.buildTreeHelper(preOrder, left, inOrderPivotIndex-1)
        root.right = self.buildTreeHelper(preOrder, inOrderPivotIndex+1, right)
        return root

    def buildTree(self, preOrder, inOrder):
        self.preOrderIndex = 0
        self.inOrderIndexMap = {val:idx for idx, val in enumerate(inOrder)}
        return self.buildTreeHelper(preOrder, 0, len(preOrder)-1)

# driver code    
t = Solution()
preOrder = [3,9,20,15,7]
inOrder = [9,3,15,20,7]

t.root = t.buildTree(preOrder, inOrder)
print("Inorder traversal of the constructed tree is : ")
print(t.root)