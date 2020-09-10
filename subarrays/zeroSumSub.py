



'''(Prefix Sums Technique [M]): Given an array of integers, 
find the contiguous subarray that sums to 0. The array can contain both negative and 
positive integers.For example: Input = [2,4,-2,1,-3,5,-3], Result = [4,-2,1,-3]'''

def zeroSumSub(arr):

    if arr == None or len(arr) == 0:
        return None

    curr_sum = 0
    hashMap = {}

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == 0:
            return [0, i]
        
        if curr_sum in hashMap:
            return arr[hashMap[curr_sum] + 1: i + 1]

        hashMap[curr_sum] = i

    return None

print(zeroSumSub([2,4,-2,1,-3,5,-3]))


# Output: [4,-2,1,-3]
# Time: O(n) Space: O(n)



