# Movement Notes
'''
up   = x-1, y
down = x+1, y
right= x, y+1
left = x, y-1
'''

# movement possibilites
'''
1) Last index reached, path closed
2) Out of bound
3) Position already travelled

=> This needs a seperate fucntion to check the path = isSafe

'''
def isSafe(srcx, srcy, newx, newy, maze, row, col, visited):
    
    if ( 
    #Out of bound check
       (newx >= 0 and newx < row) and (newy >= 0 and newy < col) and
    # path closed check
       maze[newx][newy] == 1 and
    # Position already travelled
       (visited[newx][newy] == False)):
        return True
    else:
        return False


def ratInaMaze(maze, row, col, srcx, srcy, output, visited):
    # base case
    # destination coordinates are [row-1][col-1]
    if(srcx == row-1 and srcy == col -1):
        print(output)

    # processing
    # ----------
    # up
    newx = srcx - 1
    newy = srcy
    if isSafe(srcx, srcy, newx, newy, maze, row, col, visited):
        # mark visited
        visited[newx][newy] = True
        # call recusrion
        ratInaMaze(maze, row, col, newx, newy, output + "U", visited)
        # backtracking
        visited[newx][newy] = False

    # right
    newx = srcx
    newy = srcy + 1
    if isSafe(srcx, srcy, newx, newy, maze, row, col, visited):
        # mark visited
        visited[newx][newy] = True
        # call recusrion
        ratInaMaze(maze, row, col, newx, newy, output + "R", visited)
        # backtracking
        visited[newx][newy] = False
    # down
    newx = srcx + 1
    newy = srcy
    if isSafe(srcx, srcy, newx, newy, maze, row, col, visited):
        # mark visited
        visited[newx][newy] = True
        # call recusrion
        ratInaMaze(maze, row, col, newx, newy, output + "D", visited)
        # backtracking
        visited[newx][newy] = False
    # left
    newx = srcx
    newy = srcy - 1
    if isSafe(srcx, srcy, newx, newy, maze, row, col, visited):
        # mark visited
        visited[newx][newy] = True
        # call recusrion
        ratInaMaze(maze, row, col, newx, newy, output + "L", visited)
        # backtracking
        visited[newx][newy] = False


if __name__ == '__main__':
    maze = [
        [1,0,0,0],
        [1,1,0,0],
        [1,1,1,0],
        [1,1,1,1]
    ]
    row = 4
    col = 4
    srcx = 0
    srcy = 0
    output = ""
    if maze[0][0] == 0:
        print("No Path Existis")
    else:
        visited = [[0 for _ in range(row)] for _ in range(col)]
        visited[srcx][srcy] = True
        ratInaMaze(maze, row, col, srcx, srcy, output, visited)