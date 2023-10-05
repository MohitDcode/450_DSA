def maxProfit(prices):
    maxProfit = 0
    minPurchase = prices[0]

    for price in prices:
        currProfit = price - minPurchase
        if currProfit > maxProfit:
            maxProfit = currProfit
        if price < minPurchase:
            minPurchase = price
    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))