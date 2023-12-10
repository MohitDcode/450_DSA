# Given an expression with only ‘}’ and ‘{‘. The expression may not be balanced. 
# Find minimum number of bracket reversals to make the expression balanced.
# Input:  exp = "}{"
# Output: 2
class List(list):
    def push(self, x):
        self.append(x)
def countMinReversals(Str):
    st = List()
    ans = 0

    for i in range(len(Str)):
        if Str[i] == '{':
            st.append(Str[i])
        else:
            if len(st) > 0:
                st.pop() # If stack has a '{' present for '}' encountered, pop from the stack.
            else:
                # If stack is empty, change '}' to '{' and push it to stack and increment ans by 1
                st.push('{')
                ans += 1
    
    if (len(st) % 2 != 0):
        return -1
    ans += len(st)//2
    return ans

expr = "}{"
print(countMinReversals(expr)) #1