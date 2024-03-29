




'''(Partitioning Arrays: Dutch Flag [M]): Dutch National Flag Problem: 
Given an array of integers A and a pivot, rearrange A in the following order:
[Elements less than pivot, elements equal to pivot, elements greater than pivot]
For example, if A = [5,2,4,4,6,4,4,3] and pivot = 4 -> result = [3,2,4,4,4,4,6,5]'''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def dutch_flag(arr, pivot):
    low_bound = 0
    high_bound = len(arr) - 1
    i = 0

    while i <= high_bound:
        if arr[i] < pivot:
            swap(arr, i, low_bound)
            low_bound += 1
            i += 1
        elif arr[i] > pivot:
            swap(arr, i, high_bound)
            # don't increment i here bc high is sorted
            high_bound -= 1
        else:
            i += 1
    return arr

print(dutch_flag([5,2,4,4,6,4,4,3], 4))


# Output: [3, 2, 4, 4, 4, 4, 6, 5]
# Time: O(n) Space: O(1)





