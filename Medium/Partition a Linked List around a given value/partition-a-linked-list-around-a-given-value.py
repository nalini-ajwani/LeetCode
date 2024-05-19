#User function Template for python3

"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def partition(self, head, x):
        less_head = Node(0)
        equal_head = Node(0)
        greater_head = Node(0)
        
        less = less_head
        equal = equal_head
        greater = greater_head
        
        current = head
        while current:
            if current.data < x:
                less.next = current
                less = less.next
            elif current.data == x:
                equal.next = current
                equal = equal.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        greater.next = None
        equal.next = greater_head.next
        less.next = equal_head.next
        
        return less_head.next
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.partition(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends