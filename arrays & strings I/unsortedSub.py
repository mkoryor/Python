




''' (Traverse Both Ends [M]):Given an array of integers, find the continuous 
subarray, which when sorted, results in the entire array being sorted.For example: 
A = [0,2,3,1,8,6,9], result is the subarray [2,3,1,8,6]'''

def unsorted_sub(arr):

    start = 0
    end = len(arr) - 1

    # find start of dip
    while start <= len(arr) - 1:
        if arr[start + 1] < arr[start]:
            break
        start += 1

    # no dip found 
    if start == len(arr) - 1:
        return None

    # find bump from end
    while end >= 0:
        if arr[end - 1] > arr[end]:
            break
        end -= 1

    # subarray from arr[start:end + 1]
    sub = arr[start: end + 1]

    # find max and min in arr
    max_val = min(sub)
    min_val = max(sub)
    k = start 

    while k <= end:
        if arr[k] > max_val:
            max_val = arr[k]

        if arr[k] < min_val:
            min_val = arr[k]
        k += 1

    # expand start end end outward
    while start > 0 and arr[start - 1] > min_val:
        start -= 1
    while end < len(arr) - 1 and arr[end + 1] < max_val:
        end += 1

    return arr[start: end + 1]

print(unsorted_sub([0,2,3,1,8,6,9]))


# Output: [2,3,1,8,6]
# Time: O(n) Space: O(1)


