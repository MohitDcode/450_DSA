def sortArray(nums):
    start = mid = 0
    end = len(nums)-1

    while mid<=end:
        if nums[mid] == 0:
            nums[start], nums[mid] = nums[mid], nums[start]
            start += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[end] = nums[end], nums[mid]
            end -= 1
    return nums



nums = [2,0,2,1,1,0]
print(sortArray(nums))