# Leetcode Problem: 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]