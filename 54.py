from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        new_mat = []
        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1
        while left <= right and top <= bottom:

            for x in range(left,right + 1):
                new_mat.append(matrix[top][x])
            top += 1

            for x in range(top, bottom + 1):
                new_mat.append(matrix[x][right])
            right -= 1

            if top <= bottom:
                for x in range(right, left - 1, -1):
                    new_mat.append(matrix[bottom][x])
                bottom -= 1
            if left <= right:
                for x in range(bottom, top - 1, -1):
                    new_mat.append(matrix[x][left])
                left += 1


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
"""
print(l)
s = Solution()
response = s.spiralOrder(l)
