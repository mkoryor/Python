




"""

1.[H] BigInteger Multiplication: You are given a number in the form of an array. 
Each digit in the array represents a digit in the number. For example, 100 -> [1,0,0]. 
Perform multiplication of 2 such number arrays. For example,

[2,0,5,0] * [2] = [4,1,0,0]
[9,9] * [1] = [9,9]

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


def multiply(a, b):

    res = [0]
    zeroCount = 0 # number of zeroes to add to the end
    for i in range(len(a) - 1, - 1, - 1):
        product = [0] * ( 1 + len(b) + zeroCount)
        carry = 0
        for j in range(len(b) - 1, -1, -1):
            p = a[i] + b[j] + carry
            carry = p // 10
            product[j + 1] = p % 10

        product[0] = carry
        res = add(res, product)
        zeroCount += 1
    
    return res

print(multiply([1,2,3], [2]))




# Output: [0, 0, 3, 4, 5]

# Time: O(m * n) Space: O(m + n)





