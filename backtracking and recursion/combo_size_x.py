




'''
(Backtracking and Recursion [M]): Technique: Permutations/Combinations using 
Auxiliary BufferLevel: Given an array of integers, print all 
combinations of size X '''

def printCombosHelper(arr, temp, startIdx, tempIdx):

    # termination cases - temp full
    if tempIdx == len(temp):
        print(temp)
        return
          
    if startIdx == len(arr):
        return

    # find candidates that go into current temp index
    for i in range(startIdx, len(arr)):
        # place item into temp
        temp[tempIdx] = arr[i]

        # recurse to the next temp index
        printCombosHelper(arr, temp, i + 1, tempIdx + 1)
    

def printCombos(arr, x):
        
    temp = [0] * x
    printCombosHelper(arr, temp, 0, 0)

print(printCombos([1,2,3,4], 3))



# Output: [1,2,3]
          [1,2,4]
          [1,3,4]
          [2,3,4]

# Time: O(2^n) Space: O(x) temp and recursion stack









    

