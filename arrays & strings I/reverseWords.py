




''' (Reverse Traversal [E]) Given a sentence, reverse the words of the sentence. 
For example, "i live in a house" becomes "house a in live i". '''

def reverseWords(s):
    
    currentWordEnd = len(s)
    wordList = []
    
    for i in reversed(range(len(s))):
        if s[i] == ' ':
            # not empty, add a space
            if len(wordList) > 0: 
                wordList.append(' ')

            wordList.append(s[i + 1: currentWordEnd])
            currentWordEnd = i
    
    # add first word
    firstWord = s[:currentWordEnd]
    if len(wordList) > 0:
        wordList.append(' ')
    wordList.append(firstWord)

    return ''.join(wordList)


print(reverseWords('Ball Is Life'))


# Output: Life is Ball
# Time: O(n) Space: O(n)




