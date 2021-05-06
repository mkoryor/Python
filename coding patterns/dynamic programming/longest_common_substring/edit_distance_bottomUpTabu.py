


"""
Given strings s1 and s2, we need to transform s1 into s2 by deleting, 
inserting, or replacing characters. Write a function to calculate the 
count of the minimum number of edit operations.

Example 1:

Input: s1 = "bat"
       s2 = "but"
Output: 1
Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.
Example 2:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: We can replace first 'a' with 'c' and delete second 'c'.
"""


# Time: O(N * m) Space: O(n * m)
def find_min_operations(s1, s2):
  n1, n2 = len(s1), len(s2)
  dp = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]

  # if s2 is empty, we can remove all the characters of s1 to make it empty too
  for i1 in range(n1+1):
    dp[i1][0] = i1

  # if s1 is empty, we have to insert all the characters of s2
  for i2 in range(n2+1):
    dp[0][i2] = i2

  for i1 in range(1, n1+1):
    for i2 in range(1, n2+1):
      # If the strings have a matching character, we can recursively match for the remaining lengths
      if s1[i1 - 1] == s2[i2 - 1]:
        dp[i1][i2] = dp[i1 - 1][i2 - 1]
      else:
        dp[i1][i2] = 1 + min(dp[i1 - 1][i2],  # delete
                             min(dp[i1][i2 - 1],  # insert
                                 dp[i1 - 1][i2 - 1]))  # replace

  return dp[n1][n2]


def main():
  print(find_min_operations("bat", "but"))
  print(find_min_operations("abdca", "cbda"))
  print(find_min_operations("passpot", "ppsspqrt"))


main()


