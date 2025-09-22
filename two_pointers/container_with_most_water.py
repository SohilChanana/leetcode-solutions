# Leetcode Problem 11: Container With Most Water
# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] < height [r]:
                l += 1
            else:
                r -= 1
        
        return maxArea