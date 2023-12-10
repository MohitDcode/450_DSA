'''
Queue: First-in, first-out => pop(0) => Left most out
Stack: Last-in, first-out => pop() => Right most out
'''

def reverseQueue(q):
    s = []

    # move Queue's elements to Stack
    while len(q) != 0:
        frontElement = q[0]
        q.pop(0)
        s.append(frontElement)

    # move Stack's elements to Queue
    while len(s) != 0:
        element = s[-1]
        s.pop()
        q.append(element)

    return q

def via_recusrion(q):
    # base case
    if len(q) == 0:
        return []
    
    # rec call
    element = q[0]
    q.pop(0)
    via_recusrion(q)
    q.append(element)
    return q

# Main
if __name__=='__main__': 
    q = []
    q.append(10)
    q.append(20)
    q.append(30)
    q.append(40)
    q.append(50)
    q.append(60)
    
    print("Original Queue: ", q)
    # print("Reversed Queue: ", reverseQueue(q)) 
    print("Reversed Queue via Recursion: ", via_recusrion(q))