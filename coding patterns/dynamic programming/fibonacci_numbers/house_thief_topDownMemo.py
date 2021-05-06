



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

# Time: O(n) Space: O(1)
def find_max_steal(wealth):
  dp = [0 for x in range(len(wealth))]
  return find_max_steal_recursive(dp, wealth, 0)


def find_max_steal_recursive(dp, wealth, currentIndex):
  if currentIndex >= len(wealth):
    return 0

  if dp[currentIndex] == 0:
    # steal from current house and skip one to steal next
    stealCurrent = wealth[currentIndex] + find_max_steal_recursive(dp, wealth, currentIndex + 2)
    # skip current house to steel from the adjacent house
    skipCurrent = find_max_steal_recursive(dp, wealth, currentIndex + 1)

    dp[currentIndex] = max(stealCurrent, skipCurrent)

  return dp[currentIndex]


def main():

  print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
  print(find_max_steal([2, 10, 14, 8, 1]))


main()