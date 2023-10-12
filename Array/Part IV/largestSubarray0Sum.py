# N = 8
# nums = {15,-2,2,-8,1,7,10,23}
# Output: 5
# Explanation: The largest subarray with sum 0 will be -2 2 -8 1 7.

def largestSubarray(nums):
    dic = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        if curr_sum == 0:
            max_len = i+1
        if curr_sum in dic:
            max_len = max(max_len, i-dic[curr_sum])
        else:
            dic[curr_sum] = i
    return max_len

nums = [15,-2,2,-8,1,7,10,23]   
print(largestSubarray(nums))