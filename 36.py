from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_map = {x:0 for x in range(1,10)}

        # for





s=Solution()
l =[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

s.isValidSudoku(l)