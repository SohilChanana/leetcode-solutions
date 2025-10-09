# Leetcode Problem 69: Sqrt(x)
# https://leetcode.com/problems/sqrtx/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + (r-l) // 2
            guess = m * m
            print(m)
            if guess > x:
                r = m - 1
            elif guess < x:
                l = m + 1
                res = m
            else:
                return m
        return res
        