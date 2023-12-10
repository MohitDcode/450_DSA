class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Delete node of matching key
    def deleteNode(self, key):
        temp = self.head

        #1. If head node matches with Key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        #2. Search key and delete
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key doesn't matches
        if temp == None: # last node reached
            return
        
        # unlink the node from LL
        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

# driver code
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)

print('Created Linked list is: ')
llist.printList()
llist.deleteNode(1)
print('\nLinked List after deleting the node is: ')
llist.printList()