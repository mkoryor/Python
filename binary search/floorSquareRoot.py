


'''(Binary Search Special Trick Square Root [E]): Find the square root of an 
integer X. For example, squareRoot(4) = 2. It is ok to find the integer floor 
of the square root. So squareRoot(5) or squareRoot(8) can also return 2. 
squareRoot(9) will return 3.'''

def square(x):
    return x * x

def floorSquareRoot(x):
    if x == 0:
        return 0

    if x == 1:
        return 1
    
    low = 0
    high = x // 2

    while low <= high:
        mid = low + (high - low) // 2
        if square(mid) > x:
            high = mid - 1
        elif square(mid) < x:
            if square(mid + 1) > x:
                return mid
            low = mid + 1
        else:
            return mid

    # should not happen  
    return -1
    
print(floorSquareRoot(9))


# Output: 3
# Time: O(log(x)) Space: O(1)





