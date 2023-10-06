# Input: nums = [1,1,5]
# Output: [1,5,1]

def nextPermutation(nums):
    # Do not return anything, modify nums in-place instead.
    i = j = len(nums)-1  #we'll start from the end

    while i>0 and nums[i-1] >= nums[i]: #find the first non-assending element starting from the end
        i -= 1
    
    #two cases after first loop
    if i == 0: #i is 0(when array is sorted dicreasingly)
        nums.reverse()
        return
    while nums[j] <= nums[i-1]: #find the first number grater then nums[i-1] starting from end
        j -= 1
    # Now out pointer is pointing at two different positions
    # i. first non-assending number from end
    # j. first number greater than nums[i-1]
    # We'll swap these two numbers

    nums[i-1], nums[j] = nums[j], nums[i-1]
    
    # We'll reverse a sequence strating from i to end
    nums[i:] = nums[len(nums)-1:i-1:-1]
    print(nums)

if __name__ == "__main__":
    nums = [1,1,5]
    nextPermutation(nums)