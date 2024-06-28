#User function Template for python3

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

#Function that constructs BST from its preorder traversal.
def Bst(pre, size) -> Node:
    #code here
    def build_bst(preorder, lower_bound, upper_bound):
        nonlocal index
        
        if index >= size or preorder[index] < lower_bound or preorder[index] > upper_bound:
            return None
        
        root = Node(preorder[index])
        index += 1
        
        root.left = build_bst(preorder, lower_bound, root.data - 1)
        root.right = build_bst(preorder, root.data + 1, upper_bound)
        
        return root
    
    index = 0
    return build_bst(pre, float('-inf'), float('inf'))



#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None


def postOrd(root):
    if not root:
        return
    postOrd(root.left)
    postOrd(root.right)
    print(root.data, end=' ')


if __name__ == '__main__':
    t = int(input())

    for _tcs in range(t):
        size = int(input())
        pre = [int(x) for x in input().split()]

        root = Bst(pre, size)

        postOrd(root)
        print()

# } Driver Code Ends