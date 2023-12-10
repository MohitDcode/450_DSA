# LC 1047. Remove All Adjacent Duplicates In String
# Input: s = "abbaca"
# Output: "ca"

def removeDuplicates(s):
    ans = []

    for a in s:
        if(len(ans)>0 and ans[-1]==a):
            ans.pop()
        else:
            ans.append(a)
    return ("".join(ans))

s = "abbaca"
print(removeDuplicates(s))