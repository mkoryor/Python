




"""

1.[H] BigInteger Addition: You are given a number in the form of an array. 
Each digit in the array represents a digit in the number. For example, 100 -> [1,0,0]. 
Perform addition of 2 such number arrays. For example,
"""


def resizeWithZeroes(a, size):
    if size < len(a):
        print('can not expand size')
    
    result = [0] * size
    aIndex = len(a) - 1
    resIndex = len(result) - 1

    while aIndex >= 0:
        result[resIndex] = a[aIndex]
        resIndex -= 1
        aIndex -= 1
    
    return result

def add(a, b):

    larger = a if len(a) > len(b) else b
    smaller = b if larger == a else a
    resizer = resizeWithZeroes(smaller, len(larger))
    res = [0] * (1 + len(larger))
    carry = 0

    for i in range(len(larger) -1, -1, -1):
        curr_sum = larger[i] + resizer[i] + carry
        carry = curr_sum // 10
        res[i + 1] = curr_sum % 10
    
    res[0] = carry
    return res

print(add([1,2,1,2], [2]))


# Output: [0, 1, 2, 1, 4]

# Time: O(n) Space: O(n)






