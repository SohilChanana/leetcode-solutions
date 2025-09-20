# Leetcode Problem 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for p in s:
            if p in "({[":
                stack.append(p)
            elif p == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif p == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif p == ']':
                if not stack or stack.pop() != '[':
                    return False
        if not stack:
            return True
        return False