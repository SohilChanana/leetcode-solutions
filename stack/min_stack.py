# Leetcode Problem 155. Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val-self.min)
            self.min = min(val, self.min)
        
        

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return
        
        popped = self.stack.pop()
        if (popped < 0):
            self.min -= popped


    def top(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()