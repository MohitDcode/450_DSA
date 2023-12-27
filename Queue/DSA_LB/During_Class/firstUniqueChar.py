'''
LC 387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
'''

def iterative(s):
    for i in range(len(s)):
        if s[i] not in s[:i] and s[i] not in s[i+1:]:
            return i
    return -1

def usingDict(s):
    frequency = {}

    for char in s:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] = frequency[char] + 1
    
    for index in range(len(s)):
        if frequency[s[index]] == 1:
            return index
    return -1


# Main
if __name__=='__main__': 
    s = 'loveleetcode' #2
    print('Result using iteration:',iterative(s))
    print('Result using dictionary:',usingDict(s))