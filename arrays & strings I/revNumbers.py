




''' (Traverse Both Ends [E]) Video 1: (Level: Easy) Reverse the order of elements
in an array. For example, A = [1,2,3,4,5,6], Output = [6,5,4,3,2,1] '''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def rev(arr):
    
    start = 0
    end = len(arr) - 1

    while start <= end:
        swap(arr, start, end)
        start += 1
        end -= 1
    
    return arr

print(rev([1,2,3,4,5,6]))

# Output: [6,5,4,3,2,1]
# Time: O(n) Space: O(1)


