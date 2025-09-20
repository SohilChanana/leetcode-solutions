# Leetcode Problem 125: Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True

        ######## Create reverse of String and compare #######
        # newS = ""
        # for c in s:
        #     if c.isalnum():
        #         newS += c.lower()
        

        # if len(newS) == 1 or len(newS) == 0:
        #     return True
        # newSR = ""
        # for i in range(len(newS) - 1, -1, -1):
        #     newSR += newS[i]
        # return newSR == newS
