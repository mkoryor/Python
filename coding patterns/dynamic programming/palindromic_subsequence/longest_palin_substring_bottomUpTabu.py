


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
  # dp[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
  dp = [[False for _ in range(n)] for _ in range(n)]

  # every string with one character is a palindrome
  for i in range(n):
    dp[i][i] = True

  maxLength = 1
  for startIndex in range(n - 1, -1, -1):
    for endIndex in range(startIndex + 1, n):
      if st[startIndex] == st[endIndex]:
        # if it's a two character string or if the remaining string is a palindrome too
        if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
          dp[startIndex][endIndex] = True
          maxLength = max(maxLength, endIndex - startIndex + 1)

  return maxLength


def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
