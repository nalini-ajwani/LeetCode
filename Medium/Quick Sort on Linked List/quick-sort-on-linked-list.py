#User function Template for python3

def quickSort(head):
    if not head or not head.next:
        return head

    # Partitioning the list and getting new heads for the three lists
    smaller_head, equal_head, greater_head = partition(head)

    # Recursively sorting the smaller and greater lists
    smaller_sorted = quickSort(smaller_head)
    greater_sorted = quickSort(greater_head)

    # Combining the results
    return concatenate(smaller_sorted, equal_head, greater_sorted)

def partition(head):
    if not head:
        return None, None, None

    pivot = head.data
    smaller_head = smaller_tail = None
    equal_head = equal_tail = None
    greater_head = greater_tail = None

    current = head
    while current:
        if current.data < pivot:
            smaller_head, smaller_tail = add_node(smaller_head, smaller_tail, current)
        elif current.data == pivot:
            equal_head, equal_tail = add_node(equal_head, equal_tail, current)
        else:
            greater_head, greater_tail = add_node(greater_head, greater_tail, current)
        current = current.next

    if smaller_tail:
        smaller_tail.next = None
    if equal_tail:
        equal_tail.next = None
    if greater_tail:
        greater_tail.next = None

    return smaller_head, equal_head, greater_head

def add_node(head, tail, node):
    if not head:
        head = tail = node
    else:
        tail.next = node
        tail = node
    return head, tail

def concatenate(smaller, equal, greater):
    if not smaller:
        head = equal
    else:
        head = smaller
        tail = get_tail(smaller)
        tail.next = equal

    if not equal:
        tail = get_tail(smaller)
    else:
        tail = get_tail(equal)

    tail.next = greater
    return head

def get_tail(node):
    while node and node.next:
        node = node.next
    return node




#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

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
        
def nodeID(head,dic):
    while head:
        dic[head.data].append(id(head))
        head=head.next
        


def printList(head,dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().split()]
        
        ll=Llist()
        tail=None
        
        for nodeData in arr:
            tail=ll.insert(nodeData,tail)
            
        dic=defaultdict(list)   # dictonary to keep data and id of node
        nodeID(ll.head,dic)     # putting data and its id
        
        resHead=quickSort(ll.head)
        printList(resHead,dic)  #verifying and printing
        print()
        
    
    
# } Driver Code Ends