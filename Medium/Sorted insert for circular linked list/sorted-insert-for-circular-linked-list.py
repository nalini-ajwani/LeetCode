#User function Template for python3

'''
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  '''
class Solution:
    def sortedInsert(self, head, data):
        # Create a new node
        new_node = Node(data)
        
        # If the list is empty, make the new node as head and point to itself
        if head is None:
            new_node.next = new_node
            return new_node
        
        # If the new node data is less than the head, insert it before the head
        elif data < head.data:
            current = head
            while current.next != head:
                current = current.next
            current.next = new_node
            new_node.next = head
            return new_node
        
        # Find the position to insert the new node
        else:
            current = head
            while current.next != head and current.next.data < data:
                current = current.next
            
            # Insert the new node
            new_node.next = current.next
            current.next = new_node
            return head
                

#{ 
 # Driver Code Starts
#contributed by RavinderSinghPB
class Node: 
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
        self.last=None
  
    # Function to insert a new node  
    def push(self, data):
        if not self.head:
            nn=Node(data)
            self.head=nn
            self.last=nn
            nn.next=nn
            return
        nn=Node(data)
        nn.next=self.head
        self.last.next=nn
        self.last=nn 
  

# Utility function to print the linked LinkedList

def printList(head):
    if not head:
        return
    temp = head 
    print (temp.data,end=' ') 
    temp = temp.next
    while(temp != head): 
        print (temp.data,end=' ') 
        temp = temp.next
  
    
if __name__ =='__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        data=int(input())

        cll=LinkedList()
        for e in arr:
            cll.push(e)
            
        reshead=Solution().sortedInsert(cll.head,data)
        printList(reshead)
        print()
        


# } Driver Code Ends