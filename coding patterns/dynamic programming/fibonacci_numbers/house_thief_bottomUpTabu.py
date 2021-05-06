


"""

Given a number array representing the wealth of ‘n’ houses, 
determine the maximum amount of money the thief can steal without alerting 
the security system.

Example 1:

Input: {2, 5, 1, 3, 6, 2, 4}
Output: 15
Explanation: The thief should steal from houses 5 + 6 + 4

Input: {2, 10, 14, 8, 1}
Output: 18
Explanation: The thief should steal from houses 10 + 8
"""


# Time: O(N) Space: O(N)
def find_max_steal(wealth):
  n = len(wealth)
  if n == 0:
    return 0
  dp = [0 for x in range(n+1)]  # '+1' to handle the zero house
  dp[0] = 0  # if there are no houses, the thief can't steal anything
  dp[1] = wealth[0]  # only one house, so the thief have to steal from it

  # please note that dp[] has one extra element to handle zero house
  for i in range(1, n):
    dp[i + 1] = max(wealth[i] + dp[i - 1], dp[i])

  return dp[n]


def main():

  print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
  print(find_max_steal([2, 10, 14, 8, 1]))


main()
