




'''(Partitioning Arrays): You are given an array of integers. 
Rearrange the array so that all zeroes are at the end of the array.
For example, [4,2,0,1,0,3,0] -> [0,0,0,4,1,2,3]'''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def zeroes_back(arr):

    write_index = len(arr) - 1
    i = len(arr) - 1

    while i >= 0:
        if arr[i] == 0:
            swap(arr, i, write_index)
            write_index -= 1
        i -= 1
    
    return arr

print(zeroes_back([4,2,0,1,0,3,0]))

# Output: [4,2,3,1,0,0,0]
# Time: O(n) Space: O(1)


