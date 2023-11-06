def coinChange(coins, amount):
    if amount == 0: return 0
    memo = [float("inf")]*(amount+1)
    coins.sort()
    myset = set(coins)
    for i in range(coins[0], amount+1): # no need to start from 0, instead start from the coins minimum
        if i in myset: # when the amount value is one of the coins values, then the minimum count is 1 for sure. This is our base case.
            memo[i] = 1
        else:
            tmp = float("inf") # track the minimum when iterating the coins array for this round
            for coin in coins:
                if i - coin >= 0:
                    tmp = min(tmp, memo[i-coin])
            memo[i] = tmp+1
    return memo[amount] if memo[amount] != float("inf") else -1



coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))