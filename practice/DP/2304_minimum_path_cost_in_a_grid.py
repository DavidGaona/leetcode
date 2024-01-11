import heapq
from typing import List
from math import inf

from math import inf


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        dp = [[inf for x in range(len(grid[0]))] for y in range(len(grid))]
        # print(dp)
        n = len(grid)
        m = len(grid[0])
        # fill first line of dp
        for j in range(m):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(m):
                for k in range(m):
                    dummy = dp[i - 1][k] + moveCost[grid[i - 1][k]][k]
                    dammy = dp[i - 1][k]
                    dammu = moveCost[grid[i - 1][k]][j]
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + moveCost[grid[i - 1][k]][j])
                dp[i][j] += grid[i][j]
        print(dp)
        return 17


sol = Solution()
sol.minPathCost([[5, 3], [4, 0], [2, 1]], [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]])


