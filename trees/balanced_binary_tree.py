# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def checkHeight(root):
            if not root:
                return 0
            leftHeight = checkHeight(root.left)
            if leftHeight == -1:
                return -1
            rightHeight = checkHeight(root.right)
            if rightHeight == -1:
                return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            return max(leftHeight, rightHeight) + 1
        
        return checkHeight(root) != -1
        

        