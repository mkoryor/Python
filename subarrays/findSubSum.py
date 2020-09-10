




'''(Sliding Window using Two Pointers): Given an array of positive integers, 
find the contiguous subarray that sums to a given number X.
For example, input = [1,2,3,5,2] and X=8, Result = [3,5]'''

def findSubSum(arr, x):
    
    start, end = 0, 0
    windowSum = arr[0]

    while start <= len(arr) - 1:
        # start inched forward, bring end back to start
        if start > end:
            end = start
            windowSum = arr[start]
        
        # expand to the right
        if windowSum < x:
            if end == len(arr) - 1:
                # reached end, cannot expand further
                break 

            end += 1
            windowSum += arr[end]
        
        # contract from left
        elif windowSum > x:
            windowSum -= arr[start]
            start += 1
        else:
            return arr[start:end + 1]
    

print(findSubSum([1,2,3,5,2], 8))


# Output: [2,5]
# Time: O(n) Space: O(1)





