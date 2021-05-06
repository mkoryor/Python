


"""

Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). 
In an increasing subsequence, all the elements are in increasing order (from 
lowest to highest).

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LIS is {2,3,6,10,12}.
Example 1:

Input: {-4,10,3,7,15}
Output: 4
Explanation: The LIS is {-4,3,7,15}.
"""


# Time: O(N^2) Space: O(N)
def find_LIS_length(nums):
  n = len(nums)
  dp = [[-1 for _ in range(n+1)] for _ in range(n)]
  return find_LIS_length_recursive(dp, nums, 0, -1)


def find_LIS_length_recursive(dp, nums, currentIndex, previousIndex):
  if currentIndex == len(nums):
    return 0

  if dp[currentIndex][previousIndex + 1] == -1:
    # include nums[currentIndex] if it is larger than the last included number
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
      c1 = 1 + find_LIS_length_recursive(dp, nums, currentIndex + 1, currentIndex)

    c2 = find_LIS_length_recursive(
      dp, nums, currentIndex + 1, previousIndex)
    dp[currentIndex][previousIndex + 1] = max(c1, c2)

  return dp[currentIndex][previousIndex + 1]


def main():
  print(find_LIS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LIS_length([-4, 10, 3, 7, 15]))


main()