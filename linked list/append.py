




"""([E]) The Append function, used to append a node to a linked list.."""
  
# Node class 
class Node: 
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 

# Linked List class contains a Node object 
class LinkedList: 
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    def append(self, new_data):

        new_node = Node(new_data)

        if self.head == None:
            self.head = new_data
            return 

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
    
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    

if __name__=='__main__': 
  
    llist = LinkedList() 
    llist.head = Node(5)
    llist.append(2)
    llist.printlist()
    
    
# Output: 5
          2
          
# Time: O(1) Space: O(1)




