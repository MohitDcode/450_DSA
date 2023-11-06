# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def maxProfitFinder(prices, i, minPrice, maxProfit):# base case
    # base case
    if i == len(prices):
        return 

    # processing
    # for i in range(len(prices)):
    if(prices[i] < minPrice):
        minPrice = prices[i]
    
    todaysProfit = prices[i] - minPrice

    if(todaysProfit > maxProfit):
        maxProfit = todaysProfit

    # Recursive relation
    maxProfitFinder(prices, i+1, minPrice, maxProfit)

prices = [7,1,5,3,6,4]
minPrice = float('inf')
maxProfit = float('-inf')
print(maxProfitFinder(prices, 0, minPrice, maxProfit))