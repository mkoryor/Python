

"""
Given a number ‘n’, implement a method to count how many possible ways there are 
to express ‘n’ as the sum of 1, 3, or 4.

Example 1:

n : 4
Number of ways = 4
Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4} 
Example 2:

n : 5
Number of ways = 6
Explanation: Following are the six ways we can express 'n' : 
{1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1}, 
{1,4}, {4,1}

"""


# Time: O(N) Space: O(N)
def count_ways(n):
  if n == 0:
    return 1  # base case, we don't need to subtract any thing, so there is only one way

  if n == 1:
    return 1  # we take subtract 1 to be left with zero, and that is the only way

  if n == 2:
    return 1  # we can subtract 1 twice to get zero and that is the only way

  if n == 3:
    return 2  # '3' can be expressed as {1, 1, 1}, {3}

  # if we subtract 1, we are left with 'n-1'
  subtract1 = count_ways(n - 1)
  # if we subtract 3, we are left with 'n-3'
  subtract3 = count_ways(n - 3)
  # if we subtract 4, we are left with 'n-4'
  subtract4 = count_ways(n - 4)

  return subtract1 + subtract3 + subtract4


def main():

  print(count_ways(4))
  print(count_ways(5))
  print(count_ways(6))


main()

