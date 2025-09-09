# Leetcode Problem 238: Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)
        suffix = 1
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * suffix
            suffix = suffix * nums[i]

        return res