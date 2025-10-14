# Leetcode Problem 567: Permutation in String
# https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ################## Unoptimal Sliding Window ##################
        # s1Map = Counter(s1)
        # s1Len = len(s1)
        # l = 0
        # s2Map = {}

        # for r in range(len(s2)):
        #     s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1
        #     while r - l + 1 > s1Len:
        #         s2Map[s2[l]] -= 1
        #         if s2Map[s2[l]] == 0:
        #             del s2Map[s2[l]]
        #         l += 1
        #     print(s2Map)
        #     if s2Map == s1Map:
        #         return True
        # return False


        ################## Optimal Sliding Window ##################
        if len(s1) > len(s2): return False


        s1Map, s2Map = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord('a')] += 1 
            s2Map[ord(s2[i]) - ord('a')] += 1 
        
        matches = 0
        for i in range(26):
            if s1Map[i] == s2Map[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Map[index] += 1
            if s1Map[index] == s2Map[index]:
                matches += 1
            elif s1Map[index] + 1 == s2Map[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Map[index] -= 1
            if s1Map[index] == s2Map[index]:
                matches += 1
            elif s1Map[index] - 1 == s2Map[index]:
                matches -= 1
            
            l += 1


        return matches == 26 



        