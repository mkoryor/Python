



'''(Kadane's Algorithm): Given an array of integers, find the contiguous subarray 
(with at least 1 element) with the maximum sum. The array can contain both negative 
and positive integers. For example:  [1,2,-1,2,-3,2,-5]  -> first 4 elements have the 
largest sum. Return (0,3)'''

def maximumSubSum(arr):
    
    maxSum = arr[0]
    maxEndingHere = arr[0]

    for i in range(len(arr)):
        maxEndingHere = max(maxEndingHere + arr[i], arr[i])
        maxSum = max(maxSum, maxEndingHere)
        
    return maxSum

print(maximumSubSum([1,2,-1,2,-3,2, -5]))


# Output: 5 - sub = [1,2,-1,2]
# Time: O(n) Space: O(1)





