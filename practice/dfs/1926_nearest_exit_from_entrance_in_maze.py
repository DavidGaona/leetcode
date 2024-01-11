from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])
        final_counter = -1

        def dfs(i, j, counter):
            nonlocal final_counter, n, m

            # Check if it's a wall
            if maze[i][j] == "+":
                return

            # Check if it's the exit
            if entrance[0] != i or entrance[1] != j:
                if i == 0 or i == (n - 1) or j == 0 or j == (m - 1):
                    if final_counter == -1:
                        final_counter = counter
                    else:
                        final_counter = min(counter, final_counter)

            maze[i][j] = "+"

            # Up
            if i != 0:
                dfs(i - 1, j, counter + 1)

            # Left
            if j != 0:
                dfs(i, j - 1, counter + 1)

            # Down
            if i != (n - 1):
                dfs(i + 1, j, counter + 1)

            # Right
            if j != (m - 1):
                dfs(i, j + 1, counter + 1)

        dfs(entrance[0], entrance[1], 0)
        return final_counter


sol = Solution()
print(sol.nearestExit([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]], [1, 2]))
