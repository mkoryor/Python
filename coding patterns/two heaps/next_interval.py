

"""

[H] Given an array of intervals, find the next interval of each interval. 
In a list of intervals, for an interval 'i' its next interval 'j'
will have the smallest ‘start’ greater than or equal to the 'end' of ‘i'.

Write a function to return an array containing indices of the next 
interval of each input interval. If there is no next interval of a 
given interval, return -1. It is given that none of the intervals have 
the same start point.

Example 1:

Input: Intervals [[2,3], [3,4], [5,6]]
Output: [1, 2, -1]
Explanation: The next interval of [2,3] is [3,4] having index '1'. 
Similarly, the next interval of [3,4] is [5,6] having index '2'. 
There is no next interval for [5,6] hence we have '-1'.

"""


from heapq import *



# Time: O(NlogN) Space: O(N)
class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
  n = len(intervals)

  # heaps for finding the maximum start and end
  maxStartHeap, maxEndHeap = [], []

  result = [0 for x in range(n)]
  for endIndex in range(n):
    heappush(maxStartHeap, (-intervals[endIndex].start, endIndex))
    heappush(maxEndHeap, (-intervals[endIndex].end, endIndex))

  # go through all the intervals to find each interval's next interval
  for _ in range(n):
    # let's find the next interval of the interval which has the highest 'end'
    topEnd, endIndex = heappop(maxEndHeap)
    result[endIndex] = -1  # defaults to - 1
    if -maxStartHeap[0][0] >= -topEnd:
      topStart, startIndex = heappop(maxStartHeap)
      # find the the interval that has the closest 'start'
      while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
        topStart, startIndex = heappop(maxStartHeap)
      result[endIndex] = startIndex
      # put the interval back as it could be the next interval of other intervals
      heappush(maxStartHeap, (topStart, startIndex))

  return result


def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()
