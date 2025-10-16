# Leetcode Problem 209: Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = float('inf')
        l = 0
        sum = 0

        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                currLen = (r - l) + 1
                res = min(res, currLen)
                sum -= nums[l]
                l += 1
        return 0 if res == float('inf') else res
            
        