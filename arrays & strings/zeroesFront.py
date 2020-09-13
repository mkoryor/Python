



'''(Partitioning Arrays): You are given an array of integers. 
Rearrange the array so that all zeroes are at the beginning of the array.
For example, [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]'''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def zeroes_front(arr):
    
    # pointer to replace zeroes to front
    write_index = 0
    i = 0

    while i <= len(arr) - 1:
        if arr[i] == 0:
            swap(arr, i, write_index)
            write_index += 1
        i += 1
    
    return arr

print(zeroes_front([4,2,0,1,0,3,0]))

# Output: O(n)
# Time: O(n) Space: O(1)




