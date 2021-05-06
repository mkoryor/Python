


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


# Time: O(2^n) Space: O(N)
def find_LPS_length(st):
  return find_LPS_length_recursive(st, 0, len(st) - 1)


def find_LPS_length_recursive(st, startIndex, endIndex):
  if startIndex > endIndex:
    return 0

  # every sequence with one element is a palindrome of length 1
  if startIndex == endIndex:
    return 1

  # case 1: elements at the beginning and the end are the same
  if st[startIndex] == st[endIndex]:
    return 2 + find_LPS_length_recursive(st, startIndex + 1, endIndex - 1)

  # case 2: skip one element either from the beginning or the end
  c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
  c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)
  return max(c1, c2)


def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()