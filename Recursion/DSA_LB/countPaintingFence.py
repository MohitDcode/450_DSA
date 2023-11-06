'''
Given a fence with n posts and k colors, find out the number of ways of painting the fence such that at most 2 adjacent posts have the same color. 
Since the answer can be large return it modulo 10^9 + 7.

Examples:

    Input : n = 2 k = 4
    Output : 16
    Explanation: We have 4 colors and 2 posts.
    Ways when both posts have same color : 4 
    Ways when both posts have diff color :4(choices for 1st post) * 3(choices for 2nd post) = 12

'''
def countPaintingFence(n,k):
    # base case
    if n == 1:
        return k
    if n == 2:
        return (k + k*(k - 1))  # same + different
    
    # processing
    ans = (n - 1) * (countPaintingFence(n-1, k) # last two poles with different colors
                     + countPaintingFence(n-2, k)) # last two poles with same colors
    
    return ans

if __name__ == "__main__":
    n = 3 #poles
    k = 3 #colors
    print(countPaintingFence(n,k))