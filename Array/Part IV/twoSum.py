# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def twoSum(nums, target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
        numMap[nums[i]] = i
    return []


nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
