# Leetcode Problem 1: Two Sum
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for i, num in enumerate(nums):
            if (target - num) in numMap:
                return [numMap[target-num], i]
            numMap[num] = i