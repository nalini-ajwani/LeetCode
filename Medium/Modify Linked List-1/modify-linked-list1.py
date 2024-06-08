#User function Template for python3

class Solution:
    def modify_the_list(self, head):
        if not head or not head.next:
            return head
        
        if not head.next.next:
            head.data, head.next.data = head.next.data - head.data, head.data
            return head
            
        slow = head
        fast = head.next.next
        track = [head]
        
        while fast and fast.next:
            slow = slow.next
            track.append(slow)
            
            if not fast.next.next:
                break
            
            fast = fast.next.next
        
        '''print(track)
        print(slow.data)
        print(fast.data)'''
        
        slow = slow.next
        if not fast.next:
            slow = slow.next
            
        while slow:
            node = track.pop(-1)
            node.data, slow.data = slow.data - node.data, node.data
            slow = slow.next
        
        
        return head
#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def modify_the_list(head):
    current = head
    while current is not None:
        if current.next is not None and current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


t = int(input())
while t > 0:
    n = int(input())
    linked_list_arr = list(map(int, input().split()))
    head = None
    temp = None
    for a in linked_list_arr:
        new_node = Node(a)
        if head is None:
            head = new_node
        else:
            temp.next = new_node
        temp = new_node
    head = Solution().modify_the_list(head)
    print_list(head)
    t -= 1
# } Driver Code Ends