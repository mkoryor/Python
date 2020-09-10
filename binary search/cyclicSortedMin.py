





'''(Binary Search Special Trick Cyclic Sorted Array [E]): 1. (Level: Easy) Given a sorted array A that has 
been rotated in a cycle, find the smallest element of the array in O(log(n)) time. For example,
[1,2,4,5,7,8] rotated by 3 gives us A = [5,7,8,1,2,4] and the smallest number is 1.
[1,2,4,5,7,8] rotated by 1 gives us A = [8,1,2,4,5,7] and the smallest number is 1.'''


def cyclicSortedMin(arr):
    
    low = 0
    high = len(arr) - 1
    right = arr[-1]

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] <= right and mid == 0 or arr[mid - 1] > arr[mid]:
            return mid
        
        elif arr[mid] > right:
            low = mid + 1
        else:
            high = mid - 1
        
    return -1 

print(cyclicSortedMin([1,2,4,5,7,8]))


# Output: 0
# Time: O(logn) Space: O(1)




