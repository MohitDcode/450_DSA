from collections import deque
from createTree import *

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.hd = float('inf') # horizontal distance
        
def bottomView(root):
    if root == None:
        return
    hd = 0
    min_hd, max_hd = 0, 0
    hd_dict = dict()
    q = deque()
    root.hd = hd
    # push node and hd to queue
    q.append(root)

    while(q):
        curr_node = q.popleft()
        hd = curr_node.hd

        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        # Put the dequeued tree node to dictionaryhaving key as horizontal distance.
        hd_dict[hd] = curr_node.val

        if curr_node.left:
            curr_node.left.hd = hd - 1
            q.append(curr_node.left)
        
        if curr_node.right:
            curr_node.right.hd = hd + 1
            q.append(curr_node.right)

    # Traverse the map from least horizontal distance tomost horizontal distance.
    for i in range(min_hd, max_hd+1):
        print(hd_dict[i], end=" ")

# Driver program to test above function
if __name__ == '__main__':
    arr = [10,20,40,None,None,50,70,110,None,None,111,None,None,80,None,None,30,None,60,None,90,112,None,None,113,None,None]
    root = to_binary_tree(arr)
    print('Bottom View:')
    bottomView(root)