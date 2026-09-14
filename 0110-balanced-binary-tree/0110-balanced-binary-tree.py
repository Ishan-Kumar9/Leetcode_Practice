# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        def balanced(node):
            if not node:
                return 0
            h1 = balanced(node.left)
            h2 = balanced(node.right)
            if abs(h1-h2) > 1:
                self.flag = False
            return max(h1,h2)+1
        balanced(root)
        return self.flag 