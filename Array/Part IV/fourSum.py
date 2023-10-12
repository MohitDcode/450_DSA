# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

def fourSum(nums, target):
    ans = set()
    n = len(nums)
    nums.sort()

    for i in range(n):
        for j in range(i+1,n):
            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right] + nums[j]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    ans.add((nums[i], nums[left], nums[right], nums[j]))

                    left += 1
                    right -= 1
    return list(ans)


nums = [2,2,3,2,2,2]
target = 8
print(fourSum(nums, target))