



'''(Binary Search Special Trick Unknown length [M]): Given a sorted array whose 
length is not known, perform binary search for a target T. Do the search in O(log(n)) time.'''

def binarySearchOverRange(arr, T, low, high):

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == T:
            return mid
        elif arr[mid] < T:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binarySearchForLastIndex(arr, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        try: 
            temp = arr[mid]
        except Exception as e:
            # mid is out of bounds, go to lower half
            high = mid - 1
            continue

        try:
            temp = arr[mid + 1]
        except Exception as e:
            # mid + 1 is out of bounds, mid is last index
            return mid
        
        # both mid and mid + 1 are inside array, mid is not last index
        low = mid + 1
    
    # this does not have end of the array
    return -1 


def findWithUnknownLength(arr, T):

    # 1,2,4,8,16,32
    high = 1 
    lastIndex = -1

    # consider putting a sanity limit here, don't go more
    # than index 1 million. 
    while True:
        try:
            temp = arr[high]
        except Exception as e:
            lastIndex = binarySearchForLastIndex(arr, high // 2, high)
            break
        high *= 2
    
    return binarySearchOverRange(arr, T, 0, lastIndex)


print(findWithUnknownLength([1,2,5,6,9,10], 5))


# Output: 2 -> lets imagine out input is unknown :)
# Time: O(logn) Space: O(1)






