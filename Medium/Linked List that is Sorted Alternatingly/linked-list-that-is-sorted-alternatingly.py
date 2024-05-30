#User function Template for python3


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class Solution:
    def sort(self, h1):
        if not h1 or not h1.next:
            return h1
        
        # Function to reverse the linked list
        def reverse(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        # Function to merge two sorted linked lists
        def merge(list1, list2):
            dummy = Node(0)
            current = dummy
            while list1 and list2:
                if list1.data <= list2.data:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            
            if list1:
                current.next = list1
            if list2:
                current.next = list2

            return dummy.next

        # Split the list into two lists: ascending and descending
        ascending = h1
        descending = h1.next
        asc_current = ascending
        desc_current = descending

        while asc_current and asc_current.next and desc_current and desc_current.next:
            asc_current.next = asc_current.next.next
            desc_current.next = desc_current.next.next
            asc_current = asc_current.next
            desc_current = desc_current.next
        
        if asc_current:
            asc_current.next = None
        if desc_current:
            desc_current.next = None

        # Reverse the descending list
        descending = reverse(descending)

        # Merge the two lists
        sorted_head = merge(ascending, descending)

        return sorted_head



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n1=int(input())
        arr1=[int(x) for x in input().split()]
        ll1=Llist()
        tail=None
        for nodeData in arr1:
            tail=ll1.insert(nodeData,tail)
            
        
        ob = Solution()
        resHead=ob.sort(ll1.head)
        printList(resHead)
        print()
        
    
    
# } Driver Code Ends