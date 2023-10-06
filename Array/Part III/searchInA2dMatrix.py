# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

def searchMatrix(matrix: list[list[int]], target: int):
    if len(matrix) == 0:
        return False
    
    row = 0
    col = len(matrix[0])-1
    print(matrix[row][col])
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            print("1: ",row, col, matrix[row][col])
            return True
        elif matrix[row][col] < target:
            print("2: ",row, col, matrix[row][col])
            row += 1
        elif matrix[row][col] > target:
            # print("3: ",row, col, matrix[row][col])
            print("3: matrix[{}][{}]:".format(row, col), matrix[row][col])
            col -= 1
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
print(searchMatrix(matrix,target))