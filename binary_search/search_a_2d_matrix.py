# leetcode Problem 74: Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROW_LEN = len(matrix[0])
        COL_LEN = len(matrix)
        l, r = 0, (ROW_LEN * COL_LEN) - 1

        while l <= r:
            mid = l + ((r-l) // 2)
            i, j = mid // ROW_LEN, mid % ROW_LEN

            if target > matrix[i][j]:
                l = mid + 1
            elif target < matrix[i][j]:
                r = mid - 1
            else:
                return True
        return False