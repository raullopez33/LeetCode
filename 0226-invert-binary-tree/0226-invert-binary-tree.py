# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# we will be conducting a recursive solutions using depth first search
# Let's get right into it lol -- I need to keep going - help me chief

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        #flip the nodes
        tmp = root.right
        root.right = root.left
        root.left = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
