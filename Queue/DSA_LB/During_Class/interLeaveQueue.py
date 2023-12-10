'''
Queue: First-in, first-out => pop(0) => Left most out
Stack: Last-in, first-out => pop() => Right most out
'''

def interLeaveQueue(first):
    # push first half of given queue in a new queue - 'second'
    second = []
    first_size = len(first)
    for _ in range(first_size//2):
        temp = first[0]
        first.pop(0)
        second.append(temp)

    # merge both the halves into the original queue
    for _ in range(first_size//2):
        temp = second[0]
        second.pop(0)
        first.append(temp)

        temp = first[0]
        first.pop(0)
        first.append(temp)
    
    return first

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
    print("InterLeave Queue:", interLeaveQueue(q)) 