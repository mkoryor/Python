


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



# Time: O(N) Space: O(N)
def count_ways(n):
  dp = [0 for x in range(n+1)]
  dp[0] = 1
  dp[1] = 1
  dp[2] = 2

  for i in range(3, n+1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

  return dp[n]


def main():

  print(count_ways(3))
  print(count_ways(4))
  print(count_ways(5))


main()
