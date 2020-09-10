


'''(Record and Move on Technique [E]): Given a sorted array A and a target T, 
find the target. If the target is not in the array, find the number closest to the target. 
For example, if A = [2,3,5,8,9,11] and T = 7, return 8.'''

def record(arr, mid, res, T):
    if res == -1 or abs(arr[mid] - T) < abs(arr[res] - T):
        return mid
    return res

def closestElement(arr, T):

    low = 0
    high = len(arr) - 1
    res = -1

    while low <= high:
        mid = low + (high - low) // 2

        res = record(arr, mid, res, T)
        if arr[mid] > T:
            high = mid - 1

        elif arr[mid] < T:
            low = mid + 1
        
        else:
            return mid
    return res

print(closestElement([2,3,5,8,9,11], 7))


# Output: 3
# Time: O(logn) Space: O(1)




