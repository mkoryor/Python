


'''Implementation of Binary Search that you should know well.'''

def binarySearch(arr, T):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] < T:
            low = mid + 1
        
        elif arr[mid] > T:
            high = mid - 1

        else:
            # return index of searched val
            return mid

    return -1
    
print(binarySearch([1,2,2,6,9], 9))


# Output: 4
# Time: O(logn) Space: O(1)




