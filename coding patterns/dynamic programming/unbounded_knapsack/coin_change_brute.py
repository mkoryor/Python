


"""
Given an infinite supply of ‘n’ coin denominations and a total money amount, 
we are asked to find the total number of distinct ways to make up that amount.

Example:

Denominations: {1,2,3}
Total amount: 5
Output: 5
Explanation: There are five ways to make the change for '5', here are those ways:
  1. {1,1,1,1,1} 
  2. {1,1,1,2} 
  3. {1,2,2}
  4. {1,1,3}
  5. {2,3}
"""


# Time: O(2^c + t) Space: O(C + T)
def count_change(denominations, total):
  return count_change_recursive(denominations, total, 0)


def count_change_recursive(denominations, total, currentIndex):
  # base checks
  if total == 0:
    return 1

  n = len(denominations)
  if n == 0 or currentIndex >= n:
    return 0

  # recursive call after selecting the coin at the currentIndex
  # if the coin at currentIndex exceeds the total, we shouldn't process this
  sum1 = 0
  if denominations[currentIndex] <= total:
    sum1 = count_change_recursive(
      denominations, total - denominations[currentIndex], currentIndex)

  # recursive call after excluding the coin at the currentIndex
  sum2 = count_change_recursive(denominations, total, currentIndex + 1)

  return sum1 + sum2


def main():
  print(count_change([1, 2, 3], 5))


main()

