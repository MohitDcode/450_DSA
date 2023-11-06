'''
Given an integer array nums that may contain duplicates, return all possible subsets
The solution set must not contain duplicate subsets. Return the solution in any order.
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
'''

def subsetsWithDup(nums):
        res = []
        nums.sort()
        
        def subsets(index, elements):
            # base case
            if index == len(nums):
                res.append(elements) if elements not in res else None
                return

            subsets(index + 1, elements) # not pick
            subsets(index + 1, elements + [nums[index]]) # pick

        subsets(0, [])
        return res

nums = [1,2,2]
print(subsetsWithDup(nums))