'''
LC 239. Sliding Window Maximum
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left
of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves 
right by one position. Return the max sliding window.
'''
import collections
def maxSlidingWindow(nums, k):
    d = collections.deque()
    out = []

    for i, n in enumerate(nums):
        print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, out))
        while d and nums[d[-1]] < n:
            d.pop()
            print("\t Popped from d because d has elements and nums[d.top] < curr element")
        d.append(i)
        print(("\t added i to d"))
        if d[0] == i-k:
            d.popleft()
            print("\t Popped left from d because it's outside the window's leftmost (i-k)")
        if i >= k-1:
            out.append(nums[d[0]])
            print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
    return out

# Main
if __name__=='__main__': 
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print('Result:',maxSlidingWindow(nums, k))
    # Output: [3,3,5,5,6,7]