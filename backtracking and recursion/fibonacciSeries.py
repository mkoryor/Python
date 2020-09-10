



'''
(Backtracking and Recursion [E]):  Fibonacci Series with Recursion - 
Find the Nth element of the Fibonacci series - 1,1,2,3,5,8,..

'''

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

print(fibo(3))


# Output: 3
# Time: O(2^n) Space: O(n)



