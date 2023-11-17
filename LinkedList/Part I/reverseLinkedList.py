# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
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
        return self.head
    
    # Print the LL
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

    # Reverse the LL
    def reversedList(self):
        prev = None
        current = self.head

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

# Driver Code
llist = LinkedList()
arr = [1,2,3,4,5]
for i in range(len(arr)):
    llist.push(arr[i])

print('Created Linked list is: ')
llist.printList()

llist.reversedList()
print('\nReversed Linked list is: ')
llist.printList()