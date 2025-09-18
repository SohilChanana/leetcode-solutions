# Leetcode Problem 128: Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    ############### Brute force approach using sorting ################
    # def longestConsecutive(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """

    #     if not nums:
    #         return 0

    #     nums.sort()
    #     longestStreak = 1

    #     currNum = nums[0]
    #     currStreak = 1
    #     i = 0
    #     while i < len(nums):
    #         if nums[i] != currNum:
    #             if nums[i] == currNum + 1:
    #                 currStreak += 1
    #                 currNum = nums[i]
    #                 longestStreak = max(currStreak, longestStreak)
    #             else:
    #                 currStreak = 1
    #                 currNum = nums[i]

    #         i += 1

    #     return longestStreak
    
    ############### Optimized approach using HashSet ################
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numSet = set(nums)
        longest  = 0

        for n in numSet:
            if (n-1) not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest