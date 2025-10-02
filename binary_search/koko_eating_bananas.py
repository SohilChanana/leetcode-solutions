# Leetcode Problem 875: Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += (p + k - 1) // k
            
            if totalTime > h:
                l = k + 1
            else:
                r = k - 1
        
        return l