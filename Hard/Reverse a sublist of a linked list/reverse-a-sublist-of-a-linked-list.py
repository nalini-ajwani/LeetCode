#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverseBetween(self, head, m, n):
        if not head or m == n:
            return head
        
        # Create a dummy node to handle edge cases easily
        dummy = Node(0)
        dummy.next = head
        pre = dummy
        
        # Move `pre` to the node just before the reversal starts
        for _ in range(m - 1):
            pre = pre.next
        
        # `start` will point to the first node of the segment to be reversed
        start = pre.next
        # `then` will point to the node that will be reversed
        then = start.next
        
        # Reverse the segment
        for _ in range(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next
        
        return dummy.next


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # prints the elements of linked list starting with head
    def printList(self, head):
        if head is None:
            print(' ')
            return
        curr_node = head
        while curr_node:
            print(curr_node.data,end=" ")
            curr_node=curr_node.next
        print()
    
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        inp = list(map(int,input().split())) 
        N=inp[0]
        m=inp[1]
        n=inp[2]
        
        a = LinkedList() # create a new linked list 'a'.
        nodes = list(map(int, input().strip().split()))
        for x in nodes:
            a.append(x)
            
       
        ob=Solution()
        newhead=ob.reverseBetween(a.head, m, n)
        a.printList(newhead)
# } Driver Code Ends