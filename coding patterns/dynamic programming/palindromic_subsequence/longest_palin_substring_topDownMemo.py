






"""
Given a string, find the length of its Longest Palindromic Substring (LPS). 
In a palindromic string, elements read the same backward and forward.

Example 1:

Input: "abdbca"
Output: 3
Explanation: LPS is "bdb".
Example 2:

Input: = "cddpd"
Output: 3
Explanation: LPS is "dpd".
Example 3:

Input: = "pqr"
Output: 1
Explanation: LPS could be "p", "q" or "r".
"""


# Time: O(N^2) Space: O(N^2)
def find_LPS_length(st):
  n = len(st)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  return find_LPS_length_recursive(dp, st, 0, n - 1)


def find_LPS_length_recursive(dp, st, startIndex, endIndex):
  if startIndex > endIndex:
    return 0

  # every string with one character is a palindrome
  if startIndex == endIndex:
    return 1

  if dp[startIndex][endIndex] == -1:
    # case 1: elements at the beginning and the end are the same
    if st[startIndex] == st[endIndex]:
      remainingLength = endIndex - startIndex - 1
      # if the remaining string is a palindrome too
      if remainingLength == find_LPS_length_recursive(dp, st, startIndex + 1, endIndex - 1):
        dp[startIndex][endIndex] = remainingLength + 2
        return dp[startIndex][endIndex]

    # case 2: skip one character either from the beginning or the end
    c1 = find_LPS_length_recursive(dp, st, startIndex + 1, endIndex)
    c2 = find_LPS_length_recursive(dp, st, startIndex, endIndex - 1)
    dp[startIndex][endIndex] = max(c1, c2)

  return dp[startIndex][endIndex]


def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()


