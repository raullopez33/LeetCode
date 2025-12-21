# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.right) and self.isBalanced(root.left)

    

    def height(self, curr):
        if not curr:
            return 0
        
        left = self.height(curr.left)
        right = self.height(curr.right)

        return 1 + max(left, right)