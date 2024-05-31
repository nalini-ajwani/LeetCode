#User function Template for python3


'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def zigzag(self, head_node):
        if not head_node or not head_node.next:
            return head_node
        
        # Initialize flag as True for the first comparison a < b
        flag = True
        current = head_node
        
        while current.next:
            if flag:  # Expect current < next
                if current.data > current.next.data:
                    # Swap data if current > next
                    current.data, current.next.data = current.next.data, current.data
            else:  # Expect current > next
                if current.data < current.next.data:
                    # Swap data if current < next
                    current.data, current.next.data = current.next.data, current.data
            
            # Move to the next pair
            current = current.next
            # Toggle the flag
            flag = not flag
        
        return head_node


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import io
import sys

# Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    # append at the end of the list
    def append(self,new_node):
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node
        self.tail = self.tail.next

# Print linked list
def print_list(head_node):
    curr_node = head_node;
    while curr_node is not None:
        print(curr_node.data, end = ' ')
        curr_node = curr_node.next
    print()

if __name__ == '__main__':
    for cases in range(int(input())):
        n = int(input())
        nodes = list(map(int,input().strip().split()))
        
        a = LinkedList()
        for x in nodes:
            a.append(Node(x))
        
        print_list(Solution().zigzag(a.head))

# } Driver Code Ends