# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        
        def inorder(node):
            if node is None:
                return
            # Traverse left subtree
            inorder(node.left)
            # Visit root
            result.append(node.val)
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return result
