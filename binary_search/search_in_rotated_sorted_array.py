# Leetcode Problem 33: Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2 
            if nums[m] == target:
                return m
            
            # If middle is in the left chunk
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # If middle is in the right chunk
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else: 
                    l = m + 1
        return -1