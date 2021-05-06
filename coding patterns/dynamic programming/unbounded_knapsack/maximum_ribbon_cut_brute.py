

"""

We are given a ribbon of length ‘n’ and a set of possible ribbon lengths. 
Now we need to cut the ribbon into the maximum number of pieces that comply 
with the above-mentioned possible lengths. Write a method that will return the 
count of pieces.

Example 1:

n: 5
Ribbon Lengths: {2,3,5}
Output: 2
Explanation: Ribbon pieces will be {2,3}.
Example 2:

n: 7
Ribbon Lengths: {2,3}
Output: 3
Explanation: Ribbon pieces will be {2,2,3}.
"""



import math

# Time: O(2^L+T) Space: O(L + T)
def count_ribbon_pieces(ribbonLengths, total):
  maxPieces = count_ribbon_pieces_recursive(ribbonLengths, total, 0)
  return -1 if maxPieces == -math.inf else maxPieces


def count_ribbon_pieces_recursive(ribbonLengths, total, currentIndex):
  # base check
  if total == 0:
    return 0

  n = len(ribbonLengths)
  if n == 0 or currentIndex >= n:
    return -math.inf

  # recursive call after selecting the ribbon length at the currentIndex
  # if the ribbon length at the currentIndex exceeds the total, we shouldn't process this
  c1 = -math.inf
  if ribbonLengths[currentIndex] <= total:
    result = count_ribbon_pieces_recursive(
      ribbonLengths, total - ribbonLengths[currentIndex], currentIndex)
    if result != -math.inf:
      c1 = result + 1

  # recursive call after excluding the ribbon length at the currentIndex
  c2 = count_ribbon_pieces_recursive(ribbonLengths, total, currentIndex + 1)
  return max(c1, c2)


def main():
  print(count_ribbon_pieces([2, 3, 5], 5))
  print(count_ribbon_pieces([2, 3], 7))
  print(count_ribbon_pieces([3, 5, 7], 13))
  print(count_ribbon_pieces([3, 5], 7))


main()