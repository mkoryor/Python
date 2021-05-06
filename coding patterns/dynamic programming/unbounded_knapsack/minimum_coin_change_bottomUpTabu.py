



"""
Given an infinite supply of ‘n’ coin denominations and a total money amount, 
we are asked to find the minimum number of coins needed to make up that amount.

Example 1:

Denominations: {1,2,3}
Total amount: 5
Output: 2
Explanation: We need minimum of two coins {2,3} to make a total of '5'
Example 2:

Denominations: {1,2,3}
Total amount: 11
Output: 4
Explanation: We need minimum four coins {2,3,3,3} to make a total of '11'
"""


import math



# Time: O(C * T) Space: O(C * T)
def count_change(denominations, total):
  n = len(denominations)
  dp = [[math.inf for _ in range(total+1)] for _ in range(n)]

  # populate the total=0 columns, as we don't need any coin to make zero total
  for i in range(n):
    dp[i][0] = 0

  for i in range(n):
    for t in range(1, total+1):
      if i > 0:
        dp[i][t] = dp[i - 1][t]  # exclude the coin
      if t >= denominations[i]:
        if dp[i][t - denominations[i]] != math.inf:
          # include the coin
          dp[i][t] = min(dp[i][t], dp[i][t - denominations[i]] + 1)

  # total combinations will be at the bottom-right corner.
  return -1 if dp[n - 1][total] == math.inf else dp[n - 1][total]


def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()

