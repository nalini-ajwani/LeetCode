# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
  def skipMdeleteN(self, head, M, N):
    # Handle empty list or N=0 case
    if not head or N == 0:
      return head

    curr = head
    prev = None

    while curr:
      # Skip M nodes
      for _ in range(M):
        if not curr:
          return head  # Reached end of list before skipping M nodes
        prev = curr
        curr = curr.next

      # Delete N nodes
      for _ in range(N):
        if not curr:
          break  # Reached end of list before deleting N nodes
        next_node = curr.next
        del curr
        curr = next_node

      # If prev exists, connect it to the remaining list
      if prev:
        prev.next = curr

    return head



#{ 
 # Driver Code Starts
#main

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ") 
            temp = temp.next
        print("")


if __name__=='__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        m,p = list(map(int, input().strip().split()))
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        Solution().skipMdeleteN(llist.head, m, p)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends