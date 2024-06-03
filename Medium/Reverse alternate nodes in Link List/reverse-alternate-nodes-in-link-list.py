"""
  reverse alternate nodes and append at the end
  The input list will have at least one element
  Node is defined as
class Node:

	# Constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def rearrange(self, head):
        if not head or not head.next:
            return head

        alternate_head = None
        alternate_tail = None
        current = head
        index = 0

        while current and current.next:
            temp = current.next
            current.next = temp.next
            
            if not alternate_head:
                alternate_head = temp
                alternate_tail = temp
            else:
                alternate_tail.next = temp
                alternate_tail = temp

            current = current.next
            temp.next = None
            index += 1

        # Step 2: Reverse the extracted list
        prev = None
        current = alternate_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        reversed_alternate_head = prev

        # Step 3: Append the reversed list to the end of the original list
        current = head
        while current.next:
            current = current.next
        current.next = reversed_alternate_head

        return head




#{ 
 # Driver Code Starts
# Node Class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked list class contains node object
class LinkedList:
    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Code execution starts here
if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
            
        Solution().rearrange(llist.head)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends