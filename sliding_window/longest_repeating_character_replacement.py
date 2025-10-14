# Leetcode Problem 424: Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ################ Unoptimal ##################
        # maxLen = 0
        # count = {}

        # l = 0
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)

        #     while (r - l + 1) - max(count.values()) > k:
        #         count[s[l]] -= 1
        #         l += 1


        #     maxLen = max(maxLen, r - l + 1 )
        # return maxLen


        ################ Optimal ##################
        maxLen = 0
        maxFreq = 0
        count = {}

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1


            maxLen = max(maxLen, r - l + 1 )
        return maxLen