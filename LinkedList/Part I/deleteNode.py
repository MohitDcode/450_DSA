# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
import ConvertArrayToLinkedList as LinkedList


def deleteNode(head,node):
    # locate victim node
    victim_node = node.next
    # overwrite node's value by victim node's value
    node.data = victim_node.data
    # break the linkage of victim node
    node.next = victim_node.next
    # release victim node
    del victim_node
    return 


arr1 = [4,5,1,9]
n1 = len(arr1)
head = LinkedList.arrayToList(arr1, n1)
# LinkedList.display(list1) 
arr2 = [5]
n2 = len(arr2)
node = LinkedList.arrayToList(arr1, n1)
LinkedList.display(deleteNode(head,node))