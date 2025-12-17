# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# THis is a DFS algorithm and to stay on track Recursion is best
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #when we reach a null node, then return 0 since we are tracking values throuhh return values 
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)