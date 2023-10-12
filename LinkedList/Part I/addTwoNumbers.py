# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

import ConvertArrayToLinkedList as LinkedList
def addTwoNumbers(l1,l2):
    dummyHead = LinkedList.Node(0)
    tail = dummyHead
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.data if l1 is not None else 0
        digit2 = l2.data if l2 is not None else 0

        sum = digit1 + digit2 + carry
        digit = sum % 10
        carry = sum // 10

        newNode = LinkedList.Node(digit)
        tail.next = newNode
        tail = tail.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    
    result = dummyHead.next
    dummyHead.next = None
    return result

arr1 = [2,4,3]
n1 = len(arr1)
arr2 = [5,6,4]
n2 = len(arr2)
list1 = LinkedList.arrayToList(arr1, n1)
# LinkedList.display(list1) 
list2 = LinkedList.arrayToList(arr2, n2)
# LinkedList.display(list2) 
LinkedList.display(addTwoNumbers(list1,list2))