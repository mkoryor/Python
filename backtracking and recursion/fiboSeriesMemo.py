


'''
(Backtracking and Recursion):  Fibonacci Series with Memoization - 
Find the Nth element of the Fibonacci series - 1,1,2,3,5,8,..

'''

def fibo_help(n, memo = {}):
    if n <= 2:
        return 1
    
    if n in memo:
        return memo[n]
    
    res = fibo_help(n - 1, memo) + fibo_help(n - 2, memo)
    memo[n] = res
    return res

def fibo(n):
    return fibo_help(n)

print(fibo(10))
    


# Output: 55
# Time: O(n) Space: O(n)



