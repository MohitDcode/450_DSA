def coinChange(coins, amount):
    if amount == 0: return 0
    mini = float('inf')
    ans = float('inf')

    for i in range(0,len(coins)):
        coin = coins[i]
        if coin <= amount: # use the current coin or not
            recAns = coinChange(coins, amount-coin) # -coin as current is being used
            if recAns != float('inf'):
                ans = 1 + recAns # +1 as we have the coin used
        mini = min(mini, ans) # minimum possible coins
    return mini

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))