

"""
Given a stair with ‘n’ steps, implement a method to count how many 
possible ways are there to reach the top of the staircase, given that, 
at every step you can either take 1 step, 2 steps, or 3 steps.

Example 1:

Number of stairs (n) : 3
Number of ways = 4
Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3} 
Example 2:

Number of stairs (n) : 4
Number of ways = 7
Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1}, 
{2,2}, {1,3}, {3,1}

"""

# Time: O(N) Space: O(1)
def count_ways(n):
  if n < 2:
    return 1
  if n == 2:
    return 2
  n1, n2, n3 = 1, 1, 2
  for i in range(3, n+1):
    n1, n2, n3 = n2, n3, n1+n2+n3
  return n3


def main():

  print(count_ways(3))
  print(count_ways(4))
  print(count_ways(5))


main()
