

"""
Given a sequence, find the length of its longest repeating subsequence (LRS). 
A repeating subsequence will be the one that appears at least twice in the original 
sequence and is not overlapping (i.e. none of the corresponding characters in the 
repeating subsequences have the same index).

Example 1:

Input: “t o m o r r o w”
Output: 2
Explanation: The longest repeating subsequence is “or” {tomorrow}.

Example 2:

Input: “a a b d b c e c”
Output: 3
Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.
"""


# Time: O(N^2) Space: O(N)
def find_LRS_length(str):
  n = len(str)
  dp = [[-1 for _ in range(n)] for _ in range(n)]
  return find_LRS_length_recursive(dp, str, 0, 0)


def find_LRS_length_recursive(dp,  str, i1, i2):
  n = len(str)
  if i1 == n or i2 == n:
    return 0

  if dp[i1][i2] == -1:
    if i1 != i2 and str[i1] == str[i2]:
      dp[i1][i2] = 1 + find_LRS_length_recursive(dp, str, i1 + 1, i2 + 1)
    else:
      c1 = find_LRS_length_recursive(dp, str, i1, i2 + 1)
      c2 = find_LRS_length_recursive(dp, str, i1 + 1, i2)
      dp[i1][i2] = max(c1, c2)

  return dp[i1][i2]


def main():
  print(find_LRS_length("tomorrow"))
  print(find_LRS_length("aabdbcec"))
  print(find_LRS_length("fmff"))


main()
