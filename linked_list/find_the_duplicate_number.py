# Leetcode Problem 287: Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
        
            if slow == slow2:
                return slow