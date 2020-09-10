



'''
(Binary Special Tricks Find Peaks) Search for a Peak: A peak element in array 
A is an A[i] where its adjacent elements are less than A[i]. So, A[i - 1] < A[i] 
and A[i + 1] < A[i].Assume there are no duplicates. Also, assume that A[-1] and 
A[length] are negative infinity (-inf). So A[0] can be a peak if A[1] < A[0].

A = [1,3,4,5,2] => Peak = 5
A = [5,3,1] => Peak = 5
A = [1,3,5] => Peak = 5

'''

def find_peak(arr):
    
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        left = arr[mid - 1] if mid > 0 else 0
        right = arr[mid + 1] if mid < len(arr) - 1 else 0

        if left < arr[mid] and right > arr[mid]:
            low = mid + 1 # go right
        elif right < arr[mid] and left > arr[mid]:
            high = mid - 1 # go left
        elif right > arr[mid] and left > arr[mid]:
            high = mid - 1 # valley go either way
        else:
            return mid

    # should not happen
    return -1

print(find_peak([1,3,4,5,2]))


# Output: 3
# Time: O(logn) Space: O(1)







