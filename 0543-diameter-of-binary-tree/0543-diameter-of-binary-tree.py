# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Understand: The diameter of a tree is defined as the number of edges on the longest path betwenn two nodes. 
We want to return the value of the longest paths, essentially the max diameter between two nodes. We are not bound to 
having the path go through the node so that means we will keep track of the longest diameter as we bubble up.

Plan: We need a recursive function to go through the tree and find the heights of a tree(node) and return that to us while also
keeping track of the biggest diameter as we traverse
'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Member variable for this class instantiated
        self.res = 0

        def DFS(curr):
            if not curr:
                return 0
            left = DFS(curr.left)
            right = DFS(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        DFS(root)
        return self.res