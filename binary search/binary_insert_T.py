





'''(Binary Search Duplicates Technique [E]) You are given a sorted array A and a target T. 
Return the index where T would be placed if inserted in order. For example,
A = [1,2,4,5,6,8] and T = 3, return index 2
A = [1,2,4,5,6,8] and T = 0, return index 0
A = [1,2,4,5,6,8] and T = 4, return index 3.'''

def binary_insert_T(arr, T):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == T:
            if mid == len(arr) - 1:
                return len(arr)
            low = mid + 1

        else:
            if mid == 0 or arr[mid - 1] <= T:
                return mid
            high = mid - 1
        
    return -1

print(binary_insert_T([1,2,4,5,6,8], 3))


# Output: 2
# Time: O(logn) Space: O(1)






