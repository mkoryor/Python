




''' (Traverse Both Ends [E]): Given a sorted array in non-decreasing order, 
return an array of squares of each number, also in non-decreasing 
order. For example: [-4,-2,-1,0,3,5] -> [0,1,4,9,16,25]'''


def squared(n):
    return n * n
    
def arr_squares(arr):


    start = 0
    end = len(arr) - 1
    res = [0] * len(arr)
    resIndex = len(res) - 1

    while start <= end:

        if abs(arr[start]) > abs(arr[end]):
            res[resIndex] = squared(arr[start])
            start += 1
        else:
            res[resIndex] = squared(arr[end])
            end -= 1
        resIndex -= 1

    return res
            

print(arr_squares([-4,-2,-1,0,3,5]))

# Output: [0,1,4,9,16, 25]
# Time: O(n) Space: O(1)




