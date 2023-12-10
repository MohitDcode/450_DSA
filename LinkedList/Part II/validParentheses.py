# LC 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

def isValid(s: str):
    d = {'(':')', '{':'}','[':']'}
    stack = []

    for i in s:
        if i in d:
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i: # check for right bracket
        # if it's the right bracket and the stack is empty(meaning no matching left bracket), 
        # or the left bracket doesn't match
            return False
    return len(stack) == 0 # finally check if the stack still contains unmatched left bracket


def isValid2(s):
    st = []
    for c in s:
        if c == '(' or c == '{' or c == '[':
            st.append(c)
        else:
            if not st or (
            (st[-1] == '(' and c != ')') or
            (st[-1] == '{' and c != '}') or
            (st[-1] == '[' and c != ']')):
                return False
            st.pop()
    return not st

s1 = "()[]{}" # True
s2 = "({[]]" # False
print(isValid2(s1))
