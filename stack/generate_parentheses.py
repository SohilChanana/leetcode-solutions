# Leetcode Problem 22: Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # add open if open < n
        # Only add close if close < open

        stack = []
        res = []

        def backtrack(openNum, closeNum):
            if openNum == closeNum == n:
                res.append("".join(stack))
                return
            
            if openNum < n:
                stack.append("(")
                backtrack(openNum + 1, closeNum)
                stack.pop()
            
            if closeNum < openNum:
                stack.append(")")
                backtrack(openNum, closeNum + 1)
                stack.pop()

        backtrack(0, 0)
        return res