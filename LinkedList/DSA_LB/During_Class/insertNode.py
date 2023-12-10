class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insertBeg(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Insert after a pos
    def insertAfter(self, prev_node, new_data):
        
        # 1.Check if a given node exists
        if prev_node is None:
            print("The previous node must be in linked list")
            return
        
        # 2.Create a new node and put in new_data
        new_node = Node(new_data)

        # 3.Make next of new node as next of prev_node
        new_node.next = prev_node.next

        # 4.Make next of prev_node as new node
        prev_node.next = new_node

    # Insert at tail
    def insertTail(self, new_data):
        new_node = Node(new_data)
        temp = self.head

        # set next of new node as null as it would be the new tail
        new_node.next = None

        # 1.If LL is empty
        if self.head is None: 
            return new_node
        
        # 2.If LL is not empty
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        
    # Insert at position
    def insertPos(self, pos, new_data):
        temp = self.head

        if pos < 1:
            print('\nInvalid Position')

        if pos == 1:
            newNode = Node(new_data)
            newNode.next = self.head
            self.head = newNode
        else:
            while pos != 0:
                pos -= 1
                if pos == 1:
                    newNode = Node(new_data)
                    newNode.next = temp.next
                    temp.next = newNode
                    break
                temp = temp.next

                if temp == None:
                    break
            
            if pos != 1:
                print('\nPosition out of range')


    # Print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


# code execution
if __name__ == '__main__':
    llist = LinkedList() #start with empty list

    # 1. Insert at Head
    llist.insertBeg(6)
    llist.insertBeg(5)
    llist.insertBeg(4)
    llist.insertBeg(3)
    llist.insertBeg(1)
    print('Created linked list is: ')
    llist.printList()

    # 2. Insert after a position
    llist.insertAfter(llist.head,2) # insert 2 after 1
    print('\nAfter inserting 2: ')
    llist.printList()

    # 3. Insert at Tail
    llist.insertTail(7)
    print('\nAfter insert at Tail: ')
    llist.printList()

    # 4. Insert at a specific position
    llist.insertPos(1, 0)
    llist.insertPos(9, 8)
    print('\nAfter insert at Position: ')
    llist.printList()
