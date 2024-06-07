#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        # Code here
        def is_vowel(char):
            return char in 'aeiou'
            
        vowel_dummy = Node(0)
        cons_dummy = Node(0)
        vowel_tail = vowel_dummy
        cons_tail = cons_dummy
        
        curr = head
        while curr:
            if is_vowel(curr.data):
                vowel_tail.next = curr
                vowel_tail = vowel_tail.next
                
            else:
                cons_tail.next = curr
                cons_tail = cons_tail.next
            
            curr = curr.next
            
        cons_tail.next = None
        vowel_tail.next = cons_dummy.next
        return vowel_dummy.next


#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, val):
        self.data = val
        self.next = None


# Linked List Class
class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends