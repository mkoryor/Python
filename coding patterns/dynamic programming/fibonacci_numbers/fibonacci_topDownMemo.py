


"""
[E] 1. Top-down with Memoization #
In this approach, we try to solve the bigger problem by recursively finding the solution 
to smaller sub-problems. Whenever we solve a sub-problem, we cache its result so that we 
don’t end up solving it repeatedly if it’s called multiple times. Instead, we can just 
return the saved result.This technique of storing the results of already solved 
subproblems is called Memoization.

Write a function to calculate the nth Fibonacci number.
Fibonacci numbers are a series of numbers in which each number is the 
sum of the two preceding numbers. First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, …

Mathematically we can define the Fibonacci numbers as:
Fib(n) = Fib(n-1) + Fib(n-2), for n > 1
Given that: Fib(0) = 0, and Fib(1) = 1
"""

# Time: O(N) Space: O(1)
def calculateFibonacci(n):
  memoize = [-1 for x in range(n+1)]
  return calculateFibonacciRecur(memoize, n)


def calculateFibonacciRecur(memoize, n):
  if n < 2:
    return n

  # if we have already solved this subproblem, simply return the result from the cache
  if memoize[n] >= 0:
    return memoize[n]

  memoize[n] = calculateFibonacciRecur(
    memoize, n - 1) + calculateFibonacciRecur(memoize, n - 2)
  return memoize[n]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()


