# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
import ConvertArrayToLinkedList as LinkedList
def mergeTwoLists(list1:list[int],list2:list[int]) -> list[int]:
    temp = dummy = LinkedList.Node(0)
    while list1 and list2:
        if list1.data < list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    if list1:
        temp.next = list1
        list1 = list1.next
    if list2:
        temp.next = list2
        list2 = list2.next
    return dummy.next

arr1 = [1,2,4]
n1 = len(arr1)
arr2 = [1,3,4]
n2 = len(arr2)
list1 = LinkedList.arrayToList(arr1, n1)
# LinkedList.display(list1) 
list2 = LinkedList.arrayToList(arr2, n2)
# LinkedList.display(list2) 
LinkedList.display(mergeTwoLists(list1,list2))