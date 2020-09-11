




'''
(Backtracking and Recursion [M]): Technique: Permutations/Combinations 
using Auxiliary BufferLevel: MediumPhone Number Mnemonics: Given an N digit 
phone number, print all the strings that canbe made from that phone number. 
Since 1 and 0 don't correspond to any characters, ignorethem.

For example:213 => AD, AE, AF, BD, BE, BF, CE, CE, CF
            456 => GJM, GJN, GJO, GKM, GKN, GKO
'''






def printWordsHelper(arr, temp, arrIdx, tempIdx):

    hashMap = {'0': '', '1':'', '2':'abc', '3': 'def',
               '4': 'ghi', '5': 'jkl', '6': 'mnop', 
               '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    # termination case
    if tempIdx >= len(temp) or arrIdx >= len(arr):
        print(temp[:tempIdx])
        return 

    # find canidates for temp position
    letters = hashMap[arr[arrIdx]]

    
    if len(letters) == 0:
        printWordsHelper(arr, temp, arrIdx + 1, tempIdx)
    
    # place candidates in temp
    for char in letters:
        temp[tempIdx] = char
        printWordsHelper(arr, temp, arrIdx + 1, tempIdx + 1)


def printWords(phoneNumber):

    temp = [0] * len(phoneNumber)
    printWordsHelper(phoneNumber, temp, 0, 0)

print(printWords('213'))



# Output: ['a', 'd']
          ['a', 'e']
          ['a', 'f']
          ['b', 'd']
          ['b', 'e']
          ['b', 'f']
          ['c', 'd']
          ['c', 'e']
          ['c', 'f']
          
Time: O(4^n) where n is size of phoneNumber Space: O(n) size of phoneNumber


    


