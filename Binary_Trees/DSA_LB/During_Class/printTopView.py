from createTree import *

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.hd = 0 # horizontal distance
        
def topView(root):
    if root == None:
        return
    q = []
    m = dict()
    hd = 0
    root.hd = hd

    # push node and hd to queue
    q.append(root)

    while(len(q)):
        root = q[0]
        hd = root.hd

        # count function
        if hd not in m:
            m[hd] = root.val
        if root.left:
            root.left.hd = hd - 1
            q.append(root.left)
        if root.right:
            root.right.hd = hd + 1
            q.append(root.right)
        
        q.pop(0)
    
    for i in sorted(m):
        print(m[i], end=" ")


        
def bottomView(root):
    print()

# Driver program to test above function
if __name__ == '__main__':
    arr = [10,20,40,None,None,50,70,110,None,None,111,None,None,80,None,None,30,None,60,None,90,112,None,None,113,None,None]
    root = to_binary_tree(arr)
    print('Top View:')
    topView(root)