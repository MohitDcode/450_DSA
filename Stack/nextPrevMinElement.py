def nextMinElement(arr):
    ans = []
    for i in range(0, len(arr), 1):
        next = -1

        for j in range(i+1, len(arr), 1):
            if arr[i] > arr[j]:
                next = arr[j]
                break
        ans.append(next)
    return ans

def nextSmallerElement(nums):
    stack = []
    res = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[i] < nums[stack[-1]]:
            res[stack.pop()] = nums[i]
        stack.append(i)

    return res

def previousSmallerElement(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)-1,-1,-1):
        while stack and nums[i] < nums[stack[-1]]:
            result[stack.pop()] = nums[i]
        stack.append(i)

    return result

if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print('Given Array is:', arr)
    print("Next minimum element is:",nextSmallerElement(arr))
    print("Previous minimum element is:",previousSmallerElement(arr))