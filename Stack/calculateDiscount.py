# LC 1475. Final Prices With a Special Discount in a Shop
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]

def finalPrices(prices):
    stack = []
    output = prices

    for i,n in enumerate(prices):
        # top of stack is larger than current element
        while stack and prices[stack[-1]] >= n:
            # assign the new price into output array
            idx = stack.pop()
            ans = prices[idx] - n
            output[idx] = ans
        stack.append(i)
    return output




prices = [8,4,6,2,3]
print('Discounted prices are:', finalPrices(prices))