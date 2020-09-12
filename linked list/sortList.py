




"""([E]): You are given a Linked List with nodes 
that have values 0, 1 or 2. Sort the linked list. For example,

Input: 1 -> 0 -> 2 -> 1 -> 2 -> 1
Output: 0 -> 1 -> 1 -> 1 -> 2 -> 2.."""
  
# Python program to sort a linked list of 0, 1 and 2 
class LinkedList(object): 
    def __init__(self): 
  
         # head of list 
         self.head = None
  
    # Linked list Node 
    class Node(object): 
        def __init__(self, data): 
            self.data = data
            self.next = None
  
    def sortList(self): 
        # initialise count of 0 1 and 2 as 0 
        count = [0, 0, 0] 
  
        ptr = self.head 
  
        # count total number of '0', '1' and '2' 
        # * count[0] will store total number of '0's 
        # * count[1] will store total number of '1's 
        # * count[2] will store total number of '2's   
        while ptr != None: 
            count[ptr.data] += 1
            ptr = ptr.next
        i = 0
        ptr = self.head 
  
        # Let say count[0] = n1, count[1] = n2 and count[2] = n3 
        # * now start traversing list from head node, 
        # * 1) fill the list with 0, till n1 > 0 
        # * 2) fill the list with 1, till n2 > 0 
        # * 3) fill the list with 2, till n3 > 0   
        while ptr != None: 
            if count[i] == 0: 
                i += 1
            else: 
                ptr.data = i 
                count[i] -= 1
                ptr = ptr.next
  
    # Utility functions 
    # Inserts a new Node at front of the list. 
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        # Put in the data 
        new_node = self.Node(new_data) 
        # 3. Make next of new Node as head 
        new_node.next = self.head 
        # 4. Move the head to point to new Node 
        self.head = new_node 

    def printList(self): 
        temp = self.head 
        while temp != None: 
            print(str(temp.data))
            temp = temp.next
        print('')
  

if __name__ == '__main__':
    llist = LinkedList() 
    llist.push(0) 
    llist.push(1) 
    llist.push(2)
    llist.push(0)

    
    print("Linked List before sorting")
    llist.printList() 
    llist.sortList() 
    print("Linked List after sorting")
    llist.printList() 
    
 
 
# Output: Linked List before sorting
          0
          2
          1
          0

          Linked List after sorting
          0
          0
          1
          2
          
          
# TIme: O(n) where n is number of nodes in linked list 
# Space: O(1) 





