

"""

Given two strings ‘s1’ and ‘s2’, find the length of the longest substring which 
is common in both the strings.

Example 1:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".
Example 2:

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 3
Explanation: The longest common substring is "ssp".
"""


# Time: O(3^m+n) Space: O(m + n)
def find_LCS_length(s1, s2):
  return find_LCS_length_recursive(s1, s2, 0, 0, 0)


def find_LCS_length_recursive(s1, s2, i1, i2, count):
  if i1 == len(s1) or i2 == len(s2):
    return count

  if s1[i1] == s2[i2]:
    count = find_LCS_length_recursive(s1, s2, i1 + 1, i2 + 1, count + 1)

  c1 = find_LCS_length_recursive(s1, s2, i1, i2 + 1, 0)
  c2 = find_LCS_length_recursive(s1, s2, i1 + 1, i2, 0)

  return max(count, max(c1, c2))


def main():
  print(find_LCS_length("abdca", "cbda"))
  print(find_LCS_length("passport", "ppsspt"))


main()
