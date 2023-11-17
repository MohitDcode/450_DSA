# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def LinkedList():
    head = None

# Reverse the LL
def reversedList(node):
    if node == None:
        return node
    if node.next == None:
        return node
    
    node1 = reversedList(node.next)
    node.next.next = node
    node.next = None
    return node1

# Print the LL
def printList():
    temp = head
    while(temp != None):
        print(temp.data, end=' ')
        temp = temp.next

# Insert a new node at the beginning
def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

# Driver Code
if __name__ == '__main__':
    head = LinkedList()
    arr = [1,2,3,4,5]
    for i in range(len(arr)):
        head = push(head, arr[i])

    print('Created Linked list is: ')
    printList()

    head = reversedList(head)
    print('\nReversed Linked list is: ')
    printList()