

"""Given a number sequence, find the length of its Longest Alternating Subsequence (LAS). 
A subsequence is considered alternating if its elements are in alternating order.

A three element sequence (a1, a2, a3) will be an alternating sequence if its 
elements hold one of the following conditions:

{a1 > a2 < a3 } or { a1 < a2 > a3}. 
Example 1:

Input: {1,2,3,4}
Output: 2
Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}
Example 2:

Input: {3,2,1,4}
Output: 3
Explanation: The LAS are {3,2,4} and {2,1,4}.
"""

# Time; O(2^n) Space: O(N)
def find_LAS_length(nums):
  # we have to start with two recursive calls, one where we will consider that the first element is
  # bigger than the second element and one where the first element is smaller than the second element
  return max(find_LAS_length_recursive(nums, -1, 0, True), find_LAS_length_recursive(nums, -1, 0, False))


def find_LAS_length_recursive(nums,  previousIndex,  currentIndex,  isAsc):
  if currentIndex == len(nums):
    return 0

  c1 = 0
  # if ascending, the next element should be bigger
  if isAsc:
    if previousIndex == -1 or nums[previousIndex] < nums[currentIndex]:
      c1 = 1 + find_LAS_length_recursive(nums, currentIndex, currentIndex + 1, not isAsc)
  else:  # if descending, the next element should be smaller
    if previousIndex == -1 or nums[previousIndex] > nums[currentIndex]:
      c1 = 1 + find_LAS_length_recursive(nums, currentIndex, currentIndex + 1, not isAsc)
  # skip the current element
  c2 = find_LAS_length_recursive(
    nums, previousIndex, currentIndex + 1, isAsc)
  return max(c1, c2)


def main():
  print(find_LAS_length([1, 2, 3, 4]))
  print(find_LAS_length([3, 2, 1, 4]))
  print(find_LAS_length([1, 3, 2, 4]))


main()