# Leetcode Problem 199: Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            rightmost = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                res.append(rightmost.val)
        return res


