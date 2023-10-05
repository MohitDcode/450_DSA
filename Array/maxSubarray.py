def maxSubArray(nums):
    maxSum = nums[0]
    currSum = nums[0]

    for num in nums[1:]:
        currSum = max(num, currSum+num)
        maxSum = max(maxSum, currSum)
    return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print("Max subarray sum is :", maxSubArray(nums))