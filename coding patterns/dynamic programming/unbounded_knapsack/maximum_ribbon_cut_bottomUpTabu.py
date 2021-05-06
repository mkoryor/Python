





"""

We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. 
Now we need to cut the ribbon into the maximum number of pieces that comply 
with the above-mentioned possible lengths. Write a method that will return the 
count of pieces.

Example 1:

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.
Example 2:

n: 7
Ribbon Lengths: {2,3}
Output: 3
Explanation: Ribbon pieces will be {2,2,3}.
"""





import math


# Time: O(L * N) Space: O(L * N)
def count_ribbon_pieces(ribbonLengths, total):
  n = len(ribbonLengths)
  dp = [[-math.inf for _ in range(total+1)] for _ in range(n)]

  # populate the total=0 columns, as we don't need any ribbon to make zero total
  for i in range(n):
    dp[i][0] = 0

  for i in range(n):
    for t in range(1, total+1):
      if i > 0:  # exclude the ribbon
        dp[i][t] = dp[i - 1][t]
      # include the ribbon and check if the remaining length can be cut into available lengths
      if t >= ribbonLengths[i] and dp[i][t - ribbonLengths[i]] != -math.inf:
        dp[i][t] = max(dp[i][t], dp[i][t - ribbonLengths[i]] + 1)

  # total combinations will be at the bottom-right corner, return '-1' if cutting is not possible
  return -1 if dp[n - 1][total] == -math.inf else dp[n - 1][total]


def main():
  print(count_ribbon_pieces([2, 3, 5], 5))
  print(count_ribbon_pieces([2, 3], 7))
  print(count_ribbon_pieces([3, 5, 7], 13))
  print(count_ribbon_pieces([3, 5], 7))


main()
