from typing import List, Union, Collection, Mapping, Optional

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Make a grid of 0's with len(text2) + 1 columns 
        # and len(text1) + 1 rows.
        len_1 = len(text1)
        len_2 = len(text2)
        dp_grid = [[0]*(len_2+1) for _ in range(len_1+1)]

        # Iterate up each column, starting from the last one. 
        for j in reversed(range(len_2)):
            for i in reversed(range(len_1)):
                if text1[i] == text2[j]:
                    dp_grid[i][j] = dp_grid[i+1][j+1] + 1
                else:
                    dp_grid[i][j] = max(dp_grid[i+1][j], dp_grid[i][j+1])

        # The original problem's answer is in dp_grid[0][0]. Return it.  
        return dp_grid[0][0]
