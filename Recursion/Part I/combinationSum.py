'''
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
'''

def combinationSum(candidates, target):
    res = []
    candidates.sort()

    def dfs(idx, path, cur):
        if cur > target:
            return
        if cur == target:
            res.append(path)
            return
        for i in range(idx, len(candidates)):
            dfs(i, path+[candidates[i]], cur+candidates[i])
    
    dfs(0, [], 0)
    return res    

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))
