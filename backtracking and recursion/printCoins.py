




"""
(Backtracking and Recursion [M]): Technique: Permutations/Combinations using 
Auxiliary BufferLevel: Coin Change Problem: Given a set of coin denominations, 
print out the different ways you can make a target amount. You can use as many 
coins of each denomination as you like.

For example: If coins are [1,2,5] and the target is 5, output will be:

[1,1,1,1,1]
[1,1,1,2]
[1,2,2]
[5]
"""

def printCoinsHelper(coins, T, startIdx, temp, sums):
    # termination cases
    if sums > T:
        return
    
    if sums == T:
        print(temp)
        return 
    # find candidates that go into temp
    for i in range(startIdx, len(coins)):
        # place candidate into temp and recurse
        temp.append(coins[i])
        printCoinsHelper(coins, T, i, temp, sums + coins[i])
        temp.pop()



def printCoins(coins, T):
    temp = []
    printCoinsHelper(coins, T, 0, temp, 0)


printCoins([1,2,5], 5)




# Output: [1, 1, 1, 1, 1]
          [1, 1, 1, 2]
          [1, 2, 2]
          [5]
          
Time: O(n!) factorial complexity    Space: O(T) b/c temp & stack call are size of target





