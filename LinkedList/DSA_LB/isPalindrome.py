# LC 234
# https://leetcode.com/problems/palindrome-linked-list/description/
# Input: head = [1,2,2,1]
# Output: true
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def LinkedList():
    head = None

# Find Palindrome
def isPalindrome(head):
    current = head
    nums = list()

    while current is not None:
        nums.append(current.data)
        current = current.next
    return nums == nums[::-1]

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
    arr = [1,2,3,2,1]
    for i in range(len(arr)):
        head = push(head, arr[i])

    print('Created Linked list is: ')
    printList()

    result = isPalindrome(head)
    print('\nPalindrome status is:', result)