class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def printLeftBoundary(root):
    while root:
        if root.left or root.right:
            print(root.val, end=" ")
        if root.left:
            root = root.left
        else:
            root = root.right

def printRightBoundary(root):
    if not root:
        return
    curr = root.right
    while curr:
        if curr.left or curr.right:
            print(curr.val, end=" ")
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left

def printLeaves(root):
    if not root:
        return
    printLeaves(root.left)
    if not root.left and not root.right:
        print(root.val, end=" ")
    printLeaves(root.right)
def boundaryTraversal(root):
    if not root:
        return
    print(root.val, end=" ")
    printLeftBoundary(root.left)
    printLeaves(root.left)
    printLeaves(root.right)
    printRightBoundary(root)
 
# Driver program to test above function
if __name__ == '__main__':
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)
    root.right = TreeNode(22)
    root.right.right = TreeNode(25)

    boundaryTraversal(root)