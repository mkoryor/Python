


"""

[M] Given an array of numbers and a number ‘K’, we need to remove ‘K’ 
numbers from the array such that we are left with maximum distinct numbers.

Example 1:

Input: [7, 3, 5, 8, 5, 3, 3], and K=2
Output: 3
Explanation: We can remove two occurrences of 3 to be left with 3 
distinct numbers [7, 3, 8], we have 
to skip 5 because it is not distinct and occurred twice. 
Another solution could be to remove one instance of '5' and '3' each to be left with three 
distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.

"""



from heapq import *


# Time: O(N * logK + KlogK) Space: O(N)

def find_maximum_distinct_elements(nums, k):
  distinctElementsCount = 0
  if len(nums) <= k:
    return distinctElementsCount

  # find the frequency of each number
  numFrequencyMap = {}
  for i in nums:
    numFrequencyMap[i] = numFrequencyMap.get(i, 0) + 1

  minHeap = []
  # insert all numbers with frequency greater than '1' into the min-heap
  for num, frequency in numFrequencyMap.items():
    if frequency == 1:
      distinctElementsCount += 1
    else:
      heappush(minHeap, (frequency, num))

  # following a greedy approach, try removing the least frequent numbers first from the min-heap
  while k > 0 and minHeap:
    frequency, num = heappop(minHeap)
    # to make an element distinct, we need to remove all of its occurrences except one
    k -= frequency - 1
    if k >= 0:
      distinctElementsCount += 1

  # if k > 0, this means we have to remove some distinct numbers
  if k > 0:
    distinctElementsCount -= k

  return distinctElementsCount


def main():

  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()



