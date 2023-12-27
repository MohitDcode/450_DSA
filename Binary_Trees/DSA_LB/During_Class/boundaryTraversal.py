class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isLeaf(root):
    if root.left == None and root.right == None:
        return True
    else:
        return False
    
def addLeftBoundary(root, res):
    root = root.left
    while (root is not None):
        if isLeaf(root) is not True:
            res.append(root.val)
        if (root.left is not None):
            root = root.left
        else:
            root = root.right

def addRightBoundary(root, res):
    root = root.right
    # we need to traverse anticlockwise for this
    stk = []
    while (root is not None):
        if isLeaf(root) is not True:
            stk.append(root.val)
        if (root.right is not None):
            root = root.right
        else:
            root = root.left
    
    while(len(stk) != 0):
        res.append(stk.pop(-1))

def addLeaves(root, res):
    if root is None:
        return
    if (isLeaf(root) is True):
        res.append(root.val)
        return
    addLeaves(root.left, res)
    addLeaves(root.right, res)

def boundaryTraversal(root, res):
    if root is None:
        return
    if isLeaf(root) is not True:
        res.append(root.val) # if it's leaf, it's done by addLeaf
    addLeftBoundary(root, res)
    addLeaves(root, res)
    addRightBoundary(root, res)

 
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

    res = []
    boundaryTraversal(root, res)
    for i in res:
        print(i)