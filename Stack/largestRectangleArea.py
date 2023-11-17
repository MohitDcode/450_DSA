# LC 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

def largestRectangleArea(heights):
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, height * width)
        stack.append(i)

    while stack:
        height = heights[stack.pop()]
        width = len(heights) - stack[-1] - 1 if stack else len(heights)
        max_area = max(max_area, height * width)

    return max_area

def largestHistogramArea(heights):
        n = len(heights)
        # left boundary => next smaller element to left
        stack = []
        nextSmallerLeft = [0]*n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nextSmallerLeft[i] = stack[-1] + 1
            stack.append(i)
        
        # right boundary => next smaller element to right
        stack = []
        nextSmallerRight = [n-1]*n
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                nextSmallerRight[i] = stack[-1] - 1
            stack.append(i)
        
        res = heights[0]
        for i in range(n):
            height = heights[i]
            weidth = int(nextSmallerRight[i] - nextSmallerLeft[i] + 1)
            area = height * weidth
            res = max(res, area)
            
        return res

heights = [2,1,5,6,2,3]
# print("Largest rectangle area is", largestRectangleArea(heights))
print("Largest Histogram area is", largestHistogramArea(heights))
