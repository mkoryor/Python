



"""

[M] Any number will be called a happy number if, after repeatedly replacing it with 
a number equal to the sum of the square of all of its digits, leads us to number ‘1’. 
All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck 
in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:
2^2 + 3^2 = 4 + 9 = 13
1^2 + 3^2 = 1 + 9 = 10
1^2 + 0^2 = 1 + 0 = 1
​
"""


# Time: O(logn) Space: O(1)
def find_happy_number(num):
  slow, fast = num, num
  while True:
    slow = find_square_sum(slow)  # move one step
    fast = find_square_sum(find_square_sum(fast))  # move two steps
    if slow == fast:  # found the cycle
      break
  return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
  _sum = 0
  while (num > 0):
    digit = num % 10
    _sum += digit * digit
    num //= 10
  return _sum


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()

