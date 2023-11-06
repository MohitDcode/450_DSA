class Node:
    # fucntion to initialize node objects
    def __init__(self, data):
        self.data = data
        self.next = None #initialize as null

class LinkedList:
    # function to initialize head
    def __init__(self):
        self.head = None

    # function to insert a new node at the beginning of the LL
    def push(self, new_data):
        # 1.Allocate a new node
        new_node = Node(new_data)

        # 2.Make next of the new node as head
        new_node.next = self.head

        # 3.Move the head to point the new Node
        self.head = new_node

    # Method-1: count the number of nodes iteratively
    def getCountIter(self):
        temp = self.head
        count = 0

        # iterate till end of LL is reached
        while(temp):
            count += 1
            temp = temp.next
        return count
    
    # Method-2: count the number of nodes recursively
    def getCount(self, node, count = 0):
        # base case
        if(not node):
            return count
        else:
            return self.getCount(node.next, count+1)
    # A wrapper over getCountRec()
    def getCountRec(self):
        return self.getCount(self.head)    
    

# driver code
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)

    # function call
    print("Count of node is :", llist.getCountRec())