# LeetCode 682. Baseball Game
# https://leetcode.com/problems/baseball-game/

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        scores = []
        for op in operations:
            if op == 'D':
                scores.append(scores[-1] * 2)
            elif op == '+':
                scores.append(scores[-1] + scores [-2])
            elif op == 'C':
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)
        