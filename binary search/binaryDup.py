


'''(Binary Search Duplicates Technique [E]): Given a sorted array that can contain duplicates, find the first 
occurrence of a target element T.For example, if A = [2,3,4,4,5,6] and T = 4, return index 2.'''

def binaryDup(arr, T):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > T or arr[mid] == T and mid > 0 and arr[mid - 1] == T:
            high = mid - 1
        
        elif arr[mid] < T:
            low = mid + 1
            
        else:
            return mid
    
    return -1

print(binaryDup([2,3,4,4,5,6], 4))


# Output: 2
# Time: O(logn) Space: O(1)



