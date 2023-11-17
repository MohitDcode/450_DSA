from Stack import Stack

def solve(s, pos, ans):
    # base case
    if pos == 1:
        ans = s.peek()
        return ans
    # 1 solved case
    pos -= 1
    temp = s.peek()
    s.pop()
    # recursion
    res = solve(s, pos, ans)
    s.push(temp)
    return res

def getMiddleElement(s):
    size = s.size
    if s.is_empty():
        print('Stack is empty')
        return None
    else: 
        pos = 0
        # odd
        if size & 1:
            pos = (size//2) + 1
        # even
        else:
            pos = size//2
        ans = 0
        a = solve(s, pos, ans)
        return a

# Driver Code
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)

print('Middle Element:', getMiddleElement(s))