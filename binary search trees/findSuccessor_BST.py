






def findSuccessor(self, node, root):

    if node.right != None:
        curr = node.right

        while curr.left != None:
            curr = curr.left
        return curr
    
    else:
        curr = root
        successor = None

        while curr != None:
            if curr.val > node.val:
                successor = curr
            
            elif curr.val < node.val:
                curr = curr.right
            elif curr == node:
                break
    
        return successor
    
    
    
    
    
    
