




"""
Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). 
In a palindromic subsequence, elements read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by 
deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: "abdbca"
Output: 5
Explanation: LPS is "abdba".
Example 2:

Input: = "cddpd"
Output: 3
Explanation: LPS is "ddd".
"""


# Time: O(N^2) Space: O(N^2)
def find_LPS_length(st):
  n = len(st)
  # dp[i][j] stores the length of LPS from index 'i' to index 'j'
  dp = [[0 for _ in range(n)] for _ in range(n)]

  # every sequence with one element is a palindrome of length 1
  for i in range(n):
    dp[i][i] = 1

  for startIndex in range(n - 1, -1, -1):
    for endIndex in range(startIndex + 1, n):
      # case 1: elements at the beginning and the end are the same
      if st[startIndex] == st[endIndex]:
        dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
      else:  # case 2: skip one element either from the beginning or the end
        dp[startIndex][endIndex] = max(
          dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

  return dp[0][n - 1]


def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()

