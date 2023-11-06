'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
'''

def maximalSquare(matrix, i, j, row, col, maxim):
    # base case
    if (i >= row or j >= col):
        return 0
    
    # processing
    # 1) traverse to right, diagonal and down
    right = maximalSquare(matrix, i, j+1, row, col, maxim)
    diagonal = maximalSquare(matrix, i+1, j+1, row, col, maxim)
    down = maximalSquare(matrix, i+1, j, row, col, maxim)
    
    # print('right',right)
    # print('diagonal', diagonal)
    # print('down',down)

    # 2) check if square builds from current position
    if matrix[i][j] == "1":
        ans = 1 + min(right, diagonal, down)
        maxim = max(maxim, ans)
        return maxim
    else: #standing at 0
        return 0

if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    row = len(matrix)
    col = len(matrix[0])
    maxim = 0
    ans = maximalSquare(matrix, 0, 0, row, col, maxim)
    print(ans*ans)