#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self,head1,head2):
        ptr1 = head1
        ptr2 = head2
        
        new_head = None
        new_tail = None
        
        while ptr1 and ptr2:
            if ptr1.data == ptr2.data:
                if new_head is None:
                    new_head = Node(ptr1.data)
                    new_tail = new_head
                else:
                    new_tail.next = Node(ptr1.data)
                    new_tail = new_tail.next
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            elif ptr1.data < ptr2.data:
                ptr1 = ptr1.next
            else:
                ptr2 = ptr2.next
        
        return new_head



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1,n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        ob = Solution()
        result = ob.findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends