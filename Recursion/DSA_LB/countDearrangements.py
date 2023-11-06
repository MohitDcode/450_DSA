'''
dearrangement of {0,1,2,3} is {2,3,1,0}
i.e. no element appears in its original position.

1) n=1 -> {1}: 0 possible dearrangement
2) n=2 -> {1,2}: 1 possible dearrangement
3) n=3 -> {1,2,3}: 2 possible dearrangements
4) n=4 -> 9 possible dearrangements
'''

def countDearrangements(n):
    # base case
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    ans = (n-1) * (countDearrangements(n-1) + (countDearrangements(n-2)))
    return ans

if __name__ == "__main__":
    n = 4 #9
    print(countDearrangements(n))