

"""
Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.

Example 1:

Input: "abdbca"
Output: 3
Explanation: Palindrome pieces are "a", "bdb", "c", "a".
Example 2:

Input: = "cddpd"
Output: 2
Explanation: Palindrome pieces are "c", "d", "dpd".
"""




# Time: O(N^2) Space: O(N^2)
def find_MPP_cuts(st):
  n = len(st)
  # isPalindrome[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
  isPalindrome = [[False for _ in range(n)] for _ in range(n)]

  # every string with one character is a palindrome
  for i in range(n):
    isPalindrome[i][i] = True

  # populate isPalindrome table
  for startIndex in range(n-1, -1, -1):
    for endIndex in range(startIndex+1, n):
      if st[startIndex] == st[endIndex]:
        # if it's a two character string or if the remaining string is a palindrome too
        if endIndex - startIndex == 1 or isPalindrome[startIndex + 1][endIndex - 1]:
          isPalindrome[startIndex][endIndex] = True

  # now lets populate the second table, every index in 'cuts' stores the minimum cuts needed
  # for the substring from that index till the end
  cuts = [0 for _ in range(n)]
  for startIndex in range(n-1, -1, -1):
    minCuts = n  # maximum cuts
    for endIndex in range(n-1, startIndex-1, -1):
      if isPalindrome[startIndex][endIndex]:
        # we can cut here as we got a palindrome
        # also we don't need any cut if the whole substring is a palindrome
        minCuts = 0 if endIndex == n-1 else min(minCuts, 1 + cuts[endIndex + 1])

    cuts[startIndex] = minCuts

  return cuts[0]


def main():
  print(find_MPP_cuts("abdbca"))
  print(find_MPP_cuts("cdpdd"))
  print(find_MPP_cuts("pqr"))
  print(find_MPP_cuts("pp"))
  print(find_MPP_cuts("madam"))


main()