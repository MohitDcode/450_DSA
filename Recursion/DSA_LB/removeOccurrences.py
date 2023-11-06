# Input: s = "daabcbaabcbc", part = "abc"
# Output: "dab"
# Explanation: The following operations are done:
# - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
# - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
# - s = "dababc", remove "abc" starting at index 3, so s = "dab".
# Now s has no occurrences of "abc".

def removeOccurences(s, part):
    if part not in s:
        return s
    else:
        s_new = s.replace(part, '', 1)
        return removeOccurences(s_new, part)

s = "daabcbaabcbc"
part = "abc"
print(removeOccurences(s, part))