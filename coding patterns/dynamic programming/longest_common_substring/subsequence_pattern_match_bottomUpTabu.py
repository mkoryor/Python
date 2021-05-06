

"""
Given a string and a pattern, write a method to count the number of 
times the pattern appears in the string as a subsequence.

Example 1: Input: string: “baxmx”, pattern: “ax”
Output: 2
Explanation: {baxmx, baxmx}.

Example 2:

Input: string: “tomorrow”, pattern: “tor”
Output: 4
Explanation: Following are the four occurences: 
{tomorrow, tomorrow, tomorrow, tomorrow}.
"""

# Time: O(m * n) Space: O(m * n)
def find_SPM_count(str, pat):
  strLen, patLen = len(str), len(pat)
  # every empty pattern has one match
  if patLen == 0:
    return 1

  if strLen == 0 or patLen > strLen:
    return 0

  # dp[strIndex][patIndex] will be storing the count of SPM up to str[0..strIndex-1][0..patIndex-1]
  dp = [[0 for _ in range(patLen+1)] for _ in range(strLen+1)]

  # for the empty pattern, we have one matching
  for i in range(strLen+1):
    dp[i][0] = 1

  for strIndex in range(1, strLen+1):
    for patIndex in range(1, patLen+1):
      if str[strIndex - 1] == pat[patIndex - 1]:
        dp[strIndex][patIndex] = dp[strIndex - 1][patIndex - 1]
      dp[strIndex][patIndex] += dp[strIndex - 1][patIndex]

  return dp[strLen][patLen]


def main():
  print(find_SPM_count("baxmx", "ax"))
  print(find_SPM_count("tomorrow", "tor"))

main()