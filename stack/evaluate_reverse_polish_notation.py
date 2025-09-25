# Leetcode Problem 150: Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c in {'+', '-', '/', '*'}:
                num1 = stack.pop()
                num2 = stack.pop()
                if c == '+':
                    res = num1 + num2
                elif c == '-':
                    res = num2 - num1
                elif c == '*':
                    res = num1 * num2
                elif c == '/':
                    res = int(float(num2) / num1)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack.pop()