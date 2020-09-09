

''' (E) Given an array of numbers, replace each even number with 
two of the same number. e.g, [1,2,5,6,8] -> [1,2,2,5,6,6,8,8]. Assume that
the array has enough space to accommodate the result '''

def findLastNum(arr):
    i = len(arr) - 1
    
    while i >= 0 and arr[i] == -1:
        i -= 1
    return i

def cloneEvenNumbers(arr):
    
    # helper func to grab last number
    i = findLastNum(arr)
    end = len(arr)

    while i >= 0:
        
        if arr[i] % 2 == 0:
            # add two instances if even num
            end -= 1
            arr[end] = arr[i]
            end -= 1
            arr[end] = arr[i]
        else:
            # add one instances if odd num
            end -= 1
            arr[end] = arr[i]
        i -= 1
    
    return arr


print(cloneEvenNumbers([1,2,5,6,8,-1,-1,-1]))

# Output: [1, 2, 2, 5, 6, 6, 8, 8]
# Time: O(n) Space: O(1)
