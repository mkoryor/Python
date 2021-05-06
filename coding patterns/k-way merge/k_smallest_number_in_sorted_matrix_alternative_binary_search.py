


"""

[H] Given an N * NN∗N matrix where each row and column is sorted in ascending order, 
find the Kth smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.


"""

# Time: O(N * log(max - min))   Space: O(1)

def find_Kth_smallest(matrix, k):
  n = len(matrix)
  start, end = matrix[0][0], matrix[n - 1][n - 1]
  while start < end:
    mid = start + (end - start) / 2
    smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

    count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

    if count == k:
      return smaller
    if count < k:
      start = larger  # search higher
    else:
      end = smaller  # search lower

  return start
  

def count_less_equal(matrix, mid, smaller, larger):
  count, n = 0, len(matrix)
  row, col = n - 1, 0
  while row >= 0 and col < n:
    if matrix[row][col] > mid:
      # as matrix[row][col] is bigger than the mid, let's keep track of the
      # smallest number greater than the mid
      larger = min(larger, matrix[row][col])
      row -= 1
    else:
      # as matrix[row][col] is less than or equal to the mid, let's keep track of the
      # biggest number less than or equal to the mid
      smaller = max(smaller, matrix[row][col])
      count += row + 1
      col += 1

  return count, smaller, larger


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[1, 4], [2, 5]], 2)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest([[-5]], 1)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))


main()