# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

import ConvertArrayToLinkedList as LinkedList
def removeNthFromEnd(head,n):
    i = j = head

    for k in range(n):
        j = j.next
    #now i and j will be at difference n
    if j == None: #Only happens when we are supposed to remove the first element
        return head.next
    while j.next != None:
        i = i.next
        j = j.next
    i.next = i.next.next
    return head

arr1 = [1,2,3,4,5]
arr1_len = len(arr1)
head = LinkedList.arrayToList(arr1, arr1_len)
n = 2
LinkedList.display(removeNthFromEnd(head,n))