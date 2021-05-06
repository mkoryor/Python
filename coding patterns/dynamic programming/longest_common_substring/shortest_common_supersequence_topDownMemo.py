


"""
Given two sequences ‘s1’ and ‘s2’, write a method to find the length 
of the shortest sequence which has ‘s1’ and ‘s2’ as subsequences.

Example 2:

Input: s1: "abcf" s2:"bdcf" 
Output: 5
Explanation: The shortest common super-sequence (SCS) is "abdcf". 
Example 2:

Input: s1: "dynamic" s2:"programming" 
Output: 15
Explanation: The SCS is "dynprogrammicng". 
"""

# Time: O(n * m) Space: O(n * m)
def find_SCS_length(s1, s2):
  dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
  return find_SCS_length_recursive(dp, s1, s2, 0, 0)


def find_SCS_length_recursive(dp, s1, s2,  i1,  i2):
  n1, n2 = len(s1), len(s2)
  # if we have reached the end of a string, return the remaining length of the
  # other string, as in this case we have to take all of the remaining other string
  if i1 == n1:
    return n2 - i2
  if i2 == n2:
    return n1 - i1

  if dp[i1][i2] == -1:
    if s1[i1] == s2[i2]:
      dp[i1][i2] = 1 + \
                   find_SCS_length_recursive(dp, s1, s2, i1 + 1, i2 + 1)
    else:
      length1 = 1 + find_SCS_length_recursive(dp, s1, s2, i1, i2 + 1)
      length2 = 1 + find_SCS_length_recursive(dp, s1, s2, i1 + 1, i2)
      dp[i1][i2] = min(length1, length2)

  return dp[i1][i2]


def main():
  print(find_SCS_length("abcf", "bdcf"))
  print(find_SCS_length("dynamic", "programming"))


main()
