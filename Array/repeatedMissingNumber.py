# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.

# Input:[3 1 2 5 3] 
# Output:[3, 4] 

def repeatedMissingNumber(nums):
    numberMap = {}
    length = len(nums)

    for i in nums:
        if not i in numberMap:
            numberMap[i] = True
        else:
            print("Repeating =",i)
    
    for i in range(1, length + 1):
        if not i in numberMap:
            print("Missing =", i)

nums = [3,1,2,5,3]
repeatedMissingNumber(nums)