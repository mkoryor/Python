



"""
[E] Given an array of n-1n−1 integers in the range from 11 to nn, 
find the one number that is missing from the array.

Example:

Input: 1, 5, 2, 6, 4
Answer: 3
"""


# answer ok, but might overflow when adding

# Time: O(n) Space: O(1) 
def find_missing_number(arr):
  n = len(arr) + 1
  # find sum of all numbers from 1 to n.
  s1 = 0
  for i in range (1, n+1):
    s1 += i

  # subtract all numbers in input from sum.
  for i in arr:
    s1 -= i
  
  # s1, now, is the missing number
  return s1

def main():
  arr = [1, 5, 2, 6, 4] 
  print('Missing number is:' + str(find_missing_number(arr)))

main()













