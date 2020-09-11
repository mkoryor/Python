




"""
(Backtracking and Recursion [M]):Technique: Permutations/Combinations using 
Auxiliary BufferLevel: MediumGiven an array A, print all permutations of size X.
For example,
Input:A = [1,2,3] X = 2

Output:
[1, 2]
[1, 3]
[2, 1]
[2, 3]
[3, 1]
[3, 2]
"""



def printPermHelper(arr, temp, tempIdx, insideT):
    # termination case
    if tempIdx == len(temp):
        print(temp)
        return
    
    # find candidates that go into current temp index
    for i in range(len(arr)):
        if not insideT[i]:
            # place candidate into temp index
            temp[tempIdx] = arr[i]
            insideT[i] = True

            # recurse to next temp index
            printPermHelper(arr, temp, tempIdx + 1, insideT)
            insideT[i] = False

def printPerm(arr, x):
    
    temp = [0] * x
    insideT = [False] * len(arr)
    printPermHelper(arr, temp, 0, insideT)

print(printPerm([1,2,3], 2))



# Output: [1, 2]
          [1, 3]
          [2, 1]
          [2, 3]
          [3, 1]
          [3, 2]

Time: O(2^n) factorial complexity  Space: O(n) temp allocation and stack call





