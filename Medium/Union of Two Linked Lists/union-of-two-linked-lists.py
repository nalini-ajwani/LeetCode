#User function Template for python3
class Solution:
    def union(self, head1,head2):
        arr=[]
        temp1=head1
        while temp1:
            arr.append(temp1.data)
            temp1=temp1.next
            
        temp2=head2
        while temp2:
            arr.append(temp2.data)
            temp2=temp2.next
            
        arr=sorted(list(set(arr)))
        new_head=Node(arr[0])
        a=new_head
        for i in range(1,len(arr)):
            new_head.next=Node(arr[i])
            new_head=new_head.next
        return a

 
        
        
        # code here
        # return head of resultant linkedlist


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
    for _ in range(int(input())):
        
        n1 = int(input())
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        n2 = int(input())
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        ob = Solution()
        printList(ob.union(ll1.head,ll2.head))
        print()

# } Driver Code Ends