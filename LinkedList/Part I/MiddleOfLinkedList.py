# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

def middleNode(head):
    temp = head

    while temp and temp.next:
        head = head.next
        temp = temp.next.next
    return head

head = [1,2,3,4,5]
print(middleNode(head))