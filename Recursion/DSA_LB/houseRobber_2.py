def houseRobber(nums, start, end):
    # base case
    if start > end:
        return 0
    
    # processing & rr
    option1 = nums[start] + houseRobber(nums, start+2, end) # first index position
    option2 = 0 + houseRobber(nums, start+1, end)  # second index position

    return max(option1, option2)

def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    
    option1 = houseRobber(nums, 0, n-2) # First to second last element
    option2 = houseRobber(nums, 1, n-1) # Second to last element

    return max(option1, option2)


nums = [1,2,3,1] #4
# nums = [2,7,9,3,1] #11

index = 0
print(rob(nums))