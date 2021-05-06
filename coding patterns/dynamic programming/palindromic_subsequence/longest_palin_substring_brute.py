

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
"""


# Time: O(3^n) Space: O(N)
def find_LPS_length(st):
  return find_LPS_length_recursive(st, 0, len(st) - 1)


def find_LPS_length_recursive(st, startIndex, endIndex):
  if startIndex > endIndex:
    return 0

  # every string with one character is a palindrome
  if startIndex == endIndex:
    return 1

  # case 1: elements at the beginning and the end are the same
  if st[startIndex] == st[endIndex]:
    remainingLength = endIndex - startIndex - 1
    # check if the remaining string is also a palindrome
    if remainingLength == find_LPS_length_recursive(st, startIndex + 1, endIndex - 1):
      return remainingLength + 2

  # case 2: skip one character either from the beginning or the end
  c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
  c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)
  return max(c1, c2)


def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()
