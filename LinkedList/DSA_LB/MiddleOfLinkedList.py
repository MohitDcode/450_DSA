# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def LinkedList():
    head = None

def middleNode(head):
    temp = head

    while temp and temp.next:
        head = head.next
        temp = temp.next.next
    return head

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

    head = middleNode(head)
    print('\nMiddle of the Linked list is: ')
    printList()