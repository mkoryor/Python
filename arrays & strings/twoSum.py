




''' (Traverse Both Ends [E]): Two Sum Problem - Find 2 numbers in a sorted array 
that sum to X. For example, if A = [1,2,3,4,5] and X = 9, the numbers are 4 and 5. '''


def two_sum(arr, x):


    start = 0
    end = len(arr) - 1

    while start <= end:
        curr_sums = arr[start] + arr[end]

        if curr_sums < x:
            start += 1
        elif curr_sums > x:
            end -= 1
        else:
            return [start, end]
    
print(two_sum([1,2,3,4,5], 9))

# Output: [3,4]
# Time: O(n) Space: O(1)





