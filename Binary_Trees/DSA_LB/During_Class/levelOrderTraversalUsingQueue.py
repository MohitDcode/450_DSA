class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def printLevelOrder(root):
    if root is None:
        return 
    queue = []
    queue.append(root)

    while len(queue) > 0:
        # Print front of queue and remove it from queue
        print(queue[0].val, end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


# Driver Program to test above function
if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
 
    print("Level Order Traversal of binary tree is -")
    printLevelOrder(root)
        