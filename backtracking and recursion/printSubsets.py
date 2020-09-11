


"""
(Backtracking and Recursion [M]):Technique: Permutations/Combinations using
Auxiliary BufferLevel: MediumGiven an array of integers A, print all its subsets.
For example:
Input:​ [1, 2, 3]

Output: []
        [1]
        [1, 2]
        [1, 2, 3]
        [1, 3]
        [2]
        [2, 3]
        [3]
          
"""




def printSubsetHelper(arr, temp, startIdx, tempIdx):
    print(temp[:tempIdx])

    # termination case - temp full
    if temp == len(temp):
        return 
    
    if startIdx == len(arr):
        return 

    # find candidate that go into current temp index
    for i in range(startIdx, len(arr)):
        # place item into temp
        temp[tempIdx] = arr[i]

        # recurse to next temp index
        printSubsetHelper(arr, temp, i + 1, tempIdx + 1)


def printSubsets(arr):

    temp = [0] * len(arr)
    printSubsetHelper(arr, temp, 0, 0)

printSubsets([1,2,3])



# Output: []
          [1]
          [1, 2]
          [1, 2, 3]
          [1, 3]
          [2]
          [2, 3]
          [3]
          
# Time: O(n!) factorial complexity Space: O(n) temp allocation and call stack
          




