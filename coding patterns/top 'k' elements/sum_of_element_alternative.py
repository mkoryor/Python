



"""
[M] Given an array, find the sum of all numbers between the K1’th and K2’th 
smallest elements of that array.

Example 1:

Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. 
The sum of numbers coming
between 5 and 15 is 23 (11+12).
"""



from heapq import *


# Time: O(N * logK2) Space: O(K2)
def find_sum_of_elements(nums, k1, k2):
  maxHeap = []
  # keep smallest k2 numbers in the max heap
  for i in range(len(nums)):
    if i < k2 - 1:
      heappush(maxHeap, -nums[i])
    elif nums[i] < -maxHeap[0]:
      heappop(maxHeap) # as we are interested only in the smallest k2 numbers
      heappush(maxHeap, -nums[i])

  # get the sum of numbers between k1 and k2 indices
  # these numbers will be at the top of the max heap
  elementSum = 0
  for _ in range(k2 - k1 - 1):
    elementSum += -heappop(maxHeap)

  return elementSum


def main():

  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
  print("Sum of all numbers between k1 and k2 smallest numbers: " +
        str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
