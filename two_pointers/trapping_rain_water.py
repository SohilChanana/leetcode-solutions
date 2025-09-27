# Leetcode Problem 42: Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        
        ############# Suffix Solution #############
        # arrayLength = len(height)

        # leftMax = [0] * arrayLength
        # rightMax = [0] * arrayLength

        # leftMax[0] = height[0]
        # rightMax[arrayLength - 1] = height[arrayLength - 1]

        # for i in range(1, arrayLength):
        #     leftMax[i] = max(height[i], leftMax[i-1])
        
        # for i in range(arrayLength - 2, -1, -1):
        #     rightMax[i] = max(rightMax[i + 1], height[i])

        # total = 0
        # for i in range(arrayLength):
        #     total += min(leftMax[i], rightMax[i]) - height[i]

        # return total

        ############# Two-Pointer Solution #############

        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        total = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r] 

        return total