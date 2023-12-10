# LC 160. Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def LinkedList():
    head = None

def printList(head_ref):
    temp = head_ref
    while(temp != None):
        print(temp.data, end='->')
        temp = temp.next

def push(head_ref, new_data):
    new_node = Node(new_data)
    new_node.data = new_data
    new_node.next = head_ref
    head_ref = new_node
    return head_ref

def getIntersectionNode(headA, headB):
    l1, l2 = headA, headB
    while l1 != l2: # equal head means intersection point
        if l1:
            l1 = l1.next
        else:
            l1 = headB
        
        if l2:
            l2 = l2.next
        else:
            l2 = headA
        printList(l1)
        return(l1)

if __name__ == '__main__':
    arrA = [4,1,8,4,5]
    headA = LinkedList()
    for i in range(len(arrA)-1, -1, -1):
        headA = push(headA, arrA[i])
    # print('Created Linked list A is: ')
    # printList(headA)

    arrB = [5,6,1,8,4,5]
    headB = LinkedList()
    for i in range(len(arrB)-1, -1, -1):
        headB = push(headB, arrB[i])
    # print('\nCreated Linked list B is: ')
    # printList(headB)
    # print('\n')
    print('Intercsection point is:', getIntersectionNode(headA, headB))