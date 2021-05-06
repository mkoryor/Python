

"""
Given a number sequence, find the increasing subsequence with the highest sum. 
Write a method that returns the highest sum.

Example 1:

Input: {4,1,2,6,10,1,12}
Output: 32
Explanation: The increaseing sequence is {4,6,10,12}. 
Please note the difference, as the LIS is {1,2,6,10,12} which has a sum of '31'.
Example 2:

Input: {-4,10,3,7,15}
Output: 25
Explanation: The increaseing sequences are {10, 15} and {3,7,15}.
"""


# Time: O(2^n) Space: O(n)
def find_MSIS(nums):
  return find_MSIS_recursive(nums, 0, -1, 0)


def find_MSIS_recursive(nums,  currentIndex,  previousIndex,  sum):
  if currentIndex == len(nums):
    return sum

  # include nums[currentIndex] if it is larger than the last included number
  s1 = sum
  if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
    s1 = find_MSIS_recursive(nums, currentIndex+1, currentIndex, sum + nums[currentIndex])

  # excluding the number at currentIndex
  s2 = find_MSIS_recursive(nums, currentIndex+1, previousIndex, sum)

  return max(s1, s2)


def main():
  print(find_MSIS([4, 1, 2, 6, 10, 1, 12]))
  print(find_MSIS([-4, 10, 3, 7, 15]))


main()


