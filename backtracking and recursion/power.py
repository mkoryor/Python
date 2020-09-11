



'''
(Recursion):  Power Function: Implement a function to 
calculate xn. Both x and n can be positive/negative and overflow doesn't happen. 
Try doing it in O(log(n)) time. '''


def positivePower(x, power):
    if power == 0:
        return 1
    if power == 1:
        return x
    
    halfpower = positivePower(x, power // 2)
    if power % 2 == 0:
        return halfpower ** 2
    else:
        return x * halfpower ** 2

def power(x, power):

    res = positivePower(abs(x), abs(power))

    # handle negative power
    if power < 0:
        res = 1 // res
    
    # handle negative x
    if x < 0 and power % 2 != 0:
        res = -1 * res
    
    return res

print(power(4, 2))



# Output: 16
# Time: O(logn) Space: O(logn) on call stack



