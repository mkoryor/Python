

"""

[E] 2. Bottom-up with Tabulation #
Tabulation is the opposite of the top-down approach and avoids recursion. In this approach, 
we solve the problem “bottom-up” (i.e. by solving all the related sub-problems first). 
This is typically done by filling up an n-dimensional table. 
Based on the results in the table, the solution to the top/original problem is then computed.

Tabulation is the opposite of Memoization, as in Memoization we solve 
the problem and maintain a map of already solved sub-problems. In other words, 
in memoization, we do it top-down in the sense that we solve the top problem first 
(which typically recurses down to solve the sub-problems).

Write a function to calculate the nth Fibonacci number.

Fibonacci numbers are a series of numbers in which each number is the sum of the 
two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

Mathematically we can define the Fibonacci numbers as:
Fib(n) = Fib(n-1) + Fib(n-2), for n > 1
Given that: Fib(0) = 0, and Fib(1) = 1
"""



# Time: O(N) Space: O(1)
def calculateFibonacci(n):
  dp = [0, 1]
  for i in range(2, n + 1):
    dp.append(dp[i - 1] + dp[i - 2])

  return dp[n]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()
