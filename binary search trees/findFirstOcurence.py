



def findFirstOccurence(self, root, T):
    current = root
    result = None

    while current != None:
        if current.val > T:
            current = current.left
        elif current.val < T:
            current = current.right

        else:
            result = current
            current = current.left
            
    return result
    
    
    
