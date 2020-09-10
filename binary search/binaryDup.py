


'''(Binary Search [E]): Given a sorted array that can contain duplicates, find the first 
occurrence of a target element T.For example, if A = [2,3,4,4,5,6] and T = 4, return index 2.'''

def binaryDup(arr, x):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > x or arr[mid] == x and mid > 0 and arr[mid - 1] == x:
            high = mid - 1
        
        elif arr[mid] < x:
            low = mid + 1
            
        else:
            return mid
    
    return -1

print(binaryDup([2,3,4,4,5,6], 4))


# Output: 2
# Time: O(logn) Space: O(1)



