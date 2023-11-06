def maximiseTheCuts(n, x, y, z):
    # base case
    if n == 0:
        return 0
    
    # processing & rr
    a = b = c = 0
    if n-x > 0:
        a = 1 + maximiseTheCuts(n-x, x, y, z)
    if n-y > 0:
        b = 1 + maximiseTheCuts(n-y, x, y, z)
    if n-z > 0:
        c = 1 + maximiseTheCuts(n-z, x, y, z)
    return max(a, max(b,c))

if __name__ == "__main__":
    n = 5
    x = 5
    y = 3
    z = 2
    ans =  maximiseTheCuts(n, x, y, z)
    if ans < 0:
        print(0) # no cut can be made
    else:
        print(ans)
    