'''
Queue: First-in, first-out => pop(0) => Left most out
Stack: Last-in, first-out => pop() => Right most out
'''

def reverseQueue(q, k):
    n = len(q)
    s = []
    # push first K elements into stack
    for _ in range(k):
        tmp = q[0]
        q.pop(0)
        s.append(tmp)

    # push all K elements into Queue
    while len(s) != 0:
        temp = s[-1]
        s.pop()
        q.append(temp)

    # pop and push first n-K element into Queue again
    for _ in range(n-k):
        temp = q[0]
        q.pop(0)
        q.append(temp)
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
    
    print("Original Queue:", q)
    print("K Reversed Queue:", reverseQueue(q,4)) 
    # print("Reversed Queue via Recursion: ", via_recusrion(q))