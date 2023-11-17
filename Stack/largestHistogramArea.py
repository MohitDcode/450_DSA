def largestHistogramArea(heights):
    n = len(heights)
    
    # Left Small Element
    stack = []
    leftSmallElement = [0] * n

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            leftSmallElement[i] = stack[-1] + 1
        stack.append(i)
    
    # Right Small Element
    stack = []
    rightSmallElement = [n-1] * n

    for i in range(n-1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            rightSmallElement[i] = stack[-1] - 1
        stack.append(i)

    # Calculate area
    res = heights[0]

    for i in range(n):
        height = heights[i]
        weidth = rightSmallElement[i] - leftSmallElement[i] + 1
        area = height * weidth
        res = max(res, area)
    return res       

heights = [2,1,5,6,2,3]
print("largest possible area is:", largestHistogramArea(heights))