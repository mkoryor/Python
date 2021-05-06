

"""
Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS). 
A subsequence is considered bitonic if it is monotonically increasing and then 
monotonically decreasing.

Example 1:

Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LBS is {2,3,6,10,1}.
Example 2:

Input: {4,2,5,9,7,6,10,3,1}
Output: 7
Explanation: The LBS is {4,5,9,7,6,3,1}.
"""

# Time: O(N^2) Space: O(N)
def find_LBS_length(nums):
  n = len(nums)

  lds = [[-1 for _ in range(n+1)] for _ in range(n)]
  ldsRev = [[-1 for _ in range(n+1)] for _ in range(n)]

  maxLength = 0
  for i in range(n):
    c1 = find_LDS_length(lds, nums, i, -1)
    c2 = find_LDS_length_rev(ldsRev, nums, i, -1)
    maxLength = max(maxLength, c1 + c2 - 1)

  return maxLength

# find the longest decreasing subsequence from currentIndex till the end of the array


def find_LDS_length(dp,  nums,  currentIndex,  previousIndex):
  if currentIndex == len(nums):
    return 0

  if dp[currentIndex][previousIndex + 1] == -1:
    # include nums[currentIndex] if it is smaller than the previous number
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
      c1 = 1 + find_LDS_length(dp, nums, currentIndex + 1, currentIndex)

    # excluding the number at currentIndex
    c2 = find_LDS_length(dp, nums, currentIndex + 1, previousIndex)

    dp[currentIndex][previousIndex + 1] = max(c1, c2)

  return dp[currentIndex][previousIndex + 1]

# find the longest decreasing subsequence from currentIndex till the beginning of the array


def find_LDS_length_rev(dp,  nums,  currentIndex,  previousIndex):
  if currentIndex < 0:
    return 0

  if dp[currentIndex][previousIndex + 1] == -1:
    # include nums[currentIndex] if it is smaller than the previous number
    c1 = 0
    if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
      c1 = 1 + find_LDS_length_rev(dp, nums,
                                   currentIndex - 1, currentIndex)

    # excluding the number at currentIndex
    c2 = find_LDS_length_rev(dp, nums, currentIndex - 1, previousIndex)

    dp[currentIndex][previousIndex + 1] = max(c1, c2)
  return dp[currentIndex][previousIndex + 1]


def main():
  print(find_LBS_length([4, 2, 3, 6, 10, 1, 12]))
  print(find_LBS_length([4, 2, 5, 9, 7, 6, 10, 3, 1]))


main()