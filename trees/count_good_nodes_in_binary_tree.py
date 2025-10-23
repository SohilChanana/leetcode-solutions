# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def checkGood(node, maxVal):
            if not node:
                return 0

            if node.val >= maxVal:
                res = 1
            else:
                res = 0
            maxVal = max(node.val, maxVal)
            res = res + checkGood(node.left, maxVal) + checkGood(node.right, maxVal)
            return res
        return checkGood(root, root.val)
        