# Input: nums = [100,4,200,1,3,2]
# Output: 4


def longestConsecutive(nums):
    max_length = 0
    uniques = set(nums)

    while uniques:
        low = high = uniques.pop()

        while low-1 in uniques or high+1 in uniques:
            if low-1 in uniques:
                uniques.remove(low-1)
                low -= 1
            if high+1 in uniques:
                uniques.remove(high+1)
                high += 1
        max_length = max(high - low + 1, max_length)
    return max_length

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))