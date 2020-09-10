




'''(Sliding Window using Two Pointers [M]): Given a String, find the longest 
substring with unique characters. For example: "whatwhywhere" --> "atwhy" '''

def longestSubStringUnique(s):
    
    start, end = 0, 0
    maxlen = 1
    hashMap = {}
    hashMap[s[0]] = 0
    res = [0, 0]
    

    while end < len(s) - 1:
        # expand end pointer
        end += 1
        toAdd = s[end]

        if toAdd in hashMap and hashMap.get(toAdd) >= start:
            start = hashMap.get(toAdd) + 1
        
        # set toAdd to end index position
        hashMap[toAdd] = end
    
        # update result
        if end - start + 1 > maxlen:
            maxlen = end - start + 1
            res = s[start: end + 1]

    return res

print(longestSubStringUnique('whatwhywhere'))

# Output: 'atwhy'
# Time: O(n) Space: O(size of char set) ->  O(1)



