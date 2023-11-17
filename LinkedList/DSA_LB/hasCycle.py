# LC 141
# https://leetcode.com/problems/linked-list-cycle/
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def LinkedList():
    head = None

# Find Palindrome
def hasCycle(head):
    slow , fast = head , head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

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
    arr = [3,2,0,-4]
    for i in range(len(arr)-1, -1, -1):
    # for i in arr[::-1]:
        head = push(head,arr[i])

    print('Created Linked list is: ')
    printList()

    result = hasCycle(head)
    print('\nLL Cycle status is:', result)