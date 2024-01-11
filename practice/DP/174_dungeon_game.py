import copy
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        memo = [[0 for _ in range(m)] for _ in range(n)]
        memo[0][0] = dungeon[0][0]
        for i in range(1, n):
            memo[i][0] = min(memo[i - 1][0], dungeon[i][0] + memo[i - 1][0])
            dungeon[i][0] += dungeon[i - 1][0]

        for j in range(1, m):
            memo[0][j] = min(memo[0][j - 1], dungeon[0][j] + memo[0][j - 1])
            dungeon[0][j] += dungeon[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                if memo[i - 1][j] > memo[i][j - 1]:
                    memo[i][j] = memo[i - 1][j]
                    memo[i][j] = min(memo[i][j], dungeon[i - 1][j] + dungeon[i][j])
                else:
                    memo[i][j] = memo[i][j - 1]
                    memo[i][j] = min(memo[i][j], dungeon[i][j - 1] + dungeon[i][j])
                dungeon[i][j] += max(dungeon[i - 1][j], dungeon[i][j - 1])
        print(dungeon)
        print(memo)
    
        if memo[-1][-1] >= 0:
            return 1

        return (memo[-1][-1] * -1) + 1


sol = Solution()
print(sol.calculateMinimumHP([[1,-3,2],[0,-1,2],[0,0,-2]]))
