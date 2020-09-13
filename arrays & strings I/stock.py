


"""
([M] maxDiff technique)iven a list of stock prices for a company, find the maximum 
amount of money you can makewith one trade. A trade is a buy and sell.

"""

def oneTrade(prices):

    minSoFar = float('inf')
    maxDiff = 0

    for i in range(len(prices)):
        minSoFar = min(minSoFar, prices[i])
        maxDiff = max(prices[i] - minSoFar, maxDiff)

    return maxDiff

print(oneTrade([9,3,2,1,5,7,2,8,3,4]))



