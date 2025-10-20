# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = 0
        def depth(root):
            if not root:
                return 0
            leftDepth = depth(root.left)
            rightDepth = depth(root.right)
            self.res = max(self.res, leftDepth + rightDepth)

            return 1 + max(leftDepth, rightDepth)
        depth(root)
        return self.res

        
        