def houseRobber(nums, size, index):
    # base case
    if index >= size:
        return 0
    
    # processing & rr
    option1 = nums[index] + houseRobber(nums, size, index+2) # first index position
    option2 = 0 + houseRobber(nums, size, index+1)  # second index position

    return max(option1, option2)



# nums = [1,2,3,1] #4
nums = [2,7,9,3,1] #12
size = len(nums)
index = 0
print(houseRobber(nums, size, index))