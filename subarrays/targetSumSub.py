



'''(Prefix Sums Technique [M]): Given an array of positive and negative 
integers, find a subarray whose sum equals X.For example: 
Input = [2,4,-2,1,-3,5,-3], X = 5 --> Result = [2,4,-2,1]
'''

def targetSumSub(arr, target):

    curr_sum = 0
    hashMap = {}

    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if curr_sum == target:
            # get sub that equals target
            return arr[0:i + 1]
        
        if curr_sum - target in hashMap:
            return arr[hashMap[curr_sum - target] + 1, i]
        
        hashMap[curr_sum] = i

    # not found
    return None 

print(targetSumSub([2,4,-2,1,-3,5,-3], 5))


# Output: [2,4,-2,1]
# Time: O(n) Space: O(n)




