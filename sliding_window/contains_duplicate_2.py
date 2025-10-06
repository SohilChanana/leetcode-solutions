# Leetcode Problem 219: Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        ############# Hash Set ###########
        # window = set()
        # l = 0

        # for r in range(len(nums)):
        #     if r - l > k:
        #         window.remove(nums[l])
        #         l += 1
        #     if nums[r] in window:
        #         return True
        #     window.add(nums[r])
        # return False

        ############# Hash Map ###########
        map = {}

        for i in range(len(nums)):
            if nums[i] in map and i - map[nums[i]] <= k:
                return True
            map[nums[i]] = i
        return False

        